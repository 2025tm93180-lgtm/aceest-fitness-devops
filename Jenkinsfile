
pipeline {
    agent any

    environment {
        DOCKER_IMAGE = '2025tm93180/aceest-fitness'
        DOCKER_TAG = 'v1.2.0'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Python Validation') {
            steps {
                sh 'python3 -m py_compile app.py'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'docker build -t aceest-fitness:test .'
                sh 'docker run --rm aceest-fitness:test python -m pytest -v'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withCredentials([string(
                    credentialsId: 'sonarqube-token',
                    variable: 'SONAR_TOKEN'
                )]) {
                    sh '''
                        /opt/sonar-scanner-8.3.1.16491-linux-x64/bin/sonar-scanner \
                        -Dsonar.host.url=http://localhost:9000 \
                        -Dsonar.token="$SONAR_TOKEN"
                    '''
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-credentials',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASSWORD'
                )]) {
                    sh '''
                        echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push ${DOCKER_IMAGE}:${DOCKER_TAG}
                        docker logout
                    '''
                }
            }
        }
    }

    post {
        always {
            echo 'ACEest Fitness CI/CD pipeline completed.'
        }
        success {
            echo 'Build and tests successful!'
        }
        failure {
            echo 'Pipeline failed. Check the console output.'
        }
    }
}
