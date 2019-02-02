;; Auto-generated. Do not edit!


(when (boundp 'cvg_sim_msgs::MotorStatus)
  (if (not (find-package "CVG_SIM_MSGS"))
    (make-package "CVG_SIM_MSGS"))
  (shadow 'MotorStatus (find-package "CVG_SIM_MSGS")))
(unless (find-package "CVG_SIM_MSGS::MOTORSTATUS")
  (make-package "CVG_SIM_MSGS::MOTORSTATUS"))

(in-package "ROS")
;;//! \htmlinclude MotorStatus.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass cvg_sim_msgs::MotorStatus
  :super ros::object
  :slots (_header _on _running _frequency _current ))

(defmethod cvg_sim_msgs::MotorStatus
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:on __on) nil)
    ((:running __running) nil)
    ((:frequency __frequency) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:current __current) (make-array 0 :initial-element 0 :element-type :char))
    )
   (send-super :init)
   (setq _header __header)
   (setq _on __on)
   (setq _running __running)
   (setq _frequency __frequency)
   (setq _current __current)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:on
   (&optional __on)
   (if __on (setq _on __on)) _on)
  (:running
   (&optional __running)
   (if __running (setq _running __running)) _running)
  (:frequency
   (&optional __frequency)
   (if __frequency (setq _frequency __frequency)) _frequency)
  (:current
   (&optional __current)
   (if __current (setq _current __current)) _current)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; bool _on
    1
    ;; bool _running
    1
    ;; float32[] _frequency
    (* 4    (length _frequency)) 4
    ;; uint8[] _current
    (* 1    (length _current)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; bool _on
       (if _on (write-byte -1 s) (write-byte 0 s))
     ;; bool _running
       (if _running (write-byte -1 s) (write-byte 0 s))
     ;; float32[] _frequency
     (write-long (length _frequency) s)
     (dotimes (i (length _frequency))
       (sys::poke (elt _frequency i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; uint8[] _current
     (write-long (length _current) s)
     (princ _current s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; bool _on
     (setq _on (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _running
     (setq _running (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; float32[] _frequency
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _frequency (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _frequency i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;; uint8[] _current
   (let ((n (sys::peek buf ptr- :integer))) (incf ptr- 4)
     (setq _current (make-array n :element-type :char))
     (replace _current buf :start2 ptr-) (incf ptr- n))
   ;;
   self)
  )

(setf (get cvg_sim_msgs::MotorStatus :md5sum-) "1469bebf9a94a2d2a47aefabd197f250")
(setf (get cvg_sim_msgs::MotorStatus :datatype-) "cvg_sim_msgs/MotorStatus")
(setf (get cvg_sim_msgs::MotorStatus :definition-)
      "Header header
bool on
bool running
float32[] frequency
uint8[] current

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



(provide :cvg_sim_msgs/MotorStatus "1469bebf9a94a2d2a47aefabd197f250")


