; Auto-generated. Do not edit!


(cl:in-package cvg_sim_msgs-msg)


;//! \htmlinclude YawrateCommand.msg.html

(cl:defclass <YawrateCommand> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (turnrate
    :reader turnrate
    :initarg :turnrate
    :type cl:float
    :initform 0.0))
)

(cl:defclass YawrateCommand (<YawrateCommand>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <YawrateCommand>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'YawrateCommand)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name cvg_sim_msgs-msg:<YawrateCommand> is deprecated: use cvg_sim_msgs-msg:YawrateCommand instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <YawrateCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cvg_sim_msgs-msg:header-val is deprecated.  Use cvg_sim_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'turnrate-val :lambda-list '(m))
(cl:defmethod turnrate-val ((m <YawrateCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cvg_sim_msgs-msg:turnrate-val is deprecated.  Use cvg_sim_msgs-msg:turnrate instead.")
  (turnrate m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <YawrateCommand>) ostream)
  "Serializes a message object of type '<YawrateCommand>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'turnrate))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <YawrateCommand>) istream)
  "Deserializes a message object of type '<YawrateCommand>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'turnrate) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<YawrateCommand>)))
  "Returns string type for a message object of type '<YawrateCommand>"
  "cvg_sim_msgs/YawrateCommand")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'YawrateCommand)))
  "Returns string type for a message object of type 'YawrateCommand"
  "cvg_sim_msgs/YawrateCommand")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<YawrateCommand>)))
  "Returns md5sum for a message object of type '<YawrateCommand>"
  "d8d2a0a1e3daa0fc410bf30a154fa6b6")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'YawrateCommand)))
  "Returns md5sum for a message object of type 'YawrateCommand"
  "d8d2a0a1e3daa0fc410bf30a154fa6b6")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<YawrateCommand>)))
  "Returns full string definition for message of type '<YawrateCommand>"
  (cl:format cl:nil "Header header~%float32 turnrate~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'YawrateCommand)))
  "Returns full string definition for message of type 'YawrateCommand"
  (cl:format cl:nil "Header header~%float32 turnrate~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <YawrateCommand>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <YawrateCommand>))
  "Converts a ROS message object to a list"
  (cl:list 'YawrateCommand
    (cl:cons ':header (header msg))
    (cl:cons ':turnrate (turnrate msg))
))
