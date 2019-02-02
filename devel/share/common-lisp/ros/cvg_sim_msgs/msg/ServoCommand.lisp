; Auto-generated. Do not edit!


(cl:in-package cvg_sim_msgs-msg)


;//! \htmlinclude ServoCommand.msg.html

(cl:defclass <ServoCommand> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (value
    :reader value
    :initarg :value
    :type (cl:vector cl:fixnum)
   :initform (cl:make-array 0 :element-type 'cl:fixnum :initial-element 0)))
)

(cl:defclass ServoCommand (<ServoCommand>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ServoCommand>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ServoCommand)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name cvg_sim_msgs-msg:<ServoCommand> is deprecated: use cvg_sim_msgs-msg:ServoCommand instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <ServoCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cvg_sim_msgs-msg:header-val is deprecated.  Use cvg_sim_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'value-val :lambda-list '(m))
(cl:defmethod value-val ((m <ServoCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cvg_sim_msgs-msg:value-val is deprecated.  Use cvg_sim_msgs-msg:value instead.")
  (value m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ServoCommand>) ostream)
  "Serializes a message object of type '<ServoCommand>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'value))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:write-byte (cl:ldb (cl:byte 8 0) ele) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) ele) ostream))
   (cl:slot-value msg 'value))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ServoCommand>) istream)
  "Deserializes a message object of type '<ServoCommand>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'value) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'value)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:aref vals i)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:aref vals i)) (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ServoCommand>)))
  "Returns string type for a message object of type '<ServoCommand>"
  "cvg_sim_msgs/ServoCommand")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ServoCommand)))
  "Returns string type for a message object of type 'ServoCommand"
  "cvg_sim_msgs/ServoCommand")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ServoCommand>)))
  "Returns md5sum for a message object of type '<ServoCommand>"
  "d60ef35d4e3412dc6686b189be2523d0")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ServoCommand)))
  "Returns md5sum for a message object of type 'ServoCommand"
  "d60ef35d4e3412dc6686b189be2523d0")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ServoCommand>)))
  "Returns full string definition for message of type '<ServoCommand>"
  (cl:format cl:nil "Header header~%uint16[] value~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ServoCommand)))
  "Returns full string definition for message of type 'ServoCommand"
  (cl:format cl:nil "Header header~%uint16[] value~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ServoCommand>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'value) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 2)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ServoCommand>))
  "Converts a ROS message object to a list"
  (cl:list 'ServoCommand
    (cl:cons ':header (header msg))
    (cl:cons ':value (value msg))
))
