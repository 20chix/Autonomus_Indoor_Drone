/****************************************************************************
** Meta object code from reading C++ file 'qnode.hpp'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.7)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../../../../src/drone_waypointer/include/drone_waypointer/qnode.hpp"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'qnode.hpp' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.7. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_drone_waypointer__QNode[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
      14,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
      14,       // signalCount

 // signals: signature, parameters, type, tag, flags
      25,   24,   24,   24, 0x05,
      39,   24,   24,   24, 0x05,
      54,   24,   24,   24, 0x05,
      68,   24,   24,   24, 0x05,
      86,   24,   24,   24, 0x05,
     102,   24,   24,   24, 0x05,
     123,   24,   24,   24, 0x05,
     135,   24,   24,   24, 0x05,
     148,   24,   24,   24, 0x05,
     167,   24,   24,   24, 0x05,
     190,   24,   24,   24, 0x05,
     221,   24,   24,   24, 0x05,
     237,   24,   24,   24, 0x05,
     246,   24,   24,   24, 0x05,

       0        // eod
};

static const char qt_meta_stringdata_drone_waypointer__QNode[] = {
    "drone_waypointer::QNode\0\0dataUpdated()\0"
    "imageUpdated()\0rosShutdown()\0"
    "realPoseUpdated()\0targetUpdated()\0"
    "requestNewWaypoint()\0dataReady()\0"
    "imageReady()\0sampleFlightpath()\0"
    "estimatedPoseUpdated()\0"
    "externalEstimatedPoseUpdated()\0"
    "sampleWayHome()\0goHome()\0"
    "updateWayHomeFinalPoint()\0"
};

void drone_waypointer::QNode::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        QNode *_t = static_cast<QNode *>(_o);
        switch (_id) {
        case 0: _t->dataUpdated(); break;
        case 1: _t->imageUpdated(); break;
        case 2: _t->rosShutdown(); break;
        case 3: _t->realPoseUpdated(); break;
        case 4: _t->targetUpdated(); break;
        case 5: _t->requestNewWaypoint(); break;
        case 6: _t->dataReady(); break;
        case 7: _t->imageReady(); break;
        case 8: _t->sampleFlightpath(); break;
        case 9: _t->estimatedPoseUpdated(); break;
        case 10: _t->externalEstimatedPoseUpdated(); break;
        case 11: _t->sampleWayHome(); break;
        case 12: _t->goHome(); break;
        case 13: _t->updateWayHomeFinalPoint(); break;
        default: ;
        }
    }
    Q_UNUSED(_a);
}

const QMetaObjectExtraData drone_waypointer::QNode::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject drone_waypointer::QNode::staticMetaObject = {
    { &QThread::staticMetaObject, qt_meta_stringdata_drone_waypointer__QNode,
      qt_meta_data_drone_waypointer__QNode, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &drone_waypointer::QNode::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *drone_waypointer::QNode::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *drone_waypointer::QNode::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_drone_waypointer__QNode))
        return static_cast<void*>(const_cast< QNode*>(this));
    return QThread::qt_metacast(_clname);
}

int drone_waypointer::QNode::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QThread::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 14)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 14;
    }
    return _id;
}

// SIGNAL 0
void drone_waypointer::QNode::dataUpdated()
{
    QMetaObject::activate(this, &staticMetaObject, 0, 0);
}

// SIGNAL 1
void drone_waypointer::QNode::imageUpdated()
{
    QMetaObject::activate(this, &staticMetaObject, 1, 0);
}

// SIGNAL 2
void drone_waypointer::QNode::rosShutdown()
{
    QMetaObject::activate(this, &staticMetaObject, 2, 0);
}

// SIGNAL 3
void drone_waypointer::QNode::realPoseUpdated()
{
    QMetaObject::activate(this, &staticMetaObject, 3, 0);
}

// SIGNAL 4
void drone_waypointer::QNode::targetUpdated()
{
    QMetaObject::activate(this, &staticMetaObject, 4, 0);
}

// SIGNAL 5
void drone_waypointer::QNode::requestNewWaypoint()
{
    QMetaObject::activate(this, &staticMetaObject, 5, 0);
}

// SIGNAL 6
void drone_waypointer::QNode::dataReady()
{
    QMetaObject::activate(this, &staticMetaObject, 6, 0);
}

// SIGNAL 7
void drone_waypointer::QNode::imageReady()
{
    QMetaObject::activate(this, &staticMetaObject, 7, 0);
}

// SIGNAL 8
void drone_waypointer::QNode::sampleFlightpath()
{
    QMetaObject::activate(this, &staticMetaObject, 8, 0);
}

// SIGNAL 9
void drone_waypointer::QNode::estimatedPoseUpdated()
{
    QMetaObject::activate(this, &staticMetaObject, 9, 0);
}

// SIGNAL 10
void drone_waypointer::QNode::externalEstimatedPoseUpdated()
{
    QMetaObject::activate(this, &staticMetaObject, 10, 0);
}

// SIGNAL 11
void drone_waypointer::QNode::sampleWayHome()
{
    QMetaObject::activate(this, &staticMetaObject, 11, 0);
}

// SIGNAL 12
void drone_waypointer::QNode::goHome()
{
    QMetaObject::activate(this, &staticMetaObject, 12, 0);
}

// SIGNAL 13
void drone_waypointer::QNode::updateWayHomeFinalPoint()
{
    QMetaObject::activate(this, &staticMetaObject, 13, 0);
}
QT_END_MOC_NAMESPACE
