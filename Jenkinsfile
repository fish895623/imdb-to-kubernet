pipeline {
  agent any
  stages {
    stage("Test") {
      agent {
        docker { dockerfile Dockerfile.dev }
      }
      steps {
        sh 'echo "Test Complete"'
      }
    }
  }
}
