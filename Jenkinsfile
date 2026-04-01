pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/your-username/fake-news-detector.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t fake-news-app .'
            }
        }

        stage('Run Container') {
            steps {
                bat 'docker run -d -p 5000:5000 fake-news-app'
            }
        }
    }
}