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
                    image 'python:latest' 
                }
            }
            steps {
                script {
                    sh 'ls /Users/romain/.jenkins/workspace/Test_master/'
                    def MyFile = new File('/Users/romain/.jenkins/workspace/Test_master/Echo.py')
                    def FileText = MyFile.text
                    print FileText
                    echo FileText.indexOf("Version")
                    echo FileText.readLines().get(2)
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
