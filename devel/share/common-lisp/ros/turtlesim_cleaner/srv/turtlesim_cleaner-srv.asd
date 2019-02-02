
(cl:in-package :asdf)

(defsystem "turtlesim_cleaner-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "MoveCircle" :depends-on ("_package_MoveCircle"))
    (:file "_package_MoveCircle" :depends-on ("_package"))
    (:file "MoveSquare" :depends-on ("_package_MoveSquare"))
    (:file "_package_MoveSquare" :depends-on ("_package"))
  ))