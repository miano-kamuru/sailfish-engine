/*
Author:miano
Project:sailFish engine
MainWindow_Skeleton_menuBarSkeleton -component file for Relationship_OneToOneWindow activated by relationship
/one to one
*/

import QtQuick 2.6
import QtQuick.Controls 2.6
import QtQuick.Layouts 1.12
import QtQuick.Controls.Material 2.6

ApplicationWindow {
	Material.theme:Material.Light;
	id:parentW;
	visible:false;
	flags:Qt.Dialog;
	modality:Qt.WindowModal;
	title:qsTr("create a one to one relationship");
    width:mainLayout.width;
    height:mainLayout.height
    maximumWidth:mainLayout.width 
    maximumHeight:mainLayout.height;
    
    	//Layout
    	ColumnLayout { //COlumnlayout starts here --main layout
    		id:mainLayout
    		GroupBox{ //group box
    			Layout.margins:10;
    		RowLayout { //row layout
    			spacing:20;

    			Text { //text1
    			id:text1
    			text:qsTr("One")
    			font.pointSize:14;
                color:"Grey";
    		 } //text1 ends here

    		 ComboBox { //combobox1 
    		 	id:combobox1;
    		 	Layout.preferredWidth:250
    		 	model:['object1','object2']
    		 } //combobox1 ends here

    		 Text { //text2
    		 	id:text2;
    		 	text:qsTr("To One");
    		 	font.pointSize:text1.font.pointSize;
                color:"Grey";
    		 } //text2 ends here

    		 ComboBox { //combobox 2
    		 	Layout.preferredWidth:combobox1.Layout.preferredWidth;
    		 	model:['object1','object2']
    		 } //combobox2 ends here
             
    		} //row layout ends here
    	}//groupbox ends here

    		RowLayout { //rowlayout
    			Layout.margins:10;
    			Layout.alignment:Qt.AlignRight;
    			Button {Material.background:Material.Blue;text:qsTr("&Done");}
    			Button {Material.background:Material.Blue;text:qsTr("&Cancel"); onClicked:parentW.close();}
    		} //row layout ends here

    	} //columnlayout ends here --main layout
    
}