pipeline {
  agent none
  stages {
    stage("flake8") {
      agent {
        dockerfile {
          filename 'jenkins/Dockerfile.test'
          reuseNode true
        }
      }
      when {
        // expression { env.BRANCH_NAME =~ "(.*)-patch-*" }
        expression { env.BRANCH_NAME =~ "PR-*" }
      }
      steps {
        echo env.BRANCH_NAME
        sh 'pytest Testpytest.py'
        // sh "pytest app.py"
      }
    }
  }
}
