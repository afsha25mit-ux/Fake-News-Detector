pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t fake-news-app .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 5000:5000 fake-news-app'
            }
        }
    }
}