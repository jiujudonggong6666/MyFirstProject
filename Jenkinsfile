pipeline {
    agent {docker { image 'python:3.6.0' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                retry(3){
                 sh 'pip install -r requirements.txt'
                }
                timeout(time:3,unit:'MINUTES')
                sh 'python run.py'
            }
        }
        post{
            always {
                echo 'This will always run'
            }
            success {
                echo 'This will run only if successful'
            }
            failure {
                echo 'This will run only if failed'
            }
            unstable {
                echo 'This will run only if the run was marked as unstable'
            }
            changed {
                echo 'This will run only if the state of the Pipeline has changed'
                echo 'For example, if the Pipeline was previously failing but is now successful'
            }
    }
}