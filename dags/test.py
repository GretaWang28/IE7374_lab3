"""
Hello World DAG - Demo for team meeting
This shows basic Airflow functionality
"""

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# Task functions
def print_hello():
    """First task - prints hello"""
    print("=" * 50)
    print("Hello from Airflow!")
    print("This is our first automated task")
    print("=" * 50)
    return "Hello task completed"

def print_team_info():
    """Second task - shows team info"""
    print("MOMENT Team Pipeline Demo")
    print(f"Execution date: {datetime.now()}")
    print("This will run our data pipeline automatically!")
    return "Team info displayed"

def analyze_mock_data():
    """Third task - simulates data analysis"""
    print("Analyzing data...")
    mock_results = {
        'books_downloaded': 10,
        'books_processed': 10,
        'anomalies_found': 0,
        'bias_detected': 'Low'
    }
    for key, value in mock_results.items():
        print(f"{key}: {value}")
    return mock_results

# DAG default arguments
default_args = {
    'owner': 'moment-team',
    'depends_on_past': False,
    'start_date': datetime(2025, 2, 10),
    'email_on_failure': False,
    'retries': 2,  # Retry failed tasks 2 times
    'retry_delay': timedelta(minutes=1),
}

# Create the DAG
dag = DAG(
    dag_id='hello_world_demo',
    default_args=default_args,
    description='Demo DAG for team meeting',
    schedule_interval=None,  # Manual trigger only
    catchup=False,
    tags=['demo', 'meeting'],
)

# Define tasks
task1 = PythonOperator(
    task_id='say_hello',
    python_callable=print_hello,
    dag=dag,
)

task2 = PythonOperator(
    task_id='show_team_info',
    python_callable=print_team_info,
    dag=dag,
)

task3 = PythonOperator(
    task_id='analyze_data',
    python_callable=analyze_mock_data,
    dag=dag,
)

task4 = BashOperator(
    task_id='print_completion',
    bash_command='echo "Pipeline completed successfully!"',
    dag=dag,
)

# Define task dependencies (workflow)
# This creates: task1 -> task2 -> task3 -> task4
task1 >> task2 >> task3 >> task4