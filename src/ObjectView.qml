import QtQuick 2.6
import QtQuick.Controls 2.6
import QtQuick.Controls.Material 2.6

Rectangle {  //PARENT RECTANGLE TO OBJECT SCROLL VIEW
             color:"#282828"
             width:parent.width/5
             height:parent.height
             anchors.verticalCenter:parent.verticalCenter

             ScrollView { //scrollview for list model! -parent to list view
             id:scrollObj

             width:parent.width
             height:parent.height-190
             anchors.verticalCenter:parent.verticalCenter

  ListView { //ListView to display created objects
    model:objectModel //model
    anchors.fill:parent //parent is the scrollview ->scrollObj
    //Delegate for list view
    delegate:Button {
    Material.theme:Material.Dark
    width:parent.width-15
    text:name
    icon.source:"icons/document-open-recent.svg"
    icon.color:"transparent"
    icon.width:parent.width/5;
    icon.height:parent.width/5;
    display:Button.TextUnderIcon
    flat:true
    autoExclusive:true
    checkable:true
    id:control
    background: Rectangle { //will be used to highlight the currently selected object
        color:control.checked ? "black" : "transparent"
        opacity:0.2
    }
    onClicked:{
    manager.currentEntitySelected=String(text); 
    manager.triggerPropertyTableDisplay();
    } //update the currently selected object --onClickedEnds here
   } //end listview delegate
  } //object names listview
 } //end listview ScrollView
} //END PARENT RECTANGLE TO OBJECT SCROLL VIEW