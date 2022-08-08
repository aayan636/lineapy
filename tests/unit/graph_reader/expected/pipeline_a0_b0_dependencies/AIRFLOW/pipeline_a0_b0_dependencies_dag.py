import pipeline_a0_b0_dependencies_module
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

default_dag_args = {
    "owner": "airflow",
    "retries": 2,
    "start_date": days_ago(1),
}

dag = DAG(
    dag_id="pipeline_a0_b0_dependencies_dag",
    schedule_interval="*/15 * * * *",
    max_active_runs=1,
    catchup=False,
    default_args=default_dag_args,
)


run_session_including_b0 = PythonOperator(
    dag=dag,
    task_id="run_session_including_b0_task",
    python_callable=pipeline_a0_b0_dependencies_module.run_session_including_b0,
)

run_session_including_a0 = PythonOperator(
    dag=dag,
    task_id="run_session_including_a0_task",
    python_callable=pipeline_a0_b0_dependencies_module.run_session_including_a0,
)


run_session_including_b0 >> run_session_including_a0