pipeline {
    agent none 
    stages {
        stage('Test'){
            agent any
            steps {
                sh 'ls'
                sh "cat Echo.py"
                input 'Is everything OK ?'
            }
        }
        stage('Build') { 
            agent {
                docker {
                    image 'python:latest' 
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
