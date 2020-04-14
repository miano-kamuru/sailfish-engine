/*
Author:miano
Project:sailFish engine
NewObjectWindow_Skeleton -component file for NewObjectWindow
*/
ApplicationWindow {
      Material.theme : Material.Light
      id:parent_w1;
      title:"Create New Object";
      flags:Qt.Dialog;
      modality:Qt.WindowModal;
      width:450;
      height:250;
      minimumWidth:450;
      minimumHeight:250;
      maximumWidth:500;
      maximumHeight:250;
      visible:false;
     
      //layout
      GroupBox { //groupbox
            anchors.fill:parent;
            anchors.margins:10;
            ColumnLayout { //column layout 
                  anchors.fill:parent;
                  anchors.margins:10;

                  TextField { //textfield1 object name
                        id:textfield1;
                        Layout.alignment:Qt.AlignCenter;
                        Layout.preferredWidth:parent.width;
                        placeholderText:qsTr("Object name");
                        maximumLength:30;
                        focus:true
                  }//textfield 1 ends here

            
            TextField {//textfield 2
                  id:textfield2;
                  Layout.alignment:textfield1.Layout.alignment;
                  Layout.preferredWidth:textfield1.Layout.preferredWidth;
                  placeholderText:qsTr("Describe the object (optional)");
                  maximumLength:120;
            } //textfield 2 ends here

            RowLayout { //row layout for buttons
                        spacing:20;
                        Layout.alignment:Qt.AlignRight;

                        //create button starts here
                        Button {Material.background:Material.Blue;text:qsTr("create");
                  onClicked:{ //onClicked starts
                        var key="";
                        for(var check=0;check<entityList.length;check++){
                              if(entityList[check]==textfield1.text){
                                    key="entity present";
                                    break;
                              }
                        }
                        if(key=="" && key!="entity present"){
                              if(textfield1.text!=""){ //object name is not blank
                                  manager.addEntity(textfield1.text,textfield2.text); //submit to manager if everything is ok
                                  entityList.push(textfield1.text);
                                  createObjectNode(textfield1.text);
                                  textfield1.clear(); //clear textfield 1 
                                  textfield2.clear(); //clear textField 2
                                  parent_w1.close();

                        }//end if1
                 }
                 else {
                 if(key=="entity present") //if entity is present
                    manager.node_ObjectExistsError() //trigger object exists error
                 } //end else  
                   } //onClicked for create ends 
                  }//submit button ends here

                  //cancel button starts here
                  Button {Material.background:Material.Blue;text:qsTr("cancel"); 
                  onClicked:{
                        textfield1.clear(); //clear textfield 1 
                        textfield2.clear(); //clear textfield 2
                        parent_w1.close(); //close the window
                  } //onclicked ends here
                  } //button2 (cancel button) ends here
            }//row layout for button ends here
            } //column layout ends here
      } //groupbox ends here
}