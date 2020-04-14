/*
Author:miano
Project:sailFish engine
DeleteRelationship_Skeleton -this is a component for DeleteRelationship Window
*/
import QtQuick 2.6
import QtQuick.Controls 2.6
import QtQuick.Layouts 1.12
import QtQuick.Controls.Material 2.6

ApplicationWindow {
	id:parentW;
  flags:Qt.Dialog;
  modality:Qt.WindowModal;
	Material.theme: Material.Light
	visible:false
    width:mainLayout.width+40
    height:mainLayout.height+40
    maximumWidth:mainLayout.width+40
    maximumHeight:mainLayout.height+40
    title:"Delete Everything"

    
    GroupBox { //main Groupbox
    	anchors.fill:parent;
    	anchors.margins:10;

    	ColumnLayout { //main Column Layout
    		id:mainLayout
    		spacing:30

          Text { //text
          	text:"Delete everything in this project ?";
            font.pointSize:12
          } //text ends here

          RowLayout { //Button row layout
          	Layout.alignment:Qt.AlignRight;

            Button { //button delete starts here
            	Material.background:Material.Blue;
            	text:qsTr("&Delete");
            } //button Delete ends here

            Button { //button cancel
            	Material.background:Material.Blue;
            	text:qsTr("&Cancel");
            	onClicked:parentW.close();
            } //button cancel ends here

          } //Button Row Layout ends here

    	} //Main Column layout ends here
    } //main groupbox ends here

} 