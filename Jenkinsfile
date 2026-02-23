pipeline {
    agent any

    stages {
        stage('Initialize') {
            steps {
                echo 'Starting Build for Rahul...'
                // Verifying root directory structure
                bat 'dir'
            }
        }

        stage('Python Automation') {
            steps {
                // Entering the subfolder identified in your logs
                dir('python-selenium-sample-master') {
                    script {
                        echo 'Installing Selenium and dependencies...'
                        // Corrected: Added .txt to match your actual file system
                        bat 'pip install -r requirements.txt'
                        
                        echo 'Executing LambdaTest Script...'
                        // Running the script found in your repository
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
            echo 'Success! Your Selenium tests executed.'
        }
        failure {
            echo 'Failed! Please check the console output for Python errors.'
        }
    }
}