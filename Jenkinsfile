pipeline {
    agent {docker { image 'ubuntu:16.04'} }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh 'pip install -r requirements.txt'
                sh 'python run.py'
            }
        }
    }
}
111111111111
2222

33333333