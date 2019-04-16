pipeline {
  agent any
  environment {
    PACKAGE_NAME = 'dummy_jenkins'
    ROS_WORKSPACE = "${WORKSPACE}_ws"
  }
  stages {
    stage('Setup') {
      steps {
        sh 'printenv'
        sh """
          mkdir -p ${ROS_WORKSPACE}/src
          cp -R . ${ROS_WORKSPACE}/src/${PACKAGE_NAME}
        """
      }
    }
    stage('Build') {
      steps {
        dir(path: "${ROS_WORKSPACE}") {
          sh '''
            . /opt/ros/kinetic/setup.sh
            catkin_make
          '''
        }

      }
}

    stage('Test') {
      steps {
        dir(path: "${ROS_WORKSPACE}") {
          sh '''
            . /opt/ros/kinetic/setup.sh
            . /home/hadi/catkin_ws/devel/setup.sh
            cd /home/hadi/catkin_ws/src/localizer_dwm1001/test/
            ./run_tests.sh
          '''
        }
      }
}

}

}