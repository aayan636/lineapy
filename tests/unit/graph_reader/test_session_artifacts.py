from lineapy.graph_reader.session_artifacts import SessionArtifacts
from lineapy.utils.utils import prettify


def test_refactor(execute):
    # a0 --> (a0+=1) \                       /--> (f=c+7)
    #                 \                     /
    #                  >--> b=a*2+a0 --> (c=b+3) -------\
    #                 /                                  \
    # (a=1) --> a+=1 /-----> d=a*4 --> e=d+5 --> (e+=6) --\
    #                    \                                 \
    #                     \--> a+=1 ------------------------\--> (g = c+e*2)--\
    #                                                    \                     \
    #                                                     \---------------------\--> (h=a+g) --\
    #                                                                                           >---> (z.append(h))
    #                                                                                z = [1] --/

    """
    Node with parentheses are artifacts,
    """
    code = """import lineapy
art = {}
a0 = 0
a0 += 1
art['a0'] = lineapy.save(a0,"a0")
a=1
art['a'] = lineapy.save(a, "a")

a+=1
b = a*2 + a0
c = b+3
d = a*4
e = d+5
e+=6
art['c'] = lineapy.save(c, "c")
art['e'] = lineapy.save(e, "e")

f = c+7
art['f'] = lineapy.save(f, "f")
a+=1
g = c+e *2
art['g2'] = lineapy.save(g,'g2')
h = a+g
art['h'] = lineapy.save(h,'h')
z = [1]
z.append(h)
art['z'] = lineapy.save(z,'z')
"""

    expection_result_all = """import copy
def get_a():
  a = 1
  return a

def get_a0():
  a0 = 0
  a0 += 1
  return a0

def get_a_for_artifact_c_and_downstream(a):
  a += 1
  return a

def get_c(a, a0):
  b = a * 2 + a0
  c = b + 3
  return c

def get_f(c):
  f = c + 7
  return f

def get_e(a):
  d = a * 4
  e = d + 5
  e += 6
  return e

def get_g2(c, e):
  g = c + e * 2
  return g

def get_h(a, g):
  a += 1
  h = a + g
  return h

def get_z(h):
  z = [1]
  z.append(h)
  return z

def pipeline():
  sessionartifacts = []
  a = get_a()
  sessionartifacts.append(copy.deepcopy(a))
  a0 = get_a0()
  sessionartifacts.append(copy.deepcopy(a0))
  a = get_a_for_artifact_c_and_downstream(a)
  c = get_c(a, a0)
  sessionartifacts.append(copy.deepcopy(c))
  f = get_f(c)
  sessionartifacts.append(copy.deepcopy(f))
  e = get_e(a)
  sessionartifacts.append(copy.deepcopy(e))
  g = get_g2(c, e)
  sessionartifacts.append(copy.deepcopy(g))
  h = get_h(a, g)
  sessionartifacts.append(copy.deepcopy(h))
  z = get_z(h)
  sessionartifacts.append(copy.deepcopy(z))
  return sessionartifacts

if __name__=="__main__":
  pipeline()
    """

    res = execute(code, snapshot=False)
    art = res.values["art"]
    assert len(res.values["art"]) == 8

    sas = SessionArtifacts(list(art.values()))
    refactor_code = sas.get_session_module_definition(
        indentation=2, keep_lineapy_save=False
    )
    assert prettify(refactor_code) == prettify(expection_result_all)

    expection_result_a0_c_h = """import copy
def get_a0():
  a0 = 0
  a0 += 1
  return a0

def get_a_for_artifact_c_and_downstream():
  a = 1
  a += 1
  return a

def get_c(a, a0):
  b = a * 2 + a0
  c = b + 3
  return c

def get_h(a, c):
  d = a * 4
  e = d + 5
  e += 6
  a += 1
  g = c + e * 2
  h = a + g
  return h

def pipeline():
  sessionartifacts = []
  a0 = get_a0()
  lineapy.save(a0, "a0")
  sessionartifacts.append(copy.deepcopy(a0))
  a = get_a_for_artifact_c_and_downstream()
  c = get_c(a, a0)
  lineapy.save(c, "c")
  sessionartifacts.append(copy.deepcopy(c))
  h = get_h(a, c)
  lineapy.save(h, "h")
  sessionartifacts.append(copy.deepcopy(h))
  return sessionartifacts

if __name__=="__main__":
  pipeline()
    """

    sas = SessionArtifacts(
        [a for i, a in enumerate(list(art.values())) if i in [0, 2, 6]]
    )  # a0, c, h
    refactor_code_a0_c_h = sas.get_session_module_definition(
        indentation=2, keep_lineapy_save=True
    )
    assert prettify(refactor_code_a0_c_h) == prettify(expection_result_a0_c_h)

    expection_result_h = """def get_h():
  a0 = 0
  a0 += 1
  a = 1
  a += 1
  b = a * 2 + a0
  c = b + 3
  d = a * 4
  e = d + 5
  e += 6
  a += 1
  g = c + e * 2
  h = a + g
  return h

def pipeline():
  h = get_h()
  return h

if __name__=="__main__":
  pipeline()
    """

    sas = SessionArtifacts(
        [a for i, a in enumerate(list(art.values())) if i in [6]]
    )  # a0, c, h
    refactor_code_h = sas.get_session_module_definition(indentation=2)
    assert prettify(refactor_code_h) == prettify(expection_result_h)


