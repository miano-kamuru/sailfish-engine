/*
Author:miano
Project:sailFish engine
IntegerProperty_Skeleton -component file for creating integer property
*/

import QtQuick 2.6
import QtQuick.Controls 2.6
import QtQuick.Layouts 1.12
import QtQuick.Controls.Material 2.6

ApplicationWindow { 
	title:"Create an Integer property";
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
         model:['object 1','object 2','object 3']
     } //end object display combobox

    TextField { //property name text field
    	 Layout.preferredWidth:parentW.width-20
         placeholderText:qsTr('property name'); 
         font.pointSize:14
    } //end property textfield
    

    TextField { //property name text field
         Layout.preferredWidth:parentW.width-20
         placeholderText:qsTr('maximum integer (optional)'); 
         font.pointSize:14
    } //end property textfield

    TextField { //property name text field
         Layout.preferredWidth:parentW.width-20
         placeholderText:qsTr('minimum integer (optional)'); 
         font.pointSize:14
    } //end property textfield




    

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