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

class RawImu {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.angular_velocity = null;
      this.linear_acceleration = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('angular_velocity')) {
        this.angular_velocity = initObj.angular_velocity
      }
      else {
        this.angular_velocity = new Array(3).fill(0);
      }
      if (initObj.hasOwnProperty('linear_acceleration')) {
        this.linear_acceleration = initObj.linear_acceleration
      }
      else {
        this.linear_acceleration = new Array(3).fill(0);
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type RawImu
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Check that the constant length array field [angular_velocity] has the right length
    if (obj.angular_velocity.length !== 3) {
      throw new Error('Unable to serialize array field angular_velocity - length must be 3')
    }
    // Serialize message field [angular_velocity]
    bufferOffset = _arraySerializer.uint16(obj.angular_velocity, buffer, bufferOffset, 3);
    // Check that the constant length array field [linear_acceleration] has the right length
    if (obj.linear_acceleration.length !== 3) {
      throw new Error('Unable to serialize array field linear_acceleration - length must be 3')
    }
    // Serialize message field [linear_acceleration]
    bufferOffset = _arraySerializer.uint16(obj.linear_acceleration, buffer, bufferOffset, 3);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type RawImu
    let len;
    let data = new RawImu(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [angular_velocity]
    data.angular_velocity = _arrayDeserializer.uint16(buffer, bufferOffset, 3)
    // Deserialize message field [linear_acceleration]
    data.linear_acceleration = _arrayDeserializer.uint16(buffer, bufferOffset, 3)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 12;
  }

  static datatype() {
    // Returns string type for a message object
    return 'cvg_sim_msgs/RawImu';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '0879a838e899792bcf72ccfe7b5595ef';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
    uint16[3] angular_velocity
    uint16[3] linear_acceleration
    
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
    const resolved = new RawImu(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.angular_velocity !== undefined) {
      resolved.angular_velocity = msg.angular_velocity;
    }
    else {
      resolved.angular_velocity = new Array(3).fill(0)
    }

    if (msg.linear_acceleration !== undefined) {
      resolved.linear_acceleration = msg.linear_acceleration;
    }
    else {
      resolved.linear_acceleration = new Array(3).fill(0)
    }

    return resolved;
    }
};

module.exports = RawImu;
