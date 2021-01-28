pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                script{
                    python test.py
                }
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
