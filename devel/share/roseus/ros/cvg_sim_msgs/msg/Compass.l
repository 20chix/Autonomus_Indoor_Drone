;; Auto-generated. Do not edit!


(when (boundp 'cvg_sim_msgs::Compass)
  (if (not (find-package "CVG_SIM_MSGS"))
    (make-package "CVG_SIM_MSGS"))
  (shadow 'Compass (find-package "CVG_SIM_MSGS")))
(unless (find-package "CVG_SIM_MSGS::COMPASS")
  (make-package "CVG_SIM_MSGS::COMPASS"))

(in-package "ROS")
;;//! \htmlinclude Compass.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass cvg_sim_msgs::Compass
  :super ros::object
  :slots (_header _magnetic_heading _declination ))

(defmethod cvg_sim_msgs::Compass
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:magnetic_heading __magnetic_heading) 0.0)
    ((:declination __declination) 0.0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _magnetic_heading (float __magnetic_heading))
   (setq _declination (float __declination))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:magnetic_heading
   (&optional __magnetic_heading)
   (if __magnetic_heading (setq _magnetic_heading __magnetic_heading)) _magnetic_heading)
  (:declination
   (&optional __declination)
   (if __declination (setq _declination __declination)) _declination)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; float32 _magnetic_heading
    4
    ;; float32 _declination
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; float32 _magnetic_heading
       (sys::poke _magnetic_heading (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _declination
       (sys::poke _declination (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; float32 _magnetic_heading
     (setq _magnetic_heading (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _declination
     (setq _declination (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get cvg_sim_msgs::Compass :md5sum-) "69b5db73a2f794a5a815baf6b84a4be5")
(setf (get cvg_sim_msgs::Compass :datatype-) "cvg_sim_msgs/Compass")
(setf (get cvg_sim_msgs::Compass :definition-)
      "Header header
float32 magnetic_heading
float32 declination


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



(provide :cvg_sim_msgs/Compass "69b5db73a2f794a5a815baf6b84a4be5")


