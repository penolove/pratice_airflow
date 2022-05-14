# pratice_airflow

this example setup with: https://airflow.apache.org/docs/apache-airflow/stable/start/local.html

## start service

```bash
# use docker-compose
docker-compose -f docker-compose-local-executor.yaml up
# or docker compose plugin
docker compose -f docker-compose-local-executor.yaml up

```

service will started at http://localhost:8080/

## login and create user

when you visit the page above and try to login
the password msg will show password msg in your terminal (seems a bug)

like

```bash
airflow_1  | standalone | Airflow is ready
airflow_1  | standalone | Login with username: admin  password: UtkWctbbuDYFtAvc  <- !this is random generated!
```

or you can access the airflow container to create your own role

```bash
docker-compose -f docker-compose-local-executor.yaml exec airflow bash

# in container
airflow users  create --role Admin --username penolove --email admin --firstname admin --lastname admin --password 5566isbest
```

## examples

default set AIRFLOW__CORE__LOAD_EXAMPLES=True as True
which means you will also see example dags from airflows

you will see a dag named: abcd-example-abcd

this dag definition is in dags/abcd-example-abcd.py

feel free to add dags into dags folder, once you save the py file with dag definition

it will soon appear in the UI.
