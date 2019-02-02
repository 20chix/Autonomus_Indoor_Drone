# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "move_quadcopter: 7 messages, 0 services")

set(MSG_I_FLAGS "-Imove_quadcopter:/home/hadi/catkin_ws/devel/share/move_quadcopter/msg;-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg;-Igeometry_msgs:/opt/ros/kinetic/share/geometry_msgs/cmake/../msg;-Iactionlib_msgs:/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(move_quadcopter_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateFeedback.msg" NAME_WE)
add_custom_target(_move_quadcopter_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "move_quadcopter" "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateFeedback.msg" ""
)

get_filename_component(_filename "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateActionFeedback.msg" NAME_WE)
add_custom_target(_move_quadcopter_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "move_quadcopter" "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateActionFeedback.msg" "move_quadcopter/NavigateFeedback:actionlib_msgs/GoalID:std_msgs/Header:actionlib_msgs/GoalStatus"
)

get_filename_component(_filename "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateAction.msg" NAME_WE)
add_custom_target(_move_quadcopter_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "move_quadcopter" "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateAction.msg" "std_msgs/Header:move_quadcopter/NavigateActionResult:move_quadcopter/NavigateGoal:geometry_msgs/Point:move_quadcopter/NavigateActionGoal:move_quadcopter/NavigateFeedback:actionlib_msgs/GoalID:move_quadcopter/NavigateActionFeedback:move_quadcopter/NavigateResult:actionlib_msgs/GoalStatus"
)

get_filename_component(_filename "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateResult.msg" NAME_WE)
add_custom_target(_move_quadcopter_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "move_quadcopter" "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateResult.msg" "geometry_msgs/Point"
)

get_filename_component(_filename "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateActionResult.msg" NAME_WE)
add_custom_target(_move_quadcopter_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "move_quadcopter" "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateActionResult.msg" "geometry_msgs/Point:actionlib_msgs/GoalID:std_msgs/Header:move_quadcopter/NavigateResult:actionlib_msgs/GoalStatus"
)

get_filename_component(_filename "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateGoal.msg" NAME_WE)
add_custom_target(_move_quadcopter_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "move_quadcopter" "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateGoal.msg" "geometry_msgs/Point"
)

