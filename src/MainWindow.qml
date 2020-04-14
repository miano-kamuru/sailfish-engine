/*
Author:miano
Project:sailFish engine
MainWindow -run this file
*/

import QtQuick 2.6
import QtQuick.Controls 2.6
import QtQuick.Controls.Material 2.6
import QtQuick.Controls 1.4 as PropertyTable
import QtQuick.Controls.Styles 1.4
import QtQuick.Window 2.12
import QtQml.Models 2.12
MainWindow_Skeleton { //import MainWindow_Skeleton
 id:mainWin
 Material.theme: Material.Dark
 Material.accent: Material.Purple

  ListModel { //object model --this model will be used to display object folders!
        id:objectModel //NOTE THAT THIS IS THE OBJECT MODEL ID
  }//end object model

  ListModel {
        id:propertiesModel;
}
  width:Screen.desktopAvailableWidth/2;
  minimumWidth:Screen.desktopAvailableWidth/2;

function delObjectDialog(arg){ //this dialog is invoked when user wants to delete object
   var newObject = Qt.createQmlObject(arg,mainWin,"deleteObject");
 } //end delete object dialog

function visualizeObjectDialog(arg){ //visualize object dialog 
  var newObject = Qt.createQmlObject(arg,mainWin,"visualizeObject");
} //end visualize object dialog

function renderObjectDialog(arg){ //visualize object dialog 
  var newObject = Qt.createQmlObject(arg,mainWin,"renderObject");
} //end visualize object dialog

function createRelationshipView(arg){ //visualize object dialog 
  var newObject = Qt.createQmlObject(arg,mainWin,"relationshipV");
} //end visualize object dialog

function noObjectExists(){ //this dialog is invoked if no object exists --Error msg
  var component = Qt.createComponent("NoObjectExistsDialog.qml");
   var diag = component.createObject(mainWin);
} //end noObjectExists

function objectNameError(){ //invoked if object exists --error msg
	  var component = Qt.createComponent("ObjectNameError.qml");
      var diag = component.createObject(mainWin);
}

function attributeNameError(){ //invoked if object exists --error msg
    var component = Qt.createComponent("AttributeNameError.qml");
      var diag = component.createObject(mainWin);
}

function selectObjectError(){ //invoked if object is not selected --error msg
    var component = Qt.createComponent("SelectObjectError.qml");
      var diag = component.createObject(mainWin);
}//end select object

function selectAttributeToRenameError(){ //invoked if attribute is not selected --error msg
    var component = Qt.createComponent("AttributeToRenameError.qml");
      var diag = component.createObject(mainWin);
}//end select attribute

function selectObjectErrorRename(){ //invoked if object is not selected for rename --error msg
    var component = Qt.createComponent("SelectObjectErrorRename.qml");
      var diag = component.createObject(mainWin);
}//end select object

function selectToCreateRelationshipErr(){ //invoked if object is not selected for new relationship --error msg
    var component = Qt.createComponent("selectToCreateRelationship.qml");
      var diag = component.createObject(mainWin);
}//end select object error

function notEnoughObjectsError(){ //invoked if object count is less than two
  var component = Qt.createComponent("notEnoughObjectsError.qml");
  var diag = component.createObject(mainWin);
} //end notEnoughObjectsError

function selectAttributeError(){ //invoked if Attribute is not selected --error msg
    var component = Qt.createComponent("SelectAttributeError.qml");
      var diag = component.createObject(mainWin);
}//end select attribute error

function propertyNameError(){ //invoked if property name is not entered --error msg
    var component = Qt.createComponent("PropertyNameError.qml");
      var diag = component.createObject(mainWin);
} //end property name error

function attributeExistsError(){ //invoked if attribute exists in object --error msg
   var component = Qt.createComponent("AttributeExistsError.qml");
    var diag = component.createObject(mainWin);
}

function relationshipExistsError(){
  var component = Qt.createComponent("RelationshipExistsError.qml");
    var diag = component.createObject(mainWin);
}
function addObjectModel(arg){ //append objectModel
	objectModel.append({'name':arg});
} //end append object model

function setObjectModel(arg){ //rename object
  objectModel.setProperty(arg[0],"name",arg[1]);
}//end setObjectModel

function setPropertiesModel(arg){ //rename object
  propertiesModel.setProperty(arg[0],"name",arg[1]);
}//end setObjectModel

function removeObjectItem(arg){ //remove item from objectModel 
	objectModel.remove(arg)
}

function newPropertyDialog(arg){ //this dialog is invoked when user wants to create property/attribute
   var newObject = Qt.createQmlObject(arg,mainWin,"newProperty");
 } //end delete object dialog

function renameObjectDialog(arg){ //this dialog is invoked when user wants to rename object
   var newObject = Qt.createQmlObject(arg,mainWin,"renameObject");
 } //end rename object dialog

function renamePropertyDialog(arg){ //this dialog is invoked when user wants to rename attribute
   var newObject = Qt.createQmlObject(arg,mainWin,"renameProperty");
 } //end rename object dialog

function oneToOneDialog(arg){ //this dialog is invoked when user wants to create one to one relationship
   var newObject = Qt.createQmlObject(arg,mainWin,"oneToOne");
 } //end one to one dialog

function oneToManyDialog(arg){ //one to many dialog creator
    var newObject = Qt.createQmlObject(arg,mainWin,"oneToMany");
} //end one to many dialog

function cleanPropertiesModel(){ //clears all the properties
  propertiesModel.clear();
}

function appendPropertiesModel(arg){ //add properties to table
    propertiesModel.append({"name":arg[0],"type":arg[1],"interfaceType":arg[2],"description":arg[3]});
}

function removePropertiesModel(arg){
  propertiesModel.remove(arg)
} //end removePropertiesModel

function getCurrentProperty(arg){
 if(arg!=-1) //if property selected
   return propertiesModel.get(arg).name
 else
  return "None"
} //end getCurrentPropert

}