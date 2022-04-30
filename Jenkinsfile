pipeline{
    agent any
     stages {
        stage('UiAutoTestHmtt') {
            steps {
                bat 'pytest'
            }
        }
     }
     stages {
        stage('AllureReport') {
            steps {
                 allure includeProperties: false, jdk: 'jdk-12.0.2', results: [[path: 'report/result']]
            }
        }
     }
    post {
        always {
            junit 'report/junitxml'
            emailext body: '''<html>
                                    <h1>total cases: ${TEST_COUNTS,var="total"}</h1>
                              </html>''',
                     subject: '',
                     to: '2650116409@qq.com'
        }
    }
}