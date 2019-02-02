# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "turtlesim_cleaner: 0 messages, 2 services")

set(MSG_I_FLAGS "-Igeometry_msgs:/opt/ros/kinetic/share/geometry_msgs/cmake/../msg;-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(turtlesim_cleaner_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/hadi/catkin_ws/src/turtlesim_cleaner/srv/MoveSquare.srv" NAME_WE)
add_custom_target(_turtlesim_cleaner_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "turtlesim_cleaner" "/home/hadi/catkin_ws/src/turtlesim_cleaner/srv/MoveSquare.srv" ""
)

get_filename_component(_filename "/home/hadi/catkin_ws/src/turtlesim_cleaner/srv/MoveCircle.srv" NAME_WE)
add_custom_target(_turtlesim_cleaner_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "turtlesim_cleaner" "/home/hadi/catkin_ws/src/turtlesim_cleaner/srv/MoveCircle.srv" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages

### Generating Services
_generate_srv_cpp(turtlesim_cleaner
  "/home/hadi/catkin_ws/src/turtlesim_cleaner/srv/MoveSquare.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/turtlesim_cleaner
)
_generate_srv_cpp(turtlesim_cleaner
  "/home/hadi/catkin_ws/src/turtlesim_cleaner/srv/MoveCircle.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/turtlesim_cleaner
)

### Generating Module File
_generate_module_cpp(turtlesim_cleaner
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/turtlesim_cleaner
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(turtlesim_cleaner_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(turtlesim_cleaner_generate_messages turtlesim_cleaner_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/hadi/catkin_ws/src/turtlesim_cleaner/srv/MoveSquare.srv" NAME_WE)
add_dependencies(turtlesim_cleaner_generate_messages_cpp _turtlesim_cleaner_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/hadi/catkin_ws/src/turtlesim_cleaner/srv/MoveCircle.srv" NAME_WE)
add_dependencies(turtlesim_cleaner_generate_messages_cpp _turtlesim_cleaner_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(turtlesim_cleaner_gencpp)
add_dependencies(turtlesim_cleaner_gencpp turtlesim_cleaner_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS turtlesim_cleaner_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages

### Generating Services
_generate_srv_eus(turtlesim_cleaner
  "/home/hadi/catkin_ws/src/turtlesim_cleaner/srv/MoveSquare.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/turtlesim_cleaner
)
_generate_srv_eus(turtlesim_cleaner
  "/home/hadi/catkin_ws/src/turtlesim_cleaner/srv/MoveCircle.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/turtlesim_cleaner
)

### Generating Module File
_generate_module_eus(turtlesim_cleaner
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/turtlesim_cleaner
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(turtlesim_cleaner_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(turtlesim_cleaner_generate_messages turtlesim_cleaner_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/hadi/catkin_ws/src/turtlesim_cleaner/srv/MoveSquare.srv" NAME_WE)
add_dependencies(turtlesim_cleaner_generate_messages_eus _turtlesim_cleaner_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/hadi/catkin_ws/src/turtlesim_cleaner/srv/MoveCircle.srv" NAME_WE)
add_dependencies(turtlesim_cleaner_generate_messages_eus _turtlesim_cleaner_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(turtlesim_cleaner_geneus)
add_dependencies(turtlesim_cleaner_geneus turtlesim_cleaner_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS turtlesim_cleaner_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages

### Generating Services
_generate_srv_lisp(turtlesim_cleaner
  "/home/hadi/catkin_ws/src/turtlesim_cleaner/srv/MoveSquare.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/turtlesim_cleaner
)
_generate_srv_lisp(turtlesim_cleaner
  "/home/hadi/catkin_ws/src/turtlesim_cleaner/srv/MoveCircle.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/turtlesim_cleaner
)

### Generating Module File
_generate_module_lisp(turtlesim_cleaner
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/turtlesim_cleaner
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(turtlesim_cleaner_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(turtlesim_cleaner_generate_messages turtlesim_cleaner_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/hadi/catkin_ws/src/turtlesim_cleaner/srv/MoveSquare.srv" NAME_WE)
add_dependencies(turtlesim_cleaner_generate_messages_lisp _turtlesim_cleaner_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/hadi/catkin_ws/src/turtlesim_cleaner/srv/MoveCircle.srv" NAME_WE)
add_dependencies(turtlesim_cleaner_generate_messages_lisp _turtlesim_cleaner_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(turtlesim_cleaner_genlisp)
add_dependencies(turtlesim_cleaner_genlisp turtlesim_cleaner_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS turtlesim_cleaner_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages

### Generating Services
_generate_srv_nodejs(turtlesim_cleaner
  "/home/hadi/catkin_ws/src/turtlesim_cleaner/srv/MoveSquare.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/turtlesim_cleaner
)
_generate_srv_nodejs(turtlesim_cleaner
  "/home/hadi/catkin_ws/src/turtlesim_cleaner/srv/MoveCircle.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/turtlesim_cleaner
)

### Generating Module File
_generate_module_nodejs(turtlesim_cleaner
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/turtlesim_cleaner
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(turtlesim_cleaner_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(turtlesim_cleaner_generate_messages turtlesim_cleaner_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/hadi/catkin_ws/src/turtlesim_cleaner/srv/MoveSquare.srv" NAME_WE)
add_dependencies(turtlesim_cleaner_generate_messages_nodejs _turtlesim_cleaner_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/hadi/catkin_ws/src/turtlesim_cleaner/srv/MoveCircle.srv" NAME_WE)
add_dependencies(turtlesim_cleaner_generate_messages_nodejs _turtlesim_cleaner_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(turtlesim_cleaner_gennodejs)
add_dependencies(turtlesim_cleaner_gennodejs turtlesim_cleaner_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS turtlesim_cleaner_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages

### Generating Services
_generate_srv_py(turtlesim_cleaner
  "/home/hadi/catkin_ws/src/turtlesim_cleaner/srv/MoveSquare.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/turtlesim_cleaner
)
_generate_srv_py(turtlesim_cleaner
  "/home/hadi/catkin_ws/src/turtlesim_cleaner/srv/MoveCircle.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/turtlesim_cleaner
)

### Generating Module File
_generate_module_py(turtlesim_cleaner
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/turtlesim_cleaner
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(turtlesim_cleaner_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(turtlesim_cleaner_generate_messages turtlesim_cleaner_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/hadi/catkin_ws/src/turtlesim_cleaner/srv/MoveSquare.srv" NAME_WE)
add_dependencies(turtlesim_cleaner_generate_messages_py _turtlesim_cleaner_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/hadi/catkin_ws/src/turtlesim_cleaner/srv/MoveCircle.srv" NAME_WE)
add_dependencies(turtlesim_cleaner_generate_messages_py _turtlesim_cleaner_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(turtlesim_cleaner_genpy)
add_dependencies(turtlesim_cleaner_genpy turtlesim_cleaner_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS turtlesim_cleaner_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/turtlesim_cleaner)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/turtlesim_cleaner
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_cpp)
  add_dependencies(turtlesim_cleaner_generate_messages_cpp geometry_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/turtlesim_cleaner)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/turtlesim_cleaner
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_eus)
  add_dependencies(turtlesim_cleaner_generate_messages_eus geometry_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/turtlesim_cleaner)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/turtlesim_cleaner
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_lisp)
  add_dependencies(turtlesim_cleaner_generate_messages_lisp geometry_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/turtlesim_cleaner)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/turtlesim_cleaner
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_nodejs)
  add_dependencies(turtlesim_cleaner_generate_messages_nodejs geometry_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/turtlesim_cleaner)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/turtlesim_cleaner\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/turtlesim_cleaner
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_py)
  add_dependencies(turtlesim_cleaner_generate_messages_py geometry_msgs_generate_messages_py)
endif()
