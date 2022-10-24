pipeline {
    agent {label 'node1'}

    stages {
        stage("Build"){
            steps{
                sh '''#!/bin/bash
                    sudo docker build /home/ubuntu/workspace/Pipeline1 -t aleknd19/test
                    '''   
            }
        }
        stage("Run"){
            steps{
                sh '''#!/bin/bash
                    sudo docker run -d -p 8000:80 aleksnd19/test
                    '''  
            }
        }

    }
}
