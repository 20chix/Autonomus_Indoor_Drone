
(cl:in-package :asdf)

(defsystem "move_quadcopter-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :actionlib_msgs-msg
               :geometry_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "NavigateAction" :depends-on ("_package_NavigateAction"))
    (:file "_package_NavigateAction" :depends-on ("_package"))
    (:file "NavigateActionFeedback" :depends-on ("_package_NavigateActionFeedback"))
    (:file "_package_NavigateActionFeedback" :depends-on ("_package"))
    (:file "NavigateActionGoal" :depends-on ("_package_NavigateActionGoal"))
    (:file "_package_NavigateActionGoal" :depends-on ("_package"))
    (:file "NavigateActionResult" :depends-on ("_package_NavigateActionResult"))
    (:file "_package_NavigateActionResult" :depends-on ("_package"))
    (:file "NavigateFeedback" :depends-on ("_package_NavigateFeedback"))
    (:file "_package_NavigateFeedback" :depends-on ("_package"))
    (:file "NavigateGoal" :depends-on ("_package_NavigateGoal"))
    (:file "_package_NavigateGoal" :depends-on ("_package"))
    (:file "NavigateResult" :depends-on ("_package_NavigateResult"))
    (:file "_package_NavigateResult" :depends-on ("_package"))
  ))