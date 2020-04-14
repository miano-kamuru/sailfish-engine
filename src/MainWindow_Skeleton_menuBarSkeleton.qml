/*
Author:miano
Project:sailFish engine
MainWindow_Skeleton_menuBarSkeleton -component file for MainWindow_Skeleton menu bar
*/

import QtQuick 2.6
import QtQuick.Controls 2.6
import QtQuick.Controls.Material 2.6

MenuBar {
   Material.theme: Material.Dark
   Menu { //File menu
   title:qsTr("&File");
   MenuItem{text:qsTr("&project manager");}
   MenuSeparator{}
   MenuItem{text:qsTr("&Save"); onTriggered:manager.save()} //save project
   MenuSeparator{}
   MenuItem{text:qsTr("&Exit"); onTriggered:Qt.quit()}
   }

   Menu { //Edit menu
   title:qsTr("&Edit");
   Action{text:qsTr("&Rollback");}
   MenuSeparator{}
   Menu { //edit menu for objects
      title:qsTr("&Object");
      Action{text:qsTr("&Delete Object"); onTriggered:manager.triggerObjectDelete();} //delete object Window
      Action{text:qsTr("&Rename Object"); onTriggered:manager.triggerObjectRename();} //rename object
   } //end edit menu for objects
   Action{text:qsTr("&Delete Relationship"); onTriggered:deleteRelationshipWindow.show();} //deleteRelationshipWindow
   Action{text:qsTr("&Delete Everything"); onTriggered:deleteEverythingWindow.show();} //deleteEverythingWindow
   }

   Menu { //Tools menu
   title:qsTr("Tools");
   MenuItem{text:qsTr("New &Object"); onTriggered:newObjectWindow.show();} //create new object
   Menu { //create object properties/attributes
      title:qsTr("&Object attributes");
      Action{text:qsTr("&String"); onTriggered:manager.triggerNewStringProperty();} //String 
      Action{text:qsTr("&Integer"); onTriggered:manager.triggerNewIntegerProperty()} //Integer
      Action{text:qsTr("&Boolean"); onTriggered:manager.triggerNewBooleanProperty()} //Boolean
      Action{text:qsTr("&Float"); onTriggered:manager.triggerNewFloatProperty()} //Float type
      Action{text:qsTr("&Expression Layers");} //expression layer type
   }
   MenuSeparator{}
   Menu { //create relationships
      title:qsTr("&Relationships");
      Action{text:qsTr("One To One"); onTriggered:manager.triggerOneToOne();} //one to one
      Action{text:qsTr("One To Many"); onTriggered:manager.triggerOneToMany();} //one to many
   }
   MenuSeparator{}
   MenuItem{text:qsTr("&Edit Project properties"); onTriggered:projectPropertiesWindow.show();} //edit project properties
   MenuItem{text:qsTr("&Project Ui preferences");}
   }
   
   Menu { //filters menu
      title:qsTr("Filters");
      Action{text:qsTr("&Simple &Filter");}
      Action{text:qsTr("&Selector");}
   }

   Menu { //View menu
      title:qsTr("View");
      Action{text:qsTr("&Node Graph"); onTriggered:manager.triggerRelationshipView()}
      Action{text:qsTr("&Summary");}
   }

   Menu { //Build menu
   title:qsTr("Build"); 
   MenuItem{text:qsTr("&Build Project");} //create new object
   MenuItem{text:qsTr("&Run Project");} //edit project properties
   MenuSeparator {}
   MenuItem{text:qsTr("Generate &Sql Only");}
   }


   Menu { //About menu
   title:qsTr("Help");
   MenuItem{text:qsTr("&Documentation");} //display documentation
   MenuSeparator{}
   MenuItem{text:qsTr("&About &sailFish"); onTriggered:aboutWindow.show();} //display about dialog
   }	

}
