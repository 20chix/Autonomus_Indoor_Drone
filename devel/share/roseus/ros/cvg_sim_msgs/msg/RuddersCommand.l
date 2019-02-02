;; Auto-generated. Do not edit!


(when (boundp 'cvg_sim_msgs::RuddersCommand)
  (if (not (find-package "CVG_SIM_MSGS"))
    (make-package "CVG_SIM_MSGS"))
  (shadow 'RuddersCommand (find-package "CVG_SIM_MSGS")))
(unless (find-package "CVG_SIM_MSGS::RUDDERSCOMMAND")
  (make-package "CVG_SIM_MSGS::RUDDERSCOMMAND"))

(in-package "ROS")
;;//! \htmlinclude RuddersCommand.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass cvg_sim_msgs::RuddersCommand
  :super ros::object
  :slots (_header _aileron _elevator _rudder ))

(defmethod cvg_sim_msgs::RuddersCommand
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:aileron __aileron) 0.0)
    ((:elevator __elevator) 0.0)
    ((:rudder __rudder) 0.0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _aileron (float __aileron))
   (setq _elevator (float __elevator))
   (setq _rudder (float __rudder))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:aileron
   (&optional __aileron)
   (if __aileron (setq _aileron __aileron)) _aileron)
  (:elevator
   (&optional __elevator)
   (if __elevator (setq _elevator __elevator)) _elevator)
  (:rudder
   (&optional __rudder)
   (if __rudder (setq _rudder __rudder)) _rudder)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; float32 _aileron
    4
    ;; float32 _elevator
    4
    ;; float32 _rudder
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; float32 _aileron
       (sys::poke _aileron (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _elevator
       (sys::poke _elevator (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _rudder
       (sys::poke _rudder (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; float32 _aileron
     (setq _aileron (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _elevator
     (setq _elevator (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _rudder
     (setq _rudder (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get cvg_sim_msgs::RuddersCommand :md5sum-) "2e136cb8cfffc2233e404b320c27bca6")
(setf (get cvg_sim_msgs::RuddersCommand :datatype-) "cvg_sim_msgs/RuddersCommand")
(setf (get cvg_sim_msgs::RuddersCommand :definition-)
      "Header header
float32 aileron
float32 elevator
float32 rudder

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



(provide :cvg_sim_msgs/RuddersCommand "2e136cb8cfffc2233e404b320c27bca6")