def test_module_import(execute):
    code = """import lineapy
art = {}
import pandas
df = pandas.DataFrame({'a':[1,2]})
art['df'] = lineapy.save(df,'df')

df2 = pandas.concat([df,df])
art['df2'] = lineapy.save(df2,'df2')
    """
    expection_result_all = """import copy
import pandas

def get_df():
    df = pandas.DataFrame({"a": [1, 2]})
    return df

def get_df2(df):
    df2 = pandas.concat([df, df])
    return df2

def pipeline():
    sessionartifacts = []
    df = get_df()
    sessionartifacts.append(copy.deepcopy(df))
    df2 = get_df2(df)
    sessionartifacts.append(copy.deepcopy(df2))
    return sessionartifacts

if __name__=="__main__":
    pipeline()
"""

    res = execute(code, snapshot=False)
    art = res.values["art"]
    assert len(res.values["art"]) == 2

    sas = SessionArtifacts(list(art.values()))
    refactor_code = sas.get_session_module_definition()
    assert prettify(refactor_code) == prettify(expection_result_all)


def test_module_import_alias(execute):
    code = """import lineapy
art = {}
import pandas as pd
df = pd.DataFrame({'a':[1,2]})
art['df'] = lineapy.save(df,'df')

df2 = pd.concat([df,df])
art['df2'] = lineapy.save(df2,'df2')
    """
    expection_result_all = """import copy
import pandas as pd

def get_df():
    df = pd.DataFrame({"a": [1, 2]})
    return df

def get_df2(df):
    df2 = pd.concat([df, df])
    return df2

def pipeline():
    sessionartifacts = []
    df = get_df()
    sessionartifacts.append(copy.deepcopy(df))
    df2 = get_df2(df)
    sessionartifacts.append(copy.deepcopy(df2))
    return sessionartifacts

if __name__=="__main__":
    pipeline()
"""

    res = execute(code, snapshot=False)
    art = res.values["art"]
    assert len(res.values["art"]) == 2

    sas = SessionArtifacts(list(art.values()))
    refactor_code = sas.get_session_module_definition()
    assert prettify(refactor_code) == prettify(expection_result_all)


def test_module_import_from(execute):
    code = """import lineapy
art = {}
import pandas as pd
from sklearn.linear_model import LinearRegression
# Load train data
url1 = "https://raw.githubusercontent.com/LineaLabs/lineapy/main/examples/tutorials/data/iris.csv"
train_df = pd.read_csv(url1)
# Initiate the model
mod = LinearRegression()
# Fit the model
mod.fit(
    X=train_df[["petal.width"]],
    y=train_df["petal.length"],
)
# Save the fitted model as an artifact
art['model'] = lineapy.save(mod, "iris_model")
# Load data to predict (assume it comes from a different source)
pred_df = pd.read_csv(url1)
# Make predictions
petal_length_pred =  mod.predict(X=pred_df[["petal.width"]])
# Save the predictions
art['pred'] = lineapy.save(petal_length_pred, "iris_petal_length_pred")
    """
    expection_result_all = """import copy
import pandas as pd
from sklearn.linear_model import LinearRegression

def get_url1_for_artifact_iris_model_and_downstream():
    url1 = "https://raw.githubusercontent.com/LineaLabs/lineapy/main/examples/tutorials/data/iris.csv"
    return url1

def get_iris_model(url1):
    train_df = pd.read_csv(url1)
    mod = LinearRegression()
    mod.fit(
        X=train_df[["petal.width"]],
        y=train_df["petal.length"],
    )
    return mod

def get_iris_petal_length_pred(mod, url1):
    pred_df = pd.read_csv(url1)
    petal_length_pred = mod.predict(X=pred_df[["petal.width"]])
    return petal_length_pred

def pipeline():
    sessionartifacts = []
    url1 = get_url1_for_artifact_iris_model_and_downstream()
    mod = get_iris_model(url1)
    sessionartifacts.append(copy.deepcopy(mod))
    petal_length_pred = get_iris_petal_length_pred(mod, url1)
    sessionartifacts.append(copy.deepcopy(petal_length_pred))
    return sessionartifacts

if __name__=="__main__":
    pipeline()
"""

    res = execute(code, snapshot=False)
    art = res.values["art"]
    assert len(res.values["art"]) == 2

    sas = SessionArtifacts(list(art.values()))
    refactor_code = sas.get_session_module_definition()
    assert prettify(refactor_code) == prettify(expection_result_all)