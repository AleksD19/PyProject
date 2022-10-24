pipeline {
    agent {label 'node1'}

    stages {
        stage('Build & Run') {
            steps {
                sh '''#!/bin/bash
                    sudo docker rm -f $(sudo docker ps -a -q)
                    '''     
                sh '''#!/bin/bash
                    sudo docker build /home/jenkins/workspace/Pipeline1 -t aleknd19/test
                    '''   
            }
        }

    }
}
