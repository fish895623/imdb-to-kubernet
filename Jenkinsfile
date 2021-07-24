pipeline {
  agent none
  stages {
    stage("Test") {
      agent {
        dockerfile {
          filename 'jenkins/Dockerfile.test'
        }
      }
      when { branch pattern: "/[a-z]{3,6}/", comparator: "REGEXP" }
      steps {
        sh 'echo "Test Complete"'
        echo env.BRANCH_NAME
      }
    }
  }
}
