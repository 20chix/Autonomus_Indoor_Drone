; Auto-generated. Do not edit!


(cl:in-package cvg_sim_gazebo_plugins-srv)


;//! \htmlinclude SetBias-request.msg.html

(cl:defclass <SetBias-request> (roslisp-msg-protocol:ros-message)
  ((bias
    :reader bias
    :initarg :bias
    :type geometry_msgs-msg:Vector3
    :initform (cl:make-instance 'geometry_msgs-msg:Vector3)))
)

(cl:defclass SetBias-request (<SetBias-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SetBias-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SetBias-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name cvg_sim_gazebo_plugins-srv:<SetBias-request> is deprecated: use cvg_sim_gazebo_plugins-srv:SetBias-request instead.")))

(cl:ensure-generic-function 'bias-val :lambda-list '(m))
(cl:defmethod bias-val ((m <SetBias-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cvg_sim_gazebo_plugins-srv:bias-val is deprecated.  Use cvg_sim_gazebo_plugins-srv:bias instead.")
  (bias m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SetBias-request>) ostream)
  "Serializes a message object of type '<SetBias-request>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'bias) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SetBias-request>) istream)
  "Deserializes a message object of type '<SetBias-request>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'bias) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SetBias-request>)))
  "Returns string type for a service object of type '<SetBias-request>"
  "cvg_sim_gazebo_plugins/SetBiasRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetBias-request)))
  "Returns string type for a service object of type 'SetBias-request"
  "cvg_sim_gazebo_plugins/SetBiasRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SetBias-request>)))
  "Returns md5sum for a message object of type '<SetBias-request>"
  "af1f260075d9ba9bd73ca10c6a45df07")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SetBias-request)))
  "Returns md5sum for a message object of type 'SetBias-request"
  "af1f260075d9ba9bd73ca10c6a45df07")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SetBias-request>)))
  "Returns full string definition for message of type '<SetBias-request>"
  (cl:format cl:nil "geometry_msgs/Vector3 bias~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SetBias-request)))
  "Returns full string definition for message of type 'SetBias-request"
  (cl:format cl:nil "geometry_msgs/Vector3 bias~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SetBias-request>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'bias))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SetBias-request>))
  "Converts a ROS message object to a list"
  (cl:list 'SetBias-request
    (cl:cons ':bias (bias msg))
))
;//! \htmlinclude SetBias-response.msg.html

(cl:defclass <SetBias-response> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass SetBias-response (<SetBias-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SetBias-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SetBias-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name cvg_sim_gazebo_plugins-srv:<SetBias-response> is deprecated: use cvg_sim_gazebo_plugins-srv:SetBias-response instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SetBias-response>) ostream)
  "Serializes a message object of type '<SetBias-response>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SetBias-response>) istream)
  "Deserializes a message object of type '<SetBias-response>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SetBias-response>)))
  "Returns string type for a service object of type '<SetBias-response>"
  "cvg_sim_gazebo_plugins/SetBiasResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetBias-response)))
  "Returns string type for a service object of type 'SetBias-response"
  "cvg_sim_gazebo_plugins/SetBiasResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SetBias-response>)))
  "Returns md5sum for a message object of type '<SetBias-response>"
  "af1f260075d9ba9bd73ca10c6a45df07")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SetBias-response)))
  "Returns md5sum for a message object of type 'SetBias-response"
  "af1f260075d9ba9bd73ca10c6a45df07")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SetBias-response>)))
  "Returns full string definition for message of type '<SetBias-response>"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SetBias-response)))
  "Returns full string definition for message of type 'SetBias-response"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SetBias-response>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SetBias-response>))
  "Converts a ROS message object to a list"
  (cl:list 'SetBias-response
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'SetBias)))
  'SetBias-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'SetBias)))
  'SetBias-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetBias)))
  "Returns string type for a service object of type '<SetBias>"
  "cvg_sim_gazebo_plugins/SetBias")