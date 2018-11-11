pipeline {
    agent {docker { image 'python:3.6.0' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh 'docker build -t myproject .'
                sh 'docker run -it myproject'
            }
        }
    }
}