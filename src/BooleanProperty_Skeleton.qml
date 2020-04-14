/*
Author:miano
Project:sailFish engine
BooleanProperty_Skeleton -component file for creating boolean property
*/

import QtQuick 2.6
import QtQuick.Controls 2.6
import QtQuick.Layouts 1.12
import QtQuick.Controls.Material 2.6

ApplicationWindow { 
	title:"Create a Boolean property";
	modality:Qt.WindowModal;
	flags:Qt.Dialog;
	visible:false;
    width:400;
    height:mainLayout.height+40;
    id:parentW

    ColumnLayout{ //main layout
    id:mainLayout
    anchors.horizontalCenter:parent.horizontalCenter

    ComboBox { //object display combobox
         Layout.preferredWidth:parentW.width-20
         displayText:"Object: "+currentText
         model:{0} //get all objects
     } //end object display combobox

    TextField { //property name text field
    	 Layout.preferredWidth:parentW.width-20
         placeholderText:qsTr('property name e.g first name'); 
         font.pointSize:14
    } //end property textfield
    
    GroupBox { //interface settings groupbox
    	title:"Inteface settings"
        Layout.preferredWidth:parentW.width-20
        id:g1
  
       ComboBox { //object display combobox
         width:parentW.width-40
         displayText:"Interface: "+currentText
         model:['combobox (default)','radiobox']
       } //end object display combobox
    

    } //end interface settings groupbox

    RowLayout { //submit and cancel button layout
    	Layout.alignment:Qt.AlignRight;

    	Button { //done button
    		Material.background:Material.Blue;
    		text:qsTr("Done");
    	} //end button

    	Button { //cancel button
    		Material.background:Material.Blue;
    		text:qsTr("Cancel");
    	} //end cancel button

    } //end submit and cancel button layout

    } //end main layout
} //end ApplicationWindow