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

class RC {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.status = null;
      this.valid = null;
      this.axis = null;
      this.axis_function = null;
      this.swit = null;
      this.swit_function = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('status')) {
        this.status = initObj.status
      }
      else {
        this.status = 0;
      }
      if (initObj.hasOwnProperty('valid')) {
        this.valid = initObj.valid
      }
      else {
        this.valid = false;
      }
      if (initObj.hasOwnProperty('axis')) {
        this.axis = initObj.axis
      }
      else {
        this.axis = [];
      }
      if (initObj.hasOwnProperty('axis_function')) {
        this.axis_function = initObj.axis_function
      }
      else {
        this.axis_function = [];
      }
      if (initObj.hasOwnProperty('swit')) {
        this.swit = initObj.swit
      }
      else {
        this.swit = [];
      }
      if (initObj.hasOwnProperty('swit_function')) {
        this.swit_function = initObj.swit_function
      }
      else {
        this.swit_function = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type RC
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [status]
    bufferOffset = _serializer.uint8(obj.status, buffer, bufferOffset);
    // Serialize message field [valid]
    bufferOffset = _serializer.bool(obj.valid, buffer, bufferOffset);
    // Serialize message field [axis]
    bufferOffset = _arraySerializer.float32(obj.axis, buffer, bufferOffset, null);
    // Serialize message field [axis_function]
    bufferOffset = _arraySerializer.uint8(obj.axis_function, buffer, bufferOffset, null);
    // Serialize message field [swit]
    bufferOffset = _arraySerializer.int8(obj.swit, buffer, bufferOffset, null);
    // Serialize message field [swit_function]
    bufferOffset = _arraySerializer.uint8(obj.swit_function, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type RC
    let len;
    let data = new RC(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [status]
    data.status = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [valid]
    data.valid = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [axis]
    data.axis = _arrayDeserializer.float32(buffer, bufferOffset, null)
    // Deserialize message field [axis_function]
    data.axis_function = _arrayDeserializer.uint8(buffer, bufferOffset, null)
    // Deserialize message field [swit]
    data.swit = _arrayDeserializer.int8(buffer, bufferOffset, null)
    // Deserialize message field [swit_function]
    data.swit_function = _arrayDeserializer.uint8(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    length += 4 * object.axis.length;
    length += object.axis_function.length;
    length += object.swit.length;
    length += object.swit_function.length;
    return length + 18;
  }

  static datatype() {
    // Returns string type for a message object
    return 'cvg_sim_msgs/RC';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '2691c2fe8c5ab2323146bdd8dd2e449e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
    
    uint8 ROLL = 1
    uint8 PITCH = 2
    uint8 YAW = 3
    uint8 STEER = 4
    uint8 HEIGHT = 5
    uint8 THRUST = 6
    uint8 BRAKE = 7
    
    uint8 status
    bool valid
    
    float32[] axis
    uint8[] axis_function
    
    int8[] swit
    uint8[] swit_function
    
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
    const resolved = new RC(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.status !== undefined) {
      resolved.status = msg.status;
    }
    else {
      resolved.status = 0
    }

    if (msg.valid !== undefined) {
      resolved.valid = msg.valid;
    }
    else {
      resolved.valid = false
    }

    if (msg.axis !== undefined) {
      resolved.axis = msg.axis;
    }
    else {
      resolved.axis = []
    }

    if (msg.axis_function !== undefined) {
      resolved.axis_function = msg.axis_function;
    }
    else {
      resolved.axis_function = []
    }

    if (msg.swit !== undefined) {
      resolved.swit = msg.swit;
    }
    else {
      resolved.swit = []
    }

    if (msg.swit_function !== undefined) {
      resolved.swit_function = msg.swit_function;
    }
    else {
      resolved.swit_function = []
    }

    return resolved;
    }
};

// Constants for message
RC.Constants = {
  ROLL: 1,
  PITCH: 2,
  YAW: 3,
  STEER: 4,
  HEIGHT: 5,
  THRUST: 6,
  BRAKE: 7,
}

module.exports = RC;
