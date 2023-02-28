pipeline {
    agent any

    environment{
        PATH = 'C:\\WINDOWS\\system32;C:\\Users\\ELIOT\\AppData\\Local\\Programs\\Git\\bin;C:\\Program Files\\Docker\\Docker\\resources\\bin;C:\\Users\\ELIOT\\AppData\\Local\\Programs\\Python\\Python39\\;C:\\Users\\ELIOT\\AppData\\Local\\Programs\\Python\\Python39\\Scripts;C:\\Users\\ELIOT\\AppData\\Local\\Programs\\Python\\Python39\\python.exe'
        dockerhub = credentials('dockerhub')
    }

    stages { 
        stage('Checkout') {
            steps {
                bat "git branch staging"
                bat "git checkout staging"
                bat "git push origin staging"
            }
        }
        stage('Install and test') {
            steps {
                bat "pip install -r requirements.txt"
                bat "python -m unittest"
            }
        }
        stage('Deploying') {
            parallel {
                stage('Docker Image Building'){
                    steps {
                        bat "docker build -t dockerfile ."
                        bat "docker logout"
                        bat "docker login -u=$dockerhub_USR -p= docker.io"
                        bat "docker tag dockerfile eliott/dockerfile:dockerfile"
                        bat "docker push eliott/dockerfile:dockerfile"
                    }
                }
                stage('Merge branch'){
                    steps {
                        bat "git config --global user.email eliott.guedj@efrei.net"
                        bat "git checkout main"
                        bat "git merge staging"
                    }
                }
                
            }
        }
    }
    triggers {
        githubPush()
    }
    post{
        always{
            bat 'docker logout'
        }
    }
}
