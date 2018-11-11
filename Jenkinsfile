pipeline {
    agent {docker { image 'python:3.6.0' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                retry(3){
                 sh 'pip install -r requirements.txt'
                }
                timeout(time:3,unit:'MINUTES'){
                   sh 'python run.py'
                }
            }
        }
    }
}