# Project Overview
This project is a performance testing suite using the **Locust** framework to simulate user behavior on a web application.

## Core Components
- `locustfile.py`: The primary entry point for all load tests. Defines the `APIUser` class and the specific tasks (GET, POST, PUT, PATCH) to be executed.
- `utils/`: A collection of helper modules. Specifically, `data_loader.py` handles the retrieval of payloads and utility functions for testing.
- `data/`: Contains raw data files, such as `payloads.json`, used by the `utils` module.

## Key Conventions
- **Payload Handling**: Always use the `utils.data_loader.get_payload(key)` function to fetch data from the `data/` directory instead of directly accessing JSON files.
- **Task Weighting**: Use the `@task(weight)` decorator in `locustfile.py` to define the frequency of different user actions.
- **Environment**: The project uses a Python environment managed via `requirements.txt`.

## Execution
To run the tests, use the following command:
```bash
locust -f locustfile.py
```
