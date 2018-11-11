pipeline {
    agent {docker docker {
            image 'python:3.6.0'
            args '-p 8080:8080'
             }
            }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                retry(3){
                 sh 'pip install -r requirements.txt'
                }
            }
        }
    }
}