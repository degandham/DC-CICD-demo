pipeline {
  agent {
    node {
      label 'master'
    }
    environment {
      BUILD_VERSION = "env.${BUILD_ID}"
    }
  }
  stages {
    stage('DEV') {
      steps {
        git(url: 'https://github.com/degandham/DC-CICD-demo', branch: 'master', changelog: true, poll: true)
        echo '${BUILD_VERSION}'
        echo 'Build the Docker Image of the Demo application'
      }
    }
    stage('TEST') {
      steps {
        echo 'Create AWS ECS "TEST" Environment'
        echo 'Deploy Docker Image to TEST Environment'
        echo 'Run Selenium Functional Tests in the TEST Environment'
        echo 'Run JMeter Performance tests in the TEST Environment'
      }
    }
    stage('STAGE') {
      steps {
        echo 'Create AWS ECS "STAGE" Environment'
        echo 'Deploy Docker Image to STAGE Environment'
        echo 'Run Selenium Functional Tests in the STAGE Environment'
        echo 'Run JMeter Performance tests in the STAGE Environment'
      }
    }
    stage('PROD') {
      steps {
        echo 'Create AWS ECS "PROD" Environment'
        echo 'Deploy Docker Image to the PROD Environment'
        echo 'Run Selenium Functional Tests in the PROD Environment'
      }
    }
  }
}
