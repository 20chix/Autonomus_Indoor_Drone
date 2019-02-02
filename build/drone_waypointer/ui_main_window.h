/********************************************************************************
** Form generated from reading UI file 'main_window.ui'
**
** Created by: Qt User Interface Compiler version 4.8.7
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAIN_WINDOW_H
#define UI_MAIN_WINDOW_H

#include <QtCore/QLocale>
#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QCheckBox>
#include <QtGui/QGridLayout>
#include <QtGui/QGroupBox>
#include <QtGui/QHBoxLayout>
#include <QtGui/QHeaderView>
#include <QtGui/QLCDNumber>
#include <QtGui/QLabel>
#include <QtGui/QLineEdit>
#include <QtGui/QMainWindow>
#include <QtGui/QMenu>
#include <QtGui/QMenuBar>
#include <QtGui/QPushButton>
#include <QtGui/QRadioButton>
#include <QtGui/QSlider>
#include <QtGui/QSpacerItem>
#include <QtGui/QSpinBox>
#include <QtGui/QStatusBar>
#include <QtGui/QTabWidget>
#include <QtGui/QTextEdit>
#include <QtGui/QToolBox>
#include <QtGui/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindowDesign
{
public:
    QAction *action_Quit;
    QAction *action_Preferences;
    QAction *actionAbout;
    QAction *actionAbout_Qt;
    QWidget *centralwidget;
    QHBoxLayout *hboxLayout;
    QTabWidget *tab_manager;
    QWidget *tab_commandPanel;
    QGroupBox *RosMaster;
    QGridLayout *gridLayout;
    QLabel *label_2;
    QPushButton *button_connect;
    QSpacerItem *horizontalSpacer;
    QLineEdit *line_edit_host;
    QLineEdit *line_edit_master;
    QCheckBox *checkbox_remember_settings;
    QLineEdit *line_edit_topic;
    QLabel *label_3;
    QLabel *label;
    QCheckBox *checkbox_use_environment;
    QSpacerItem *verticalSpacer;
    QSpacerItem *verticalSpacer_2;
    QPushButton *quit_button;
    QGroupBox *WaypointSettings;
    QGridLayout *gridLayout_2;
    QLabel *label_29;
    QSpacerItem *verticalSpacer_3;
    QPushButton *button_imagesFilePathSelect;
    QLineEdit *line_edit_loadWaypointFilePath;
    QCheckBox *checkBox_saveData;
    QPushButton *button_openWaypointsFile;
    QLineEdit *line_edit_saveWaypointFilePath;
    QLabel *label_28;
    QCheckBox *checkBox_saveImages;
    QLineEdit *line_edit_saveImageFilePath;
    QSpacerItem *horizontalSpacer_2;
    QPushButton *button_saveWaypointsFile;
    QLabel *label_26;
    QLabel *label_25;
    QSpacerItem *verticalSpacer_4;
    QSpinBox *spinBox_samplingTime;
    QSpacerItem *horizontalSpacer_3;
    QCheckBox *checkBox_safeFlight;
    QGroupBox *TopicSettings;
    QGridLayout *gridLayout_4;
    QRadioButton *radioButton_Simulation_PoseEstimation;
    QRadioButton *radioButton_External_PoseEstimation;
    QLineEdit *line_edit_realPoseTopic;
    QLabel *label_12;
    QRadioButton *radioButton_Internal_DR_PoseEstimation;
    QGroupBox *groupBox;
    QCheckBox *checkBox_batteryBellowLand;
    QCheckBox *checkBox_batteryBellowGoHome;
    QCheckBox *checkBox_noWifiSignal;
    QWidget *tab_controls;
    QLCDNumber *batteryLCD;
    QLabel *label_4;
    QLabel *label_5;
    QLCDNumber *stateLCD;
    QGroupBox *groupBox_3;
    QRadioButton *radioButton_bottomCamera;
    QRadioButton *radioButton_frontCamera;
    QLabel *label_7;
    QGroupBox *groupBox_4;
    QLabel *label_6;
    QTabWidget *tab_controlMethods;
    QWidget *tab_buttonControls;
    QPushButton *button_down;
    QPushButton *button_up;
    QPushButton *button_left;
    QPushButton *button_rotateCW;
    QPushButton *button_forward;
    QPushButton *button_backward;
    QPushButton *button_right;
    QPushButton *button_rotateCCW;
    QWidget *tab_sliderControls;
    QLCDNumber *sideways_LCD;
    QLabel *label_11;
    QSlider *sideways_slider;
    QSlider *height_slider;
    QLCDNumber *rotation_LCD;
    QSlider *fwbw_slider;
    QLabel *label_8;
    QLabel *label_10;
    QSlider *rotation_slider;
    QLabel *label_9;
    QLCDNumber *fwbw_LCD;
    QLCDNumber *height_LCD;
    QWidget *tab_WaypointControl;
    QPushButton *button_GoToWaypoint;
    QPushButton *button_LookAtWaypoint;
    QGroupBox *groupBox_5;
    QLineEdit *lineEdit_targetZ;
    QLabel *label_19;
    QLineEdit *lineEdit_targetX;
    QLineEdit *lineEdit_targetY;
    QLabel *label_20;
    QLabel *label_21;
    QGroupBox *groupBox_6;
    QLineEdit *lineEdit_targetAngleZ;
    QLineEdit *lineEdit_errorX;
    QLabel *label_24;
    QLineEdit *lineEdit_errorY;
    QLabel *label_22;
    QLabel *label_23;
    QLabel *label_27;
    QLineEdit *lineEdit_errorZ;
    QPushButton *button_GetWaypoint;
    QPushButton *button_LookNGo;
    QPushButton *button_FolowFlightpath;
    QTextEdit *textEdit_waypoints;
    QCheckBox *checkBox_recordFlight;
    QCheckBox *checkBox_invertFlightpath;
    QPushButton *button_takeoff;
    QPushButton *button_reset;
    QPushButton *button_halt;
    QPushButton *button_land;
    QGroupBox *groupBox_9;
    QLabel *label_33;
    QLabel *label_34;
    QLineEdit *lineEdit_realAngleY;
    QLabel *label_35;
    QLineEdit *lineEdit_realAngleX;
    QLineEdit *lineEdit_realAngleZ;
    QToolBox *toolBox;
    QWidget *toolBoxPage1;
    QGroupBox *groupBox_2;
    QLineEdit *lineEdit_estimatedPoseX;
    QLineEdit *lineEdit_estimatedPoseY;
    QLineEdit *lineEdit_estimatedPoseZ;
    QLabel *label_13;
    QLabel *label_14;
    QLabel *label_15;
    QWidget *toolBoxPage2;
    QGroupBox *groupBox_7;
    QLineEdit *lineEdit_realPoseX;
    QLineEdit *lineEdit_realPoseY;
    QLineEdit *lineEdit_realPoseZ;
    QLabel *label_30;
    QLabel *label_31;
    QLabel *label_32;
    QWidget *toolBoxPage3;
    QGroupBox *groupBox_8;
    QLineEdit *lineEdit_poseErrorX;
    QLineEdit *lineEdit_poseErrorY;
    QLineEdit *lineEdit_poseErrorZ;
    QLabel *label_36;
    QLabel *label_37;
    QLabel *label_38;
    QMenuBar *menubar;
    QMenu *menu_File;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindowDesign)
    {
        if (MainWindowDesign->objectName().isEmpty())
            MainWindowDesign->setObjectName(QString::fromUtf8("MainWindowDesign"));
        MainWindowDesign->resize(1000, 788);
        QIcon icon;
        icon.addFile(QString::fromUtf8(":/images/icon.png"), QSize(), QIcon::Normal, QIcon::Off);
        MainWindowDesign->setWindowIcon(icon);
        MainWindowDesign->setLocale(QLocale(QLocale::English, QLocale::Australia));
        action_Quit = new QAction(MainWindowDesign);
        action_Quit->setObjectName(QString::fromUtf8("action_Quit"));
        action_Quit->setShortcutContext(Qt::ApplicationShortcut);
        action_Preferences = new QAction(MainWindowDesign);
        action_Preferences->setObjectName(QString::fromUtf8("action_Preferences"));
        actionAbout = new QAction(MainWindowDesign);
        actionAbout->setObjectName(QString::fromUtf8("actionAbout"));
        actionAbout_Qt = new QAction(MainWindowDesign);
        actionAbout_Qt->setObjectName(QString::fromUtf8("actionAbout_Qt"));
        centralwidget = new QWidget(MainWindowDesign);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        hboxLayout = new QHBoxLayout(centralwidget);
        hboxLayout->setObjectName(QString::fromUtf8("hboxLayout"));
        tab_manager = new QTabWidget(centralwidget);
        tab_manager->setObjectName(QString::fromUtf8("tab_manager"));
        tab_manager->setEnabled(true);
        tab_manager->setMinimumSize(QSize(100, 0));
        tab_manager->setLocale(QLocale(QLocale::English, QLocale::Australia));
        tab_commandPanel = new QWidget();
        tab_commandPanel->setObjectName(QString::fromUtf8("tab_commandPanel"));
        RosMaster = new QGroupBox(tab_commandPanel);
        RosMaster->setObjectName(QString::fromUtf8("RosMaster"));
        RosMaster->setGeometry(QRect(504, 10, 451, 384));
        gridLayout = new QGridLayout(RosMaster);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        label_2 = new QLabel(RosMaster);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setFrameShape(QFrame::StyledPanel);
        label_2->setFrameShadow(QFrame::Raised);

        gridLayout->addWidget(label_2, 2, 0, 1, 1);

        button_connect = new QPushButton(RosMaster);
        button_connect->setObjectName(QString::fromUtf8("button_connect"));
        button_connect->setEnabled(true);
        QSizePolicy sizePolicy(QSizePolicy::MinimumExpanding, QSizePolicy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(button_connect->sizePolicy().hasHeightForWidth());
        button_connect->setSizePolicy(sizePolicy);

        gridLayout->addWidget(button_connect, 10, 1, 1, 1);

        horizontalSpacer = new QSpacerItem(170, 21, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer, 10, 0, 1, 1);

        line_edit_host = new QLineEdit(RosMaster);
        line_edit_host->setObjectName(QString::fromUtf8("line_edit_host"));

        gridLayout->addWidget(line_edit_host, 3, 0, 1, 2);

        line_edit_master = new QLineEdit(RosMaster);
        line_edit_master->setObjectName(QString::fromUtf8("line_edit_master"));

        gridLayout->addWidget(line_edit_master, 1, 0, 1, 2);

        checkbox_remember_settings = new QCheckBox(RosMaster);
        checkbox_remember_settings->setObjectName(QString::fromUtf8("checkbox_remember_settings"));
        checkbox_remember_settings->setLayoutDirection(Qt::RightToLeft);

        gridLayout->addWidget(checkbox_remember_settings, 9, 0, 1, 2);

        line_edit_topic = new QLineEdit(RosMaster);
        line_edit_topic->setObjectName(QString::fromUtf8("line_edit_topic"));
        line_edit_topic->setEnabled(false);

        gridLayout->addWidget(line_edit_topic, 5, 0, 1, 2);

        label_3 = new QLabel(RosMaster);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setFrameShape(QFrame::StyledPanel);
        label_3->setFrameShadow(QFrame::Raised);

        gridLayout->addWidget(label_3, 4, 0, 1, 1);

        label = new QLabel(RosMaster);
        label->setObjectName(QString::fromUtf8("label"));
        label->setFrameShape(QFrame::StyledPanel);
        label->setFrameShadow(QFrame::Raised);

        gridLayout->addWidget(label, 0, 0, 1, 1);

        checkbox_use_environment = new QCheckBox(RosMaster);
        checkbox_use_environment->setObjectName(QString::fromUtf8("checkbox_use_environment"));
        checkbox_use_environment->setLayoutDirection(Qt::RightToLeft);

        gridLayout->addWidget(checkbox_use_environment, 8, 0, 1, 2);

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer, 6, 1, 1, 1);

        verticalSpacer_2 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer_2, 6, 0, 1, 1);

        quit_button = new QPushButton(tab_commandPanel);
        quit_button->setObjectName(QString::fromUtf8("quit_button"));
        quit_button->setGeometry(QRect(750, 640, 211, 27));
        sizePolicy.setHeightForWidth(quit_button->sizePolicy().hasHeightForWidth());
        quit_button->setSizePolicy(sizePolicy);
        WaypointSettings = new QGroupBox(tab_commandPanel);
        WaypointSettings->setObjectName(QString::fromUtf8("WaypointSettings"));
        WaypointSettings->setGeometry(QRect(10, 10, 451, 471));
        gridLayout_2 = new QGridLayout(WaypointSettings);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        label_29 = new QLabel(WaypointSettings);
        label_29->setObjectName(QString::fromUtf8("label_29"));

        gridLayout_2->addWidget(label_29, 12, 2, 1, 1);

        verticalSpacer_3 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout_2->addItem(verticalSpacer_3, 13, 0, 1, 1);

        button_imagesFilePathSelect = new QPushButton(WaypointSettings);
        button_imagesFilePathSelect->setObjectName(QString::fromUtf8("button_imagesFilePathSelect"));
        button_imagesFilePathSelect->setEnabled(true);
        sizePolicy.setHeightForWidth(button_imagesFilePathSelect->sizePolicy().hasHeightForWidth());
        button_imagesFilePathSelect->setSizePolicy(sizePolicy);

        gridLayout_2->addWidget(button_imagesFilePathSelect, 10, 2, 1, 1);

        line_edit_loadWaypointFilePath = new QLineEdit(WaypointSettings);
        line_edit_loadWaypointFilePath->setObjectName(QString::fromUtf8("line_edit_loadWaypointFilePath"));

        gridLayout_2->addWidget(line_edit_loadWaypointFilePath, 1, 0, 1, 3);

        checkBox_saveData = new QCheckBox(WaypointSettings);
        checkBox_saveData->setObjectName(QString::fromUtf8("checkBox_saveData"));

        gridLayout_2->addWidget(checkBox_saveData, 11, 0, 1, 1);

        button_openWaypointsFile = new QPushButton(WaypointSettings);
        button_openWaypointsFile->setObjectName(QString::fromUtf8("button_openWaypointsFile"));
        button_openWaypointsFile->setEnabled(true);
        sizePolicy.setHeightForWidth(button_openWaypointsFile->sizePolicy().hasHeightForWidth());
        button_openWaypointsFile->setSizePolicy(sizePolicy);

        gridLayout_2->addWidget(button_openWaypointsFile, 2, 2, 1, 1);

        line_edit_saveWaypointFilePath = new QLineEdit(WaypointSettings);
        line_edit_saveWaypointFilePath->setObjectName(QString::fromUtf8("line_edit_saveWaypointFilePath"));

        gridLayout_2->addWidget(line_edit_saveWaypointFilePath, 5, 0, 1, 3);

        label_28 = new QLabel(WaypointSettings);
        label_28->setObjectName(QString::fromUtf8("label_28"));
        label_28->setFrameShape(QFrame::StyledPanel);
        label_28->setFrameShadow(QFrame::Raised);

        gridLayout_2->addWidget(label_28, 7, 0, 1, 3);

        checkBox_saveImages = new QCheckBox(WaypointSettings);
        checkBox_saveImages->setObjectName(QString::fromUtf8("checkBox_saveImages"));

        gridLayout_2->addWidget(checkBox_saveImages, 12, 0, 1, 1);

        line_edit_saveImageFilePath = new QLineEdit(WaypointSettings);
        line_edit_saveImageFilePath->setObjectName(QString::fromUtf8("line_edit_saveImageFilePath"));

        gridLayout_2->addWidget(line_edit_saveImageFilePath, 8, 0, 1, 3);

        horizontalSpacer_2 = new QSpacerItem(170, 21, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout_2->addItem(horizontalSpacer_2, 6, 0, 1, 1);

        button_saveWaypointsFile = new QPushButton(WaypointSettings);
        button_saveWaypointsFile->setObjectName(QString::fromUtf8("button_saveWaypointsFile"));
        button_saveWaypointsFile->setEnabled(true);
        sizePolicy.setHeightForWidth(button_saveWaypointsFile->sizePolicy().hasHeightForWidth());
        button_saveWaypointsFile->setSizePolicy(sizePolicy);

        gridLayout_2->addWidget(button_saveWaypointsFile, 6, 2, 1, 1);

        label_26 = new QLabel(WaypointSettings);
        label_26->setObjectName(QString::fromUtf8("label_26"));
        label_26->setFrameShape(QFrame::StyledPanel);
        label_26->setFrameShadow(QFrame::Raised);

        gridLayout_2->addWidget(label_26, 4, 0, 1, 3);

        label_25 = new QLabel(WaypointSettings);
        label_25->setObjectName(QString::fromUtf8("label_25"));
        label_25->setFrameShape(QFrame::StyledPanel);
        label_25->setFrameShadow(QFrame::Raised);

        gridLayout_2->addWidget(label_25, 0, 0, 1, 3);

        verticalSpacer_4 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout_2->addItem(verticalSpacer_4, 14, 2, 1, 1);

        spinBox_samplingTime = new QSpinBox(WaypointSettings);
        spinBox_samplingTime->setObjectName(QString::fromUtf8("spinBox_samplingTime"));
        spinBox_samplingTime->setMinimum(200);
        spinBox_samplingTime->setMaximum(60000);
        spinBox_samplingTime->setSingleStep(100);
        spinBox_samplingTime->setValue(500);

        gridLayout_2->addWidget(spinBox_samplingTime, 13, 2, 1, 1);

        horizontalSpacer_3 = new QSpacerItem(170, 21, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout_2->addItem(horizontalSpacer_3, 13, 1, 1, 1);

        checkBox_safeFlight = new QCheckBox(WaypointSettings);
        checkBox_safeFlight->setObjectName(QString::fromUtf8("checkBox_safeFlight"));

        gridLayout_2->addWidget(checkBox_safeFlight, 14, 0, 1, 1);

        TopicSettings = new QGroupBox(tab_commandPanel);
        TopicSettings->setObjectName(QString::fromUtf8("TopicSettings"));
        TopicSettings->setGeometry(QRect(10, 500, 451, 181));
        gridLayout_4 = new QGridLayout(TopicSettings);
        gridLayout_4->setObjectName(QString::fromUtf8("gridLayout_4"));
        radioButton_Simulation_PoseEstimation = new QRadioButton(TopicSettings);
        radioButton_Simulation_PoseEstimation->setObjectName(QString::fromUtf8("radioButton_Simulation_PoseEstimation"));

        gridLayout_4->addWidget(radioButton_Simulation_PoseEstimation, 2, 0, 1, 1);

        radioButton_External_PoseEstimation = new QRadioButton(TopicSettings);
        radioButton_External_PoseEstimation->setObjectName(QString::fromUtf8("radioButton_External_PoseEstimation"));

        gridLayout_4->addWidget(radioButton_External_PoseEstimation, 3, 0, 1, 1);

        line_edit_realPoseTopic = new QLineEdit(TopicSettings);
        line_edit_realPoseTopic->setObjectName(QString::fromUtf8("line_edit_realPoseTopic"));

        gridLayout_4->addWidget(line_edit_realPoseTopic, 1, 0, 1, 1);

        label_12 = new QLabel(TopicSettings);
        label_12->setObjectName(QString::fromUtf8("label_12"));
        label_12->setFrameShape(QFrame::StyledPanel);
        label_12->setFrameShadow(QFrame::Raised);

        gridLayout_4->addWidget(label_12, 0, 0, 1, 1);

        radioButton_Internal_DR_PoseEstimation = new QRadioButton(TopicSettings);
        radioButton_Internal_DR_PoseEstimation->setObjectName(QString::fromUtf8("radioButton_Internal_DR_PoseEstimation"));

        gridLayout_4->addWidget(radioButton_Internal_DR_PoseEstimation, 4, 0, 1, 1);

        groupBox = new QGroupBox(tab_commandPanel);
        groupBox->setObjectName(QString::fromUtf8("groupBox"));
        groupBox->setGeometry(QRect(520, 410, 431, 201));
        checkBox_batteryBellowLand = new QCheckBox(groupBox);
        checkBox_batteryBellowLand->setObjectName(QString::fromUtf8("checkBox_batteryBellowLand"));
        checkBox_batteryBellowLand->setGeometry(QRect(10, 30, 231, 22));
        checkBox_batteryBellowGoHome = new QCheckBox(groupBox);
        checkBox_batteryBellowGoHome->setObjectName(QString::fromUtf8("checkBox_batteryBellowGoHome"));
        checkBox_batteryBellowGoHome->setGeometry(QRect(10, 60, 231, 22));
        checkBox_noWifiSignal = new QCheckBox(groupBox);
        checkBox_noWifiSignal->setObjectName(QString::fromUtf8("checkBox_noWifiSignal"));
        checkBox_noWifiSignal->setGeometry(QRect(10, 90, 231, 22));
        tab_manager->addTab(tab_commandPanel, QString());
        tab_controls = new QWidget();
        tab_controls->setObjectName(QString::fromUtf8("tab_controls"));
        batteryLCD = new QLCDNumber(tab_controls);
        batteryLCD->setObjectName(QString::fromUtf8("batteryLCD"));
        batteryLCD->setGeometry(QRect(30, 580, 41, 31));
        batteryLCD->setNumDigits(3);
        batteryLCD->setProperty("intValue", QVariant(0));
        label_4 = new QLabel(tab_controls);
        label_4->setObjectName(QString::fromUtf8("label_4"));
        label_4->setGeometry(QRect(30, 560, 58, 15));
        label_5 = new QLabel(tab_controls);
        label_5->setObjectName(QString::fromUtf8("label_5"));
        label_5->setGeometry(QRect(90, 560, 58, 15));
        stateLCD = new QLCDNumber(tab_controls);
        stateLCD->setObjectName(QString::fromUtf8("stateLCD"));
        stateLCD->setGeometry(QRect(90, 580, 31, 31));
        stateLCD->setNumDigits(1);
        groupBox_3 = new QGroupBox(tab_controls);
        groupBox_3->setObjectName(QString::fromUtf8("groupBox_3"));
        groupBox_3->setGeometry(QRect(20, 350, 151, 81));
        radioButton_bottomCamera = new QRadioButton(groupBox_3);
        radioButton_bottomCamera->setObjectName(QString::fromUtf8("radioButton_bottomCamera"));
        radioButton_bottomCamera->setGeometry(QRect(10, 40, 131, 20));
        radioButton_frontCamera = new QRadioButton(groupBox_3);
        radioButton_frontCamera->setObjectName(QString::fromUtf8("radioButton_frontCamera"));
        radioButton_frontCamera->setGeometry(QRect(10, 20, 131, 20));
        radioButton_frontCamera->setChecked(true);
        label_7 = new QLabel(tab_controls);
        label_7->setObjectName(QString::fromUtf8("label_7"));
        label_7->setGeometry(QRect(150, 580, 101, 31));
        groupBox_4 = new QGroupBox(tab_controls);
        groupBox_4->setObjectName(QString::fromUtf8("groupBox_4"));
        groupBox_4->setGeometry(QRect(340, 340, 631, 351));
        label_6 = new QLabel(groupBox_4);
        label_6->setObjectName(QString::fromUtf8("label_6"));
        label_6->setGeometry(QRect(10, 20, 601, 321));
        QFont font;
        font.setPointSize(24);
        font.setBold(true);
        font.setWeight(75);
        label_6->setFont(font);
        label_6->setLayoutDirection(Qt::LeftToRight);
        label_6->setAutoFillBackground(true);
        tab_controlMethods = new QTabWidget(tab_controls);
        tab_controlMethods->setObjectName(QString::fromUtf8("tab_controlMethods"));
        tab_controlMethods->setGeometry(QRect(10, 10, 731, 261));
        tab_buttonControls = new QWidget();
        tab_buttonControls->setObjectName(QString::fromUtf8("tab_buttonControls"));
        button_down = new QPushButton(tab_buttonControls);
        button_down->setObjectName(QString::fromUtf8("button_down"));
        button_down->setGeometry(QRect(320, 150, 79, 25));
        button_up = new QPushButton(tab_buttonControls);
        button_up->setObjectName(QString::fromUtf8("button_up"));
        button_up->setGeometry(QRect(320, 110, 79, 25));
        button_left = new QPushButton(tab_buttonControls);
        button_left->setObjectName(QString::fromUtf8("button_left"));
        button_left->setGeometry(QRect(10, 84, 71, 31));
        button_rotateCW = new QPushButton(tab_buttonControls);
        button_rotateCW->setObjectName(QString::fromUtf8("button_rotateCW"));
        button_rotateCW->setGeometry(QRect(370, 40, 71, 51));
        button_forward = new QPushButton(tab_buttonControls);
        button_forward->setObjectName(QString::fromUtf8("button_forward"));
        button_forward->setGeometry(QRect(90, 40, 81, 31));
        button_backward = new QPushButton(tab_buttonControls);
        button_backward->setObjectName(QString::fromUtf8("button_backward"));
        button_backward->setGeometry(QRect(90, 140, 81, 31));
        button_right = new QPushButton(tab_buttonControls);
        button_right->setObjectName(QString::fromUtf8("button_right"));
        button_right->setGeometry(QRect(170, 84, 71, 31));
        button_rotateCCW = new QPushButton(tab_buttonControls);
        button_rotateCCW->setObjectName(QString::fromUtf8("button_rotateCCW"));
        button_rotateCCW->setGeometry(QRect(270, 40, 71, 51));
        tab_controlMethods->addTab(tab_buttonControls, QString());
        tab_sliderControls = new QWidget();
        tab_sliderControls->setObjectName(QString::fromUtf8("tab_sliderControls"));
        sideways_LCD = new QLCDNumber(tab_sliderControls);
        sideways_LCD->setObjectName(QString::fromUtf8("sideways_LCD"));
        sideways_LCD->setGeometry(QRect(350, 40, 61, 31));
        sideways_LCD->setSmallDecimalPoint(false);
        sideways_LCD->setNumDigits(4);
        sideways_LCD->setDigitCount(4);
        sideways_LCD->setProperty("value", QVariant(0));
        sideways_LCD->setProperty("intValue", QVariant(0));
        label_11 = new QLabel(tab_sliderControls);
        label_11->setObjectName(QString::fromUtf8("label_11"));
        label_11->setGeometry(QRect(100, 10, 61, 31));
        sideways_slider = new QSlider(tab_sliderControls);
        sideways_slider->setObjectName(QString::fromUtf8("sideways_slider"));
        sideways_slider->setGeometry(QRect(240, 50, 101, 21));
        sideways_slider->setMinimum(-100);
        sideways_slider->setMaximum(100);
        sideways_slider->setValue(0);
        sideways_slider->setOrientation(Qt::Horizontal);
        sideways_slider->setTickPosition(QSlider::TicksAbove);
        sideways_slider->setTickInterval(50);
        height_slider = new QSlider(tab_sliderControls);
        height_slider->setObjectName(QString::fromUtf8("height_slider"));
        height_slider->setGeometry(QRect(110, 50, 31, 141));
        height_slider->setMinimum(-100);
        height_slider->setMaximum(100);
        height_slider->setSingleStep(1);
        height_slider->setOrientation(Qt::Vertical);
        height_slider->setInvertedAppearance(false);
        height_slider->setInvertedControls(false);
        height_slider->setTickPosition(QSlider::TicksBelow);
        height_slider->setTickInterval(50);
        rotation_LCD = new QLCDNumber(tab_sliderControls);
        rotation_LCD->setObjectName(QString::fromUtf8("rotation_LCD"));
        rotation_LCD->setGeometry(QRect(350, 100, 61, 31));
        rotation_LCD->setSmallDecimalPoint(false);
        rotation_LCD->setNumDigits(4);
        rotation_LCD->setDigitCount(4);
        rotation_LCD->setProperty("value", QVariant(0));
        rotation_LCD->setProperty("intValue", QVariant(0));
        fwbw_slider = new QSlider(tab_sliderControls);
        fwbw_slider->setObjectName(QString::fromUtf8("fwbw_slider"));
        fwbw_slider->setGeometry(QRect(19, 49, 31, 141));
        fwbw_slider->setMinimum(-100);
        fwbw_slider->setMaximum(100);
        fwbw_slider->setSingleStep(1);
        fwbw_slider->setOrientation(Qt::Vertical);
        fwbw_slider->setInvertedAppearance(false);
        fwbw_slider->setInvertedControls(false);
        fwbw_slider->setTickPosition(QSlider::TicksBelow);
        fwbw_slider->setTickInterval(50);
        label_8 = new QLabel(tab_sliderControls);
        label_8->setObjectName(QString::fromUtf8("label_8"));
        label_8->setGeometry(QRect(20, 10, 61, 31));
        label_10 = new QLabel(tab_sliderControls);
        label_10->setObjectName(QString::fromUtf8("label_10"));
        label_10->setGeometry(QRect(260, 80, 61, 31));
        rotation_slider = new QSlider(tab_sliderControls);
        rotation_slider->setObjectName(QString::fromUtf8("rotation_slider"));
        rotation_slider->setGeometry(QRect(240, 110, 101, 21));
        rotation_slider->setMinimum(-100);
        rotation_slider->setMaximum(100);
        rotation_slider->setValue(0);
        rotation_slider->setOrientation(Qt::Horizontal);
        rotation_slider->setTickPosition(QSlider::TicksAbove);
        rotation_slider->setTickInterval(50);
        label_9 = new QLabel(tab_sliderControls);
        label_9->setObjectName(QString::fromUtf8("label_9"));
        label_9->setGeometry(QRect(260, 10, 61, 31));
        fwbw_LCD = new QLCDNumber(tab_sliderControls);
        fwbw_LCD->setObjectName(QString::fromUtf8("fwbw_LCD"));
        fwbw_LCD->setGeometry(QRect(10, 200, 61, 31));
        fwbw_LCD->setSmallDecimalPoint(false);
        fwbw_LCD->setNumDigits(4);
        fwbw_LCD->setDigitCount(4);
        fwbw_LCD->setProperty("value", QVariant(0));
        fwbw_LCD->setProperty("intValue", QVariant(0));
        height_LCD = new QLCDNumber(tab_sliderControls);
        height_LCD->setObjectName(QString::fromUtf8("height_LCD"));
        height_LCD->setGeometry(QRect(90, 200, 61, 31));
        height_LCD->setSmallDecimalPoint(false);
        height_LCD->setNumDigits(4);
        height_LCD->setDigitCount(4);
        height_LCD->setProperty("value", QVariant(0));
        height_LCD->setProperty("intValue", QVariant(0));
        tab_controlMethods->addTab(tab_sliderControls, QString());
        tab_WaypointControl = new QWidget();
        tab_WaypointControl->setObjectName(QString::fromUtf8("tab_WaypointControl"));
        button_GoToWaypoint = new QPushButton(tab_WaypointControl);
        button_GoToWaypoint->setObjectName(QString::fromUtf8("button_GoToWaypoint"));
        button_GoToWaypoint->setGeometry(QRect(30, 130, 91, 41));
        button_LookAtWaypoint = new QPushButton(tab_WaypointControl);
        button_LookAtWaypoint->setObjectName(QString::fromUtf8("button_LookAtWaypoint"));
        button_LookAtWaypoint->setGeometry(QRect(140, 130, 91, 41));
        groupBox_5 = new QGroupBox(tab_WaypointControl);
        groupBox_5->setObjectName(QString::fromUtf8("groupBox_5"));
        groupBox_5->setGeometry(QRect(10, 10, 241, 111));
        lineEdit_targetZ = new QLineEdit(groupBox_5);
        lineEdit_targetZ->setObjectName(QString::fromUtf8("lineEdit_targetZ"));
        lineEdit_targetZ->setGeometry(QRect(110, 90, 113, 21));
        label_19 = new QLabel(groupBox_5);
        label_19->setObjectName(QString::fromUtf8("label_19"));
        label_19->setGeometry(QRect(20, 90, 61, 21));
        lineEdit_targetX = new QLineEdit(groupBox_5);
        lineEdit_targetX->setObjectName(QString::fromUtf8("lineEdit_targetX"));
        lineEdit_targetX->setGeometry(QRect(110, 30, 113, 21));
        lineEdit_targetY = new QLineEdit(groupBox_5);
        lineEdit_targetY->setObjectName(QString::fromUtf8("lineEdit_targetY"));
        lineEdit_targetY->setGeometry(QRect(110, 60, 113, 21));
        label_20 = new QLabel(groupBox_5);
        label_20->setObjectName(QString::fromUtf8("label_20"));
        label_20->setGeometry(QRect(20, 30, 61, 21));
        label_21 = new QLabel(groupBox_5);
        label_21->setObjectName(QString::fromUtf8("label_21"));
        label_21->setGeometry(QRect(20, 60, 61, 21));
        groupBox_6 = new QGroupBox(tab_WaypointControl);
        groupBox_6->setObjectName(QString::fromUtf8("groupBox_6"));
        groupBox_6->setGeometry(QRect(250, 10, 241, 161));
        QFont font1;
        font1.setBold(false);
        font1.setWeight(50);
        groupBox_6->setFont(font1);
        lineEdit_targetAngleZ = new QLineEdit(groupBox_6);
        lineEdit_targetAngleZ->setObjectName(QString::fromUtf8("lineEdit_targetAngleZ"));
        lineEdit_targetAngleZ->setGeometry(QRect(70, 120, 113, 21));
        lineEdit_targetAngleZ->setReadOnly(true);
        lineEdit_errorX = new QLineEdit(groupBox_6);
        lineEdit_errorX->setObjectName(QString::fromUtf8("lineEdit_errorX"));
        lineEdit_errorX->setGeometry(QRect(70, 30, 113, 21));
        lineEdit_errorX->setReadOnly(false);
        label_24 = new QLabel(groupBox_6);
        label_24->setObjectName(QString::fromUtf8("label_24"));
        label_24->setGeometry(QRect(10, 60, 61, 21));
        lineEdit_errorY = new QLineEdit(groupBox_6);
        lineEdit_errorY->setObjectName(QString::fromUtf8("lineEdit_errorY"));
        lineEdit_errorY->setGeometry(QRect(70, 60, 113, 21));
        lineEdit_errorY->setReadOnly(true);
        label_22 = new QLabel(groupBox_6);
        label_22->setObjectName(QString::fromUtf8("label_22"));
        label_22->setGeometry(QRect(10, 120, 61, 20));
        label_23 = new QLabel(groupBox_6);
        label_23->setObjectName(QString::fromUtf8("label_23"));
        label_23->setGeometry(QRect(10, 30, 61, 21));
        label_27 = new QLabel(groupBox_6);
        label_27->setObjectName(QString::fromUtf8("label_27"));
        label_27->setGeometry(QRect(10, 90, 61, 21));
        lineEdit_errorZ = new QLineEdit(groupBox_6);
        lineEdit_errorZ->setObjectName(QString::fromUtf8("lineEdit_errorZ"));
        lineEdit_errorZ->setGeometry(QRect(70, 90, 113, 21));
        lineEdit_errorZ->setReadOnly(true);
        button_GetWaypoint = new QPushButton(tab_WaypointControl);
        button_GetWaypoint->setObjectName(QString::fromUtf8("button_GetWaypoint"));
        button_GetWaypoint->setGeometry(QRect(270, 180, 201, 41));
        button_LookNGo = new QPushButton(tab_WaypointControl);
        button_LookNGo->setObjectName(QString::fromUtf8("button_LookNGo"));
        button_LookNGo->setGeometry(QRect(30, 180, 201, 41));
        button_FolowFlightpath = new QPushButton(tab_WaypointControl);
        button_FolowFlightpath->setObjectName(QString::fromUtf8("button_FolowFlightpath"));
        button_FolowFlightpath->setGeometry(QRect(500, 180, 151, 41));
        textEdit_waypoints = new QTextEdit(tab_WaypointControl);
        textEdit_waypoints->setObjectName(QString::fromUtf8("textEdit_waypoints"));
        textEdit_waypoints->setGeometry(QRect(500, 30, 211, 91));
        checkBox_recordFlight = new QCheckBox(tab_WaypointControl);
        checkBox_recordFlight->setObjectName(QString::fromUtf8("checkBox_recordFlight"));
        checkBox_recordFlight->setGeometry(QRect(520, 130, 151, 22));
        checkBox_invertFlightpath = new QCheckBox(tab_WaypointControl);
        checkBox_invertFlightpath->setObjectName(QString::fromUtf8("checkBox_invertFlightpath"));
        checkBox_invertFlightpath->setGeometry(QRect(520, 150, 141, 22));
        tab_controlMethods->addTab(tab_WaypointControl, QString());
        button_takeoff = new QPushButton(tab_controls);
        button_takeoff->setObjectName(QString::fromUtf8("button_takeoff"));
        button_takeoff->setGeometry(QRect(140, 280, 101, 41));
        button_reset = new QPushButton(tab_controls);
        button_reset->setObjectName(QString::fromUtf8("button_reset"));
        button_reset->setGeometry(QRect(390, 280, 111, 41));
        button_halt = new QPushButton(tab_controls);
        button_halt->setObjectName(QString::fromUtf8("button_halt"));
        button_halt->setGeometry(QRect(10, 280, 101, 41));
        button_land = new QPushButton(tab_controls);
        button_land->setObjectName(QString::fromUtf8("button_land"));
        button_land->setGeometry(QRect(260, 280, 101, 41));
        groupBox_9 = new QGroupBox(tab_controls);
        groupBox_9->setObjectName(QString::fromUtf8("groupBox_9"));
        groupBox_9->setGeometry(QRect(750, 220, 171, 121));
        label_33 = new QLabel(groupBox_9);
        label_33->setObjectName(QString::fromUtf8("label_33"));
        label_33->setGeometry(QRect(10, 30, 41, 16));
        label_34 = new QLabel(groupBox_9);
        label_34->setObjectName(QString::fromUtf8("label_34"));
        label_34->setGeometry(QRect(10, 60, 41, 16));
        lineEdit_realAngleY = new QLineEdit(groupBox_9);
        lineEdit_realAngleY->setObjectName(QString::fromUtf8("lineEdit_realAngleY"));
        lineEdit_realAngleY->setGeometry(QRect(50, 60, 113, 21));
        label_35 = new QLabel(groupBox_9);
        label_35->setObjectName(QString::fromUtf8("label_35"));
        label_35->setGeometry(QRect(10, 90, 41, 16));
        lineEdit_realAngleX = new QLineEdit(groupBox_9);
        lineEdit_realAngleX->setObjectName(QString::fromUtf8("lineEdit_realAngleX"));
        lineEdit_realAngleX->setGeometry(QRect(50, 30, 113, 21));
        lineEdit_realAngleZ = new QLineEdit(groupBox_9);
        lineEdit_realAngleZ->setObjectName(QString::fromUtf8("lineEdit_realAngleZ"));
        lineEdit_realAngleZ->setGeometry(QRect(50, 90, 113, 21));
        toolBox = new QToolBox(tab_controls);
        toolBox->setObjectName(QString::fromUtf8("toolBox"));
        toolBox->setGeometry(QRect(750, 10, 171, 201));
        toolBoxPage1 = new QWidget();
        toolBoxPage1->setObjectName(QString::fromUtf8("toolBoxPage1"));
        toolBoxPage1->setGeometry(QRect(0, 0, 171, 108));
        groupBox_2 = new QGroupBox(toolBoxPage1);
        groupBox_2->setObjectName(QString::fromUtf8("groupBox_2"));
        groupBox_2->setGeometry(QRect(0, 0, 171, 101));
        lineEdit_estimatedPoseX = new QLineEdit(groupBox_2);
        lineEdit_estimatedPoseX->setObjectName(QString::fromUtf8("lineEdit_estimatedPoseX"));
        lineEdit_estimatedPoseX->setGeometry(QRect(50, 20, 113, 21));
        lineEdit_estimatedPoseY = new QLineEdit(groupBox_2);
        lineEdit_estimatedPoseY->setObjectName(QString::fromUtf8("lineEdit_estimatedPoseY"));
        lineEdit_estimatedPoseY->setGeometry(QRect(50, 50, 113, 21));
        lineEdit_estimatedPoseZ = new QLineEdit(groupBox_2);
        lineEdit_estimatedPoseZ->setObjectName(QString::fromUtf8("lineEdit_estimatedPoseZ"));
        lineEdit_estimatedPoseZ->setGeometry(QRect(50, 80, 113, 21));
        label_13 = new QLabel(groupBox_2);
        label_13->setObjectName(QString::fromUtf8("label_13"));
        label_13->setGeometry(QRect(10, 20, 31, 16));
        label_14 = new QLabel(groupBox_2);
        label_14->setObjectName(QString::fromUtf8("label_14"));
        label_14->setGeometry(QRect(10, 50, 31, 16));
        label_15 = new QLabel(groupBox_2);
        label_15->setObjectName(QString::fromUtf8("label_15"));
        label_15->setGeometry(QRect(10, 80, 31, 16));
        toolBox->addItem(toolBoxPage1, QString::fromUtf8("Drone Estimated Pose"));
        toolBoxPage2 = new QWidget();
        toolBoxPage2->setObjectName(QString::fromUtf8("toolBoxPage2"));
        toolBoxPage2->setGeometry(QRect(0, 0, 100, 30));
        groupBox_7 = new QGroupBox(toolBoxPage2);
        groupBox_7->setObjectName(QString::fromUtf8("groupBox_7"));
        groupBox_7->setGeometry(QRect(0, 0, 171, 111));
        lineEdit_realPoseX = new QLineEdit(groupBox_7);
        lineEdit_realPoseX->setObjectName(QString::fromUtf8("lineEdit_realPoseX"));
        lineEdit_realPoseX->setGeometry(QRect(50, 20, 113, 21));
        lineEdit_realPoseY = new QLineEdit(groupBox_7);
        lineEdit_realPoseY->setObjectName(QString::fromUtf8("lineEdit_realPoseY"));
        lineEdit_realPoseY->setGeometry(QRect(50, 50, 113, 21));
        lineEdit_realPoseZ = new QLineEdit(groupBox_7);
        lineEdit_realPoseZ->setObjectName(QString::fromUtf8("lineEdit_realPoseZ"));
        lineEdit_realPoseZ->setGeometry(QRect(50, 80, 113, 21));
        label_30 = new QLabel(groupBox_7);
        label_30->setObjectName(QString::fromUtf8("label_30"));
        label_30->setGeometry(QRect(10, 20, 31, 16));
        label_31 = new QLabel(groupBox_7);
        label_31->setObjectName(QString::fromUtf8("label_31"));
        label_31->setGeometry(QRect(10, 50, 31, 16));
        label_32 = new QLabel(groupBox_7);
        label_32->setObjectName(QString::fromUtf8("label_32"));
        label_32->setGeometry(QRect(10, 80, 31, 16));
        toolBox->addItem(toolBoxPage2, QString::fromUtf8("Drone Real Pose"));
        toolBoxPage3 = new QWidget();
        toolBoxPage3->setObjectName(QString::fromUtf8("toolBoxPage3"));
        toolBoxPage3->setGeometry(QRect(0, 0, 100, 30));
        groupBox_8 = new QGroupBox(toolBoxPage3);
        groupBox_8->setObjectName(QString::fromUtf8("groupBox_8"));
        groupBox_8->setGeometry(QRect(0, 0, 171, 101));
        lineEdit_poseErrorX = new QLineEdit(groupBox_8);
        lineEdit_poseErrorX->setObjectName(QString::fromUtf8("lineEdit_poseErrorX"));
        lineEdit_poseErrorX->setGeometry(QRect(50, 20, 113, 21));
        lineEdit_poseErrorY = new QLineEdit(groupBox_8);
        lineEdit_poseErrorY->setObjectName(QString::fromUtf8("lineEdit_poseErrorY"));
        lineEdit_poseErrorY->setGeometry(QRect(50, 50, 113, 21));
        lineEdit_poseErrorZ = new QLineEdit(groupBox_8);
        lineEdit_poseErrorZ->setObjectName(QString::fromUtf8("lineEdit_poseErrorZ"));
        lineEdit_poseErrorZ->setGeometry(QRect(50, 80, 113, 21));
        label_36 = new QLabel(groupBox_8);
        label_36->setObjectName(QString::fromUtf8("label_36"));
        label_36->setGeometry(QRect(10, 20, 31, 16));
        label_37 = new QLabel(groupBox_8);
        label_37->setObjectName(QString::fromUtf8("label_37"));
        label_37->setGeometry(QRect(10, 50, 31, 16));
        label_38 = new QLabel(groupBox_8);
        label_38->setObjectName(QString::fromUtf8("label_38"));
        label_38->setGeometry(QRect(10, 80, 31, 16));
        toolBox->addItem(toolBoxPage3, QString::fromUtf8("Estimation Error"));
        tab_manager->addTab(tab_controls, QString());

        hboxLayout->addWidget(tab_manager);

        MainWindowDesign->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindowDesign);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 1000, 25));
        menu_File = new QMenu(menubar);
        menu_File->setObjectName(QString::fromUtf8("menu_File"));
        MainWindowDesign->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindowDesign);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        MainWindowDesign->setStatusBar(statusbar);
        QWidget::setTabOrder(tab_controlMethods, button_forward);
        QWidget::setTabOrder(button_forward, button_left);
        QWidget::setTabOrder(button_left, button_right);
        QWidget::setTabOrder(button_right, button_backward);
        QWidget::setTabOrder(button_backward, button_rotateCCW);
        QWidget::setTabOrder(button_rotateCCW, button_rotateCW);
        QWidget::setTabOrder(button_rotateCW, button_up);
        QWidget::setTabOrder(button_up, button_down);
        QWidget::setTabOrder(button_down, fwbw_slider);
        QWidget::setTabOrder(fwbw_slider, height_slider);
        QWidget::setTabOrder(height_slider, sideways_slider);
        QWidget::setTabOrder(sideways_slider, rotation_slider);
        QWidget::setTabOrder(rotation_slider, lineEdit_targetX);
        QWidget::setTabOrder(lineEdit_targetX, lineEdit_targetY);
        QWidget::setTabOrder(lineEdit_targetY, lineEdit_targetZ);
        QWidget::setTabOrder(lineEdit_targetZ, lineEdit_errorX);
        QWidget::setTabOrder(lineEdit_errorX, lineEdit_errorY);
        QWidget::setTabOrder(lineEdit_errorY, lineEdit_errorZ);
        QWidget::setTabOrder(lineEdit_errorZ, lineEdit_targetAngleZ);
        QWidget::setTabOrder(lineEdit_targetAngleZ, textEdit_waypoints);
        QWidget::setTabOrder(textEdit_waypoints, button_GoToWaypoint);
        QWidget::setTabOrder(button_GoToWaypoint, button_LookAtWaypoint);
        QWidget::setTabOrder(button_LookAtWaypoint, button_LookNGo);
        QWidget::setTabOrder(button_LookNGo, button_GetWaypoint);
        QWidget::setTabOrder(button_GetWaypoint, button_FolowFlightpath);
        QWidget::setTabOrder(button_FolowFlightpath, button_halt);
        QWidget::setTabOrder(button_halt, button_takeoff);
        QWidget::setTabOrder(button_takeoff, button_land);
        QWidget::setTabOrder(button_land, button_reset);
        QWidget::setTabOrder(button_reset, radioButton_frontCamera);
        QWidget::setTabOrder(radioButton_frontCamera, radioButton_bottomCamera);

        menubar->addAction(menu_File->menuAction());
        menu_File->addAction(action_Preferences);
        menu_File->addSeparator();
        menu_File->addAction(actionAbout);
        menu_File->addAction(actionAbout_Qt);
        menu_File->addSeparator();
        menu_File->addAction(action_Quit);

        retranslateUi(MainWindowDesign);
        QObject::connect(action_Quit, SIGNAL(triggered()), MainWindowDesign, SLOT(close()));

        tab_manager->setCurrentIndex(0);
        tab_controlMethods->setCurrentIndex(0);


        QMetaObject::connectSlotsByName(MainWindowDesign);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindowDesign)
    {
        MainWindowDesign->setWindowTitle(QApplication::translate("MainWindowDesign", "Drone WayPointer", 0, QApplication::UnicodeUTF8));
        action_Quit->setText(QApplication::translate("MainWindowDesign", "&Quit", 0, QApplication::UnicodeUTF8));
        action_Quit->setShortcut(QApplication::translate("MainWindowDesign", "Ctrl+Q", 0, QApplication::UnicodeUTF8));
        action_Preferences->setText(QApplication::translate("MainWindowDesign", "&Preferences", 0, QApplication::UnicodeUTF8));
        actionAbout->setText(QApplication::translate("MainWindowDesign", "&About", 0, QApplication::UnicodeUTF8));
        actionAbout_Qt->setText(QApplication::translate("MainWindowDesign", "About &Qt", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        tab_manager->setToolTip(QString());
#endif // QT_NO_TOOLTIP
#ifndef QT_NO_STATUSTIP
        tab_manager->setStatusTip(QString());
#endif // QT_NO_STATUSTIP
        RosMaster->setTitle(QApplication::translate("MainWindowDesign", "Ros Master", 0, QApplication::UnicodeUTF8));
        label_2->setText(QApplication::translate("MainWindowDesign", "Ros IP", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        button_connect->setToolTip(QApplication::translate("MainWindowDesign", "Connect with the communication nodes.", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
#ifndef QT_NO_STATUSTIP
        button_connect->setStatusTip(QApplication::translate("MainWindowDesign", "Connect with the communication nodes.", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_STATUSTIP
        button_connect->setText(QApplication::translate("MainWindowDesign", "Connect", 0, QApplication::UnicodeUTF8));
        line_edit_host->setText(QApplication::translate("MainWindowDesign", "192.168.1.67", 0, QApplication::UnicodeUTF8));
        line_edit_master->setText(QApplication::translate("MainWindowDesign", "http://192.168.1.2:11311/", 0, QApplication::UnicodeUTF8));
        checkbox_remember_settings->setText(QApplication::translate("MainWindowDesign", "Remember settings on startup", 0, QApplication::UnicodeUTF8));
        line_edit_topic->setText(QApplication::translate("MainWindowDesign", "unused", 0, QApplication::UnicodeUTF8));
        label_3->setText(QApplication::translate("MainWindowDesign", "Ros Hostname", 0, QApplication::UnicodeUTF8));
        label->setText(QApplication::translate("MainWindowDesign", "Ros Master Url", 0, QApplication::UnicodeUTF8));
        checkbox_use_environment->setText(QApplication::translate("MainWindowDesign", "Use environment variables", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        quit_button->setToolTip(QApplication::translate("MainWindowDesign", "Exit the application", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
#ifndef QT_NO_STATUSTIP
        quit_button->setStatusTip(QApplication::translate("MainWindowDesign", "Exit the application", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_STATUSTIP
        quit_button->setText(QApplication::translate("MainWindowDesign", "Quit", 0, QApplication::UnicodeUTF8));
        WaypointSettings->setTitle(QApplication::translate("MainWindowDesign", "General Settings", 0, QApplication::UnicodeUTF8));
        label_29->setText(QApplication::translate("MainWindowDesign", "Image Sampling Rate[mSec]", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        button_imagesFilePathSelect->setToolTip(QApplication::translate("MainWindowDesign", "Select the save location for captured images.", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
#ifndef QT_NO_STATUSTIP
        button_imagesFilePathSelect->setStatusTip(QApplication::translate("MainWindowDesign", "Select the save location for captured images.", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_STATUSTIP
        button_imagesFilePathSelect->setText(QApplication::translate("MainWindowDesign", "Select Location", 0, QApplication::UnicodeUTF8));
        line_edit_loadWaypointFilePath->setText(QString());
        checkBox_saveData->setText(QApplication::translate("MainWindowDesign", "Save Data", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        button_openWaypointsFile->setToolTip(QApplication::translate("MainWindowDesign", "Select the waypoint file to read from.", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
#ifndef QT_NO_STATUSTIP
        button_openWaypointsFile->setStatusTip(QApplication::translate("MainWindowDesign", "Select the waypoint file to read from.", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_STATUSTIP
        button_openWaypointsFile->setText(QApplication::translate("MainWindowDesign", "Open File", 0, QApplication::UnicodeUTF8));
        line_edit_saveWaypointFilePath->setText(QString());
        label_28->setText(QApplication::translate("MainWindowDesign", "Images Save File Path", 0, QApplication::UnicodeUTF8));
        checkBox_saveImages->setText(QApplication::translate("MainWindowDesign", "Save Images", 0, QApplication::UnicodeUTF8));
        line_edit_saveImageFilePath->setText(QString());
#ifndef QT_NO_TOOLTIP
        button_saveWaypointsFile->setToolTip(QApplication::translate("MainWindowDesign", "Select location of the waypoint save file.", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
#ifndef QT_NO_STATUSTIP
        button_saveWaypointsFile->setStatusTip(QApplication::translate("MainWindowDesign", "Select location of the waypoint save file.", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_STATUSTIP
        button_saveWaypointsFile->setText(QApplication::translate("MainWindowDesign", "Select Location", 0, QApplication::UnicodeUTF8));
        label_26->setText(QApplication::translate("MainWindowDesign", "Waypoint Save File Path", 0, QApplication::UnicodeUTF8));
        label_25->setText(QApplication::translate("MainWindowDesign", "Waypoint File Path", 0, QApplication::UnicodeUTF8));
        checkBox_safeFlight->setText(QApplication::translate("MainWindowDesign", "Safe Flight", 0, QApplication::UnicodeUTF8));
        TopicSettings->setTitle(QApplication::translate("MainWindowDesign", "Drone Pose Estimation", 0, QApplication::UnicodeUTF8));
        radioButton_Simulation_PoseEstimation->setText(QApplication::translate("MainWindowDesign", "Simulation (Real Pose)", 0, QApplication::UnicodeUTF8));
        radioButton_External_PoseEstimation->setText(QApplication::translate("MainWindowDesign", "External Pose Estimation", 0, QApplication::UnicodeUTF8));
        line_edit_realPoseTopic->setText(QApplication::translate("MainWindowDesign", "/ground_truth/state", 0, QApplication::UnicodeUTF8));
        label_12->setText(QApplication::translate("MainWindowDesign", "External Pose Estimation Topic", 0, QApplication::UnicodeUTF8));
        radioButton_Internal_DR_PoseEstimation->setText(QApplication::translate("MainWindowDesign", "Internal (Dead - Reckoning)", 0, QApplication::UnicodeUTF8));
        groupBox->setTitle(QApplication::translate("MainWindowDesign", "Test Signals", 0, QApplication::UnicodeUTF8));
        checkBox_batteryBellowLand->setText(QApplication::translate("MainWindowDesign", "Battery < Land Threshold", 0, QApplication::UnicodeUTF8));
        checkBox_batteryBellowGoHome->setText(QApplication::translate("MainWindowDesign", "Battery < Go Home Threshold", 0, QApplication::UnicodeUTF8));
        checkBox_noWifiSignal->setText(QApplication::translate("MainWindowDesign", "No WiFi Signal", 0, QApplication::UnicodeUTF8));
        tab_manager->setTabText(tab_manager->indexOf(tab_commandPanel), QApplication::translate("MainWindowDesign", "Command Panel", 0, QApplication::UnicodeUTF8));
        label_4->setText(QApplication::translate("MainWindowDesign", "Battery", 0, QApplication::UnicodeUTF8));
        label_5->setText(QApplication::translate("MainWindowDesign", "State", 0, QApplication::UnicodeUTF8));
        groupBox_3->setTitle(QApplication::translate("MainWindowDesign", "Camera Select", 0, QApplication::UnicodeUTF8));
        radioButton_bottomCamera->setText(QApplication::translate("MainWindowDesign", "Bottom", 0, QApplication::UnicodeUTF8));
        radioButton_frontCamera->setText(QApplication::translate("MainWindowDesign", "Front", 0, QApplication::UnicodeUTF8));
        label_7->setText(QString());
        groupBox_4->setTitle(QApplication::translate("MainWindowDesign", "Camera View", 0, QApplication::UnicodeUTF8));
        label_6->setText(QApplication::translate("MainWindowDesign", "      NOT CONNECTED TO THE \n"
"                   DRONE!                      ", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        button_down->setToolTip(QApplication::translate("MainWindowDesign", "Move the drone Downwards.", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
#ifndef QT_NO_STATUSTIP
        button_down->setStatusTip(QApplication::translate("MainWindowDesign", "Move the drone Downwards.", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_STATUSTIP
        button_down->setText(QApplication::translate("MainWindowDesign", "Descend", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        button_up->setToolTip(QApplication::translate("MainWindowDesign", "Move the drone Upwards.", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
#ifndef QT_NO_STATUSTIP
        button_up->setStatusTip(QApplication::translate("MainWindowDesign", "Move the drone Upwards.", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_STATUSTIP
        button_up->setText(QApplication::translate("MainWindowDesign", "Acsend", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        button_left->setToolTip(QApplication::translate("MainWindowDesign", "Move the drone Left.", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
#ifndef QT_NO_STATUSTIP
        button_left->setStatusTip(QApplication::translate("MainWindowDesign", "Move the drone Left.", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_STATUSTIP
        button_left->setText(QApplication::translate("MainWindowDesign", "Left", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        button_rotateCW->setToolTip(QApplication::translate("MainWindowDesign", "Rotate the drone clockwise.", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
#ifndef QT_NO_STATUSTIP
        button_rotateCW->setStatusTip(QApplication::translate("MainWindowDesign", "Rotate the drone clockwise.", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_STATUSTIP
        button_rotateCW->setText(QApplication::translate("MainWindowDesign", "Rotate \n"
" ClockWise", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        button_forward->setToolTip(QApplication::translate("MainWindowDesign", "Move the drone Forward.", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
#ifndef QT_NO_STATUSTIP
        button_forward->setStatusTip(QApplication::translate("MainWindowDesign", "Move the drone Forward.", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_STATUSTIP
        button_forward->setText(QApplication::translate("MainWindowDesign", "Forward", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        button_backward->setToolTip(QApplication::translate("MainWindowDesign", "Move the drone Backwards.", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
#ifndef QT_NO_STATUSTIP
        button_backward->setStatusTip(QApplication::translate("MainWindowDesign", "Move the drone Backwards.", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_STATUSTIP
        button_backward->setText(QApplication::translate("MainWindowDesign", "Backward", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        button_right->setToolTip(QApplication::translate("MainWindowDesign", "Move the drone Right.", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
#ifndef QT_NO_STATUSTIP
        button_right->setStatusTip(QApplication::translate("MainWindowDesign", "Move the drone Right.", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_STATUSTIP
        button_right->setText(QApplication::translate("MainWindowDesign", "Right", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        button_rotateCCW->setToolTip(QApplication::translate("MainWindowDesign", "Rotate the drone counter-clockwise.", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
#ifndef QT_NO_STATUSTIP
        button_rotateCCW->setStatusTip(QApplication::translate("MainWindowDesign", "Rotate the drone counter-clockwise.", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_STATUSTIP
        button_rotateCCW->setText(QApplication::translate("MainWindowDesign", "Rotate \n"
" Counter-\n"
"ClockWise", 0, QApplication::UnicodeUTF8));
        tab_controlMethods->setTabText(tab_controlMethods->indexOf(tab_buttonControls), QApplication::translate("MainWindowDesign", "Button Control", 0, QApplication::UnicodeUTF8));
        label_11->setText(QApplication::translate("MainWindowDesign", "Height", 0, QApplication::UnicodeUTF8));
        label_8->setText(QApplication::translate("MainWindowDesign", "FW / BW", 0, QApplication::UnicodeUTF8));
        label_10->setText(QApplication::translate("MainWindowDesign", "Rotation", 0, QApplication::UnicodeUTF8));
        label_9->setText(QApplication::translate("MainWindowDesign", "Sideways", 0, QApplication::UnicodeUTF8));
        tab_controlMethods->setTabText(tab_controlMethods->indexOf(tab_sliderControls), QApplication::translate("MainWindowDesign", "Slider Control", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        button_GoToWaypoint->setToolTip(QApplication::translate("MainWindowDesign", "Go to a waypoint at XYZ.", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
#ifndef QT_NO_STATUSTIP
        button_GoToWaypoint->setStatusTip(QApplication::translate("MainWindowDesign", "Go to a waypoint at XYZ.", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_STATUSTIP
        button_GoToWaypoint->setText(QApplication::translate("MainWindowDesign", "GO!", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        button_LookAtWaypoint->setToolTip(QApplication::translate("MainWindowDesign", "Face a point at XY.", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
#ifndef QT_NO_STATUSTIP
        button_LookAtWaypoint->setStatusTip(QApplication::translate("MainWindowDesign", "Face a point at XY.", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_STATUSTIP
        button_LookAtWaypoint->setText(QApplication::translate("MainWindowDesign", "Look At", 0, QApplication::UnicodeUTF8));
        groupBox_5->setTitle(QApplication::translate("MainWindowDesign", "Waypoint in Map Frame [Input]", 0, QApplication::UnicodeUTF8));
        lineEdit_targetZ->setText(QApplication::translate("MainWindowDesign", "0", 0, QApplication::UnicodeUTF8));
        label_19->setText(QApplication::translate("MainWindowDesign", "Target Z", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_WHATSTHIS
        lineEdit_targetX->setWhatsThis(QString());
#endif // QT_NO_WHATSTHIS
        lineEdit_targetX->setText(QApplication::translate("MainWindowDesign", "0", 0, QApplication::UnicodeUTF8));
        lineEdit_targetY->setText(QApplication::translate("MainWindowDesign", "0", 0, QApplication::UnicodeUTF8));
        label_20->setText(QApplication::translate("MainWindowDesign", "Target X", 0, QApplication::UnicodeUTF8));
        label_21->setText(QApplication::translate("MainWindowDesign", "Target Y", 0, QApplication::UnicodeUTF8));
        groupBox_6->setTitle(QApplication::translate("MainWindowDesign", "Waypoint in Drone Frame [Output]", 0, QApplication::UnicodeUTF8));
        lineEdit_targetAngleZ->setText(QApplication::translate("MainWindowDesign", "0", 0, QApplication::UnicodeUTF8));
        lineEdit_errorX->setText(QApplication::translate("MainWindowDesign", "0", 0, QApplication::UnicodeUTF8));
        label_24->setText(QApplication::translate("MainWindowDesign", "Target Y", 0, QApplication::UnicodeUTF8));
        lineEdit_errorY->setText(QApplication::translate("MainWindowDesign", "0", 0, QApplication::UnicodeUTF8));
        label_22->setText(QApplication::translate("MainWindowDesign", "Angle Z", 0, QApplication::UnicodeUTF8));
        label_23->setText(QApplication::translate("MainWindowDesign", "Target X", 0, QApplication::UnicodeUTF8));
        label_27->setText(QApplication::translate("MainWindowDesign", "Target Z", 0, QApplication::UnicodeUTF8));
        lineEdit_errorZ->setText(QApplication::translate("MainWindowDesign", "0", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        button_GetWaypoint->setToolTip(QApplication::translate("MainWindowDesign", "Translate the given waypoint to the drone frame.", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
#ifndef QT_NO_STATUSTIP
        button_GetWaypoint->setStatusTip(QApplication::translate("MainWindowDesign", "Translate the given waypoint to the drone frame.", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_STATUSTIP
        button_GetWaypoint->setText(QApplication::translate("MainWindowDesign", "Get Waypoint", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        button_LookNGo->setToolTip(QApplication::translate("MainWindowDesign", "Move to the point at XYZ while facing it.", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
#ifndef QT_NO_STATUSTIP
        button_LookNGo->setStatusTip(QApplication::translate("MainWindowDesign", "Move to the point at XYZ while facing it.", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_STATUSTIP
        button_LookNGo->setText(QApplication::translate("MainWindowDesign", "Look N Go", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        button_FolowFlightpath->setToolTip(QApplication::translate("MainWindowDesign", "Load and follow a flightpath from a file.", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
#ifndef QT_NO_STATUSTIP
        button_FolowFlightpath->setStatusTip(QApplication::translate("MainWindowDesign", "Load and follow a flightpath from a file.", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_STATUSTIP
        button_FolowFlightpath->setText(QApplication::translate("MainWindowDesign", "Follow Flightpath", 0, QApplication::UnicodeUTF8));
        checkBox_recordFlight->setText(QApplication::translate("MainWindowDesign", "Record Flightpath", 0, QApplication::UnicodeUTF8));
        checkBox_invertFlightpath->setText(QApplication::translate("MainWindowDesign", "Invert Flightpath", 0, QApplication::UnicodeUTF8));
        tab_controlMethods->setTabText(tab_controlMethods->indexOf(tab_WaypointControl), QApplication::translate("MainWindowDesign", "Waypoint Control", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        button_takeoff->setToolTip(QApplication::translate("MainWindowDesign", "Take off the drone from ground.", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
#ifndef QT_NO_STATUSTIP
        button_takeoff->setStatusTip(QApplication::translate("MainWindowDesign", "Take off the drone from ground.", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_STATUSTIP
        button_takeoff->setText(QApplication::translate("MainWindowDesign", "Take Off", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        button_reset->setToolTip(QApplication::translate("MainWindowDesign", "Reset the drone state.", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
#ifndef QT_NO_STATUSTIP
        button_reset->setStatusTip(QApplication::translate("MainWindowDesign", "Reset the drone state.", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_STATUSTIP
        button_reset->setText(QApplication::translate("MainWindowDesign", "Reset", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        button_halt->setToolTip(QApplication::translate("MainWindowDesign", "Stop all actions and Hover.", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
#ifndef QT_NO_STATUSTIP
        button_halt->setStatusTip(QApplication::translate("MainWindowDesign", "Stop all actions and Hover.", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_STATUSTIP
        button_halt->setText(QApplication::translate("MainWindowDesign", "Halt/Hover", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        button_land->setToolTip(QApplication::translate("MainWindowDesign", "Land the drone.", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
#ifndef QT_NO_STATUSTIP
        button_land->setStatusTip(QApplication::translate("MainWindowDesign", "Land the drone.", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_STATUSTIP
        button_land->setText(QApplication::translate("MainWindowDesign", "Land", 0, QApplication::UnicodeUTF8));
        groupBox_9->setTitle(QApplication::translate("MainWindowDesign", "Drone Attitude", 0, QApplication::UnicodeUTF8));
        label_33->setText(QApplication::translate("MainWindowDesign", "RotX", 0, QApplication::UnicodeUTF8));
        label_34->setText(QApplication::translate("MainWindowDesign", "RotY", 0, QApplication::UnicodeUTF8));
        lineEdit_realAngleY->setText(QApplication::translate("MainWindowDesign", "0", 0, QApplication::UnicodeUTF8));
        label_35->setText(QApplication::translate("MainWindowDesign", "RotZ", 0, QApplication::UnicodeUTF8));
        lineEdit_realAngleX->setText(QApplication::translate("MainWindowDesign", "0", 0, QApplication::UnicodeUTF8));
        lineEdit_realAngleZ->setText(QApplication::translate("MainWindowDesign", "0", 0, QApplication::UnicodeUTF8));
        groupBox_2->setTitle(QString());
        lineEdit_estimatedPoseX->setText(QApplication::translate("MainWindowDesign", "0", 0, QApplication::UnicodeUTF8));
        lineEdit_estimatedPoseY->setText(QApplication::translate("MainWindowDesign", "0", 0, QApplication::UnicodeUTF8));
        lineEdit_estimatedPoseZ->setText(QApplication::translate("MainWindowDesign", "0", 0, QApplication::UnicodeUTF8));
        label_13->setText(QApplication::translate("MainWindowDesign", "X", 0, QApplication::UnicodeUTF8));
        label_14->setText(QApplication::translate("MainWindowDesign", "Y", 0, QApplication::UnicodeUTF8));
        label_15->setText(QApplication::translate("MainWindowDesign", "Z", 0, QApplication::UnicodeUTF8));
        toolBox->setItemText(toolBox->indexOf(toolBoxPage1), QApplication::translate("MainWindowDesign", "Drone Estimated Pose", 0, QApplication::UnicodeUTF8));
        groupBox_7->setTitle(QString());
        lineEdit_realPoseX->setText(QApplication::translate("MainWindowDesign", "0", 0, QApplication::UnicodeUTF8));
        lineEdit_realPoseY->setText(QApplication::translate("MainWindowDesign", "0", 0, QApplication::UnicodeUTF8));
        lineEdit_realPoseZ->setText(QApplication::translate("MainWindowDesign", "0", 0, QApplication::UnicodeUTF8));
        label_30->setText(QApplication::translate("MainWindowDesign", "X", 0, QApplication::UnicodeUTF8));
        label_31->setText(QApplication::translate("MainWindowDesign", "Y", 0, QApplication::UnicodeUTF8));
        label_32->setText(QApplication::translate("MainWindowDesign", "Z", 0, QApplication::UnicodeUTF8));
        toolBox->setItemText(toolBox->indexOf(toolBoxPage2), QApplication::translate("MainWindowDesign", "Drone Real Pose", 0, QApplication::UnicodeUTF8));
        groupBox_8->setTitle(QString());
        lineEdit_poseErrorX->setText(QApplication::translate("MainWindowDesign", "0", 0, QApplication::UnicodeUTF8));
        lineEdit_poseErrorY->setText(QApplication::translate("MainWindowDesign", "0", 0, QApplication::UnicodeUTF8));
        lineEdit_poseErrorZ->setText(QApplication::translate("MainWindowDesign", "0", 0, QApplication::UnicodeUTF8));
        label_36->setText(QApplication::translate("MainWindowDesign", "X", 0, QApplication::UnicodeUTF8));
        label_37->setText(QApplication::translate("MainWindowDesign", "Y", 0, QApplication::UnicodeUTF8));
        label_38->setText(QApplication::translate("MainWindowDesign", "Z", 0, QApplication::UnicodeUTF8));
        toolBox->setItemText(toolBox->indexOf(toolBoxPage3), QApplication::translate("MainWindowDesign", "Estimation Error", 0, QApplication::UnicodeUTF8));
        tab_manager->setTabText(tab_manager->indexOf(tab_controls), QApplication::translate("MainWindowDesign", "Controls", 0, QApplication::UnicodeUTF8));
        menu_File->setTitle(QApplication::translate("MainWindowDesign", "&App", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class MainWindowDesign: public Ui_MainWindowDesign {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAIN_WINDOW_H
