"""
This is an example dag for using the for yien.
"""
from airflow.operators.bash_operator import BashOperator
from airflow.models.baseoperator import BaseOperator
from airflow.utils.decorators import apply_defaults
from airflow.utils.dates import days_ago
from airflow.models import DAG


class HelloOperator(BaseOperator):
    template_fields = ['ds_without_dash']

    @apply_defaults
    def __init__(self, name: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.name = name
        self.ds_without_dash = "{{ds_nodash}}"
        # more marco https://airflow.apache.org/docs/stable/macros-ref.html

    def execute(self, context):
        message = "Hello {}".format(self.name)
        print(message, self.ds_without_dash)
        return message


with DAG(
    dag_id='abcd-example-abcd',
    start_date=days_ago(2),
    catchup=False,
    schedule_interval='0 0 * * *',
) as dag:

    b = BashOperator(
        task_id='kerkerboy',
        bash_command='echo 1',
        dag=dag,
    )
    hello_task = HelloOperator(
        task_id='sample-task',
        name='foo_bar',
        dag=dag,
    )

    b >> hello_task
