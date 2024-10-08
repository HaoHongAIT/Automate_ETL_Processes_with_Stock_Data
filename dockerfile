# Use the official Airflow image
FROM apache/airflow:2.8.1-python3.10

# Set the environment variables for Airflow
ENV AIRFLOW_HOME=/opt/airflow

# Install additional Python dependencies if needed
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy DAGs and other necessary files
COPY ./dags $AIRFLOW_HOME/dags
COPY ./plugins $AIRFLOW_HOME/plugins

# Set up entrypoint (Airflow commands can be overridden via docker-compose or run command)
ENTRYPOINT ["airflow"]

# Default command
CMD ["webserver"]
