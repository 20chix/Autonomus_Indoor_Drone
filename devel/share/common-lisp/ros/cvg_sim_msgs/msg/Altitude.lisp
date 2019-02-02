; Auto-generated. Do not edit!


(cl:in-package cvg_sim_msgs-msg)


;//! \htmlinclude Altitude.msg.html

(cl:defclass <Altitude> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (height
    :reader height
    :initarg :height
    :type cl:float
    :initform 0.0)
   (altitude
    :reader altitude
    :initarg :altitude
    :type cl:float
    :initform 0.0)
   (elevation
    :reader elevation
    :initarg :elevation
    :type cl:float
    :initform 0.0)
   (qnh
    :reader qnh
    :initarg :qnh
    :type cl:float
    :initform 0.0))
)

(cl:defclass Altitude (<Altitude>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Altitude>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Altitude)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name cvg_sim_msgs-msg:<Altitude> is deprecated: use cvg_sim_msgs-msg:Altitude instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <Altitude>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cvg_sim_msgs-msg:header-val is deprecated.  Use cvg_sim_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'height-val :lambda-list '(m))
(cl:defmethod height-val ((m <Altitude>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cvg_sim_msgs-msg:height-val is deprecated.  Use cvg_sim_msgs-msg:height instead.")
  (height m))

(cl:ensure-generic-function 'altitude-val :lambda-list '(m))
(cl:defmethod altitude-val ((m <Altitude>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cvg_sim_msgs-msg:altitude-val is deprecated.  Use cvg_sim_msgs-msg:altitude instead.")
  (altitude m))

(cl:ensure-generic-function 'elevation-val :lambda-list '(m))
(cl:defmethod elevation-val ((m <Altitude>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cvg_sim_msgs-msg:elevation-val is deprecated.  Use cvg_sim_msgs-msg:elevation instead.")
  (elevation m))

(cl:ensure-generic-function 'qnh-val :lambda-list '(m))
(cl:defmethod qnh-val ((m <Altitude>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cvg_sim_msgs-msg:qnh-val is deprecated.  Use cvg_sim_msgs-msg:qnh instead.")
  (qnh m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Altitude>) ostream)
  "Serializes a message object of type '<Altitude>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'height))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'altitude))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'elevation))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'qnh))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Altitude>) istream)
  "Deserializes a message object of type '<Altitude>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'height) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'altitude) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'elevation) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'qnh) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Altitude>)))
  "Returns string type for a message object of type '<Altitude>"
  "cvg_sim_msgs/Altitude")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Altitude)))
  "Returns string type for a message object of type 'Altitude"
  "cvg_sim_msgs/Altitude")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Altitude>)))
  "Returns md5sum for a message object of type '<Altitude>"
  "b9fb5f353226e94d84dfd4ef8a74c81d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Altitude)))
  "Returns md5sum for a message object of type 'Altitude"
  "b9fb5f353226e94d84dfd4ef8a74c81d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Altitude>)))
  "Returns full string definition for message of type '<Altitude>"
  (cl:format cl:nil "Header header~%float32 height~%float32 altitude~%float32 elevation~%float32 qnh~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Altitude)))
  "Returns full string definition for message of type 'Altitude"
  (cl:format cl:nil "Header header~%float32 height~%float32 altitude~%float32 elevation~%float32 qnh~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Altitude>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Altitude>))
  "Converts a ROS message object to a list"
  (cl:list 'Altitude
    (cl:cons ':header (header msg))
    (cl:cons ':height (height msg))
    (cl:cons ':altitude (altitude msg))
    (cl:cons ':elevation (elevation msg))
    (cl:cons ':qnh (qnh msg))
))
