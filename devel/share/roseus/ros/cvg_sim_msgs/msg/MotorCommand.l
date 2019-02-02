;; Auto-generated. Do not edit!


(when (boundp 'cvg_sim_msgs::MotorCommand)
  (if (not (find-package "CVG_SIM_MSGS"))
    (make-package "CVG_SIM_MSGS"))
  (shadow 'MotorCommand (find-package "CVG_SIM_MSGS")))
(unless (find-package "CVG_SIM_MSGS::MOTORCOMMAND")
  (make-package "CVG_SIM_MSGS::MOTORCOMMAND"))

(in-package "ROS")
;;//! \htmlinclude MotorCommand.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass cvg_sim_msgs::MotorCommand
  :super ros::object
  :slots (_header _force _torque _frequency _voltage ))

(defmethod cvg_sim_msgs::MotorCommand
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:force __force) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:torque __torque) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:frequency __frequency) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:voltage __voltage) (make-array 0 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _header __header)
   (setq _force __force)
   (setq _torque __torque)
   (setq _frequency __frequency)
   (setq _voltage __voltage)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:force
   (&optional __force)
   (if __force (setq _force __force)) _force)
  (:torque
   (&optional __torque)
   (if __torque (setq _torque __torque)) _torque)
  (:frequency
   (&optional __frequency)
   (if __frequency (setq _frequency __frequency)) _frequency)
  (:voltage
   (&optional __voltage)
   (if __voltage (setq _voltage __voltage)) _voltage)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; float32[] _force
    (* 4    (length _force)) 4
    ;; float32[] _torque
    (* 4    (length _torque)) 4
    ;; float32[] _frequency
    (* 4    (length _frequency)) 4
    ;; float32[] _voltage
    (* 4    (length _voltage)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; float32[] _force
     (write-long (length _force) s)
     (dotimes (i (length _force))
       (sys::poke (elt _force i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; float32[] _torque
     (write-long (length _torque) s)
     (dotimes (i (length _torque))
       (sys::poke (elt _torque i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; float32[] _frequency
     (write-long (length _frequency) s)
     (dotimes (i (length _frequency))
       (sys::poke (elt _frequency i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; float32[] _voltage
     (write-long (length _voltage) s)
     (dotimes (i (length _voltage))
       (sys::poke (elt _voltage i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; float32[] _force
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _force (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _force i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;; float32[] _torque
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _torque (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _torque i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;; float32[] _frequency
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _frequency (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _frequency i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;; float32[] _voltage
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _voltage (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _voltage i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;;
   self)
  )

(setf (get cvg_sim_msgs::MotorCommand :md5sum-) "ccd4d4d4606731d1c73409e9bfa55808")
(setf (get cvg_sim_msgs::MotorCommand :datatype-) "cvg_sim_msgs/MotorCommand")
(setf (get cvg_sim_msgs::MotorCommand :definition-)
      "Header header
float32[] force
float32[] torque
float32[] frequency
float32[] voltage

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



(provide :cvg_sim_msgs/MotorCommand "ccd4d4d4606731d1c73409e9bfa55808")


