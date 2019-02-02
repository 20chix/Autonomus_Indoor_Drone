;; Auto-generated. Do not edit!


(when (boundp 'cvg_sim_msgs::RawImu)
  (if (not (find-package "CVG_SIM_MSGS"))
    (make-package "CVG_SIM_MSGS"))
  (shadow 'RawImu (find-package "CVG_SIM_MSGS")))
(unless (find-package "CVG_SIM_MSGS::RAWIMU")
  (make-package "CVG_SIM_MSGS::RAWIMU"))

(in-package "ROS")
;;//! \htmlinclude RawImu.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass cvg_sim_msgs::RawImu
  :super ros::object
  :slots (_header _angular_velocity _linear_acceleration ))

(defmethod cvg_sim_msgs::RawImu
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:angular_velocity __angular_velocity) (make-array 3 :initial-element 0 :element-type :integer))
    ((:linear_acceleration __linear_acceleration) (make-array 3 :initial-element 0 :element-type :integer))
    )
   (send-super :init)
   (setq _header __header)
   (setq _angular_velocity __angular_velocity)
   (setq _linear_acceleration __linear_acceleration)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:angular_velocity
   (&optional __angular_velocity)
   (if __angular_velocity (setq _angular_velocity __angular_velocity)) _angular_velocity)
  (:linear_acceleration
   (&optional __linear_acceleration)
   (if __linear_acceleration (setq _linear_acceleration __linear_acceleration)) _linear_acceleration)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; uint16[3] _angular_velocity
    (* 2    3)
    ;; uint16[3] _linear_acceleration
    (* 2    3)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; uint16[3] _angular_velocity
     (dotimes (i 3)
       (write-word (elt _angular_velocity i) s)
       )
     ;; uint16[3] _linear_acceleration
     (dotimes (i 3)
       (write-word (elt _linear_acceleration i) s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; uint16[3] _angular_velocity
   (dotimes (i (length _angular_velocity))
     (setf (elt _angular_velocity i) (sys::peek buf ptr- :short)) (incf ptr- 2)
     )
   ;; uint16[3] _linear_acceleration
   (dotimes (i (length _linear_acceleration))
     (setf (elt _linear_acceleration i) (sys::peek buf ptr- :short)) (incf ptr- 2)
     )
   ;;
   self)
  )

(setf (get cvg_sim_msgs::RawImu :md5sum-) "0879a838e899792bcf72ccfe7b5595ef")
(setf (get cvg_sim_msgs::RawImu :datatype-) "cvg_sim_msgs/RawImu")
(setf (get cvg_sim_msgs::RawImu :definition-)
      "Header header
uint16[3] angular_velocity
uint16[3] linear_acceleration

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

")



(provide :cvg_sim_msgs/RawImu "0879a838e899792bcf72ccfe7b5595ef")


