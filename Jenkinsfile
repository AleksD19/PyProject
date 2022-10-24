pipeline {
    agent { label 'node1' }

    stages {
        stage('Build & Run') {
            steps {
                sh '''#!/bin/bash
                    hostname -i
                    '''      
            }
        }

    }
}
