; Auto-generated. Do not edit!


(cl:in-package cvg_sim_msgs-msg)


;//! \htmlinclude RuddersCommand.msg.html

(cl:defclass <RuddersCommand> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (aileron
    :reader aileron
    :initarg :aileron
    :type cl:float
    :initform 0.0)
   (elevator
    :reader elevator
    :initarg :elevator
    :type cl:float
    :initform 0.0)
   (rudder
    :reader rudder
    :initarg :rudder
    :type cl:float
    :initform 0.0))
)

(cl:defclass RuddersCommand (<RuddersCommand>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <RuddersCommand>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'RuddersCommand)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name cvg_sim_msgs-msg:<RuddersCommand> is deprecated: use cvg_sim_msgs-msg:RuddersCommand instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <RuddersCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cvg_sim_msgs-msg:header-val is deprecated.  Use cvg_sim_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'aileron-val :lambda-list '(m))
(cl:defmethod aileron-val ((m <RuddersCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cvg_sim_msgs-msg:aileron-val is deprecated.  Use cvg_sim_msgs-msg:aileron instead.")
  (aileron m))

(cl:ensure-generic-function 'elevator-val :lambda-list '(m))
(cl:defmethod elevator-val ((m <RuddersCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cvg_sim_msgs-msg:elevator-val is deprecated.  Use cvg_sim_msgs-msg:elevator instead.")
  (elevator m))

(cl:ensure-generic-function 'rudder-val :lambda-list '(m))
(cl:defmethod rudder-val ((m <RuddersCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cvg_sim_msgs-msg:rudder-val is deprecated.  Use cvg_sim_msgs-msg:rudder instead.")
  (rudder m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <RuddersCommand>) ostream)
  "Serializes a message object of type '<RuddersCommand>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'aileron))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'elevator))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'rudder))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <RuddersCommand>) istream)
  "Deserializes a message object of type '<RuddersCommand>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'aileron) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'elevator) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'rudder) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<RuddersCommand>)))
  "Returns string type for a message object of type '<RuddersCommand>"
  "cvg_sim_msgs/RuddersCommand")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'RuddersCommand)))
  "Returns string type for a message object of type 'RuddersCommand"
  "cvg_sim_msgs/RuddersCommand")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<RuddersCommand>)))
  "Returns md5sum for a message object of type '<RuddersCommand>"
  "2e136cb8cfffc2233e404b320c27bca6")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'RuddersCommand)))
  "Returns md5sum for a message object of type 'RuddersCommand"
  "2e136cb8cfffc2233e404b320c27bca6")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<RuddersCommand>)))
  "Returns full string definition for message of type '<RuddersCommand>"
  (cl:format cl:nil "Header header~%float32 aileron~%float32 elevator~%float32 rudder~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'RuddersCommand)))
  "Returns full string definition for message of type 'RuddersCommand"
  (cl:format cl:nil "Header header~%float32 aileron~%float32 elevator~%float32 rudder~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <RuddersCommand>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <RuddersCommand>))
  "Converts a ROS message object to a list"
  (cl:list 'RuddersCommand
    (cl:cons ':header (header msg))
    (cl:cons ':aileron (aileron msg))
    (cl:cons ':elevator (elevator msg))
    (cl:cons ':rudder (rudder msg))
))
