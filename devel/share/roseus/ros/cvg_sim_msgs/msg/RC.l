;; Auto-generated. Do not edit!


(when (boundp 'cvg_sim_msgs::RC)
  (if (not (find-package "CVG_SIM_MSGS"))
    (make-package "CVG_SIM_MSGS"))
  (shadow 'RC (find-package "CVG_SIM_MSGS")))
(unless (find-package "CVG_SIM_MSGS::RC")
  (make-package "CVG_SIM_MSGS::RC"))

(in-package "ROS")
;;//! \htmlinclude RC.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(intern "*ROLL*" (find-package "CVG_SIM_MSGS::RC"))
(shadow '*ROLL* (find-package "CVG_SIM_MSGS::RC"))
(defconstant cvg_sim_msgs::RC::*ROLL* 1)
(intern "*PITCH*" (find-package "CVG_SIM_MSGS::RC"))
(shadow '*PITCH* (find-package "CVG_SIM_MSGS::RC"))
(defconstant cvg_sim_msgs::RC::*PITCH* 2)
(intern "*YAW*" (find-package "CVG_SIM_MSGS::RC"))
(shadow '*YAW* (find-package "CVG_SIM_MSGS::RC"))
(defconstant cvg_sim_msgs::RC::*YAW* 3)
(intern "*STEER*" (find-package "CVG_SIM_MSGS::RC"))
(shadow '*STEER* (find-package "CVG_SIM_MSGS::RC"))
(defconstant cvg_sim_msgs::RC::*STEER* 4)
(intern "*HEIGHT*" (find-package "CVG_SIM_MSGS::RC"))
(shadow '*HEIGHT* (find-package "CVG_SIM_MSGS::RC"))
(defconstant cvg_sim_msgs::RC::*HEIGHT* 5)
(intern "*THRUST*" (find-package "CVG_SIM_MSGS::RC"))
(shadow '*THRUST* (find-package "CVG_SIM_MSGS::RC"))
(defconstant cvg_sim_msgs::RC::*THRUST* 6)
(intern "*BRAKE*" (find-package "CVG_SIM_MSGS::RC"))
(shadow '*BRAKE* (find-package "CVG_SIM_MSGS::RC"))
(defconstant cvg_sim_msgs::RC::*BRAKE* 7)
(defclass cvg_sim_msgs::RC
  :super ros::object
  :slots (_header _status _valid _axis _axis_function _swit _swit_function ))

(defmethod cvg_sim_msgs::RC
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:status __status) 0)
    ((:valid __valid) nil)
    ((:axis __axis) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:axis_function __axis_function) (make-array 0 :initial-element 0 :element-type :char))
    ((:swit __swit) (make-array 0 :initial-element 0 :element-type :integer))
    ((:swit_function __swit_function) (make-array 0 :initial-element 0 :element-type :char))
    )
   (send-super :init)
   (setq _header __header)
   (setq _status (round __status))
   (setq _valid __valid)
   (setq _axis __axis)
   (setq _axis_function __axis_function)
   (setq _swit __swit)
   (setq _swit_function __swit_function)
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
  (:valid
   (&optional __valid)
   (if __valid (setq _valid __valid)) _valid)
  (:axis
   (&optional __axis)
   (if __axis (setq _axis __axis)) _axis)
  (:axis_function
   (&optional __axis_function)
   (if __axis_function (setq _axis_function __axis_function)) _axis_function)
  (:swit
   (&optional __swit)
   (if __swit (setq _swit __swit)) _swit)
  (:swit_function
   (&optional __swit_function)
   (if __swit_function (setq _swit_function __swit_function)) _swit_function)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; uint8 _status
    1
    ;; bool _valid
    1
    ;; float32[] _axis
    (* 4    (length _axis)) 4
    ;; uint8[] _axis_function
    (* 1    (length _axis_function)) 4
    ;; int8[] _swit
    (* 1    (length _swit)) 4
    ;; uint8[] _swit_function
    (* 1    (length _swit_function)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; uint8 _status
       (write-byte _status s)
     ;; bool _valid
       (if _valid (write-byte -1 s) (write-byte 0 s))
     ;; float32[] _axis
     (write-long (length _axis) s)
     (dotimes (i (length _axis))
       (sys::poke (elt _axis i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; uint8[] _axis_function
     (write-long (length _axis_function) s)
     (princ _axis_function s)
     ;; int8[] _swit
     (write-long (length _swit) s)
     (dotimes (i (length _swit))
       (write-byte (elt _swit i) s)
       )
     ;; uint8[] _swit_function
     (write-long (length _swit_function) s)
     (princ _swit_function s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; uint8 _status
     (setq _status (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; bool _valid
     (setq _valid (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; float32[] _axis
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _axis (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _axis i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;; uint8[] _axis_function
   (let ((n (sys::peek buf ptr- :integer))) (incf ptr- 4)
     (setq _axis_function (make-array n :element-type :char))
     (replace _axis_function buf :start2 ptr-) (incf ptr- n))
   ;; int8[] _swit
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _swit (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _swit i) (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> (elt _swit i) 127) (setf (elt _swit i) (- (elt _swit i) 256)))
     ))
   ;; uint8[] _swit_function
   (let ((n (sys::peek buf ptr- :integer))) (incf ptr- 4)
     (setq _swit_function (make-array n :element-type :char))
     (replace _swit_function buf :start2 ptr-) (incf ptr- n))
   ;;
   self)
  )

(setf (get cvg_sim_msgs::RC :md5sum-) "2691c2fe8c5ab2323146bdd8dd2e449e")
(setf (get cvg_sim_msgs::RC :datatype-) "cvg_sim_msgs/RC")
(setf (get cvg_sim_msgs::RC :definition-)
      "Header header

uint8 ROLL = 1
uint8 PITCH = 2
uint8 YAW = 3
uint8 STEER = 4
uint8 HEIGHT = 5
uint8 THRUST = 6
uint8 BRAKE = 7

uint8 status
bool valid

float32[] axis
uint8[] axis_function

int8[] swit
uint8[] swit_function

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



(provide :cvg_sim_msgs/RC "2691c2fe8c5ab2323146bdd8dd2e449e")


