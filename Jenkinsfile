pipeline {
    agent {label 'node1'}

    stages {
        stage("Build"){
            steps{
                sh '''#!/bin/bash
                    sudo docker build /home/ubuntu/workspace/Pipeline1 -t aleksnd19/assignment
                    '''   
            }
        }
        stage("Run"){
            steps{
                sh '''#!/bin/bash
                    sudo docker run -d -p 8000:8000 aleksnd19/assignment
                    '''  
            }
        }
        stage("Push"){
            steps{
                sh '''#!/bin/bash
                    sudo docker push aleksnd19/assignment
                    '''  
            }
        }

    }
}
