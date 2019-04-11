pipeline {
    agent any
    stages {
        stage('Source_Into_ROS') {
            steps {
                timeout(time: 1, unit: 'MINUTES') {
                    sh '/home/hadi/catkin_ws/src/jenkins/source.sh'
                }
            }
        }
        stage('Compile') {
            steps {
                timeout(time: 1, unit: 'MINUTES') {
                    sh '/home/hadi/catkin_ws/src/jenkins/1_source.sh'
                }
            }
        }
        stage('Compile') {
            steps {
                timeout(time: 1, unit: 'MINUTES') {
                    sh '/home/hadi/catkin_ws/src/jenkins/2_catkin_make.sh'
                }
            }
        }
        stage('Run_dwm1001') {
            steps {
                timeout(time: 1, unit: 'MINUTES') {
                    sh '/home/hadi/catkin_ws/src/jenkins/3_launch_dwm1001.sh'
                }
            }
        }
        stage('Run_joy') {
            steps {
                timeout(time: 1, unit: 'MINUTES') {
                    sh '/home/hadi/catkin_ws/src/jenkins/4_launch_joy.sh'
                }
            }
        }
        stage('Run_gazebo') {
            steps {
                timeout(time: 3, unit: 'MINUTES') {
                    sh '/home/hadi/catkin_ws/src/jenkins/5_launch_tum_simulator.sh'
                }
            }
        }
        stage('Run_unittest') {
            steps {
                timeout(time: 1, unit: 'MINUTES') {
                    sh '/home/hadi/catkin_ws/src/localizer_dwm1001/run_tests.sh'
                }
            }
        }
    }
}
