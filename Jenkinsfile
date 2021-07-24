pipeline {
  agent any
  stages {
    stage("Test") {
      agent {
        dockerfile
        filename 'Dockerfile.dev'
      }
    steps {
        sh 'echo "Test Complete"'
      }
    }
  }
}
