/*
Author:miano
Project:sailFish engine
FloatProperty_Skeleton -component file for creating floating point property
*/

import QtQuick 2.6
import QtQuick.Controls 2.6
import QtQuick.Layouts 1.12
import QtQuick.Controls.Material 2.6

ApplicationWindow { 
	title:"Create a Floating point property";
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
         placeholderText:qsTr('property name e.g first name'); 
         font.pointSize:14
    } //end property textfield
    
    GroupBox { //interface settings groupbox
    	title:"Inteface settings"
        implicitWidth:parentW.width-20
        id:g1
     RowLayout{ //row layout
       ComboBox { //object display combobox
         Layout.preferredWidth:g1.width/1.4
         displayText:"Interface: "+currentText
         model:['textbox (default)','combobox','checkbox']
       } //end object display combobox
    
       Button { //property ui settings
          text:"settings"
       } //end property ui settings
     }//end row layout

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