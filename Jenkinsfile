pipeline {
    agent {docker { image 'python:3.6.0' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh 'pip install Flask'
                sh 'pip MyprojectFlask.py'
            }
        }
    }
}