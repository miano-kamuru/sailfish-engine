/*
Author:miano
Project:sailFish engine
About window -component file for AboutWindow
*/

import QtQuick 2.6
import QtQuick.Controls 2.6
import QtQuick.Layouts 1.12
import QtQuick.Controls.Material 2.6

ApplicationWindow {
	Material.theme: Material.Light
	title:"About sailFish";
	width:400;
	height:200;
	visible:false;
	flags:Qt.Dialog;
	modality:Qt.WindowModal;
    
    ColumnLayout { //column layout
	
	anchors.fill:parent;
	spacing:0;

	Rectangle {
		Layout.preferredWidth:300;
		Layout.preferredHeight:firstText.height+secondText.height;
		Layout.alignment:Qt.AlignCenter;
		color:"transparent";
		Text {
			id:firstText;
			text:qsTr("sailFish engine");
			font.pointSize:14;
			anchors.horizontalCenter:parent.horizontalCenter
		}

		Text {
			anchors.top:firstText.bottom;
			anchors.horizontalCenter:parent.horizontalCenter;
			id:secondText
			text:qsTr("version 1.0");
			font.pointSize:7;
		}
    } 
    
    Rectangle {
    	Layout.alignment:Qt.AlignCenter;
    	Layout.preferredWidth:300;
		Layout.preferredHeight:thirdText.height;
    	color:"transparent"
		Text {
			//anchors.top:secondText.bottom;
			//anchors.horizontalCenter:parent.horizontalCenter;
			id:thirdText;
			text:qsTr("Copyright 2019 miano kamuru");
			anchors.horizontalCenter:parent.horizontalCenter;
		}
	}
	

 } //column layout ends here
	
}
