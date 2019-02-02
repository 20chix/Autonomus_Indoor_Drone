// Auto-generated. Do not edit!

// (in-package lsd_slam_viewer.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class keyframeGraphMsg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.numFrames = null;
      this.frameData = null;
      this.numConstraints = null;
      this.constraintsData = null;
    }
    else {
      if (initObj.hasOwnProperty('numFrames')) {
        this.numFrames = initObj.numFrames
      }
      else {
        this.numFrames = 0;
      }
      if (initObj.hasOwnProperty('frameData')) {
        this.frameData = initObj.frameData
      }
      else {
        this.frameData = [];
      }
      if (initObj.hasOwnProperty('numConstraints')) {
        this.numConstraints = initObj.numConstraints
      }
      else {
        this.numConstraints = 0;
      }
      if (initObj.hasOwnProperty('constraintsData')) {
        this.constraintsData = initObj.constraintsData
      }
      else {
        this.constraintsData = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type keyframeGraphMsg
    // Serialize message field [numFrames]
    bufferOffset = _serializer.uint32(obj.numFrames, buffer, bufferOffset);
    // Serialize message field [frameData]
    bufferOffset = _arraySerializer.uint8(obj.frameData, buffer, bufferOffset, null);
    // Serialize message field [numConstraints]
    bufferOffset = _serializer.uint32(obj.numConstraints, buffer, bufferOffset);
    // Serialize message field [constraintsData]
    bufferOffset = _arraySerializer.uint8(obj.constraintsData, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type keyframeGraphMsg
    let len;
    let data = new keyframeGraphMsg(null);
    // Deserialize message field [numFrames]
    data.numFrames = _deserializer.uint32(buffer, bufferOffset);
    // Deserialize message field [frameData]
    data.frameData = _arrayDeserializer.uint8(buffer, bufferOffset, null)
    // Deserialize message field [numConstraints]
    data.numConstraints = _deserializer.uint32(buffer, bufferOffset);
    // Deserialize message field [constraintsData]
    data.constraintsData = _arrayDeserializer.uint8(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.frameData.length;
    length += object.constraintsData.length;
    return length + 16;
  }

  static datatype() {
    // Returns string type for a message object
    return 'lsd_slam_viewer/keyframeGraphMsg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd23a8a86773b54db7399debf884d0c9e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # data as serialization of sim(3)'s: (int id, float[7] camToWorld)
    uint32 numFrames
    uint8[] frameData
    
    
    # constraints (int from, int to, float err)
    uint32 numConstraints
    uint8[] constraintsData
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new keyframeGraphMsg(null);
    if (msg.numFrames !== undefined) {
      resolved.numFrames = msg.numFrames;
    }
    else {
      resolved.numFrames = 0
    }

    if (msg.frameData !== undefined) {
      resolved.frameData = msg.frameData;
    }
    else {
      resolved.frameData = []
    }

    if (msg.numConstraints !== undefined) {
      resolved.numConstraints = msg.numConstraints;
    }
    else {
      resolved.numConstraints = 0
    }

    if (msg.constraintsData !== undefined) {
      resolved.constraintsData = msg.constraintsData;
    }
    else {
      resolved.constraintsData = []
    }

    return resolved;
    }
};

module.exports = keyframeGraphMsg;
