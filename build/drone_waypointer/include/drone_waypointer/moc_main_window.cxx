/****************************************************************************
** Meta object code from reading C++ file 'main_window.hpp'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.7)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../../../../src/drone_waypointer/include/drone_waypointer/main_window.hpp"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'main_window.hpp' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.7. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_drone_waypointer__MainWindow[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
      57,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: signature, parameters, type, tag, flags
      30,   29,   29,   29, 0x0a,
      63,   57,   29,   29, 0x0a,
     101,   95,   29,   29, 0x0a,
     147,   29,   29,   29, 0x0a,
     172,   29,   29,   29, 0x0a,
     200,   29,   29,   29, 0x0a,
     225,   29,   29,   29, 0x0a,
     251,   29,   29,   29, 0x0a,
     279,   29,   29,   29, 0x0a,
     308,   29,   29,   29, 0x0a,
     338,   29,   29,   29, 0x0a,
     367,   29,   29,   29, 0x0a,
     392,   29,   29,   29, 0x0a,
     415,   29,   29,   29, 0x0a,
     440,   29,   29,   29, 0x0a,
     465,   29,   29,   29, 0x0a,
     491,   29,   29,   29, 0x0a,
     520,   29,   29,   29, 0x0a,
     551,   29,   29,   29, 0x0a,
     584,   29,   29,   29, 0x0a,
     624,  617,   29,   29, 0x0a,
     642,   29,   29,   29, 0x0a,
     675,   29,   29,   29, 0x0a,
     710,   29,   29,   29, 0x0a,
     742,   29,   29,   29, 0x0a,
     770,   29,   29,   29, 0x0a,
     806,   29,   29,   29, 0x0a,
     844,   29,   29,   29, 0x0a,
     882,   29,   29,   29, 0x0a,
     922,   29,   29,   29, 0x0a,
     939,   29,   29,   29, 0x0a,
     977,  954,   29,   29, 0x0a,
    1011,   29,   29,   29, 0x0a,
    1047,   29,   29,   29, 0x0a,
    1085,   29,   29,   29, 0x0a,
    1126,   29,   29,   29, 0x0a,
    1165,   29,   29,   29, 0x0a,
    1182,   29,   29,   29, 0x0a,
    1200,   29,   29,   29, 0x0a,
    1238,   29,   29,   29, 0x0a,
    1275,   29,   29,   29, 0x0a,
    1289,   29,   29,   29, 0x0a,
    1303,   29,   29,   29, 0x0a,
    1319,   29,   29,   29, 0x0a,
    1364,   29,   29,   29, 0x0a,
    1411,   29,   29,   29, 0x0a,
    1451,   29,   29,   29, 0x0a,
    1489,   29,   29,   29, 0x0a,
    1502,   29,   29,   29, 0x0a,
    1516,   29,   29,   29, 0x0a,
    1533,   29,   29,   29, 0x0a,
    1555,   29,   29,   29, 0x0a,
    1585,   29,   29,   29, 0x0a,
    1607,   29,   29,   29, 0x0a,
    1626,   29,   29,   29, 0x0a,
    1677,   29,   29,   29, 0x0a,
    1726,   29,   29,   29, 0x0a,

       0        // eod
};

static const char qt_meta_stringdata_drone_waypointer__MainWindow[] = {
    "drone_waypointer::MainWindow\0\0"
    "on_actionAbout_triggered()\0check\0"
    "on_button_connect_clicked(bool)\0state\0"
    "on_checkbox_use_environment_stateChanged(int)\0"
    "on_quit_button_clicked()\0"
    "on_button_takeoff_clicked()\0"
    "on_button_land_clicked()\0"
    "on_button_reset_clicked()\0"
    "on_button_forward_clicked()\0"
    "on_button_backward_clicked()\0"
    "on_button_rotateCCW_clicked()\0"
    "on_button_rotateCW_clicked()\0"
    "on_button_halt_clicked()\0"
    "on_button_up_clicked()\0on_button_down_clicked()\0"
    "on_button_left_clicked()\0"
    "on_button_right_clicked()\0"
    "on_fwbw_slider_sliderMoved()\0"
    "on_height_slider_sliderMoved()\0"
    "on_sideways_slider_sliderMoved()\0"
    "on_rotation_slider_sliderMoved()\0"
    "slider\0resetSliders(int)\0"
    "on_button_GoToWaypoint_clicked()\0"
    "on_button_LookAtWaypoint_clicked()\0"
    "on_button_GetWaypoint_clicked()\0"
    "on_button_LookNGo_clicked()\0"
    "on_button_FolowFlightpath_clicked()\0"
    "on_button_openWaypointsFile_clicked()\0"
    "on_button_saveWaypointsFile_clicked()\0"
    "on_checkBox_recordFlight_stateChanged()\0"
    "updateWaypoint()\0saveWaypoint()\0"
    "inFilename,outFilename\0"
    "invertFlightpath(QString,QString)\0"
    "on_checkBox_saveData_stateChanged()\0"
    "on_checkBox_saveImages_stateChanged()\0"
    "on_button_imagesFilePathSelect_clicked()\0"
    "on_spinBox_samplingTime_valueChanged()\0"
    "saveDataToFile()\0saveImageToFile()\0"
    "on_radioButton_bottomCamera_clicked()\0"
    "on_radioButton_frontCamera_clicked()\0"
    "saveWayHome()\0loadWayHome()\0changeWayHome()\0"
    "on_checkBox_batteryBellowLand_stateChanged()\0"
    "on_checkBox_batteryBellowGoHome_stateChanged()\0"
    "on_checkBox_noWifiSignal_stateChanged()\0"
    "on_checkBox_safeFlight_stateChanged()\0"
    "updateData()\0updateImage()\0updateRealPose()\0"
    "updateEstimatedPose()\0"
    "updateExternalEstimatedPose()\0"
    "updateTargetInDrone()\0updateSliderLCDs()\0"
    "on_radioButton_Simulation_PoseEstimation_clicked()\0"
    "on_radioButton_External_PoseEstimation_clicked()\0"
    "on_radioButton_Internal_DR_PoseEstimation_clicked()\0"
};

void drone_waypointer::MainWindow::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        MainWindow *_t = static_cast<MainWindow *>(_o);
        switch (_id) {
        case 0: _t->on_actionAbout_triggered(); break;
        case 1: _t->on_button_connect_clicked((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 2: _t->on_checkbox_use_environment_stateChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 3: _t->on_quit_button_clicked(); break;
        case 4: _t->on_button_takeoff_clicked(); break;
        case 5: _t->on_button_land_clicked(); break;
        case 6: _t->on_button_reset_clicked(); break;
        case 7: _t->on_button_forward_clicked(); break;
        case 8: _t->on_button_backward_clicked(); break;
        case 9: _t->on_button_rotateCCW_clicked(); break;
        case 10: _t->on_button_rotateCW_clicked(); break;
        case 11: _t->on_button_halt_clicked(); break;
        case 12: _t->on_button_up_clicked(); break;
        case 13: _t->on_button_down_clicked(); break;
        case 14: _t->on_button_left_clicked(); break;
        case 15: _t->on_button_right_clicked(); break;
        case 16: _t->on_fwbw_slider_sliderMoved(); break;
        case 17: _t->on_height_slider_sliderMoved(); break;
        case 18: _t->on_sideways_slider_sliderMoved(); break;
        case 19: _t->on_rotation_slider_sliderMoved(); break;
        case 20: _t->resetSliders((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 21: _t->on_button_GoToWaypoint_clicked(); break;
        case 22: _t->on_button_LookAtWaypoint_clicked(); break;
        case 23: _t->on_button_GetWaypoint_clicked(); break;
        case 24: _t->on_button_LookNGo_clicked(); break;
        case 25: _t->on_button_FolowFlightpath_clicked(); break;
        case 26: _t->on_button_openWaypointsFile_clicked(); break;
        case 27: _t->on_button_saveWaypointsFile_clicked(); break;
        case 28: _t->on_checkBox_recordFlight_stateChanged(); break;
        case 29: _t->updateWaypoint(); break;
        case 30: _t->saveWaypoint(); break;
        case 31: _t->invertFlightpath((*reinterpret_cast< QString(*)>(_a[1])),(*reinterpret_cast< QString(*)>(_a[2]))); break;
        case 32: _t->on_checkBox_saveData_stateChanged(); break;
        case 33: _t->on_checkBox_saveImages_stateChanged(); break;
        case 34: _t->on_button_imagesFilePathSelect_clicked(); break;
        case 35: _t->on_spinBox_samplingTime_valueChanged(); break;
        case 36: _t->saveDataToFile(); break;
        case 37: _t->saveImageToFile(); break;
        case 38: _t->on_radioButton_bottomCamera_clicked(); break;
        case 39: _t->on_radioButton_frontCamera_clicked(); break;
        case 40: _t->saveWayHome(); break;
        case 41: _t->loadWayHome(); break;
        case 42: _t->changeWayHome(); break;
        case 43: _t->on_checkBox_batteryBellowLand_stateChanged(); break;
        case 44: _t->on_checkBox_batteryBellowGoHome_stateChanged(); break;
        case 45: _t->on_checkBox_noWifiSignal_stateChanged(); break;
        case 46: _t->on_checkBox_safeFlight_stateChanged(); break;
        case 47: _t->updateData(); break;
        case 48: _t->updateImage(); break;
        case 49: _t->updateRealPose(); break;
        case 50: _t->updateEstimatedPose(); break;
        case 51: _t->updateExternalEstimatedPose(); break;
        case 52: _t->updateTargetInDrone(); break;
        case 53: _t->updateSliderLCDs(); break;
        case 54: _t->on_radioButton_Simulation_PoseEstimation_clicked(); break;
        case 55: _t->on_radioButton_External_PoseEstimation_clicked(); break;
        case 56: _t->on_radioButton_Internal_DR_PoseEstimation_clicked(); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData drone_waypointer::MainWindow::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject drone_waypointer::MainWindow::staticMetaObject = {
    { &QMainWindow::staticMetaObject, qt_meta_stringdata_drone_waypointer__MainWindow,
      qt_meta_data_drone_waypointer__MainWindow, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &drone_waypointer::MainWindow::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *drone_waypointer::MainWindow::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *drone_waypointer::MainWindow::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_drone_waypointer__MainWindow))
        return static_cast<void*>(const_cast< MainWindow*>(this));
    return QMainWindow::qt_metacast(_clname);
}

int drone_waypointer::MainWindow::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QMainWindow::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 57)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 57;
    }
    return _id;
}
QT_END_MOC_NAMESPACE
