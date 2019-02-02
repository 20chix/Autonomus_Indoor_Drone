;; Auto-generated. Do not edit!


(when (boundp 'cvg_sim_msgs::Altitude)
  (if (not (find-package "CVG_SIM_MSGS"))
    (make-package "CVG_SIM_MSGS"))
  (shadow 'Altitude (find-package "CVG_SIM_MSGS")))
(unless (find-package "CVG_SIM_MSGS::ALTITUDE")
  (make-package "CVG_SIM_MSGS::ALTITUDE"))

(in-package "ROS")
;;//! \htmlinclude Altitude.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass cvg_sim_msgs::Altitude
  :super ros::object
  :slots (_header _height _altitude _elevation _qnh ))

(defmethod cvg_sim_msgs::Altitude
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:height __height) 0.0)
    ((:altitude __altitude) 0.0)
    ((:elevation __elevation) 0.0)
    ((:qnh __qnh) 0.0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _height (float __height))
   (setq _altitude (float __altitude))
   (setq _elevation (float __elevation))
   (setq _qnh (float __qnh))
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
  (:altitude
   (&optional __altitude)
   (if __altitude (setq _altitude __altitude)) _altitude)
  (:elevation
   (&optional __elevation)
   (if __elevation (setq _elevation __elevation)) _elevation)
  (:qnh
   (&optional __qnh)
   (if __qnh (setq _qnh __qnh)) _qnh)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; float32 _height
    4
    ;; float32 _altitude
    4
    ;; float32 _elevation
    4
    ;; float32 _qnh
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
     ;; float32 _altitude
       (sys::poke _altitude (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _elevation
       (sys::poke _elevation (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _qnh
       (sys::poke _qnh (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; float32 _height
     (setq _height (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _altitude
     (setq _altitude (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _elevation
     (setq _elevation (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _qnh
     (setq _qnh (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get cvg_sim_msgs::Altitude :md5sum-) "b9fb5f353226e94d84dfd4ef8a74c81d")
(setf (get cvg_sim_msgs::Altitude :datatype-) "cvg_sim_msgs/Altitude")
(setf (get cvg_sim_msgs::Altitude :definition-)
      "Header header
float32 height
float32 altitude
float32 elevation
float32 qnh

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



(provide :cvg_sim_msgs/Altitude "b9fb5f353226e94d84dfd4ef8a74c81d")


