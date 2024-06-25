 pipeline {
    agent any

    environment {
        DOCKER_CREDENTIAL_ID = 'dockerhub-credentials'
        GITHUB_CREDENTIAL_ID = 'github-credentials'
    }

    stages {
        stage('Checkout') {
            steps {
                git credentialsId: env.GITHUB_CREDENTIAL_ID, url: 'https://github.com/wsanchezo/docker-multi-container-project.git'
            }
        }

        stage('Build App Image') {
            steps {
                script {
                    docker.build('app-image', '-f Dockerfile.app .').withRun { c ->
                        sh 'docker cp app/requirements.txt requirements.txt'
                        sh 'docker build -t app-image .'
                    }
                }
            }
        }

        stage('Build DB Image') {
            steps {
                script {
                    docker.build('db-image', '-f Dockerfile.db .').withRun { c ->
                        sh 'docker build -t db-image .'
                    }
                }
            }
        }

        stage('Push Images to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', env.DOCKER_CREDENTIAL_ID) {
                        docker.image('app-image').push()
                        docker.image('db-image').push()
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sh 'docker-compose down'
                    sh 'docker-compose up -d'
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
        success {
            mail to: 'you@example.com',
                 subject: "Successful Build: ${env.JOB_NAME} ${env.BUILD_NUMBER}",
                 body: "Good job! The build ${env.BUILD_NUMBER} was successful."
        }
        failure {
            mail to: 'you@example.com',
                 subject: "Failed Build: ${env.JOB_NAME} ${env.BUILD_NUMBER}",
                 body: "Oops! The build ${env.BUILD_NUMBER} failed. Please check the logs."
        }
    }
}
