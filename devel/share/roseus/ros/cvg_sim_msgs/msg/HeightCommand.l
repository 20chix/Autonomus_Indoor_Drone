;; Auto-generated. Do not edit!


(when (boundp 'cvg_sim_msgs::HeightCommand)
  (if (not (find-package "CVG_SIM_MSGS"))
    (make-package "CVG_SIM_MSGS"))
  (shadow 'HeightCommand (find-package "CVG_SIM_MSGS")))
(unless (find-package "CVG_SIM_MSGS::HEIGHTCOMMAND")
  (make-package "CVG_SIM_MSGS::HEIGHTCOMMAND"))

(in-package "ROS")
;;//! \htmlinclude HeightCommand.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass cvg_sim_msgs::HeightCommand
  :super ros::object
  :slots (_header _height ))

(defmethod cvg_sim_msgs::HeightCommand
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:height __height) 0.0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _height (float __height))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:height
   (&optional __height)
   (if __height (setq _height __height)) _height)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; float32 _height
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; float32 _height
       (sys::poke _height (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; float32 _height
     (setq _height (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get cvg_sim_msgs::HeightCommand :md5sum-) "8c63aeb4f8d9305792b3627c1e7a1ab1")
(setf (get cvg_sim_msgs::HeightCommand :datatype-) "cvg_sim_msgs/HeightCommand")
(setf (get cvg_sim_msgs::HeightCommand :definition-)
      "Header header
float32 height

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



(provide :cvg_sim_msgs/HeightCommand "8c63aeb4f8d9305792b3627c1e7a1ab1")


