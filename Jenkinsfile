pipeline {
  agent none
  stages {
    stage("Test") {
      // agent {
      //   dockerfile {
      //     filename 'jenkins/Dockerfile.test'
      //   }
      // }
      agent any
      when {
        expression { env.BRANCH_NAME =~ "(.*)-patch-*" }
      }
      steps {
        sh 'echo "Test Complete"'
        echo env.BRANCH_NAME
      }
    }
  }
}
