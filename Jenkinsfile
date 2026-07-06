pipeline {
    agent any
    
    stages {
        stage('1. Code Pull') {
            steps {
                echo 'Pulling HTML, CSS, and JS files from local Git repository...'
                checkout scm
            }
        }

        stage('2. SonarQube Quality Analysis') {
            steps {
                echo 'Sending web application files to local SonarQube dashboard...'
                withSonarQubeEnv('Local-SonarQube') {
                    // Instructs SonarQube to parse HTML, CSS, and Javascript files
                    sh 'sonar-scanner -Dsonar.projectKey=web-login-pipeline -Dsonar.sources=.'
                }
            }
        }

        stage('3. Verify Code Integrity') {
            steps {
                echo 'Verifying core assets exist on the local system...'
                // Simple checks to ensure your web server files are structurally sound
                sh 'test -f index.html'
                sh 'test -f style.css'
                sh 'test -f app.js'
                echo '🚀 PIPELINE SUCCESS: Web assets verified and quality scanned!'
            }
        }
    }
}