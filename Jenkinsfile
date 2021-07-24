pipeline {
  agent none
  stages {
    stage("Test") {
      agent {
        dockerfile {
          filename 'jenkins/Dockerfile.test'
        }
      }
      when {
        expression { env.BRANCH_NAME =~ "/develop-patch-\d{0,}-\d{0,}/" }
      }
      steps {
        sh 'echo "Test Complete"'
        echo env.BRANCH_NAME
      }
    }
  }
}
