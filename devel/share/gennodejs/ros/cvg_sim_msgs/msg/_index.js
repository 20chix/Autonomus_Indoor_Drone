
"use strict";

let Altimeter = require('./Altimeter.js');
let MotorPWM = require('./MotorPWM.js');
let Supply = require('./Supply.js');
let RC = require('./RC.js');
let MotorStatus = require('./MotorStatus.js');
let Altitude = require('./Altitude.js');
let Compass = require('./Compass.js');
let RawRC = require('./RawRC.js');
let PositionXYCommand = require('./PositionXYCommand.js');
let ThrustCommand = require('./ThrustCommand.js');
let RuddersCommand = require('./RuddersCommand.js');
let VelocityZCommand = require('./VelocityZCommand.js');
let AttitudeCommand = require('./AttitudeCommand.js');
let ControllerState = require('./ControllerState.js');
let ServoCommand = require('./ServoCommand.js');
let VelocityXYCommand = require('./VelocityXYCommand.js');
let YawrateCommand = require('./YawrateCommand.js');
let MotorCommand = require('./MotorCommand.js');
let HeadingCommand = require('./HeadingCommand.js');
let RawMagnetic = require('./RawMagnetic.js');
let RawImu = require('./RawImu.js');
let HeightCommand = require('./HeightCommand.js');

module.exports = {
  Altimeter: Altimeter,
  MotorPWM: MotorPWM,
  Supply: Supply,
  RC: RC,
  MotorStatus: MotorStatus,
  Altitude: Altitude,
  Compass: Compass,
  RawRC: RawRC,
  PositionXYCommand: PositionXYCommand,
  ThrustCommand: ThrustCommand,
  RuddersCommand: RuddersCommand,
  VelocityZCommand: VelocityZCommand,
  AttitudeCommand: AttitudeCommand,
  ControllerState: ControllerState,
  ServoCommand: ServoCommand,
  VelocityXYCommand: VelocityXYCommand,
  YawrateCommand: YawrateCommand,
  MotorCommand: MotorCommand,
  HeadingCommand: HeadingCommand,
  RawMagnetic: RawMagnetic,
  RawImu: RawImu,
  HeightCommand: HeightCommand,
};
