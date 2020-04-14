/*
Author:miano
Project:sailFish engine
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
	visible:true
    width:mainLayout.width+40
    height:mainLayout.height+40
    maximumWidth:mainLayout.width+40
    maximumHeight:mainLayout.height+40
    title:"Error"
    
    GroupBox { //main Groupbox
    	anchors.fill:parent;
    	anchors.margins:10;

    	ColumnLayout { //main Column Layout
    		id:mainLayout
    		spacing:30

          Button { //button error
            Material.background:Material.Pink;
          	text:"! Select object to create relationship";
            font.pointSize:12
          } //text ends here

     
            Button { //button cancel
              Layout.alignment:Qt.AlignCenter;
            	Material.background:Material.Blue;
            	text:qsTr("&Cancel");
            	onClicked:parentW.destroy();
            } //button cancel ends here

    

    	} //Main Column layout ends here
    } //main groupbox ends here

} 