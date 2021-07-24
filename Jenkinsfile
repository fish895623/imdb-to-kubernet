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
        sh "pytest Transormer.py"
      }
    }
  }
}
