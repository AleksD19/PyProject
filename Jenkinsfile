pipeline {
    agent {label 'node1'}

    stages {
        stage('Build & Run') {
            steps {
       
                sh '''#!/bin/bash
                    sudo docker build /home/ubuntu/workspace/Pipeline1 -t aleknd19/test
                    '''   
            }
        }

    }
}

