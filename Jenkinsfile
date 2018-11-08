pipeline {
    agent {sudo docker { image 'python:3.6.0' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}