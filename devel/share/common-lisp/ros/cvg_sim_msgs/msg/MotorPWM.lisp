; Auto-generated. Do not edit!


(cl:in-package cvg_sim_msgs-msg)


;//! \htmlinclude MotorPWM.msg.html

(cl:defclass <MotorPWM> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (pwm
    :reader pwm
    :initarg :pwm
    :type (cl:vector cl:fixnum)
   :initform (cl:make-array 0 :element-type 'cl:fixnum :initial-element 0)))
)

(cl:defclass MotorPWM (<MotorPWM>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MotorPWM>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MotorPWM)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name cvg_sim_msgs-msg:<MotorPWM> is deprecated: use cvg_sim_msgs-msg:MotorPWM instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <MotorPWM>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cvg_sim_msgs-msg:header-val is deprecated.  Use cvg_sim_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'pwm-val :lambda-list '(m))
(cl:defmethod pwm-val ((m <MotorPWM>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cvg_sim_msgs-msg:pwm-val is deprecated.  Use cvg_sim_msgs-msg:pwm instead.")
  (pwm m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MotorPWM>) ostream)
  "Serializes a message object of type '<MotorPWM>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'pwm))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:write-byte (cl:ldb (cl:byte 8 0) ele) ostream))
   (cl:slot-value msg 'pwm))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MotorPWM>) istream)
  "Deserializes a message object of type '<MotorPWM>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'pwm) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'pwm)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:aref vals i)) (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MotorPWM>)))
  "Returns string type for a message object of type '<MotorPWM>"
  "cvg_sim_msgs/MotorPWM")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MotorPWM)))
  "Returns string type for a message object of type 'MotorPWM"
  "cvg_sim_msgs/MotorPWM")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MotorPWM>)))
  "Returns md5sum for a message object of type '<MotorPWM>"
  "42f78dd80f99e0208248b8a257b8a645")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MotorPWM)))
  "Returns md5sum for a message object of type 'MotorPWM"
  "42f78dd80f99e0208248b8a257b8a645")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MotorPWM>)))
  "Returns full string definition for message of type '<MotorPWM>"
  (cl:format cl:nil "Header header~%uint8[] pwm~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MotorPWM)))
  "Returns full string definition for message of type 'MotorPWM"
  (cl:format cl:nil "Header header~%uint8[] pwm~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MotorPWM>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'pwm) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 1)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MotorPWM>))
  "Converts a ROS message object to a list"
  (cl:list 'MotorPWM
    (cl:cons ':header (header msg))
    (cl:cons ':pwm (pwm msg))
))
