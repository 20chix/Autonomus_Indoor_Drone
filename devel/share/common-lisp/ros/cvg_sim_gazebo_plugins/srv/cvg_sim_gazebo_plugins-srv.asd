
(cl:in-package :asdf)

(defsystem "cvg_sim_gazebo_plugins-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
)
  :components ((:file "_package")
    (:file "SetBias" :depends-on ("_package_SetBias"))
    (:file "_package_SetBias" :depends-on ("_package"))
  ))