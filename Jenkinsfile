pipeline {

    agent any

    stages {

        stage('Setup Python Environment') {
            steps {
                bat '"C:\\Users\\LongStay\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m venv venv'
                bat 'call venv\\Scripts\\activate && python -m pip install --upgrade pip'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'call venv\\Scripts\\activate && pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'call venv\\Scripts\\activate && pytest --alluredir=allure-results'
            }
        }
    }

    post {

        always {

            allure([
                includeProperties: false,
                jdk: '',
                results: [[path: 'allure-results']]
            ])

            publishHTML([
                allowMissing: true,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'reports',
                reportFiles: 'report.html',
                reportName: 'Pytest HTML Report'
            ])
        }
    }
}