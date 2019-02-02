;; Auto-generated. Do not edit!


(when (boundp 'cvg_sim_msgs::ServoCommand)
  (if (not (find-package "CVG_SIM_MSGS"))
    (make-package "CVG_SIM_MSGS"))
  (shadow 'ServoCommand (find-package "CVG_SIM_MSGS")))
(unless (find-package "CVG_SIM_MSGS::SERVOCOMMAND")
  (make-package "CVG_SIM_MSGS::SERVOCOMMAND"))

(in-package "ROS")
;;//! \htmlinclude ServoCommand.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass cvg_sim_msgs::ServoCommand
  :super ros::object
  :slots (_header _value ))

(defmethod cvg_sim_msgs::ServoCommand
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:value __value) (make-array 0 :initial-element 0 :element-type :integer))
    )
   (send-super :init)
   (setq _header __header)
   (setq _value __value)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:value
   (&optional __value)
   (if __value (setq _value __value)) _value)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; uint16[] _value
    (* 2    (length _value)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; uint16[] _value
     (write-long (length _value) s)
     (dotimes (i (length _value))
       (write-word (elt _value i) s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; uint16[] _value
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _value (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _value i) (sys::peek buf ptr- :short)) (incf ptr- 2)
     ))
   ;;
   self)
  )

(setf (get cvg_sim_msgs::ServoCommand :md5sum-) "d60ef35d4e3412dc6686b189be2523d0")
(setf (get cvg_sim_msgs::ServoCommand :datatype-) "cvg_sim_msgs/ServoCommand")
(setf (get cvg_sim_msgs::ServoCommand :definition-)
      "Header header
uint16[] value

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



(provide :cvg_sim_msgs/ServoCommand "d60ef35d4e3412dc6686b189be2523d0")


