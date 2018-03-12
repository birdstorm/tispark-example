from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator

from datetime import datetime, timedelta
import os
import sys

# set to SPARK_HOME
os.environ['SPARK_HOME'] = '/usr/local/spark'
sys.path.append(os.path.join(os.environ['SPARK_HOME'], 'bin'))

args = {
    'owner': 'airflow',
    'depends_on_past': False,  # set this to true if individual task instance depends on the success of the preceding task instance,
    'start_date': datetime(2018, 3, 13),  # start date
    'email': ['example@airflow.com'],  # you may configure email here
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),  # retry timeout
    'end_date': datetime(2018, 3, 14),  # end date
}

# DAG(task-name, args, schedule_interval)
# see how to set args here: https://airflow.apache.org/tutorial.html#default-arguments
# see how to set schedule_interval here: https://airflow.apache.org/scheduler.html#dag-runs
dag = DAG('tispark-test', default_args=args, schedule_interval='0 * * * *')

# task 1 prints date
pre = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag)


text = '{{ ds }} [%s] has been done' % dag.dag_id

# task 2 runs tispark job
spark_task = BashOperator(
    task_id='tispark',
    bash_command='spark-submit --class {{ params.class }} {{ params.jar }}',
    params={'class': 'com.pingcap.tispark.TiSparkExample', 'jar': '/path/to/tisparkexample-1.0-SNAPSHOT-jar-with-dependencies.jar'},
    # modify /path/to/tisparkexample-1.0-SNAPSHOT-jar-with-dependencies.jar to your actual path
    dag=dag
)

pre >> spark_task  # set dependency for different tasks, equivalent to: spark_task.set_upstream(pre)

