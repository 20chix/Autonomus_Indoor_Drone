/**
*	This file is part of Drone WayPointer.
*	
*   Copyright 2014 The University of Sheffield (www.sheffield.ac.uk)
*	Copyright 2014 Stefanos Giagkiozis < SteveGiagkiozis@gmail.com >
*
*    Drone WayPointer is free software: you can redistribute it and/or modify
*    it under the terms of the GNU General Public License as published by
*    the Free Software Foundation, either version 3 of the License, or
*    (at your option) any later version.
*
*    Drone WayPointer is distributed in the hope that it will be useful,
*    but WITHOUT ANY WARRANTY; without even the implied warranty of
*    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
*    GNU General Public License for more details.
*
*    You should have received a copy of the GNU General Public License
*    along with Drone WayPointer.  If not, see <http://www.gnu.org/licenses/>.
**/

#ifndef drone_waypointer_MAIN_WINDOW_H
#define drone_waypointer_MAIN_WINDOW_H

#include <QtGui/QMainWindow>
#include <iostream>
#include <QFileDialog>


#ifndef Q_MOC_RUN
#include "qnode.hpp"
#include "ui_main_window.h"
#endif


namespace drone_waypointer {

class MainWindow : public QMainWindow {
Q_OBJECT

public:
	MainWindow(int argc, char** argv, QWidget *parent = 0);
	~MainWindow();

	void ReadSettings(); // Load up qt program settings at startup
	void WriteSettings(); // Save qt program settings when closing

	void closeEvent(QCloseEvent *event); // Overloaded function
	void showNoMasterMessage();

public Q_SLOTS:
	void on_actionAbout_triggered();
	void on_button_connect_clicked(bool check );
	void on_checkbox_use_environment_stateChanged(int state);
	void on_quit_button_clicked();
	// --------------------
	// Push Buttons Control
	// --------------------
	void on_button_takeoff_clicked();
	void on_button_land_clicked();
	void on_button_reset_clicked();
	void on_button_forward_clicked();
	void on_button_backward_clicked();
	void on_button_rotateCCW_clicked();
	void on_button_rotateCW_clicked();
	void on_button_halt_clicked();
	void on_button_up_clicked();
	void on_button_down_clicked();
	void on_button_left_clicked();
	void on_button_right_clicked();
	// ---------------
	// Slider Controls
	// ---------------
	void on_fwbw_slider_sliderMoved();
	void on_height_slider_sliderMoved();
	void on_sideways_slider_sliderMoved();
	void on_rotation_slider_sliderMoved();
	void resetSliders(int slider);
	// ----------------
	// Waypoint Control
	// ----------------
	void on_button_GoToWaypoint_clicked();
	void on_button_LookAtWaypoint_clicked();
	void on_button_GetWaypoint_clicked();
	void on_button_LookNGo_clicked();
	void on_button_FolowFlightpath_clicked();
	void on_button_openWaypointsFile_clicked();
	void on_button_saveWaypointsFile_clicked();
	void on_checkBox_recordFlight_stateChanged();
	void updateWaypoint();
    void saveWaypoint();
    void invertFlightpath(QString inFilename, QString outFilename);
	// ------------------------
	// Sampling Data and Images
	// ------------------------
	void on_checkBox_saveData_stateChanged();
	void on_checkBox_saveImages_stateChanged();
	void on_button_imagesFilePathSelect_clicked();
	void on_spinBox_samplingTime_valueChanged();
	void saveDataToFile();
    void saveImageToFile();
	// --------------------
	// Camera Radio Buttons
	// --------------------
	void on_radioButton_bottomCamera_clicked();
	void on_radioButton_frontCamera_clicked();
	// ------------
	// Safety-Loops
	// ------------
	void saveWayHome();
	void loadWayHome();
	void changeWayHome();
	void on_checkBox_batteryBellowLand_stateChanged();
	void on_checkBox_batteryBellowGoHome_stateChanged();
	void on_checkBox_noWifiSignal_stateChanged();
	void on_checkBox_safeFlight_stateChanged();
	// ----------------------------------------
    // Updata Information to display on the GUI
    // ----------------------------------------
    void updateData();
    void updateImage();
    //QImage mat2QImage(const cv::Mat3b &src);
    void updateRealPose();
    void updateEstimatedPose();
    void updateExternalEstimatedPose();
    void updateTargetInDrone();
    void updateSliderLCDs();
    // ----------------------
    // Pose Estimation Choice
    // ----------------------
    void on_radioButton_Simulation_PoseEstimation_clicked();
    void on_radioButton_External_PoseEstimation_clicked();
    void on_radioButton_Internal_DR_PoseEstimation_clicked();
    
    
private:
	Ui::MainWindowDesign ui;
	QNode qnode;
	int wayPointCommandLine;
	int wayHomeCommandLine;
	QImage q_image;
	int dataNumber;
};

}  // namespace drone_waypointer

#endif // drone_waypointer_MAIN_WINDOW_HH
