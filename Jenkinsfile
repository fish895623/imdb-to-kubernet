pipeline {
  agent none
  stages {
    stage("Test") {
      agent {
        dockerfile {
          filename 'jenkins/Dockerfile.test'
        }
      }
      when { branch pattern: "*-patch-*", comparator: "REGEXP" }
      steps {
        sh 'echo "Test Complete"'
      }
    }
  }
}
