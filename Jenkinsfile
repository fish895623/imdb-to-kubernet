pipeline {
  agent none
  stages {
    stage("pytest") {
      agent {
        dockerfile {
          filename 'jenkins/Dockerfile.test'
        }
      }
      when {
        expression { env.BRANCH_NAME =~ "(.*)-patch-*" }
      }
      steps {
        echo env.BRANCH_NAME
        sh "pytest app.py"
      }
    }
  }
}
