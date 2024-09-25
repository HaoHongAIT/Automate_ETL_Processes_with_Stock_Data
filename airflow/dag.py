import ssl
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
from email import email
from airflow import DAG

ssl._create_default_https_context = ssl._create_unverified_context

dag = DAG('etl_dag',
          default_args={'email': ['haohong.work@gmail.com', 'kiemook@gmail.com'],
                        'email_on_failure': True, 'retries': 1,
                        'retry_delay': timedelta(minutes=5)},
          description='An Project ETL Pipeline DAG',
          schedule_interval=timedelta(days=1),
          start_date=datetime.today() - timedelta(days=1),
          tags=['etl'])

crawl_data = PythonOperator(task_id='crawl_data',
                            python_callable=craw_stock_price,
                            op_kwargs={"to_date": "{{ ds }}"},
                            dag=dag)

email_operator = PythonOperator(task_id='email_operator', python_callable=email, dag=dag)

crawl_data >> train_model >> email_operator