get_filename_component(_filename "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateActionGoal.msg" NAME_WE)
add_custom_target(_move_quadcopter_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "move_quadcopter" "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateActionGoal.msg" "move_quadcopter/NavigateGoal:actionlib_msgs/GoalID:std_msgs/Header:geometry_msgs/Point"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(move_quadcopter
  "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/move_quadcopter
)
_generate_msg_cpp(move_quadcopter
  "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateFeedback.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/move_quadcopter
)
_generate_msg_cpp(move_quadcopter
  "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateAction.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateActionResult.msg;/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateGoal.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateActionGoal.msg;/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateFeedback.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateActionFeedback.msg;/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateResult.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/move_quadcopter
)
_generate_msg_cpp(move_quadcopter
  "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/move_quadcopter
)
_generate_msg_cpp(move_quadcopter
  "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateGoal.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/move_quadcopter
)
_generate_msg_cpp(move_quadcopter
  "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/move_quadcopter
)
_generate_msg_cpp(move_quadcopter
  "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateActionResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateResult.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/move_quadcopter
)

### Generating Services

### Generating Module File
_generate_module_cpp(move_quadcopter
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/move_quadcopter
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(move_quadcopter_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(move_quadcopter_generate_messages move_quadcopter_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateFeedback.msg" NAME_WE)
add_dependencies(move_quadcopter_generate_messages_cpp _move_quadcopter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateActionFeedback.msg" NAME_WE)
add_dependencies(move_quadcopter_generate_messages_cpp _move_quadcopter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateAction.msg" NAME_WE)
add_dependencies(move_quadcopter_generate_messages_cpp _move_quadcopter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateResult.msg" NAME_WE)
add_dependencies(move_quadcopter_generate_messages_cpp _move_quadcopter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateActionResult.msg" NAME_WE)
add_dependencies(move_quadcopter_generate_messages_cpp _move_quadcopter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateGoal.msg" NAME_WE)
add_dependencies(move_quadcopter_generate_messages_cpp _move_quadcopter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateActionGoal.msg" NAME_WE)
add_dependencies(move_quadcopter_generate_messages_cpp _move_quadcopter_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(move_quadcopter_gencpp)
add_dependencies(move_quadcopter_gencpp move_quadcopter_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS move_quadcopter_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(move_quadcopter
  "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/move_quadcopter
)
_generate_msg_eus(move_quadcopter
  "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateFeedback.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/move_quadcopter
)
_generate_msg_eus(move_quadcopter
  "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateAction.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateActionResult.msg;/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateGoal.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateActionGoal.msg;/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateFeedback.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateActionFeedback.msg;/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateResult.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/move_quadcopter
)
_generate_msg_eus(move_quadcopter
  "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/move_quadcopter
)
_generate_msg_eus(move_quadcopter
  "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateGoal.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/move_quadcopter
)
_generate_msg_eus(move_quadcopter
  "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/move_quadcopter
)
_generate_msg_eus(move_quadcopter
  "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateActionResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateResult.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/move_quadcopter
)

### Generating Services

### Generating Module File
_generate_module_eus(move_quadcopter
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/move_quadcopter
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(move_quadcopter_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(move_quadcopter_generate_messages move_quadcopter_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateFeedback.msg" NAME_WE)
add_dependencies(move_quadcopter_generate_messages_eus _move_quadcopter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateActionFeedback.msg" NAME_WE)
add_dependencies(move_quadcopter_generate_messages_eus _move_quadcopter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateAction.msg" NAME_WE)
add_dependencies(move_quadcopter_generate_messages_eus _move_quadcopter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateResult.msg" NAME_WE)
add_dependencies(move_quadcopter_generate_messages_eus _move_quadcopter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateActionResult.msg" NAME_WE)
add_dependencies(move_quadcopter_generate_messages_eus _move_quadcopter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateGoal.msg" NAME_WE)
add_dependencies(move_quadcopter_generate_messages_eus _move_quadcopter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateActionGoal.msg" NAME_WE)
add_dependencies(move_quadcopter_generate_messages_eus _move_quadcopter_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(move_quadcopter_geneus)
add_dependencies(move_quadcopter_geneus move_quadcopter_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS move_quadcopter_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(move_quadcopter
  "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/move_quadcopter
)
_generate_msg_lisp(move_quadcopter
  "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateFeedback.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/move_quadcopter
)
_generate_msg_lisp(move_quadcopter
  "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateAction.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateActionResult.msg;/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateGoal.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateActionGoal.msg;/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateFeedback.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateActionFeedback.msg;/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateResult.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/move_quadcopter
)
_generate_msg_lisp(move_quadcopter
  "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/move_quadcopter
)
_generate_msg_lisp(move_quadcopter
  "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateGoal.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/move_quadcopter
)
_generate_msg_lisp(move_quadcopter
  "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/move_quadcopter
)
_generate_msg_lisp(move_quadcopter
  "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateActionResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateResult.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/move_quadcopter
)

### Generating Services

### Generating Module File
_generate_module_lisp(move_quadcopter
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/move_quadcopter
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(move_quadcopter_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(move_quadcopter_generate_messages move_quadcopter_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateFeedback.msg" NAME_WE)
add_dependencies(move_quadcopter_generate_messages_lisp _move_quadcopter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateActionFeedback.msg" NAME_WE)
add_dependencies(move_quadcopter_generate_messages_lisp _move_quadcopter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateAction.msg" NAME_WE)
add_dependencies(move_quadcopter_generate_messages_lisp _move_quadcopter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateResult.msg" NAME_WE)
add_dependencies(move_quadcopter_generate_messages_lisp _move_quadcopter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateActionResult.msg" NAME_WE)
add_dependencies(move_quadcopter_generate_messages_lisp _move_quadcopter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateGoal.msg" NAME_WE)
add_dependencies(move_quadcopter_generate_messages_lisp _move_quadcopter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateActionGoal.msg" NAME_WE)
add_dependencies(move_quadcopter_generate_messages_lisp _move_quadcopter_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(move_quadcopter_genlisp)
add_dependencies(move_quadcopter_genlisp move_quadcopter_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS move_quadcopter_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(move_quadcopter
  "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/move_quadcopter
)
_generate_msg_nodejs(move_quadcopter
  "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateFeedback.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/move_quadcopter
)
_generate_msg_nodejs(move_quadcopter
  "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateAction.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateActionResult.msg;/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateGoal.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateActionGoal.msg;/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateFeedback.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateActionFeedback.msg;/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateResult.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/move_quadcopter
)
_generate_msg_nodejs(move_quadcopter
  "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/move_quadcopter
)
_generate_msg_nodejs(move_quadcopter
  "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateGoal.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/move_quadcopter
)
_generate_msg_nodejs(move_quadcopter
  "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/move_quadcopter
)
_generate_msg_nodejs(move_quadcopter
  "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateActionResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateResult.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/move_quadcopter
)

### Generating Services

### Generating Module File
_generate_module_nodejs(move_quadcopter
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/move_quadcopter
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(move_quadcopter_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(move_quadcopter_generate_messages move_quadcopter_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateFeedback.msg" NAME_WE)
add_dependencies(move_quadcopter_generate_messages_nodejs _move_quadcopter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateActionFeedback.msg" NAME_WE)
add_dependencies(move_quadcopter_generate_messages_nodejs _move_quadcopter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateAction.msg" NAME_WE)
add_dependencies(move_quadcopter_generate_messages_nodejs _move_quadcopter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateResult.msg" NAME_WE)
add_dependencies(move_quadcopter_generate_messages_nodejs _move_quadcopter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateActionResult.msg" NAME_WE)
add_dependencies(move_quadcopter_generate_messages_nodejs _move_quadcopter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateGoal.msg" NAME_WE)
add_dependencies(move_quadcopter_generate_messages_nodejs _move_quadcopter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateActionGoal.msg" NAME_WE)
add_dependencies(move_quadcopter_generate_messages_nodejs _move_quadcopter_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(move_quadcopter_gennodejs)
add_dependencies(move_quadcopter_gennodejs move_quadcopter_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS move_quadcopter_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(move_quadcopter
  "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/move_quadcopter
)
_generate_msg_py(move_quadcopter
  "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateFeedback.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/move_quadcopter
)
_generate_msg_py(move_quadcopter
  "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateAction.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateActionResult.msg;/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateGoal.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateActionGoal.msg;/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateFeedback.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateActionFeedback.msg;/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateResult.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/move_quadcopter
)
_generate_msg_py(move_quadcopter
  "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/move_quadcopter
)
_generate_msg_py(move_quadcopter
  "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateGoal.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/move_quadcopter
)
_generate_msg_py(move_quadcopter
  "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/move_quadcopter
)
_generate_msg_py(move_quadcopter
  "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateActionResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateResult.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/move_quadcopter
)

### Generating Services

### Generating Module File
_generate_module_py(move_quadcopter
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/move_quadcopter
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(move_quadcopter_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(move_quadcopter_generate_messages move_quadcopter_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateFeedback.msg" NAME_WE)
add_dependencies(move_quadcopter_generate_messages_py _move_quadcopter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateActionFeedback.msg" NAME_WE)
add_dependencies(move_quadcopter_generate_messages_py _move_quadcopter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateAction.msg" NAME_WE)
add_dependencies(move_quadcopter_generate_messages_py _move_quadcopter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateResult.msg" NAME_WE)
add_dependencies(move_quadcopter_generate_messages_py _move_quadcopter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateActionResult.msg" NAME_WE)
add_dependencies(move_quadcopter_generate_messages_py _move_quadcopter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateGoal.msg" NAME_WE)
add_dependencies(move_quadcopter_generate_messages_py _move_quadcopter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/hadi/catkin_ws/devel/share/move_quadcopter/msg/NavigateActionGoal.msg" NAME_WE)
add_dependencies(move_quadcopter_generate_messages_py _move_quadcopter_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(move_quadcopter_genpy)
add_dependencies(move_quadcopter_genpy move_quadcopter_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS move_quadcopter_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/move_quadcopter)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/move_quadcopter
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(move_quadcopter_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()
if(TARGET geometry_msgs_generate_messages_cpp)
  add_dependencies(move_quadcopter_generate_messages_cpp geometry_msgs_generate_messages_cpp)
endif()
if(TARGET actionlib_msgs_generate_messages_cpp)
  add_dependencies(move_quadcopter_generate_messages_cpp actionlib_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/move_quadcopter)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/move_quadcopter
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(move_quadcopter_generate_messages_eus std_msgs_generate_messages_eus)
endif()
if(TARGET geometry_msgs_generate_messages_eus)
  add_dependencies(move_quadcopter_generate_messages_eus geometry_msgs_generate_messages_eus)
endif()
if(TARGET actionlib_msgs_generate_messages_eus)
  add_dependencies(move_quadcopter_generate_messages_eus actionlib_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/move_quadcopter)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/move_quadcopter
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(move_quadcopter_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()
if(TARGET geometry_msgs_generate_messages_lisp)
  add_dependencies(move_quadcopter_generate_messages_lisp geometry_msgs_generate_messages_lisp)
endif()
if(TARGET actionlib_msgs_generate_messages_lisp)
  add_dependencies(move_quadcopter_generate_messages_lisp actionlib_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/move_quadcopter)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/move_quadcopter
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(move_quadcopter_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()
if(TARGET geometry_msgs_generate_messages_nodejs)
  add_dependencies(move_quadcopter_generate_messages_nodejs geometry_msgs_generate_messages_nodejs)
endif()
if(TARGET actionlib_msgs_generate_messages_nodejs)
  add_dependencies(move_quadcopter_generate_messages_nodejs actionlib_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/move_quadcopter)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/move_quadcopter\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/move_quadcopter
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(move_quadcopter_generate_messages_py std_msgs_generate_messages_py)
endif()
if(TARGET geometry_msgs_generate_messages_py)
  add_dependencies(move_quadcopter_generate_messages_py geometry_msgs_generate_messages_py)
endif()
if(TARGET actionlib_msgs_generate_messages_py)
  add_dependencies(move_quadcopter_generate_messages_py actionlib_msgs_generate_messages_py)
endif()
