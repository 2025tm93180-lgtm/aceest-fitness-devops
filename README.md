# ACEest Fitness & Gym – DevOps CI/CD Project

## Project Overview

ACEest Fitness & Gym is a Flask-based application developed as part of the Introduction to DevOps CI/CD Assignment.

The project demonstrates an automated DevOps lifecycle using GitHub, GitHub Actions, Jenkins, Docker, Kubernetes, Pytest, and SonarQube.

### Key Features

- Flask-based REST API
- Client and fitness program management endpoints
- Input validation and error handling
- Automated testing using Pytest
- Docker containerization
- CI/CD automation using GitHub Actions and Jenkins
- Docker image publishing to GHCR and Docker Hub
- Kubernetes deployment and deployment strategies
- SonarQube static code analysis

## Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.9 | Application development |
| Flask | REST API |
| Pytest | Automated testing |
| Git and GitHub | Version control |
| GitHub Actions | CI/CD automation |
| Jenkins | CI/CD pipeline |
| Docker | Containerization |
| Docker Hub | Container image registry |
| GitHub Container Registry | Container image registry |
| Kubernetes / Minikube | Container orchestration |
| SonarQube | Static code analysis |

## Application Setup

### Prerequisites

- Python 3.9 or later
- pip
- Docker (for container-based execution)
- Git

### Clone the Repository

```bash
git clone https://github.com/2025tm93180-lgtm/aceest-fitness-devops.git
cd aceest-fitness-devops
```

### Create a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

The Flask application runs on port 5000.

## Application Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Application information |
| GET | `/health` | Health check |
| GET | `/clients` | Retrieve clients |
| POST | `/clients` | Create a client |
| GET | `/clients/<id>` | Retrieve a client by ID |
| GET | `/programs` | Retrieve fitness programs |

The application includes input validation for client details such as name, age, height, and weight.

## Automated Testing – Pytest

The project includes 15 automated tests covering application endpoints, input validation, and expected responses.

Run tests locally:

```bash
pytest -v
```

The tests are also executed inside the Docker container as part of the CI/CD pipelines.

## Version Control – Git and GitHub

The source code is maintained in GitHub.

Repository:

https://github.com/2025tm93180-lgtm/aceest-fitness-devops

The project uses Git commits and versioned Docker images to track development changes.

## Docker Containerization

The application is containerized using a Dockerfile.

Build the Docker image:

```bash
docker build -t aceest-fitness .
```

Run the container:

```bash
docker run -d -p 5000:5000 --name aceest-fitness aceest-fitness
```

Run tests inside the container:

```bash
docker run --rm aceest-fitness pytest
```

## Jenkins CI/CD Pipeline

A Jenkins Pipeline job named `ACEest-Fitness-CI-CD` is configured using the project's Jenkinsfile.

The pipeline includes the following stages:

1. Checkout source code from GitHub.
2. Validate Python syntax.
3. Build a Docker test image.
4. Execute Pytest inside the Docker container.
5. Perform SonarQube static code analysis.
6. Build the application Docker image.
7. Push the image to Docker Hub.

The Jenkins job is configured with Git SCM polling.

### Docker Hub Image

Docker Hub repository:

https://hub.docker.com/r/2025tm93180/aceest-fitness

Published image:

```text
2025tm93180/aceest-fitness:v1.2.0
```

## GitHub Actions CI/CD Pipeline

GitHub Actions is configured to execute the CI/CD workflow on pushes to the `main` branch and pull requests targeting `main`.

The workflow performs:

1. Checkout of source code.
2. Python environment setup.
3. Dependency installation.
4. Python syntax validation.
5. Docker image creation.
6. Pytest execution inside the Docker container.
7. Docker image publishing to GitHub Container Registry (GHCR) on pushes to `main`.

### GitHub Container Registry

Published image:

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
              +---------+---------+
              |                   |
              v                   v
           Jenkins           GitHub Actions
              |                   |
              v                   v
            Pytest            Build & Lint
              |                   |
              v                   v
         Docker Build         Docker Build
              |                   |
              v                   v
          Docker Hub        Pytest in Container
                                  |
                                  v
                                 GHCR
```

## Kubernetes Deployment

The application is deployed on a local Minikube Kubernetes cluster.

The production deployment uses two replicas and a NodePort service.

### Production Health Endpoint

```text
http://<MINIKUBE-IP>:30080/health
```

The health endpoint was verified successfully and returned:

```json
{"status":"healthy"}
```

The endpoint is accessible within the configured VM/cluster environment; it is not a publicly exposed cloud endpoint.

### Kubernetes Deployment Strategies

The project includes the following deployment strategy demonstrations:

- **Rolling Update:** Gradually replaces old application pods with the new version.
- **Rollback:** Reverts a deployment to a previously working version.
- **Blue-Green Deployment:** Runs blue and green deployments and switches the service to the green deployment.
- **Canary Deployment:** Runs a smaller canary deployment alongside stable replicas.
- **A/B Testing:** Exposes two application versions through separate services and NodePorts.
- **Shadow Deployment:** Runs a separate deployment without exposing it through a service. Actual traffic mirroring is not configured.

### Kubernetes Manifests

The `k8s/` directory contains the Kubernetes deployment and service manifests, including:

- `deployment.yaml`
- `service.yaml`
- `blue-green.yaml`
- `canary.yaml`
- `ab-testing.yaml`
- `shadow.yaml`

## SonarQube Static Code Analysis

SonarQube is integrated into the Jenkins pipeline to analyse application source code and tests.

The Jenkins pipeline executes SonarScanner and uploads the analysis results to the SonarQube server.

The SonarQube project dashboard displays the analysis status and reported code issues.

The analysis completed successfully. The reported quality gate status should be interpreted according to the conditions configured in the SonarQube project.

## Project Outcomes

The project demonstrates:

- Automated application testing using Pytest.
- Docker image creation and container-based test execution.
- CI/CD automation through Jenkins and GitHub Actions.
- Container image publishing to Docker Hub and GHCR.
- Kubernetes deployment and deployment strategy demonstrations.
- Static code analysis using SonarQube.

## Conclusion

This project demonstrates an end-to-end DevOps workflow for the ACEest Fitness & Gym application, covering source control, automated testing, containerization, CI/CD automation, container registries, Kubernetes deployment, and static code analysis.

## Project Links

**GitHub Repository**

https://github.com/2025tm93180-lgtm/aceest-fitness-devops

**Docker Hub Repository**

https://hub.docker.com/r/2025tm93180/aceest-fitness

**Docker Hub Image**

`2025tm93180/aceest-fitness:v1.2.0`

**GitHub Container Registry Image**

`ghcr.io/2025tm93180-lgtm/aceest-fitness:latest`
