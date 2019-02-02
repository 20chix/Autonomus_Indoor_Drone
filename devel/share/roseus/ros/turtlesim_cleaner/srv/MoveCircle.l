;; Auto-generated. Do not edit!


(when (boundp 'turtlesim_cleaner::MoveCircle)
  (if (not (find-package "TURTLESIM_CLEANER"))
    (make-package "TURTLESIM_CLEANER"))
  (shadow 'MoveCircle (find-package "TURTLESIM_CLEANER")))
(unless (find-package "TURTLESIM_CLEANER::MOVECIRCLE")
  (make-package "TURTLESIM_CLEANER::MOVECIRCLE"))
(unless (find-package "TURTLESIM_CLEANER::MOVECIRCLEREQUEST")
  (make-package "TURTLESIM_CLEANER::MOVECIRCLEREQUEST"))
(unless (find-package "TURTLESIM_CLEANER::MOVECIRCLERESPONSE")
  (make-package "TURTLESIM_CLEANER::MOVECIRCLERESPONSE"))

(in-package "ROS")





(defclass turtlesim_cleaner::MoveCircleRequest
  :super ros::object
  :slots (_s _r ))

(defmethod turtlesim_cleaner::MoveCircleRequest
  (:init
   (&key
    ((:s __s) 0.0)
    ((:r __r) 0.0)
    )
   (send-super :init)
   (setq _s (float __s))
   (setq _r (float __r))
   self)
  (:s
   (&optional __s)
   (if __s (setq _s __s)) _s)
  (:r
   (&optional __r)
   (if __r (setq _r __r)) _r)
  (:serialization-length
   ()
   (+
    ;; float32 _s
    4
    ;; float32 _r
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _s
       (sys::poke _s (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _r
       (sys::poke _r (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _s
     (setq _s (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _r
     (setq _r (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(defclass turtlesim_cleaner::MoveCircleResponse
  :super ros::object
  :slots ())

(defmethod turtlesim_cleaner::MoveCircleResponse
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass turtlesim_cleaner::MoveCircle
  :super ros::object
  :slots ())

(setf (get turtlesim_cleaner::MoveCircle :md5sum-) "6d766f6a2db01255c7ae96df4f8888c5")
(setf (get turtlesim_cleaner::MoveCircle :datatype-) "turtlesim_cleaner/MoveCircle")
(setf (get turtlesim_cleaner::MoveCircle :request) turtlesim_cleaner::MoveCircleRequest)
(setf (get turtlesim_cleaner::MoveCircle :response) turtlesim_cleaner::MoveCircleResponse)

(defmethod turtlesim_cleaner::MoveCircleRequest
  (:response () (instance turtlesim_cleaner::MoveCircleResponse :init)))

(setf (get turtlesim_cleaner::MoveCircleRequest :md5sum-) "6d766f6a2db01255c7ae96df4f8888c5")
(setf (get turtlesim_cleaner::MoveCircleRequest :datatype-) "turtlesim_cleaner/MoveCircleRequest")
(setf (get turtlesim_cleaner::MoveCircleRequest :definition-)
      "float32 s
float32 r
---

")

(setf (get turtlesim_cleaner::MoveCircleResponse :md5sum-) "6d766f6a2db01255c7ae96df4f8888c5")
(setf (get turtlesim_cleaner::MoveCircleResponse :datatype-) "turtlesim_cleaner/MoveCircleResponse")
(setf (get turtlesim_cleaner::MoveCircleResponse :definition-)
      "float32 s
float32 r
---

")



(provide :turtlesim_cleaner/MoveCircle "6d766f6a2db01255c7ae96df4f8888c5")


