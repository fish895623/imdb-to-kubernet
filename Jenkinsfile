pipeline {
  agent none
  stages {
    stage("Test") {
      agent {
        dockerfile {
          filename 'jenkins/Dockerfile.test'
        }
      }
      when { branch pattern: "/develop-patch-\d{0,}-\d{0,}/", comparator: "REGEXP" }
      steps {
        sh 'echo "Test Complete"'
        echo env.BRANCH_NAME
      }
    }
  }
}
