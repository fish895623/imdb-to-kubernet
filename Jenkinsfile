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
        sh "sh jenkins/launch.sh pylint"
      }
    }
  }
}
