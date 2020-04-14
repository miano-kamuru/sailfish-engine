/*
Author:miano
Project:sailFish engine
Project properties window -component file for ProjectProperties
*/

import QtQuick 2.6
import QtQuick.Controls 2.6
import QtQuick.Layouts 1.12
import QtQuick.Controls.Material 2.6

ApplicationWindow {
	Material.theme : Material.Light
	title:"Project properties";
	id:parentW
	flags:Qt.Dialog;
	modality:Qt.WindowModal;
	visible:false;
    width:mainLayout.width;
    height:mainLayout.height;
    minimumWidth:mainLayout.width 
    minimumHeight:mainLayout.height;
    maximumWidth:mainLayout.width;
    maximumHeight:mainLayout.height;

	//main layout
	ColumnLayout { //main column layout starts here
        id:mainLayout;

		GroupBox { //goupbox 1 starts here
			Layout.margins:10;
            ColumnLayout { //columnLayout 2 starts here
            	Layout.margins:10;
            	spacing:20;

			    RowLayout { //row layout1 starts here
				   spacing:10;
                   Text {text:qsTr("Project name");Layout.alignment:Qt.AlignLeft;}
                   TextField {Layout.preferredWidth:400;Layout.alignment:Qt.AlignRight;}
			    } //row layout1 ends here

			    RowLayout { //row layout2 starts here
			    	spacing:10;
			    	Text {text:qsTr("Version        ");}
			    	TextField {Layout.preferredWidth:400;}
			    } //row layout2 ends here
                
                RowLayout { //row layout3 starts here
			    	spacing:10;
			    	Text {text:qsTr("Developer     ");}
			    	TextField {Layout.preferredWidth:400;}
			    } //row layout2 ends here

			    RowLayout { //row layout4 starts here
			    	spacing:10;
			    	Text {text:qsTr("Description   ");}
			    	TextField {Layout.preferredWidth:400;}
			    } //row layout2 ends here
         
               RowLayout { //final rowlayout starts here --button layout
    	            Layout.margins:10;
    	            Layout.alignment:Qt.AlignRight;

                    Button{Material.background:Material.Blue;text:qsTr('&Done');} //done button ends here
                    Button{Material.background:Material.Blue;text:qsTr('&Cancel'); onClicked:parentW.close();} //cancel button ends here

              } //final rowlayout ends here --button layout

         } //column layout2 ends here

		} //groupbox 1 ends here

	} //main column layout ends here
}