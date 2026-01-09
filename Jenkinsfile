pipeline {
    agent any

    environment {
        // AWS RDS එක හැදුවාම ලැබෙන විස්තර මෙතනට දාන්න
        DB_USER = 'fastapi_user'
        DB_PASSWORD = 'fastapi123'
        DB_HOST = 'ඔබේ-rds-endpoint.aws.com'
        DB_NAME = 'user_management'
    }

    stages {
        stage('Checkout') {
            steps {
                // GitHub එකෙන් අලුත්ම code එක ලබා ගැනීම
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    ./venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Setup Environment') {
            steps {
                // .env file එක automatic සාදා ගැනීම
                sh '''
                    echo "DB_USER=${DB_USER}" > .env
                    echo "DB_PASSWORD=${DB_PASSWORD}" >> .env
                    echo "DB_HOST=${DB_HOST}" >> .env
                    echo "DB_NAME=${DB_NAME}" >> .env
                '''
            }
        }

        stage('Deploy / Restart') {
            steps {
                // FastAPI service එක restart කිරීම
                // මෙයට sudo permission අවශ්‍ය වේ
                sh 'sudo systemctl restart fastapi'
            }
        }
    }
}