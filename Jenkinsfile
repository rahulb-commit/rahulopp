pipeline {
    agent any

    environment {
        // This links the Jenkins IDs you created in Step 1 to the Python script
        LT_USERNAME = credentials('LT_USER')
        LT_ACCESS_KEY = credentials('LT_KEY')
    }

    stages {
        stage('Initialize') {
            steps {
                echo 'Preparing environment for Rahul...'
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
                        // The script will now receive the credentials via environment variables
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
            echo 'FAILURE: Check the logs. Ensure LT_USER and LT_KEY are correct in Jenkins Credentials.'
        }
    }
}