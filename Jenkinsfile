pipeline {
    agent any

    stages {
        stage('Build & Run') {
            steps {
                sudo docker rm -f $(sudo docker ps -a -q)
                sudo docker build /home/jenkins/workspace/job3 -t aleknd19/test
                sudo docker run -d -p 8000:80 aleknd19/test
            }
        }

    }
}
