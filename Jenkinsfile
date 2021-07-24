pipeline {
  agent none
  stages {
    stage("pylint") {
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
        sh 'find . -type f -name "*.py" -exec python3 -m pylint {} \;'
      }
    }
  }
}
