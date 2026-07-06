pipeline{
        agent any{
             stages{
                 stage('1.pull code'){
                      steps{
                           echo 'pulling the code from github'
                           checkout scm
                     }
                   }
                  stage('2.SonarQube code quality gate checking'){
                       steps{
                             echo 'Inspecting the code by sonarqube'
                             withSonarQubeEnv('Local-SonarQube'){
                                          sh 'sonar-scanner -Dsonar.projectKey=practicing_pipeline -Dsonar=.'
                                     }
                             }
                   }
                stage('3.Verifying code Integrity'){
                     steps{
                          echo 'Verifying the core assets'
                          sh 'test -f index.html'
                          sh 'test -f style.css'
                          sh 'test -f app.js'
                          echo 'pipeline sucess'
                      }
                 }
         }
}