; Auto-generated. Do not edit!


(cl:in-package cvg_sim_msgs-msg)


;//! \htmlinclude VelocityZCommand.msg.html

(cl:defclass <VelocityZCommand> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (z
    :reader z
    :initarg :z
    :type cl:float
    :initform 0.0))
)

(cl:defclass VelocityZCommand (<VelocityZCommand>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <VelocityZCommand>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'VelocityZCommand)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name cvg_sim_msgs-msg:<VelocityZCommand> is deprecated: use cvg_sim_msgs-msg:VelocityZCommand instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <VelocityZCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cvg_sim_msgs-msg:header-val is deprecated.  Use cvg_sim_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'z-val :lambda-list '(m))
(cl:defmethod z-val ((m <VelocityZCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cvg_sim_msgs-msg:z-val is deprecated.  Use cvg_sim_msgs-msg:z instead.")
  (z m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <VelocityZCommand>) ostream)
  "Serializes a message object of type '<VelocityZCommand>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'z))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <VelocityZCommand>) istream)
  "Deserializes a message object of type '<VelocityZCommand>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'z) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<VelocityZCommand>)))
  "Returns string type for a message object of type '<VelocityZCommand>"
  "cvg_sim_msgs/VelocityZCommand")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'VelocityZCommand)))
  "Returns string type for a message object of type 'VelocityZCommand"
  "cvg_sim_msgs/VelocityZCommand")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<VelocityZCommand>)))
  "Returns md5sum for a message object of type '<VelocityZCommand>"
  "68efb57c1ccbb065338578afbfc54ec5")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'VelocityZCommand)))
  "Returns md5sum for a message object of type 'VelocityZCommand"
  "68efb57c1ccbb065338578afbfc54ec5")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<VelocityZCommand>)))
  "Returns full string definition for message of type '<VelocityZCommand>"
  (cl:format cl:nil "Header header~%float32 z~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'VelocityZCommand)))
  "Returns full string definition for message of type 'VelocityZCommand"
  (cl:format cl:nil "Header header~%float32 z~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <VelocityZCommand>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <VelocityZCommand>))
  "Converts a ROS message object to a list"
  (cl:list 'VelocityZCommand
    (cl:cons ':header (header msg))
    (cl:cons ':z (z msg))
))
