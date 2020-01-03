pipeline {
    agent none 
    stages {
        stage('Test'){
            agent any
            steps {
                sh 'ls'
            }
        }
        stage('Build') { 
            agent {
                docker {
                    image 'python:2-alpine' 
                }
            }
            steps {
                sh 'python -m py_compile Echo.py' 
            }
        }
    }
    post {
        success {
            echo 'I guess it worked well !'
        }
        failure {
            echo 'Mission failed, will retry later ;('
        }
    }
}
