from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
import pandas as pd
from ETL.extract.multi_threading import MultiThreading
from ETL.load.load import Load
from ETL.transform.transform import Transform

#from email import email
TIME ="2024-09-14"

time_range = f'01/01/2024 - {TIME}'
stock_codes = pd.read_excel(r'./data/document/code_stock.xlsx')['ticker'].to_list()[200:201]


crawler = MultiThreading(threads=10, code_list=stock_codes)
transform = Transform(time=TIME)
load2db = Load()


dag = DAG('etl_dag',
          default_args={'email': ['haohong.work@gmail.com', 'kiemook@gmail.com'],
                        'email_on_failure': False, 'retries': 1,
                        'retry_delay': timedelta(minutes=5)},
          description='An ETL Pipeline DAG',
          schedule_interval=timedelta(days=1),
          start_date=datetime.today() - timedelta(days=1),
          tags=['etl'])

extract_task = PythonOperator(task_id='crawl_data',
                              python_callable=crawler.run,
                              op_args=time_range,
                              dag=dag)

transform_task = PythonOperator(task_id='transform_data',
                                python_callable=transform.run,
                                dag=dag)

load_task = PythonOperator(task_id='load_data',
                           python_callable=load2db.run,
                           dag=dag)

# email_operator = PythonOperator(task_id='email_operator',
#                                 python_callable=email,
#                                 dag=dag)

extract_task >> transform_task >> load_task
# extract_task >> [transform_task, load_task]

