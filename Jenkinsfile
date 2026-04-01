pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/afsha25mit-ux/Fake-News-Detector.git'
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