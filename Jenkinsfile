pipeline {
    agent any
    
    // 🔌 The correct internal Jenkins identifier is 'sonar-scanner'
    tools {
        'sonar-scanner' 'SonarQube-Server-Config-Name' // Must match the Name field you set in Jenkins Tools UI exactly!
    }
    
    stages {
        stage('1. SonarQube Quality Analysis') {
            steps {
                echo 'Sending web application files to local SonarQube dashboard...'
                withSonarQubeEnv('SonarQube-Server-Config-Name') { 
                    bat 'sonar-scanner -Dsonar.projectKey=web-login-pipeline -Dsonar.sources=.'
                }
            }
        }

        stage('2. Verify Code Integrity') {
            steps {
                echo 'Verifying core web assets exist locally...'
                bat 'if exist index.html (echo index.html found) else (echo index.html missing && exit 1)'
                bat 'if exist style.css (echo style.css found) else (echo style.css missing && exit 1)'
                bat 'if exist app.js (echo app.js found) else (echo app.js missing && exit 1)'
            }
        }
    }
}