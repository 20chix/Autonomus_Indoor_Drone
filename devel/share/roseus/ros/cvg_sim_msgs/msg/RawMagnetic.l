;; Auto-generated. Do not edit!


(when (boundp 'cvg_sim_msgs::RawMagnetic)
  (if (not (find-package "CVG_SIM_MSGS"))
    (make-package "CVG_SIM_MSGS"))
  (shadow 'RawMagnetic (find-package "CVG_SIM_MSGS")))
(unless (find-package "CVG_SIM_MSGS::RAWMAGNETIC")
  (make-package "CVG_SIM_MSGS::RAWMAGNETIC"))

(in-package "ROS")
;;//! \htmlinclude RawMagnetic.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass cvg_sim_msgs::RawMagnetic
  :super ros::object
  :slots (_header _channel ))

(defmethod cvg_sim_msgs::RawMagnetic
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:channel __channel) (make-array 3 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _header __header)
   (setq _channel __channel)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:channel
   (&optional __channel)
   (if __channel (setq _channel __channel)) _channel)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; float64[3] _channel
    (* 8    3)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; float64[3] _channel
     (dotimes (i 3)
       (sys::poke (elt _channel i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; float64[3] _channel
   (dotimes (i (length _channel))
     (setf (elt _channel i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     )
   ;;
   self)
  )

(setf (get cvg_sim_msgs::RawMagnetic :md5sum-) "babd510868ac7b486e2097c79e1384c9")
(setf (get cvg_sim_msgs::RawMagnetic :datatype-) "cvg_sim_msgs/RawMagnetic")
(setf (get cvg_sim_msgs::RawMagnetic :definition-)
      "Header header
float64[3] channel

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



(provide :cvg_sim_msgs/RawMagnetic "babd510868ac7b486e2097c79e1384c9")


