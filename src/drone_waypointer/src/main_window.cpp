/**
 * @file /src/main_window.cpp
 *
 * @brief Implementation for the qt gui.
 *
 * @date February 2011
 **/
/*****************************************************************************
** Includes
*****************************************************************************/

#include <QtGui>
#include <QMessageBox>
#include <iostream>
#ifndef Q_MOC_RUN
#include "../include/drone_waypointer/main_window.hpp"
#endif

/*****************************************************************************
** Namespaces
*****************************************************************************/

namespace drone_waypointer {

using namespace Qt;

/*****************************************************************************
** Implementation [MainWindow]
*****************************************************************************/

MainWindow::MainWindow(int argc, char** argv, QWidget *parent)
	: QMainWindow(parent)
	, qnode(argc,argv)
{
	ui.setupUi(this); // Calling this incidentally connects all ui's triggers to on_...() callbacks in this class.
    QObject::connect(ui.actionAbout_Qt, SIGNAL(triggered(bool)), qApp, SLOT(aboutQt())); // qApp is a global variable for the application

    ReadSettings();
	setWindowIcon(QIcon(":/images/icon.png"));
	ui.tab_manager->setCurrentIndex(0); // ensure the first tab is showing - qt-designer should have this already hardwired, but often loses it (settings?).
    
    
    
    QObject::connect(&qnode, SIGNAL(rosShutdown()), this, SLOT(close()));
    QObject::connect(&qnode, SIGNAL(dataUpdated()), this, SLOT(updateData()));
	QObject::connect(&qnode, SIGNAL(imageUpdated()), this, SLOT(updateImage()));
	QObject::connect(&qnode, SIGNAL(realPoseUpdated()), this, SLOT(updateRealPose()));
	QObject::connect(&qnode, SIGNAL(targetUpdated()), this, SLOT(updateTargetInDrone()));
	QObject::connect(&qnode, SIGNAL(requestNewWaypoint()), this, SLOT(updateWaypoint()));
	QObject::connect(&qnode, SIGNAL(sampleFlightpath()), this, SLOT(saveWaypoint()));
	QObject::connect(&qnode, SIGNAL(dataReady()), this, SLOT(saveDataToFile()));
	QObject::connect(&qnode, SIGNAL(imageReady()), this, SLOT(saveImageToFile()));
	QObject::connect(&qnode, SIGNAL(estimatedPoseUpdated()), this, SLOT(updateEstimatedPose()));
	QObject::connect(&qnode, SIGNAL(externalEstimatedPoseUpdated()), this, SLOT(updateExternalEstimatedPose()));
	QObject::connect(&qnode, SIGNAL(goHome()), this, SLOT(loadWayHome()));
	QObject::connect(&qnode, SIGNAL(sampleWayHome()), this, SLOT(saveWayHome()));
	QObject::connect(&qnode, SIGNAL(updateWayHomeFinalPoint()), this, SLOT(changeWayHome()));



    /*********************
    ** Auto Start
    **********************/
    if ( ui.checkbox_remember_settings->isChecked() ) {
        on_button_connect_clicked(true);
    }
    
       // Seting up some initial values for some objects
    ui.textEdit_waypoints->setReadOnly(true);
    wayPointCommandLine = 0;
    wayHomeCommandLine = 0;
    dataNumber = 0;
    ui.radioButton_Internal_DR_PoseEstimation->setChecked(true);
    // Default files used in recording and loading data
   	ui.line_edit_loadWaypointFilePath->setText(QCoreApplication::applicationDirPath() + "/path.txt");
   	ui.line_edit_saveWaypointFilePath->setText(QCoreApplication::applicationDirPath() + "/savedWaypoints.txt");
   	ui.line_edit_saveImageFilePath->setText(QCoreApplication::applicationDirPath() + "/CapturedImages/");
   	//ui.checkBox_saveData->setChecked(true); Defaults needed for Student-Edition
   	//ui.checkBox_saveImages->setChecked(true); Defaults needed for Student-Edition

   	// Initialise Data File
   	QFile::remove(QCoreApplication::applicationDirPath() + "/path.txt");
   	QFile fileOut(QCoreApplication::applicationDirPath() + "/path.txt");

	fileOut.open(QIODevice::WriteOnly | QIODevice::Append);
	QTextStream out(&fileOut);

	QString str = QString("%1 %2 %3 %4 %5 %6 %7 %8 %9 %10 %11 %12 %13 %14 %15 %16\n").arg("[Time]",7)
	.arg("[X]",12).arg("[Y]",12).arg("[Z]",12)
	.arg("[XVel]",12).arg("[YVel]",12).arg("[ZVel]",12)
	.arg("[XAcc]",12).arg("[YAcc]",12).arg("[ZAcc]",12)
	.arg("[XRot]",12).arg("[YRot]",12).arg("[ZRot]",12)
	.arg("[XRotVel]",12).arg("[YRotVel]",12).arg("[ZRotVel]",12);
	// PWM values not available in the simulator
	//.arg("[Motor 1 PWM]").arg("[Motor 2 PWM]").arg("[Motor 3 PWM]").arg("[Motor 4 PWM]"); 
	QString str2 = QString("%1 %2 %3 %4 %5 %6 %7 %8 %9 %10 %11 %12 %13 %14 %15 %16\n").arg("(Sec)",7)
	.arg("(m)",12).arg("(m)",12).arg("(m)",12)
	.arg("(m/S)",12).arg("(m/S)",12).arg("(m/S)",12)
	.arg("(m/S^2)",12).arg("(m/S^2)",12).arg("(m/S^2)",12)
	.arg("(Degrees)",12).arg("(Degrees)",12).arg("(Degrees)",12)
	.arg("(Degrees/S)",12).arg("(Degrees/S)",12).arg("(Degrees/S)",12);
	// PWM values not available in the simulator
	//.arg("(Volts)").arg("(Volts)").arg("(Volts)").arg("(Volts)");
	out << str;
	out << str2;
	fileOut.close();

	QFile::remove(QCoreApplication::applicationDirPath() + "/TestData.txt");
	QFile fileOut2(QCoreApplication::applicationDirPath() + "/TestData.txt");
	fileOut2.open(QIODevice::WriteOnly | QIODevice::Append);
	QTextStream out2(&fileOut2);
	QString str3 = QString("%1 %2 %3 %4 %5 %6 %7 %8 %9 %10\n").arg("[Time]",7)
	.arg("[X_a]",12).arg("[Y_a]",12).arg("[Z_a]",12)
	.arg("[X_e]",12).arg("[Y_e]",12).arg("[Z_e]",12)
	.arg("[T_x]",12).arg("[T_y]",12).arg("[T_z]",12);
	out2 << str3;
	fileOut2.close();

	ui.tab_manager->setCurrentIndex(0);
	ui.tab_controlMethods->setCurrentIndex(0);
	ui.checkBox_safeFlight->setChecked(true);
}

MainWindow::~MainWindow() {}

/*****************************************************************************
** Implementation [Slots]
*****************************************************************************/

void MainWindow::showNoMasterMessage() {
	QMessageBox msgBox;
	msgBox.setText("Couldn't find the ros master.");
	msgBox.exec();
    close();
}

/*
 * These triggers whenever the button is clicked, regardless of whether it
 * is already checked or not.
 */

void MainWindow::on_button_connect_clicked(bool check ) {
	if ( ui.checkbox_use_environment->isChecked() ) {
		if ( !qnode.init() ) {
			showNoMasterMessage();
		}else {
			ui.button_connect->setEnabled(false);
			ui.line_edit_master->setReadOnly(true);
			ui.line_edit_host->setReadOnly(true);
			ui.line_edit_topic->setReadOnly(true);
			ui.button_connect->setEnabled(false);
			qnode.recordData = ui.checkBox_saveData->isChecked();
			qnode.recordImages = ui.checkBox_saveImages->isChecked();
			qnode.imageSamplingTime = ui.spinBox_samplingTime->value()/1000;
			qnode.estimatorTopic = ui.line_edit_realPoseTopic->text().toUtf8().constData();
			ui.TopicSettings->setEnabled(false);
			if(ui.radioButton_Simulation_PoseEstimation->isChecked()){
				qnode.poseEstimationMethod = 1;
				ui.toolBox->setCurrentIndex(1);
			}
			else if(ui.radioButton_External_PoseEstimation->isChecked()){
				qnode.poseEstimationMethod = 2;
				ui.toolBox->setCurrentIndex(0);
			}
			else if(ui.radioButton_Internal_DR_PoseEstimation->isChecked()){
				qnode.poseEstimationMethod = 3;
				ui.toolBox->setCurrentIndex(0);
			}
			// Enable Safety Loops
			qnode.safeFlight = ui.checkBox_safeFlight->isChecked();
			qnode.testBatteryBellowLand = ui.checkBox_batteryBellowLand->isChecked();
			qnode.testBatteryBellowGoHome = ui.checkBox_batteryBellowGoHome->isChecked();
			qnode.testNoWifi = ui.checkBox_noWifiSignal->isChecked();
		}
	} else {
		if ( ! qnode.init(ui.line_edit_master->text().toStdString(),
				   ui.line_edit_host->text().toStdString()) ) {
			showNoMasterMessage();
		}else {
			ui.button_connect->setEnabled(false);
			ui.line_edit_master->setReadOnly(true);
			ui.line_edit_host->setReadOnly(true);
			ui.line_edit_topic->setReadOnly(true);
			ui.button_connect->setEnabled(false);
			qnode.recordData = ui.checkBox_saveData->isChecked();
			qnode.recordImages = ui.checkBox_saveImages->isChecked();
			qnode.imageSamplingTime = ui.spinBox_samplingTime->value()/1000;
			qnode.estimatorTopic = ui.line_edit_realPoseTopic->text().toUtf8().constData();
			ui.TopicSettings->setEnabled(false);
			if(ui.radioButton_Simulation_PoseEstimation->isChecked()){
				qnode.poseEstimationMethod = 1;
				ui.toolBox->setCurrentIndex(1);
			}
			else if(ui.radioButton_External_PoseEstimation->isChecked()){
				qnode.poseEstimationMethod = 2;
				ui.toolBox->setCurrentIndex(0);
			}
			else if(ui.radioButton_Internal_DR_PoseEstimation->isChecked()){
				qnode.poseEstimationMethod = 3;
				ui.toolBox->setCurrentIndex(0);
			}
			// Enable Safety Loops
			qnode.safeFlight = ui.checkBox_safeFlight->isChecked();
			qnode.testBatteryBellowLand = ui.checkBox_batteryBellowLand->isChecked();
			qnode.testBatteryBellowGoHome = ui.checkBox_batteryBellowGoHome->isChecked();
			qnode.testNoWifi = ui.checkBox_noWifiSignal->isChecked();
		}
	}
}


// Use Environment Variables Checkbox : If not checked the Master and Host run
//										on different machines
void MainWindow::on_checkbox_use_environment_stateChanged(int state) {
	bool enabled;
	if ( state == 0 ) {
		enabled = true;
	} else {
		enabled = false;
	}
	ui.line_edit_master->setEnabled(enabled);
	ui.line_edit_host->setEnabled(enabled);
}
// Close Application Button
void MainWindow::on_quit_button_clicked(){
	close();
}
// --------------------
// Push Buttons Control
// --------------------
void MainWindow::on_button_takeoff_clicked(){qnode.actionCode = 1;}
void MainWindow::on_button_land_clicked(){qnode.actionCode = 2;}
void MainWindow::on_button_reset_clicked(){qnode.actionCode = 3;}
// Twist Commands : command(vx,vy,vz,rx,ry,rz)
// actionCode : 0 - Reset Command Latch, 1 - Take off, 2 - Land, 3 - Reset
//				4 - Go to Waypoint, 5 - Look at Waypoint, 6 - Get Waypoint (Drone Frame)
//				7 - Look and Go to Waypoint, 8 -Follow Flightpath
//				9 - Follow flightpath home
void MainWindow::on_button_forward_clicked(){
	resetSliders(5);
	qnode.actionCode = 0;
	qnode.command(1,0,0,0,0,0);
}
void MainWindow::on_button_backward_clicked(){
	resetSliders(5);
	qnode.actionCode = 0;
	qnode.command(-1,0,0,0,0,0);
}
// ClockWise and Counter-ClockWise might be inverted on the actual drone
void MainWindow::on_button_rotateCCW_clicked(){
	resetSliders(5);
	qnode.actionCode = 0;
	qnode.command(0,0,0,0,0,0.5);
}
void MainWindow::on_button_rotateCW_clicked(){
	resetSliders(5);
	qnode.actionCode = 0;
	qnode.command(0,0,0,0,0,-0.5);
}
void MainWindow::on_button_halt_clicked(){
	resetSliders(5);
	updateSliderLCDs();
	qnode.actionCode = 0;
	qnode.command(0,0,0,0,0,0);
}
void MainWindow::on_button_up_clicked(){
	resetSliders(5);
	qnode.actionCode = 0;
	qnode.command(0,0,0.5,0,0,0);
}
void MainWindow::on_button_down_clicked(){
	resetSliders(5);
	qnode.actionCode = 0;
	qnode.command(0,0,-0.5,0,0,0);
}
// Left and Right might be inverted on the actual drone
void MainWindow::on_button_left_clicked(){
	resetSliders(5);
	qnode.actionCode = 0;
	qnode.command(0,0.5,0,0,0,0);
}
void MainWindow::on_button_right_clicked(){
	resetSliders(5);
	qnode.actionCode = 0;
	qnode.command(0,-0.5,0,0,0,0);
}
// ---------------
// Slider Controls
// ---------------
void MainWindow::on_fwbw_slider_sliderMoved(){
	resetSliders(1);
	float x = (float)(ui.fwbw_slider->value())/100;
	qnode.actionCode = 0;
	updateSliderLCDs();
	qnode.command(x,0,0,0,0,0);
}
void MainWindow::on_height_slider_sliderMoved(){
	resetSliders(3);
	float z = (float)(ui.height_slider->value())/100;
	qnode.actionCode = 0;
	updateSliderLCDs();
	qnode.command(0,0,z,0,0,0);
}
void MainWindow::on_sideways_slider_sliderMoved(){
	resetSliders(2);
	float y = -1*(float)(ui.sideways_slider->value())/100;
	qnode.actionCode = 0;
	updateSliderLCDs();
	qnode.command(0,y,0,0,0,0);
}
void MainWindow::on_rotation_slider_sliderMoved(){
	resetSliders(4);
	float zrot = -1*(float)(ui.rotation_slider->value())/100;
	qnode.actionCode = 0;
	updateSliderLCDs();
	qnode.command(0,0,0,0,0,zrot);
}

// Reset the sliders used for controlling the drone speed
void MainWindow::resetSliders(int slider){
	switch (slider){
		case 1: ui.sideways_slider->setValue(0);
				ui.height_slider->setValue(0);
				ui.rotation_slider->setValue(0);
				break;
		case 2:	ui.fwbw_slider->setValue(0);
				ui.height_slider->setValue(0);
				ui.rotation_slider->setValue(0);
				break;
		case 3:	ui.fwbw_slider->setValue(0);
				ui.sideways_slider->setValue(0);
				ui.rotation_slider->setValue(0);
				break;
		case 4:	ui.fwbw_slider->setValue(0);
				ui.sideways_slider->setValue(0);
				ui.height_slider->setValue(0);
				break;
		default:ui.fwbw_slider->setValue(0);
				ui.sideways_slider->setValue(0);
				ui.height_slider->setValue(0);
				ui.rotation_slider->setValue(0);
				break;
	}
}
// ----------------
// Waypoint Control
// ----------------
// Go to Waypoint
void MainWindow::on_button_GoToWaypoint_clicked(){
	qnode.targetInMap.position.x = ui.lineEdit_targetX->text().toFloat();
	qnode.targetInMap.position.y = ui.lineEdit_targetY->text().toFloat();
	qnode.targetInMap.position.z = ui.lineEdit_targetZ->text().toFloat();
	qnode.actionCode = 4;
}
// Look at Waypoint
void MainWindow::on_button_LookAtWaypoint_clicked(){
	qnode.targetInMap.position.x = ui.lineEdit_targetX->text().toFloat();
	qnode.targetInMap.position.y = ui.lineEdit_targetY->text().toFloat();
	qnode.targetInMap.position.z = ui.lineEdit_targetZ->text().toFloat();
	qnode.actionCode = 5;
}
// Get Waypoint Information
void MainWindow::on_button_GetWaypoint_clicked(){
	qnode.targetInMap.position.x = ui.lineEdit_targetX->text().toFloat();
	qnode.targetInMap.position.y = ui.lineEdit_targetY->text().toFloat();
	qnode.targetInMap.position.z = ui.lineEdit_targetZ->text().toFloat();
	qnode.actionCode = 6;
}
// Look while Going at the Waypoint
void MainWindow::on_button_LookNGo_clicked(){
	qnode.targetInMap.position.x = ui.lineEdit_targetX->text().toFloat();
	qnode.targetInMap.position.y = ui.lineEdit_targetY->text().toFloat();
	qnode.targetInMap.position.z = ui.lineEdit_targetZ->text().toFloat();
	qnode.actionCode = 7;
}
// Follow the flightpath
void MainWindow::on_button_FolowFlightpath_clicked(){
		ui.textEdit_waypoints->append("New Flightpath Loaded");
		ui.textEdit_waypoints->append("---------------------");
		ui.textEdit_waypoints->append("[Command] [X] [Y] [Z]");
		if(ui.checkBox_invertFlightpath->isChecked())
		{
			QString inFilename = QString("%1").arg(ui.line_edit_loadWaypointFilePath->text());
			QString outFilename = QString("%1%2").arg(QCoreApplication::applicationDirPath()).arg("/InvertedReachedWaypoints.txt");

			invertFlightpath(inFilename, outFilename);
			ui.line_edit_loadWaypointFilePath->setText(outFilename);
		}
	wayPointCommandLine = 0;
	qnode.actionCode = 8;
}
// Open the file containing a sequence of waypoint commands
void MainWindow::on_button_openWaypointsFile_clicked(){
	QString fileName = QFileDialog::getOpenFileName(this, tr("Open File"),
	QCoreApplication::applicationDirPath(), tr("Text (*.txt)"));
	wayPointCommandLine = 0;
	ui.line_edit_loadWaypointFilePath->setText(fileName);
}
// Select the destination file to save recorded waypoints with commands
void MainWindow::on_button_saveWaypointsFile_clicked(){
	QString fileName = QFileDialog::getOpenFileName(this, tr("Save File"),
	QCoreApplication::applicationDirPath(), tr("Text (*.txt)"));
	ui.line_edit_saveWaypointFilePath->setText(fileName);
}
// Location to save images
void MainWindow::on_button_imagesFilePathSelect_clicked(){
	QString fileName = QFileDialog::getExistingDirectory(this, tr("Save Location"),
	QCoreApplication::applicationDirPath());
	ui.line_edit_saveImageFilePath->setText(fileName);
}
// Read the next waypoint from the selected file
void MainWindow::updateWaypoint(){
	// File selected to load Flightpath data from
	QFile file(ui.line_edit_loadWaypointFilePath->text());
	if(!file.open(QIODevice::ReadOnly)){
		QMessageBox::information(0, "error", file.errorString());
	}
	QTextStream in(&file);
	int currentLine = 0;
	while(!in.atEnd()) {
    	QString line = in.readLine();
    	if(!line.contains("#", Qt::CaseInsensitive)){
    		QStringList list = line.split(",");
    		if(QString::compare(list[0], "GOTO", Qt::CaseInsensitive) == 0){
	    		if (currentLine == wayPointCommandLine){
	    			ui.textEdit_waypoints -> append(list[0] + " " + list[1] + " "
	    											 + list[2] + " " + list[3]);
	    			qnode.targetInMap.position.x = list[1].toFloat();
					qnode.targetInMap.position.y = list[2].toFloat();
					qnode.targetInMap.position.z = list[3].toFloat();
					ui.lineEdit_targetX -> setText(list[1]);
					ui.lineEdit_targetY -> setText(list[2]);
					ui.lineEdit_targetZ -> setText(list[3]);
	    		}
	    		currentLine ++;
	    	}
	    	// TODO : Add another If for the GOTOW command, which includes a waiting time in between way points
    	}
	}
	file.close();
	if(currentLine > wayPointCommandLine)
	{
		wayPointCommandLine ++;
		qnode.currentWaypointPtr ++;
	}
	else{
		qnode.actionCode = 0;
		qnode.command(0,0,0,0,0,0);
	}
}
// A function to save waypoints with a limit in between recorded waypoints
void MainWindow::saveWaypoint(){
	QFile file(ui.line_edit_saveWaypointFilePath->text());
	if(	qAbs(qnode.lastSavedWaypoint.position.x - qnode.currentDroneData.x) > 3*qnode.waypointAccuracy ||
			qAbs(qnode.lastSavedWaypoint.position.y - qnode.currentDroneData.y) > 3*qnode.waypointAccuracy ||
			qAbs(qnode.lastSavedWaypoint.position.z - qnode.currentDroneData.z) > 3*qnode.waypointAccuracy )
	{
		file.open(QIODevice::WriteOnly | QIODevice::Append);
		QTextStream out(&file);
		QString str = QString("GOTO,%1,%2,%3\n").
			arg(qnode.currentDroneData.x).arg(qnode.currentDroneData.y).arg(qnode.currentDroneData.z);
		qnode.lastSavedWaypoint.position.x = qnode.currentDroneData.x;
		qnode.lastSavedWaypoint.position.y = qnode.currentDroneData.y;
		qnode.lastSavedWaypoint.position.z = qnode.currentDroneData.z;
		out << str;
		file.close();
	}
}

// Invert the selected flightpath to follow backwards
void MainWindow::invertFlightpath(QString inFilename, QString outFilename){
	QFile::remove(outFilename);
	QFile outFile(outFilename);
	QFile inFile(inFilename);
	// Read the waypoint commands from the target file
	if(!inFile.open(QIODevice::ReadOnly)){
		QMessageBox::information(0, "error", inFile.errorString());
	}
	QTextStream in(&inFile);
	int currentLine = 0;
	QStringList listFinal;
	while(!in.atEnd()) {
    	QString line = in.readLine();
    	if(!line.contains("#", Qt::CaseInsensitive)){
    		QStringList list2 = line.split(",");
    		if(QString::compare(list2[0], "GOTO", Qt::CaseInsensitive) == 0){
    			listFinal.append(line);
				currentLine ++;
	    	}
	    }
	    	// TODO : Add another If for the GOTOW command, which includes a waiting time in between way points
    }
	inFile.close();
	// Write the inverted list into a file
	outFile.open(QIODevice::WriteOnly | QIODevice::Append);
	QTextStream out(&outFile);
	for(int i=currentLine-1; i>=0 ; i--){
		out << listFinal[i];
		out << "\n";
	}
	outFile.close();
}

// ------------------------
// Sampling Data and Images
// ------------------------
// Record the flightpath into a .txt document
void MainWindow::on_checkBox_recordFlight_stateChanged(){
	QFile::remove(ui.line_edit_saveWaypointFilePath->text());
	qnode.recordFlightPath = ui.checkBox_recordFlight->isChecked();
}
// Save measurements to selected destination .txt file
void MainWindow::on_checkBox_saveData_stateChanged(){
	qnode.recordData = ui.checkBox_saveData->isChecked();
}
// Save Images at the desired location
void MainWindow::on_checkBox_saveImages_stateChanged(){
	qnode.recordImages = ui.checkBox_saveImages->isChecked();
}
// Set the image sampling time
void MainWindow::on_spinBox_samplingTime_valueChanged(){
	qnode.imageSamplingTime = ui.spinBox_samplingTime->value()/1000;
}

// Save required data to a file with correct formating
void MainWindow::saveDataToFile(){
	QFile fileOut(QCoreApplication::applicationDirPath() + "/Captured Data.txt");
	fileOut.open(QIODevice::WriteOnly | QIODevice::Append);
	QTextStream out(&fileOut);
	QString str = QString("%1 %2 %3 %4 %5 %6 %7 %8 %9 %10 %11 %12 %13 %14 %15 %16\n").arg(qnode.currentDroneData.timeStamp.toSec(),7)
	.arg(qnode.currentDroneData.x,12).arg(qnode.currentDroneData.y,12).arg(qnode.currentDroneData.z,12)
	.arg(qnode.currentDroneData.xVel,12).arg(qnode.currentDroneData.yVel,12).arg(qnode.currentDroneData.zVel,12)
	.arg(qnode.currentDroneData.xAcc,12).arg(qnode.currentDroneData.yAcc,12).arg(qnode.currentDroneData.zAcc,12)
	.arg(qnode.currentDroneData.xRot,12).arg(qnode.currentDroneData.yRot,12).arg(qnode.currentDroneData.zRot,12)
	.arg(qnode.currentDroneData.xRotVel,12).arg(qnode.currentDroneData.yRotVel,12).arg(qnode.currentDroneData.zRotVel,12);
	//.arg(qnode.currentDroneData.motor1).arg(qnode.currentDroneData.motor2).arg(qnode.currentDroneData.motor3).arg(qnode.currentDroneData.motor4);
	out << str;
	dataNumber++;
	fileOut.close();

	QFile fileOut2(QCoreApplication::applicationDirPath() + "/TestData.txt");
	fileOut2.open(QIODevice::WriteOnly | QIODevice::Append);
	QTextStream out2(&fileOut2);
	QString str2 = QString("%1 %2 %3 %4 %5 %6 %7 %8 %9 %10\n").arg(qnode.currentDroneData.timeStamp.toSec(),7)
	.arg(qnode.realPose.pose.position.x,12).arg(qnode.realPose.pose.position.y,12).arg(qnode.realPose.pose.position.z,12)
	.arg(qnode.estimatedPoseDR.position.x,12).arg(qnode.estimatedPoseDR.position.y,12).arg(qnode.estimatedPoseDR.position.z,12)
	.arg(ui.lineEdit_targetX->text().toFloat(),12).arg(ui.lineEdit_targetY->text().toFloat(),12).arg(ui.lineEdit_targetZ->text().toFloat(),12);
	out2 << str2;
	fileOut2.close();
}
// Save images to a file
void MainWindow::saveImageToFile(){
	QString camera;
	// Sample the appropriate camera
	if(qnode.samplingFrontCamera)
	{
		// Convert the 3D array object to a QImage object
		//q_image = mat2QImage(qnode.CV_front_image_ptr->image);
		camera = "F";
	}
	else
	{
		//q_image = mat2QImage(qnode.CV_bottom_image_ptr->image);
		camera = "B";
	}
	if(!QDir(ui.line_edit_saveImageFilePath->text()).exists()){
   		QDir().mkdir(ui.line_edit_saveImageFilePath->text());
   	}
   	// Edit the filename with the Camera identifier and the timestamp of the image
	QString filename = QString("%1%2%3%4").arg(ui.line_edit_saveImageFilePath->text()).arg(camera)
	.arg(qnode.currentDroneData.timeStamp.toSec()).arg(".png");
	QFile imageFile(filename);
	imageFile.open(QIODevice::WriteOnly);

	QPixmap pixmap = QPixmap::fromImage(q_image);
	pixmap.save(&imageFile, "PNG");
}
// --------------------
// Camera Radio Buttons
// --------------------
// Bottom camera selected by the user to display
void MainWindow::on_radioButton_bottomCamera_clicked(){
	ui.radioButton_frontCamera->setChecked(false);
}
// Front camera selected by the user to display
void MainWindow::on_radioButton_frontCamera_clicked(){
	ui.radioButton_bottomCamera->setChecked(false);
}


// ------------
// Safety-Loops
// ------------
// Save the next waypoint on the flightpath to go home [SLOT]
void MainWindow::saveWayHome(){
	QFile file(QCoreApplication::applicationDirPath() + "/WayHome.txt");
	file.open(QIODevice::ReadWrite | QIODevice::Append);
	QTextStream out(&file);
	QString str;
	if(qnode.wayHomePtr >= 0){
		str = QString("GOTO,%1,%2,%3\n").
			arg(qnode.currentDroneData.x).arg(qnode.currentDroneData.y).arg(qnode.currentDroneData.z);
	}
	else{
		str = QString("GOTO,%1,%2,%3\n").
			arg(0).arg(0).arg(0.2);
	}
	out << str;
	file.close();
	wayHomeCommandLine++;
	qnode.wayHomePtr++;
}

// Load the first (last in the list) waypoint to return home and delete it [SLOT]
void MainWindow::loadWayHome(){
	QFile file(QCoreApplication::applicationDirPath() + "/WayHome.txt");
	if(!file.open(QIODevice::ReadOnly)){
		QMessageBox::information(0, "error", file.errorString());
	}
	QTextStream in(&file);
	int currentLine = 0;
	while(!in.atEnd()){
		QString line = in.readLine();
		if(currentLine == qnode.wayHomePtr){
			QStringList list = line.split(",");
			if(QString::compare(list[0], "GOTO", Qt::CaseInsensitive) == 0){
    			ui.textEdit_waypoints -> append(list[0] + " " + list[1] + " "
    											 + list[2] + " " + list[3]);
    			qnode.targetInMap.position.x = list[1].toFloat();
				qnode.targetInMap.position.y = list[2].toFloat();
				qnode.targetInMap.position.z = list[3].toFloat();
				ui.lineEdit_targetX -> setText(list[1]);
				ui.lineEdit_targetY -> setText(list[2]);
				ui.lineEdit_targetZ -> setText(list[3]);
    		}
		}
		currentLine++;
	}
	file.close();
	qnode.actionCode = 9;
}


// Update the Way Home file by deleting waypoints that have been followed backwards [SLOT]
void MainWindow::changeWayHome(){
	QFile file(QCoreApplication::applicationDirPath() + "/WayHome.txt");
	file.open(QIODevice::ReadOnly);
	QTextStream in(&file);
	QStringList listOfWaypoints;
	int i;
	for(i=0;i<=qnode.wayHomePtr;i++){
		QString line = in.readLine();
		listOfWaypoints << line;
	}
	file.close();
	QFile::remove(QCoreApplication::applicationDirPath() + "/WayHome.txt");
	file.open(QIODevice::WriteOnly | QIODevice::Append);
	QTextStream out(&file);
	for(i=0;i<=qnode.wayHomePtr;i++){
		out << listOfWaypoints[i] << endl;
	}
	file.close();
}
// Test Signal for Battery Low land-action threshold
void MainWindow::on_checkBox_batteryBellowLand_stateChanged(){
	qnode.testBatteryBellowLand = ui.checkBox_batteryBellowLand->isChecked();
}
// Test Signal for Battery Low go-to-base-action threshold
void MainWindow::on_checkBox_batteryBellowGoHome_stateChanged(){
	qnode.testBatteryBellowGoHome = ui.checkBox_batteryBellowGoHome->isChecked();
}
// Test Signal for No WiFi connection
void MainWindow::on_checkBox_noWifiSignal_stateChanged(){
	qnode.testNoWifi = ui.checkBox_noWifiSignal->isChecked();
}
// User select wether Safety Control Loops should be active during flight
void MainWindow::on_checkBox_safeFlight_stateChanged(){
	qnode.safeFlight = ui.checkBox_safeFlight->isChecked();
}
// ----------------------------------------
// Updata Information to display on the GUI
// ----------------------------------------
// Update some information on the UI [SLOT]
void MainWindow::updateData()
{
	ui.batteryLCD->display(qnode.battery);
	ui.stateLCD->display(qnode.droneState);
	switch (qnode.droneState)
	{
		case 0 : ui.label_7->setText("Unknown");
			break;
		case 1 : ui.label_7->setText("Inited");
			break;
		case 2 : ui.label_7->setText("Landed");
			break;
		case 3 : ui.label_7->setText("Flying");
			break;
		case 4 : ui.label_7->setText("Hovering");
			break;
		case 5 : ui.label_7->setText("Test");
			break;
		case 6 : ui.label_7->setText("Taking off");
			break;
		case 7 : ui.label_7->setText("Flying");
			break;
		case 8 : ui.label_7->setText("Landing");
			break;
		case 9 : ui.label_7->setText("Looping");
			break;
		default: ui.label_7->setText("       ");
			break;
	}
}
// Update the Image in the GUI [SLOT]
void MainWindow::updateImage()
{
	// Front Camera
	if(ui.radioButton_frontCamera->isChecked())
	{	
		//q_image = mat2QImage(qnode.CV_front_image_ptr->image);
		ui.label_6->setPixmap(QPixmap::fromImage(q_image));
	}
	// Bottom Camera
	else if(ui.radioButton_bottomCamera->isChecked())
	{
		//q_image = mat2QImage(qnode.CV_bottom_image_ptr->image);
		ui.label_6->setPixmap(QPixmap::fromImage(q_image));
	}
}
// Update drone Real Position (if simulator is used) [SLOT]
void MainWindow::updateRealPose(){
	QString str;
	// Real Pose and Orientation
	str = "";
	ui.lineEdit_realPoseX->setText(str.append(QString("%1").
		arg(qnode.realPose.pose.position.x)));
	str = "";
	ui.lineEdit_realPoseY->setText(str.append(QString("%1").
		arg(qnode.realPose.pose.position.y)));
	str = "";
	ui.lineEdit_realPoseZ->setText(str.append(QString("%1").
		arg(qnode.realPose.pose.position.z)));
	str = "";
	ui.lineEdit_realAngleX->setText(str.append(QString("%1").
		arg(qnode.currentDroneData.xRot)));
	str = "";
	ui.lineEdit_realAngleY->setText(str.append(QString("%1").
		arg(qnode.currentDroneData.yRot)));
	str = "";
	ui.lineEdit_realAngleZ->setText(str.append(QString("%1").
	arg(qnode.currentDroneData.zRot)));
}
// Use internally estimated Pose to display [SLOT]
void MainWindow::updateEstimatedPose(){
	QString str;
	float errorx, errory, errorz;
	if(ui.radioButton_Internal_DR_PoseEstimation->isChecked()){
		str = "";
		ui.lineEdit_estimatedPoseX->setText(str.append(QString("%1").
			arg(qnode.estimatedPoseDR.position.x)));
		str = "";
		ui.lineEdit_estimatedPoseY->setText(str.append(QString("%1").
			arg(qnode.estimatedPoseDR.position.y)));
		str = "";
		ui.lineEdit_estimatedPoseZ->setText(str.append(QString("%1").
			arg(qnode.estimatedPoseDR.position.z)));

		errorx = qnode.estimatedPoseDR.position.x - qnode.realPose.pose.position.x;
		errory = qnode.estimatedPoseDR.position.y - qnode.realPose.pose.position.y;
		errorz = qnode.estimatedPoseDR.position.z - qnode.realPose.pose.position.z;

		str = "";
		ui.lineEdit_poseErrorX->setText(str.append(QString("%1").
			arg(errorx)));
		str = "";
		ui.lineEdit_poseErrorY->setText(str.append(QString("%1").
			arg(errory)));
		str = "";
		ui.lineEdit_poseErrorZ->setText(str.append(QString("%1").
			arg(errorz)));
	}
	str = "";
	ui.lineEdit_realAngleX->setText(str.append(QString("%1").
		arg(qnode.currentDroneData.xRot)));
	str = "";
	ui.lineEdit_realAngleY->setText(str.append(QString("%1").
		arg(qnode.currentDroneData.yRot)));
	str = "";
	ui.lineEdit_realAngleZ->setText(str.append(QString("%1").
	arg(qnode.currentDroneData.zRot)));
}
// Use externally estimated pose to display [SLOT]
void MainWindow::updateExternalEstimatedPose(){
	QString str;
	float errorx, errory, errorz;
	if(ui.radioButton_External_PoseEstimation->isChecked()){
		str = "";
		ui.lineEdit_estimatedPoseX->setText(str.append(QString("%1").
			arg(qnode.externalEstimatedPose.pose.position.x)));
		str = "";
		ui.lineEdit_estimatedPoseX->setText(str.append(QString("%1").
			arg(qnode.externalEstimatedPose.pose.position.y)));
		str = "";
		ui.lineEdit_estimatedPoseX->setText(str.append(QString("%1").
			arg(qnode.externalEstimatedPose.pose.position.z)));

		errorx = qnode.externalEstimatedPose.pose.position.x - qnode.realPose.pose.position.x;
		errory = qnode.externalEstimatedPose.pose.position.y - qnode.realPose.pose.position.y;
		errorz = qnode.externalEstimatedPose.pose.position.z - qnode.realPose.pose.position.z;

		str = "";
		ui.lineEdit_poseErrorX->setText(str.append(QString("%1").
			arg(errorx)));
		str = "";
		ui.lineEdit_poseErrorY->setText(str.append(QString("%1").
			arg(errory)));
		str = "";
		ui.lineEdit_poseErrorZ->setText(str.append(QString("%1").
			arg(errorz)));
	}
	str = "";
	ui.lineEdit_realAngleX->setText(str.append(QString("%1").
		arg(qnode.currentDroneData.xRot)));
	str = "";
	ui.lineEdit_realAngleY->setText(str.append(QString("%1").
		arg(qnode.currentDroneData.yRot)));
	str = "";
	ui.lineEdit_realAngleZ->setText(str.append(QString("%1").
	arg(qnode.currentDroneData.zRot)));
}
// Update the appripriate objects of the UI with the Target Waypoint
// co-ordinates in the Drone frame [SLOT]
void MainWindow::updateTargetInDrone(){
	QString str;
	// Errors from the target/ Target Co-Ordinated In the Drone Frame
	// XYZ co-ordinates
	str = "";
	ui.lineEdit_errorX->setText(str.append(QString("%1").
		arg(qnode.targetInDrone.position.x)));
	str = "";
	ui.lineEdit_errorY->setText(str.append(QString("%1").
		arg(qnode.targetInDrone.position.y)));
	str = "";
	ui.lineEdit_errorZ->setText(str.append(QString("%1").
		arg(qnode.targetInDrone.position.z)));
	// Rotation and Angle Controller Errors
	str = "";
	ui.lineEdit_targetAngleZ->setText(str.append(QString("%1").
		arg(qnode.targetInDrone.orientation.z*180/M_PI)));
}
// Convert from a 2D Matrix to a QImage object
//QImage MainWindow::mat2QImage(const cv::Mat3b &src) {
//      QImage dest(src.cols, src.rows, QImage::Format_ARGB32);
 //       for (int y = 0; y < src.rows; ++y) {
 //               const cv::Vec3b *srcrow = src[y];
 //               QRgb *destrow = (QRgb*)dest.scanLine(y);
  //              for (int x = 0; x < src.cols; ++x) {
 //                       destrow[x] = qRgba(srcrow[x][2], srcrow[x][1], srcrow[x][0], 255);
 //               }
 //       }
//        return dest;
//}
// Update the LCDs to show the values of the respective sliders [SLOT]
void MainWindow::updateSliderLCDs(){
	ui.fwbw_LCD->display(ui.fwbw_slider->value());
	ui.height_LCD->display(ui.height_slider->value());
	ui.sideways_LCD->display(ui.sideways_slider->value());
	ui.rotation_LCD->display(ui.rotation_slider->value());

}
// ----------------------
// Pose Estimation Choice
// ----------------------
// Use the Real position of the drone offered by the TUM_simulator
void MainWindow::on_radioButton_Simulation_PoseEstimation_clicked(){
	if(ui.radioButton_Simulation_PoseEstimation->isChecked()){
		ui.radioButton_External_PoseEstimation->setChecked(false);
		ui.radioButton_Internal_DR_PoseEstimation->setChecked(false);
		qnode.poseEstimationMethod = 1;
	}
	else{
		ui.radioButton_Simulation_PoseEstimation->setChecked(true);
	}
}
// Use an external position estimator
void MainWindow::on_radioButton_External_PoseEstimation_clicked(){
	if(ui.radioButton_External_PoseEstimation->isChecked()){
		ui.radioButton_Simulation_PoseEstimation->setChecked(false);
		ui.radioButton_Internal_DR_PoseEstimation->setChecked(false);
		qnode.poseEstimationMethod = 2;
	}
	else{
		ui.radioButton_External_PoseEstimation->setChecked(true);
	}
}
// Use internal position estimator with dead-reckoning
void MainWindow::on_radioButton_Internal_DR_PoseEstimation_clicked(){
	if(ui.radioButton_Internal_DR_PoseEstimation->isChecked()){
		ui.radioButton_Simulation_PoseEstimation->setChecked(false);
		ui.radioButton_External_PoseEstimation->setChecked(false);
		qnode.poseEstimationMethod = 3;
	}
	else{
		ui.radioButton_Internal_DR_PoseEstimation->setChecked(true);
	}
}
// About section 
void MainWindow::on_actionAbout_triggered() {
    QMessageBox::about(this, tr("About ..."),"<h2>Drone WayPointer v1.0</h2>"
    	"<p><b>Copyright 2014 The University of Sheffield <a href=\"www.sheffield.ac.uk\">www.sheffield.ac.uk </a></b></p>"
    	"<p><b>Copyright 2014 Stefanos Giagkiozis <a href=\"SteveGiagkiozis@gmail.com\">SteveGiagkiozis@gmail.com </a></b></p>"
		"Drone WayPointer is free software: you can redistribute it and/or modify"
		"it under the terms of the GNU General Public License as published by"
		"the Free Software Foundation, either version 3 of the License, or"
		"(at your option) any later version."
		"Drone WayPointer is distributed in the hope that it will be useful,"
		"but WITHOUT ANY WARRANTY; without even the implied warranty of"
		"MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the"
		"GNU General Public License for more details."
		"You should have received a copy of the GNU General Public License"
		"along with Drone WayPointer.If not, see <a href=\"http://www.gnu.org/licenses/\">License </a>.</p>"
		"<p> For any bugs or suggestions feel free to contact me via e-mail. ENJOY!!!</p>");
}

void MainWindow::ReadSettings() {
    QSettings settings("Qt-Ros Package", "drone_waypointer");
    restoreGeometry(settings.value("geometry").toByteArray());
    restoreState(settings.value("windowState").toByteArray());
    QString master_url = settings.value("master_url",QString("http://192.168.1.2:11311/")).toString();
    QString host_url = settings.value("host_url", QString("192.168.1.3")).toString();
    //QString topic_name = settings.value("topic_name", QString("/chatter")).toString();
    ui.line_edit_master->setText(master_url);
    ui.line_edit_host->setText(host_url);
    //ui.line_edit_topic->setText(topic_name);
    bool remember = settings.value("remember_settings", false).toBool();
    ui.checkbox_remember_settings->setChecked(remember);
    bool checked = settings.value("use_environment_variables", false).toBool();
    ui.checkbox_use_environment->setChecked(checked);
    if ( checked ) {
    	ui.line_edit_master->setEnabled(false);
    	ui.line_edit_host->setEnabled(false);
    	//ui.line_edit_topic->setEnabled(false);
    }
}

void MainWindow::WriteSettings() {
    QSettings settings("Qt-Ros Package", "drone_waypointer");
    settings.setValue("master_url",ui.line_edit_master->text());
    settings.setValue("host_url",ui.line_edit_host->text());
    //settings.setValue("topic_name",ui.line_edit_topic->text());
    settings.setValue("use_environment_variables",QVariant(ui.checkbox_use_environment->isChecked()));
    settings.setValue("geometry", saveGeometry());
    settings.setValue("windowState", saveState());
    settings.setValue("remember_settings",QVariant(ui.checkbox_remember_settings->isChecked()));

}
void MainWindow::closeEvent(QCloseEvent *event)
{
	WriteSettings();
	QMainWindow::closeEvent(event);
}


}  // namespace drone_waypointer

