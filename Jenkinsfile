pipeline {
    agent { label 'node1' }

    stages {
        stage('Build & Run') {
            steps {
                sh '''#!/bin/bash
                    sudo docker images
                    '''      
            }
        }

    }
}
