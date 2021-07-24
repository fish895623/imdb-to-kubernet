pipeline {
  agent none
  stages {
    stage("Test") {
      agent {
        dockerfile {
          filename 'Dockerfile.dev'
        }
      }
      when {
        allOf{
          expression{env.BRANCH_NAME =~ /+patch+/}
        }
      }
      steps {
        sh 'echo "Test Complete"'
      }
    }
  }
}
