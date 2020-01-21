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
                    def dir = new File("path_to_parent_dir")
                    dir.eachFileRecurse (FileType.FILES) { file ->
                        list << file
                    }
                    list.each {
                        println it.path
                    }
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
