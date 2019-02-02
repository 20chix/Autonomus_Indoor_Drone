// Auto-generated. Do not edit!

// (in-package cvg_sim_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class Compass {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.magnetic_heading = null;
      this.declination = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('magnetic_heading')) {
        this.magnetic_heading = initObj.magnetic_heading
      }
      else {
        this.magnetic_heading = 0.0;
      }
      if (initObj.hasOwnProperty('declination')) {
        this.declination = initObj.declination
      }
      else {
        this.declination = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Compass
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [magnetic_heading]
    bufferOffset = _serializer.float32(obj.magnetic_heading, buffer, bufferOffset);
    // Serialize message field [declination]
    bufferOffset = _serializer.float32(obj.declination, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Compass
    let len;
    let data = new Compass(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [magnetic_heading]
    data.magnetic_heading = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [declination]
    data.declination = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'cvg_sim_msgs/Compass';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '69b5db73a2f794a5a815baf6b84a4be5';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Compass(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.magnetic_heading !== undefined) {
      resolved.magnetic_heading = msg.magnetic_heading;
    }
    else {
      resolved.magnetic_heading = 0.0
    }

    if (msg.declination !== undefined) {
      resolved.declination = msg.declination;
    }
    else {
      resolved.declination = 0.0
    }

    return resolved;
    }
};

module.exports = Compass;
