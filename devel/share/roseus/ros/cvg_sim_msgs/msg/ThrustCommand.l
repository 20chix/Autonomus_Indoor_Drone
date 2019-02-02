;; Auto-generated. Do not edit!


(when (boundp 'cvg_sim_msgs::ThrustCommand)
  (if (not (find-package "CVG_SIM_MSGS"))
    (make-package "CVG_SIM_MSGS"))
  (shadow 'ThrustCommand (find-package "CVG_SIM_MSGS")))
(unless (find-package "CVG_SIM_MSGS::THRUSTCOMMAND")
  (make-package "CVG_SIM_MSGS::THRUSTCOMMAND"))

(in-package "ROS")
;;//! \htmlinclude ThrustCommand.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass cvg_sim_msgs::ThrustCommand
  :super ros::object
  :slots (_header _thrust ))

(defmethod cvg_sim_msgs::ThrustCommand
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:thrust __thrust) 0.0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _thrust (float __thrust))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:thrust
   (&optional __thrust)
   (if __thrust (setq _thrust __thrust)) _thrust)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; float32 _thrust
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; float32 _thrust
       (sys::poke _thrust (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; float32 _thrust
     (setq _thrust (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get cvg_sim_msgs::ThrustCommand :md5sum-) "c61da3a8868a8b502eaf0b0abd839f57")
(setf (get cvg_sim_msgs::ThrustCommand :datatype-) "cvg_sim_msgs/ThrustCommand")
(setf (get cvg_sim_msgs::ThrustCommand :definition-)
      "Header header
float32 thrust

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



(provide :cvg_sim_msgs/ThrustCommand "c61da3a8868a8b502eaf0b0abd839f57")


