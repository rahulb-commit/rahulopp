pipeline {
    agent any

    stages {
        stage('Initialize') {
            steps {
                echo 'Starting Build for Rahul...'
                // This will list the root files so you can see the folders
                bat 'dir'
            }
        }

        stage('Python Automation') {
            steps {
                // dir() enters the folder shown in your 1.png
                dir('python-selenium-sample-master') {
                    script {
                        echo 'Checking folder contents...'
                        bat 'dir' // Safety check: ensures lambdatest.py is visible here
                        
                        echo 'Installing Selenium and dependencies...'
                        // We use --user or a virtual env if permissions are tight
                        // Based on 2.png, the file is just named 'requirements'
                        bat 'pip install -r requirements'
                        
                        echo 'Executing LambdaTest Script...'
                        // Based on 2.png, the filename is lambdatest.py
                        bat 'python lambdatest.py'
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Build finished.'
        }
        success {
            echo 'Success! Your Selenium tests passed.'
        }
        failure {
            echo 'Failed! Check the logs to see if Python or the Script crashed.'
        }
    }
}