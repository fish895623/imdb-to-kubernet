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
        // expression { env.BRANCH_NAME =~ "(.*)-patch-*" }
        expression { env.BRANCH_NAME =~ "PR-*" }
      }
      steps {
        echo env.BRANCH_NAME
        sh 'python3 Transformer.py'
        // sh "pytest app.py"
      }
    }
  }
}
