; Auto-generated. Do not edit!


(cl:in-package turtlesim_cleaner-srv)


;//! \htmlinclude MoveCircle-request.msg.html

(cl:defclass <MoveCircle-request> (roslisp-msg-protocol:ros-message)
  ((s
    :reader s
    :initarg :s
    :type cl:float
    :initform 0.0)
   (r
    :reader r
    :initarg :r
    :type cl:float
    :initform 0.0))
)

(cl:defclass MoveCircle-request (<MoveCircle-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MoveCircle-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MoveCircle-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name turtlesim_cleaner-srv:<MoveCircle-request> is deprecated: use turtlesim_cleaner-srv:MoveCircle-request instead.")))

(cl:ensure-generic-function 's-val :lambda-list '(m))
(cl:defmethod s-val ((m <MoveCircle-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader turtlesim_cleaner-srv:s-val is deprecated.  Use turtlesim_cleaner-srv:s instead.")
  (s m))

(cl:ensure-generic-function 'r-val :lambda-list '(m))
(cl:defmethod r-val ((m <MoveCircle-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader turtlesim_cleaner-srv:r-val is deprecated.  Use turtlesim_cleaner-srv:r instead.")
  (r m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MoveCircle-request>) ostream)
  "Serializes a message object of type '<MoveCircle-request>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 's))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'r))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MoveCircle-request>) istream)
  "Deserializes a message object of type '<MoveCircle-request>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 's) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'r) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MoveCircle-request>)))
  "Returns string type for a service object of type '<MoveCircle-request>"
  "turtlesim_cleaner/MoveCircleRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MoveCircle-request)))
  "Returns string type for a service object of type 'MoveCircle-request"
  "turtlesim_cleaner/MoveCircleRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MoveCircle-request>)))
  "Returns md5sum for a message object of type '<MoveCircle-request>"
  "6d766f6a2db01255c7ae96df4f8888c5")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MoveCircle-request)))
  "Returns md5sum for a message object of type 'MoveCircle-request"
  "6d766f6a2db01255c7ae96df4f8888c5")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MoveCircle-request>)))
  "Returns full string definition for message of type '<MoveCircle-request>"
  (cl:format cl:nil "float32 s~%float32 r~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MoveCircle-request)))
  "Returns full string definition for message of type 'MoveCircle-request"
  (cl:format cl:nil "float32 s~%float32 r~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MoveCircle-request>))
  (cl:+ 0
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MoveCircle-request>))
  "Converts a ROS message object to a list"
  (cl:list 'MoveCircle-request
    (cl:cons ':s (s msg))
    (cl:cons ':r (r msg))
))
;//! \htmlinclude MoveCircle-response.msg.html

(cl:defclass <MoveCircle-response> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass MoveCircle-response (<MoveCircle-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MoveCircle-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MoveCircle-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name turtlesim_cleaner-srv:<MoveCircle-response> is deprecated: use turtlesim_cleaner-srv:MoveCircle-response instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MoveCircle-response>) ostream)
  "Serializes a message object of type '<MoveCircle-response>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MoveCircle-response>) istream)
  "Deserializes a message object of type '<MoveCircle-response>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MoveCircle-response>)))
  "Returns string type for a service object of type '<MoveCircle-response>"
  "turtlesim_cleaner/MoveCircleResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MoveCircle-response)))
  "Returns string type for a service object of type 'MoveCircle-response"
  "turtlesim_cleaner/MoveCircleResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MoveCircle-response>)))
  "Returns md5sum for a message object of type '<MoveCircle-response>"
  "6d766f6a2db01255c7ae96df4f8888c5")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MoveCircle-response)))
  "Returns md5sum for a message object of type 'MoveCircle-response"
  "6d766f6a2db01255c7ae96df4f8888c5")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MoveCircle-response>)))
  "Returns full string definition for message of type '<MoveCircle-response>"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MoveCircle-response)))
  "Returns full string definition for message of type 'MoveCircle-response"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MoveCircle-response>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MoveCircle-response>))
  "Converts a ROS message object to a list"
  (cl:list 'MoveCircle-response
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'MoveCircle)))
  'MoveCircle-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'MoveCircle)))
  'MoveCircle-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MoveCircle)))
  "Returns string type for a service object of type '<MoveCircle>"
  "turtlesim_cleaner/MoveCircle")