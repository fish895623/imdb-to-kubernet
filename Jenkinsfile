pipeline {
  agent none
  stages {
    stage("Test") {
      agent {
        dockerfile {
          filename 'Dockerfile.dev'
        }
      }
      when { branch pattern: "patch-*", comparator: "REGEXP" }
      steps {
        sh 'echo "Test Complete"'
      }
    }
  }
}
