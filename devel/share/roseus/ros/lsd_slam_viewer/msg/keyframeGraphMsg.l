;; Auto-generated. Do not edit!


(when (boundp 'lsd_slam_viewer::keyframeGraphMsg)
  (if (not (find-package "LSD_SLAM_VIEWER"))
    (make-package "LSD_SLAM_VIEWER"))
  (shadow 'keyframeGraphMsg (find-package "LSD_SLAM_VIEWER")))
(unless (find-package "LSD_SLAM_VIEWER::KEYFRAMEGRAPHMSG")
  (make-package "LSD_SLAM_VIEWER::KEYFRAMEGRAPHMSG"))

(in-package "ROS")
;;//! \htmlinclude keyframeGraphMsg.msg.html


(defclass lsd_slam_viewer::keyframeGraphMsg
  :super ros::object
  :slots (_numFrames _frameData _numConstraints _constraintsData ))

(defmethod lsd_slam_viewer::keyframeGraphMsg
  (:init
   (&key
    ((:numFrames __numFrames) 0)
    ((:frameData __frameData) (make-array 0 :initial-element 0 :element-type :char))
    ((:numConstraints __numConstraints) 0)
    ((:constraintsData __constraintsData) (make-array 0 :initial-element 0 :element-type :char))
    )
   (send-super :init)
   (setq _numFrames (round __numFrames))
   (setq _frameData __frameData)
   (setq _numConstraints (round __numConstraints))
   (setq _constraintsData __constraintsData)
   self)
  (:numFrames
   (&optional __numFrames)
   (if __numFrames (setq _numFrames __numFrames)) _numFrames)
  (:frameData
   (&optional __frameData)
   (if __frameData (setq _frameData __frameData)) _frameData)
  (:numConstraints
   (&optional __numConstraints)
   (if __numConstraints (setq _numConstraints __numConstraints)) _numConstraints)
  (:constraintsData
   (&optional __constraintsData)
   (if __constraintsData (setq _constraintsData __constraintsData)) _constraintsData)
  (:serialization-length
   ()
   (+
    ;; uint32 _numFrames
    4
    ;; uint8[] _frameData
    (* 1    (length _frameData)) 4
    ;; uint32 _numConstraints
    4
    ;; uint8[] _constraintsData
    (* 1    (length _constraintsData)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint32 _numFrames
       (write-long _numFrames s)
     ;; uint8[] _frameData
     (write-long (length _frameData) s)
     (princ _frameData s)
     ;; uint32 _numConstraints
       (write-long _numConstraints s)
     ;; uint8[] _constraintsData
     (write-long (length _constraintsData) s)
     (princ _constraintsData s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint32 _numFrames
     (setq _numFrames (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; uint8[] _frameData
   (let ((n (sys::peek buf ptr- :integer))) (incf ptr- 4)
     (setq _frameData (make-array n :element-type :char))
     (replace _frameData buf :start2 ptr-) (incf ptr- n))
   ;; uint32 _numConstraints
     (setq _numConstraints (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; uint8[] _constraintsData
   (let ((n (sys::peek buf ptr- :integer))) (incf ptr- 4)
     (setq _constraintsData (make-array n :element-type :char))
     (replace _constraintsData buf :start2 ptr-) (incf ptr- n))
   ;;
   self)
  )

(setf (get lsd_slam_viewer::keyframeGraphMsg :md5sum-) "d23a8a86773b54db7399debf884d0c9e")
(setf (get lsd_slam_viewer::keyframeGraphMsg :datatype-) "lsd_slam_viewer/keyframeGraphMsg")
(setf (get lsd_slam_viewer::keyframeGraphMsg :definition-)
      "# data as serialization of sim(3)'s: (int id, float[7] camToWorld)
uint32 numFrames
uint8[] frameData


# constraints (int from, int to, float err)
uint32 numConstraints
uint8[] constraintsData

")



(provide :lsd_slam_viewer/keyframeGraphMsg "d23a8a86773b54db7399debf884d0c9e")


