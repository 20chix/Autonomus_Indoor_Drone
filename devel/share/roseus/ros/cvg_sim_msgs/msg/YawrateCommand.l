;; Auto-generated. Do not edit!


(when (boundp 'cvg_sim_msgs::YawrateCommand)
  (if (not (find-package "CVG_SIM_MSGS"))
    (make-package "CVG_SIM_MSGS"))
  (shadow 'YawrateCommand (find-package "CVG_SIM_MSGS")))
(unless (find-package "CVG_SIM_MSGS::YAWRATECOMMAND")
  (make-package "CVG_SIM_MSGS::YAWRATECOMMAND"))

(in-package "ROS")
;;//! \htmlinclude YawrateCommand.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass cvg_sim_msgs::YawrateCommand
  :super ros::object
  :slots (_header _turnrate ))

(defmethod cvg_sim_msgs::YawrateCommand
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:turnrate __turnrate) 0.0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _turnrate (float __turnrate))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:turnrate
   (&optional __turnrate)
   (if __turnrate (setq _turnrate __turnrate)) _turnrate)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; float32 _turnrate
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; float32 _turnrate
       (sys::poke _turnrate (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; float32 _turnrate
     (setq _turnrate (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get cvg_sim_msgs::YawrateCommand :md5sum-) "d8d2a0a1e3daa0fc410bf30a154fa6b6")
(setf (get cvg_sim_msgs::YawrateCommand :datatype-) "cvg_sim_msgs/YawrateCommand")
(setf (get cvg_sim_msgs::YawrateCommand :definition-)
      "Header header
float32 turnrate

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



(provide :cvg_sim_msgs/YawrateCommand "d8d2a0a1e3daa0fc410bf30a154fa6b6")


