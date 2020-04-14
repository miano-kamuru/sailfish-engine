/*
Author:miano
Project:sailFish engine
ROneToManyWindow_Skeleton -component file for ROneToManyWindow_Skeleton activated by relationship
/one to many
*/

import QtQuick 2.6
import QtQuick.Controls 2.6
import QtQuick.Layouts 1.12
import QtQuick.Controls.Material 2.6

ApplicationWindow {
	Material.theme : Material.Light;
	id:parentW;
	visible:false;
	title:"create one to many relationship";
	flags:Qt.Dialog;
	modality:Qt.WindowModal;
    width:mainLayout.width;
    height:mainLayout.height
    maximumWidth:mainLayout.width 
    maximumHeight:mainLayout.height;

	//main layout
	ColumnLayout { //mainLayout
    id:mainLayout;

    GroupBox { //first groupbox
    	Layout.margins:10;

     RowLayout { //first row layout starts here
     	spacing:20;

      Text {text:qsTr("One"); id:text1; font.pointSize:14; color:"Grey";} //text

      ComboBox { //combobox starts here
      	Layout.preferredWidth:250;
      model:['object 1','object 2'];
      } //combobox ends here

      Text{text:qsTr('To Many'); font.pointSize:text1.font.pointSize; color:"Grey";} //text

      ComboBox { //combobox starts here
      	Layout.preferredWidth:250;
      model:['object 1','object 2'];
      } //combobox ends here

     } //first row layout ends here

    } //first groupbox ends here

    RowLayout { //second row layout starts here
    	Layout.margins:10;
    	Layout.alignment:Qt.AlignRight;

    Button{Material.background:Material.Blue;text:qsTr('&Done');} //button ends here
    Button{Material.background:Material.Blue;text:qsTr('&Cancel'); onClicked:parentW.close();} //button ends here

    } //second row layout ends here 

	} //column layout ends here --main layout
}