import QtQuick 2.6
import QtQuick.Controls 2.6
import QtQuick.Layouts 1.12
import QtQuick.Controls.Material 2.6

ApplicationWindow {
  Material.theme: Material.Light
	id:parentW;
  flags:Qt.Dialog;
  modality:Qt.WindowModal;
	visible:false
    width:mainLayout.width+40
    height:mainLayout.height+40
    maximumWidth:mainLayout.width+40
    maximumHeight:mainLayout.height+40
    title:"Delete Object"

    
    GroupBox { //main Groupbox
    	anchors.fill:parent;
    	anchors.margins:10;

    	ColumnLayout { //main Column Layout
    		id:mainLayout
    		spacing:0

          ComboBox { //this combobox displays objects
          	displayText:"--Object--"+" "+currentText;
          	model:['object 1','object 2','object 3']; //model
          	Layout.preferredWidth:300;
          } //combobox ends here

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