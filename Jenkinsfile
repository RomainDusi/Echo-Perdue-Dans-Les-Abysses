pipeline {
    agent none 
    stages {
        stage('Test'){
            agent any
            steps {
                sh 'ls'
                def FileVersion = readJSON file: "Echo.py"
                FileVersion.each { key, value ->
                    echo "Walked through key $key and value $value"
                }
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
