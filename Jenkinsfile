pipeline {
    agent any

    environment {
        // Pulls your credentials from Jenkins
        LT_USERNAME = credentials('LT_USER')
        LT_ACCESS_KEY = credentials('LT_KEY')
        
        // This overrides the 'test' name that caused the platform conflict
        LT_PROJECT_NAME = "Rahul_Selenium_Web_Project"
        LT_BUILD_NAME = "Jenkins_Build_${BUILD_NUMBER}"
    }

    stages {
        stage('Initialize') {
            steps {
                echo "Preparing environment for Rahul - Build #${env.BUILD_NUMBER}"
                bat 'dir'
            }
        }

        stage('Python Automation') {
            steps {
                dir('python-selenium-sample-master') {
                    script {
                        echo 'Installing dependencies from requirements.txt...'
                        bat 'pip install -r requirements.txt'
                        
                        echo 'Executing LambdaTest Automation Script...'
                        // We pass the new project name via environment variables
                        bat 'python lambdatest.py'
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline Execution Finished.'
        }
        success {
            echo 'SUCCESS: The Selenium tests ran on LambdaTest!'
        }
        failure {
            echo 'FAILURE: Check the logs. If project name conflict persists, edit lambdatest.py manually.'
        }
    }
}