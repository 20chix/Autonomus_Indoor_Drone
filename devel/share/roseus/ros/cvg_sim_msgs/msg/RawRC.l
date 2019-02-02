;; Auto-generated. Do not edit!


(when (boundp 'cvg_sim_msgs::RawRC)
  (if (not (find-package "CVG_SIM_MSGS"))
    (make-package "CVG_SIM_MSGS"))
  (shadow 'RawRC (find-package "CVG_SIM_MSGS")))
(unless (find-package "CVG_SIM_MSGS::RAWRC")
  (make-package "CVG_SIM_MSGS::RAWRC"))

(in-package "ROS")
;;//! \htmlinclude RawRC.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass cvg_sim_msgs::RawRC
  :super ros::object
  :slots (_header _status _channel ))

(defmethod cvg_sim_msgs::RawRC
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:status __status) 0)
    ((:channel __channel) (make-array 0 :initial-element 0 :element-type :integer))
    )
   (send-super :init)
   (setq _header __header)
   (setq _status (round __status))
   (setq _channel __channel)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:status
   (&optional __status)
   (if __status (setq _status __status)) _status)
  (:channel
   (&optional __channel)
   (if __channel (setq _channel __channel)) _channel)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; uint8 _status
    1
    ;; uint16[] _channel
    (* 2    (length _channel)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; uint8 _status
       (write-byte _status s)
     ;; uint16[] _channel
     (write-long (length _channel) s)
     (dotimes (i (length _channel))
       (write-word (elt _channel i) s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; uint8 _status
     (setq _status (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint16[] _channel
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _channel (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _channel i) (sys::peek buf ptr- :short)) (incf ptr- 2)
     ))
   ;;
   self)
  )

(setf (get cvg_sim_msgs::RawRC :md5sum-) "f1584488325f747abea0b77036f70e2c")
(setf (get cvg_sim_msgs::RawRC :datatype-) "cvg_sim_msgs/RawRC")
(setf (get cvg_sim_msgs::RawRC :definition-)
      "Header header
uint8 status
uint16[] channel

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



(provide :cvg_sim_msgs/RawRC "f1584488325f747abea0b77036f70e2c")


