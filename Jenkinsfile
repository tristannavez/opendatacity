pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                    sh ' python test.py'
               
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
