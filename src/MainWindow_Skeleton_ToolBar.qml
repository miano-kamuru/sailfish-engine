
import QtQuick 2.6
import QtQuick.Controls 2.6
import QtQuick.Layouts 1.12
import QtQuick.Controls.Material 2.12

ToolBar {
	Rectangle {anchors.fill:parent; color:"#282828"} //background rect
	RowLayout{ //main toolbar layout
      spacing:10

      ToolButton { //new object toolbutton
       icon.source:"icons/folder_new.svg"
       icon.color:"transparent"
       text:"new object"
       onClicked:newObjectWindow.show();
      } //end new object toolbutton
      
       ToolButton { //rename object 
            icon.source:"icons/folder-activities.svg"
            icon.color:"transparent"
            text:qsTr("rename object")
            onClicked:manager.triggerObjectRename();
      } //end rename object
      
      ToolButton { //delete object 
      	icon.source:"icons/edittrash.svg"
      	icon.color:"transparent"
      	text:qsTr("delete object")
      	onClicked:manager.triggerObjectDelete()
      } //end delete object

        ToolButton { //visualize object 
        icon.color:"#00c7b5"
        icon.source:"icons/ic_important_devices_24px"
        text:qsTr("visualize object")
        onClicked:manager.triggerVisualizeEntity()
      } //end visualize object


       ToolSeparator{}

       ToolButton {  //create new string
            icon.source:"icons/ic_note_add_24px.svg"
            icon.color:"#00c7b5"
            text:qsTr("String")
            onClicked:manager.triggerNewStringProperty()
      } //end create string

      ToolButton {  //create new Boolean
            icon.source:"icons/ic_note_add_24px.svg"
            icon.color:"#00c7b5"
            text:qsTr("Boolean")
            onClicked:manager.triggerNewBooleanProperty()
      } //end create string
      
       ToolButton {  //create new Integer
            icon.source:"icons/ic_note_add_24px.svg"
            icon.color:"#00c7b5"
            text:qsTr("Integer")
            onClicked:manager.triggerNewIntegerProperty()
      } //end create integer
      
      ToolButton {  //create new Float
            icon.source:"icons/ic_note_add_24px.svg"
            icon.color:"#00c7b5"
            text:qsTr("Float")
            onClicked:manager.triggerNewFloatProperty()
      } //end create float

      ToolSeparator{} 
      //edit operations for attributes

         ToolButton { //delete Attribute
            icon.source:"icons/node-delete-segment.svg"
            icon.color:"#FFAB91";
            text:qsTr("delete property")
            onClicked:manager.triggerAtrributeDelete(propertiesView.currentRow);
      } //end delete attribute

      ToolButton { //rename Attribute
            icon.source:"icons/ic_description_24px.svg"
            icon.color:"#FFAB91";
            text:qsTr("rename property")
            onClicked:manager.triggerAtrributeRename(propertiesView.currentRow);
      } //end delete attribute

//end edit operation for attributes
      ToolSeparator{} 
      ToolButton { //relationship view
            icon.source:"icons/ic_dns_24px.svg"
            icon.color:"#00c7b5"
            text:qsTr("node view")
            onClicked:manager.triggerRelationshipView()
      } //relationship view

	} //end toolbar column layout
}