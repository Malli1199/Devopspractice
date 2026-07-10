pipeline {
    agent any

    stages {
        stage('1. Environment Pre-Check') {
            steps {
                echo '=== SYSTEM INFORMATION ==='
                // Prints the version of Windows and user context to the logs
                bat 'ver'
                bat 'whoami'
            }
        }

        stage('2. Verify Web Project Files') {
            steps {
                echo '=== CHECKING WORKSPACE ASSETS ==='
                // Checks if your HTML page exists in the pulled repository folder
                bat 'if exist index.html (echo "✅ SUCCESS: index.html is present!") else (echo "❌ ERROR: index.html missing!" && exit 1)'
                
                // Checks if your JavaScript configuration file exists
                bat 'if exist app.js (echo "✅ SUCCESS: app.js is present!") else (echo "❌ ERROR: app.js missing!" && exit 1)'
            }
        }
    }
}