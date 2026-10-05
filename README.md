# ACEest Fitness & Gym

A Flask-based fitness and gym management application developed as part of the Introduction to DevOps assignment.

## Project Overview

ACEest Fitness & Gym provides REST API endpoints for:

* Checking application health
* Managing gym clients
* Retrieving individual client details
* Viewing available fitness programs

The project demonstrates DevOps practices including:

* Git and GitHub version control
* Pytest automated testing
* Docker containerization
* Jenkins build automation
* GitHub Actions CI/CD
* GitHub Container Registry (GHCR)

## Technologies Used

* Python 3.9
* Flask
* Pytest
* Docker
* Jenkins
* GitHub Actions
* GitHub Container Registry

## Project Structure

```text
aceest-fitness-devops/
├── app.py
├── requirements.txt
├── pytest.ini
├── Dockerfile
├── .dockerignore
├── .gitignore
├── README.md
├── tests/
│   └── test_app.py
└── .github/
    └── workflows/
        └── ci.yml
```

## Local Setup

Clone the repository:

```bash
git clone https://github.com/2025tm93180-lgtm/aceest-fitness-devops.git
cd aceest-fitness-devops
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

Start the Flask application:

```bash
python app.py
```

The application runs on:

```text
http://localhost:5000
```

## API Endpoints

### Health Check

```text
GET /health
```

Example response:

```json
{
  "status": "healthy"
}
```

### Get Clients

```text
GET /clients
```

### Add Client

```text
POST /clients
```

Example request:

```json
{
  "name": "John",
  "age": 25,
  "height": 175,
  "weight": 70,
  "program": "Muscle Gain"
}
```

### Get Client

```text
GET /clients/<client_id>
```

### Get Fitness Programs

```text
GET /programs
```

## Running Tests

Run the complete Pytest suite:

```bash
pytest
```

The project currently contains 8 automated tests.

Expected result:

```text
8 passed
```

## Docker

Build the Docker image:

```bash
docker build -t aceest-fitness .
```

Run the container:

```bash
docker run -d -p 5001:5000 --name aceest-container aceest-fitness
```

Test the application:

```bash
curl http://localhost:5001/health
```

Expected response:

```json
{
  "status": "healthy"
}
```

Stop and remove the container:

```bash
docker rm -f aceest-container
```

## Jenkins Integration

Jenkins is configured with a Freestyle project named `ACEest-Fitness-Build`.

The Jenkins build performs the following steps:

1. Checks out the latest source code from GitHub.
2. Installs Python dependencies.
3. Executes the Pytest test suite.
4. Builds the Docker image.
5. Reports a successful build when all stages complete.

The Jenkins build successfully executes all 8 tests and builds the Docker image.

## GitHub Actions CI/CD

The GitHub Actions workflow is located at:

```text
.github/workflows/ci.yml
```

The workflow is triggered by:

* Pushes to the `main` branch
* Pull requests targeting the `main` branch

The pipeline performs:

1. Checkout of source code
2. Python environment setup
3. Dependency installation
4. Build and lint validation
5. Docker image creation
6. Pytest execution inside the Docker container
7. Docker image publishing to GitHub Container Registry on pushes to `main`

## Container Registry

The Docker image is published to GitHub Container Registry:

```text
ghcr.io/2025tm93180-lgtm/aceest-fitness:latest
```

## DevOps Workflow

```text
Developer
    |
    v
Git / GitHub
    |
    +--------------------+
    |                    |
    v                    v
Jenkins              GitHub Actions
    |                    |
    v                    v
Pytest              Build & Lint
    |                    |
    v                    v
Docker Build        Docker Build
                         |
                         v
                  Pytest in Container
                         |
                         v
                       GHCR
```

## Conclusion

This project demonstrates an automated DevOps lifecycle for the ACEest Fitness & Gym application using version control, automated testing, containerization, Jenkins build automation, and GitHub Actions CI/CD.
