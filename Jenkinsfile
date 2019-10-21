#!/usr/bin/env groovy
pipeline {
    agent any
    stages{
        stage ('check git') {
            steps{
                git poll: true, url: 'https://github.com/juaneml/prueba_travis.git' 
            }
        }
    }
}

  
