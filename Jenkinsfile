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
        expression { env.BRANCH_NAME =~ "develop-patch-*" }
      }
      steps {
        sh 'echo "Test Complete"'
        echo env.BRANCH_NAME
      }
    }
  }
}
