pipeline {
    agent any 

    stages {
        stage('Build') {
            steps {
                echo 'Building your application...'
                // Add your build commands here (e.g., sh 'npm install' or sh './mvnw install')
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
                // Add your test commands here (e.g., sh 'npm test')
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying application...'
            }
        }
    }
}