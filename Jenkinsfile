#!/usr/bin/env groovy
pipeline {
    agent any
    stages{
        stage ('check git') {
            steps{
                git poll: true, url: 'git@github.com:juaneml/prueba_travis.git' 
            }
        }
    }
}

  
