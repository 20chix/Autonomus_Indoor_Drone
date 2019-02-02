;; Auto-generated. Do not edit!


(when (boundp 'turtlesim_cleaner::MoveSquare)
  (if (not (find-package "TURTLESIM_CLEANER"))
    (make-package "TURTLESIM_CLEANER"))
  (shadow 'MoveSquare (find-package "TURTLESIM_CLEANER")))
(unless (find-package "TURTLESIM_CLEANER::MOVESQUARE")
  (make-package "TURTLESIM_CLEANER::MOVESQUARE"))
(unless (find-package "TURTLESIM_CLEANER::MOVESQUAREREQUEST")
  (make-package "TURTLESIM_CLEANER::MOVESQUAREREQUEST"))
(unless (find-package "TURTLESIM_CLEANER::MOVESQUARERESPONSE")
  (make-package "TURTLESIM_CLEANER::MOVESQUARERESPONSE"))

(in-package "ROS")





(defclass turtlesim_cleaner::MoveSquareRequest
  :super ros::object
  :slots (_s _r ))

(defmethod turtlesim_cleaner::MoveSquareRequest
  (:init
   (&key
    ((:s __s) 0.0)
    ((:r __r) 0)
    )
   (send-super :init)
   (setq _s (float __s))
   (setq _r (round __r))
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
    ;; int32 _r
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _s
       (sys::poke _s (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; int32 _r
       (write-long _r s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _s
     (setq _s (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; int32 _r
     (setq _r (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(defclass turtlesim_cleaner::MoveSquareResponse
  :super ros::object
  :slots ())

(defmethod turtlesim_cleaner::MoveSquareResponse
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

(defclass turtlesim_cleaner::MoveSquare
  :super ros::object
  :slots ())

(setf (get turtlesim_cleaner::MoveSquare :md5sum-) "af0b48fe9187ad9b8874f8bb3dcfb81d")
(setf (get turtlesim_cleaner::MoveSquare :datatype-) "turtlesim_cleaner/MoveSquare")
(setf (get turtlesim_cleaner::MoveSquare :request) turtlesim_cleaner::MoveSquareRequest)
(setf (get turtlesim_cleaner::MoveSquare :response) turtlesim_cleaner::MoveSquareResponse)

(defmethod turtlesim_cleaner::MoveSquareRequest
  (:response () (instance turtlesim_cleaner::MoveSquareResponse :init)))

(setf (get turtlesim_cleaner::MoveSquareRequest :md5sum-) "af0b48fe9187ad9b8874f8bb3dcfb81d")
(setf (get turtlesim_cleaner::MoveSquareRequest :datatype-) "turtlesim_cleaner/MoveSquareRequest")
(setf (get turtlesim_cleaner::MoveSquareRequest :definition-)
      "float32 s
int32 r
---

")

(setf (get turtlesim_cleaner::MoveSquareResponse :md5sum-) "af0b48fe9187ad9b8874f8bb3dcfb81d")
(setf (get turtlesim_cleaner::MoveSquareResponse :datatype-) "turtlesim_cleaner/MoveSquareResponse")
(setf (get turtlesim_cleaner::MoveSquareResponse :definition-)
      "float32 s
int32 r
---

")



(provide :turtlesim_cleaner/MoveSquare "af0b48fe9187ad9b8874f8bb3dcfb81d")


