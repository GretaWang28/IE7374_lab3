# IE7374 Lab 3 - Airflow

This lab demonstrates how to run an Apache Airflow DAG pipeline using Docker. The DAG (`hello_world_demo`) simulates a simple data pipeline with four sequential tasks.

## Prerequisites
- Docker Desktop installed and running
- At least 4GB memory allocated to Docker

## Project Structure
```
IE7374_lab3/
├── dags/
│   └── test.py          # Hello World DAG
├── plugins/
├── config/
├── .gitignore
└── docker-compose.yaml
```

## How to Run

1. Initialize Airflow:
   ```bash
   docker compose up airflow-init
   ```

2. Start Airflow:
   ```bash
   docker compose up
   ```

3. Open the Airflow UI at **http://localhost:8080**

4. Trigger the `hello_world_demo` DAG manually from the UI.

## DAG Tasks
The pipeline runs 4 tasks in sequence:
```
say_hello → show_team_info → analyze_data → print_completion
```

## Stop Airflow
```bash
docker compose down
```
