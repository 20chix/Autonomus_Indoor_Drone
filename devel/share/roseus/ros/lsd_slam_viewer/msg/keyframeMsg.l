;; Auto-generated. Do not edit!


(when (boundp 'lsd_slam_viewer::keyframeMsg)
  (if (not (find-package "LSD_SLAM_VIEWER"))
    (make-package "LSD_SLAM_VIEWER"))
  (shadow 'keyframeMsg (find-package "LSD_SLAM_VIEWER")))
(unless (find-package "LSD_SLAM_VIEWER::KEYFRAMEMSG")
  (make-package "LSD_SLAM_VIEWER::KEYFRAMEMSG"))

(in-package "ROS")
;;//! \htmlinclude keyframeMsg.msg.html


(defclass lsd_slam_viewer::keyframeMsg
  :super ros::object
  :slots (_id _time _isKeyframe _camToWorld _fx _fy _cx _cy _height _width _pointcloud ))

(defmethod lsd_slam_viewer::keyframeMsg
  (:init
   (&key
    ((:id __id) 0)
    ((:time __time) 0.0)
    ((:isKeyframe __isKeyframe) nil)
    ((:camToWorld __camToWorld) (make-array 7 :initial-element 0.0 :element-type :float))
    ((:fx __fx) 0.0)
    ((:fy __fy) 0.0)
    ((:cx __cx) 0.0)
    ((:cy __cy) 0.0)
    ((:height __height) 0)
    ((:width __width) 0)
    ((:pointcloud __pointcloud) (make-array 0 :initial-element 0 :element-type :char))
    )
   (send-super :init)
   (setq _id (round __id))
   (setq _time (float __time))
   (setq _isKeyframe __isKeyframe)
   (setq _camToWorld __camToWorld)
   (setq _fx (float __fx))
   (setq _fy (float __fy))
   (setq _cx (float __cx))
   (setq _cy (float __cy))
   (setq _height (round __height))
   (setq _width (round __width))
   (setq _pointcloud __pointcloud)
   self)
  (:id
   (&optional __id)
   (if __id (setq _id __id)) _id)
  (:time
   (&optional __time)
   (if __time (setq _time __time)) _time)
  (:isKeyframe
   (&optional __isKeyframe)
   (if __isKeyframe (setq _isKeyframe __isKeyframe)) _isKeyframe)
  (:camToWorld
   (&optional __camToWorld)
   (if __camToWorld (setq _camToWorld __camToWorld)) _camToWorld)
  (:fx
   (&optional __fx)
   (if __fx (setq _fx __fx)) _fx)
  (:fy
   (&optional __fy)
   (if __fy (setq _fy __fy)) _fy)
  (:cx
   (&optional __cx)
   (if __cx (setq _cx __cx)) _cx)
  (:cy
   (&optional __cy)
   (if __cy (setq _cy __cy)) _cy)
  (:height
   (&optional __height)
   (if __height (setq _height __height)) _height)
  (:width
   (&optional __width)
   (if __width (setq _width __width)) _width)
  (:pointcloud
   (&optional __pointcloud)
   (if __pointcloud (setq _pointcloud __pointcloud)) _pointcloud)
  (:serialization-length
   ()
   (+
    ;; int32 _id
    4
    ;; float64 _time
    8
    ;; bool _isKeyframe
    1
    ;; float32[7] _camToWorld
    (* 4    7)
    ;; float32 _fx
    4
    ;; float32 _fy
    4
    ;; float32 _cx
    4
    ;; float32 _cy
    4
    ;; uint32 _height
    4
    ;; uint32 _width
    4
    ;; uint8[] _pointcloud
    (* 1    (length _pointcloud)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _id
       (write-long _id s)
     ;; float64 _time
       (sys::poke _time (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; bool _isKeyframe
       (if _isKeyframe (write-byte -1 s) (write-byte 0 s))
     ;; float32[7] _camToWorld
     (dotimes (i 7)
       (sys::poke (elt _camToWorld i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; float32 _fx
       (sys::poke _fx (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _fy
       (sys::poke _fy (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _cx
       (sys::poke _cx (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _cy
       (sys::poke _cy (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; uint32 _height
       (write-long _height s)
     ;; uint32 _width
       (write-long _width s)
     ;; uint8[] _pointcloud
     (write-long (length _pointcloud) s)
     (princ _pointcloud s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _id
     (setq _id (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; float64 _time
     (setq _time (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; bool _isKeyframe
     (setq _isKeyframe (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; float32[7] _camToWorld
   (dotimes (i (length _camToWorld))
     (setf (elt _camToWorld i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     )
   ;; float32 _fx
     (setq _fx (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _fy
     (setq _fy (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _cx
     (setq _cx (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _cy
     (setq _cy (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; uint32 _height
     (setq _height (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; uint32 _width
     (setq _width (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; uint8[] _pointcloud
   (let ((n (sys::peek buf ptr- :integer))) (incf ptr- 4)
     (setq _pointcloud (make-array n :element-type :char))
     (replace _pointcloud buf :start2 ptr-) (incf ptr- n))
   ;;
   self)
  )

(setf (get lsd_slam_viewer::keyframeMsg :md5sum-) "42d4108dbb7d0e5d166eb68dd4054826")
(setf (get lsd_slam_viewer::keyframeMsg :datatype-) "lsd_slam_viewer/keyframeMsg")
(setf (get lsd_slam_viewer::keyframeMsg :definition-)
      "int32 id
float64 time
bool isKeyframe

# camToWorld as serialization of sophus sim(3).
# may change with keyframeGraph-updates.
float32[7] camToWorld 


# camera parameter (fx fy cx cy), width, height
# will never change, but required for display.
float32 fx
float32 fy
float32 cx
float32 cy
uint32 height
uint32 width


# data as InputPointDense (float idepth, float idepth_var, uchar color[4]), width x height
# may be empty, in that case no associated pointcloud is ever shown.
uint8[] pointcloud

")



(provide :lsd_slam_viewer/keyframeMsg "42d4108dbb7d0e5d166eb68dd4054826")


