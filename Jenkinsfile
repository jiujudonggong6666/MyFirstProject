pipeline {
    agent {docker { image 'python:3.6.0' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh 'pip install -r /home/lijunxing/my-project/requirements.txt'
                sh 'python MyprojectFlask.py'
            }
        }
    }
}