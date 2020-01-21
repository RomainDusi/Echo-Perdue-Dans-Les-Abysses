pipeline {
    agent none 
    stages {
        stage('Test'){
            agent any
            steps {
                sh 'ls'
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
                script {
                    sh 'pwd'
                    sh 'ls'
                    sh 'ls /Users/romain/.jenkins/workspace/Test_master'
                    sh 'ls /Users/romain/.jenkins/workspace/Test_master/'
                    def MyFile = new File('Echo.py')
                    def FileText = MyFile.text
                    FileText.find("Version")
                }
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
