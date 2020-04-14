
visualizeEntityDialog="""
import QtQuick 2.6
import QtQuick.Controls 2.6
import QtQuick.Layouts 1.12
import QtQuick.Controls.Material 2.6

ApplicationWindow {{
  Material.theme: Material.Light;
	id:parentW;
  flags:Qt.Dialog;
  modality:Qt.WindowModal;
	visible:true
    width:mainLayout.width+40
    height:mainLayout.height+40
    maximumWidth:mainLayout.width+40
    maximumHeight:mainLayout.height+40
    title:"visualize Object"

    
    GroupBox {{ //main Groupbox
    	anchors.fill:parent;
    	anchors.margins:10;

    	ColumnLayout {{ //main Column Layout
    		id:mainLayout
    		spacing:0

          ComboBox {{ //this combobox displays objects
                id:objectList
          	displayText:"Object:"+"  "+currentText;
          	model:{0}; //model
          	Layout.preferredWidth:300;
          	currentIndex:manager.currentEntitySelectedIndex==0 ? 0 : manager.currentEntitySelectedIndex;
          }} //combobox ends here

          RowLayout {{ //Button row layout
          	Layout.alignment:Qt.AlignRight;

            Button {{ //button visualize starts here
            	Material.background:Material.Blue;
            	text:qsTr("&Render");
            	onClicked:{{
            	parentW.destroy();
            	manager.visualizeSelectedObject(objectList.currentText)
            	}}
            }} //button visualize ends here

            Button {{ //button cancel
            	Material.background:Material.Blue;
            	text:qsTr("&Cancel");
            	onClicked:parentW.destroy();
            }} //button cancel ends here

          }} //Button Row Layout ends here

    	}} //Main Column layout ends here
    }} //main groupbox ends here

}} 
"""
#end visualizeEntitydialog
#------------------------------------------------------------------------------#
#delete a selected object or cancel dialog
deleteEntityDialog="""  
import QtQuick 2.6
import QtQuick.Controls 2.6
import QtQuick.Layouts 1.12
import QtQuick.Controls.Material 2.6

ApplicationWindow {{
  Material.theme: Material.Light;
	id:parentW;
  flags:Qt.Dialog;
  modality:Qt.WindowModal;
	visible:true
    width:mainLayout.width+40
    height:mainLayout.height+40
    maximumWidth:mainLayout.width+40
    maximumHeight:mainLayout.height+40
    title:"Delete Object"

    
    GroupBox {{ //main Groupbox
    	anchors.fill:parent;
    	anchors.margins:10;

    	ColumnLayout {{ //main Column Layout
    		id:mainLayout
    		spacing:0

          ComboBox {{ //this combobox displays objects
                id:objectList
          	displayText:"Object:"+"  "+currentText;
          	model:{0}; //model
          	Layout.preferredWidth:300;
          	currentIndex:manager.currentEntitySelectedIndex==0 ? 0 : manager.currentEntitySelectedIndex;
          }} //combobox ends here

          RowLayout {{ //Button row layout
          	Layout.alignment:Qt.AlignRight;

            Button {{ //button delete starts here
            	Material.background:Material.Blue;
            	text:qsTr("&Delete");
            	onClicked:{{
            	parentW.destroy();
            	manager.deleteSelectedObject(objectList.currentText)
            	}}
            }} //button Delete ends here

            Button {{ //button cancel
            	Material.background:Material.Blue;
            	text:qsTr("&Cancel");
            	onClicked:parentW.destroy();
            }} //button cancel ends here

          }} //Button Row Layout ends here

    	}} //Main Column layout ends here
    }} //main groupbox ends here

}} 
"""
#-----------------------------------------------------------------------------#
#rename object dialog
renameEntityDialog="""
import QtQuick 2.6
import QtQuick.Controls 2.6
import QtQuick.Layouts 1.12
import QtQuick.Controls.Material 2.6

ApplicationWindow {{
  Material.theme: Material.Light;
	id:parentW;
  flags:Qt.Dialog;
  modality:Qt.WindowModal;
	visible:true
    width:mainLayout.width+40
    height:mainLayout.height+40
    maximumWidth:mainLayout.width+40
    maximumHeight:mainLayout.height+40
    title:"Rename Object"

    
    GroupBox {{ //main Groupbox
    	anchors.fill:parent;
    	anchors.margins:10;

    	ColumnLayout {{ //main Column Layout
    		id:mainLayout
    		spacing:0

          ComboBox {{ //this combobox displays objects
                id:objectList
          	displayText:"Object:"+"  "+currentText;
          	model:{0}; //model
          	Layout.preferredWidth:300;
          	currentIndex:manager.currentEntitySelectedIndex==0 ? 0 : manager.currentEntitySelectedIndex;
          }} //combobox ends here

          TextField {{ //start rename field--enter new name for object here
            id:renameField;
            placeholderText:"rename"
            Layout.preferredWidth:objectList.Layout.preferredWidth;
          }}//end rename field

          RowLayout {{ //Button row layout
          	Layout.alignment:Qt.AlignRight;

            Button {{ //button delete starts here
            	Material.background:Material.Blue;
            	text:qsTr("&Rename");
            	onClicked:{{
            	if(renameField.length>0){{
            	 manager.renameSelectedObject(objectList.currentText,renameField.text)
            	 parentW.destroy();
            	 }}//end if 1
            	else parentW.destroy();
            	}}
            }} //button Delete ends here

            Button {{ //button cancel
            	Material.background:Material.Blue;
            	text:qsTr("&Cancel");
            	onClicked:parentW.destroy();
            }} //button cancel ends here

          }} //Button Row Layout ends here

    	}} //Main Column layout ends here
    }} //main groupbox ends here

}} //end main window for renameDialog

"""
#-----------------------------------------------------------------------------#
#rename property
renamePropertyDialog="""
import QtQuick 2.6
import QtQuick.Controls 2.6
import QtQuick.Layouts 1.12
import QtQuick.Controls.Material 2.6

ApplicationWindow {{
  property string attributeName:"{0}";
  property int row:{1}
  Material.theme: Material.Light;
	id:parentW;
  flags:Qt.Dialog;
  modality:Qt.WindowModal;
	visible:true
    width:mainLayout.width+40
    height:mainLayout.height+40
    maximumWidth:mainLayout.width+40
    maximumHeight:mainLayout.height+40
    title:"Rename Property {0}"

    
    GroupBox {{ //main Groupbox
    	anchors.fill:parent;
    	anchors.margins:10;

    	ColumnLayout {{ //main Column Layout
    		id:mainLayout
    		spacing:0

          TextField {{ //start rename field--enter new name for object here
            id:renameField;
            placeholderText:"rename"
            Layout.preferredWidth:300;
          }}//end rename field

          RowLayout {{ //Button row layout
          	Layout.alignment:Qt.AlignRight;

            Button {{ //button delete starts here
            	Material.background:Material.Blue;
            	text:qsTr("&Rename");
            	onClicked:{{
            	if(renameField.text.length>0){{
            	 manager.renameSelectedAttribute(row,attributeName,renameField.text)
            	 parentW.destroy();
            	 }}//end if 1
            	else parentW.destroy();
            	}}
            }} //button Delete ends here

            Button {{ //button cancel
            	Material.background:Material.Blue;
            	text:qsTr("&Cancel");
            	onClicked:parentW.destroy();
            }} //button cancel ends here

          }} //Button Row Layout ends here

    	}} //Main Column layout ends here
    }} //main groupbox ends here

}} //end main window for renameDialog

"""
#end rename property
#-----------------------------------------------------------------------------#

#create new String atribute window
new_stringPropertyDialog="""
/*
Author:miano
Project:sailFish engine
StringProperty_Skeleton -component file for creating string property
*/

import QtQuick 2.6
import QtQuick.Controls 2.6
import QtQuick.Layouts 1.12
import QtQuick.Controls.Material 2.6

ApplicationWindow {{
    property var counterList:[];
    title:"Create a string property";
    modality:Qt.WindowModal;
    flags:Qt.Dialog;
    visible:true;
    width:400;
    height:mainLayout.height+40;
    id:parentW

    ColumnLayout{{ //main layout
    id:mainLayout
    anchors.horizontalCenter:parent.horizontalCenter

    ComboBox {{ //object display combobox
         id:objectComboBox;
         Layout.preferredWidth:parentW.width-20
         displayText:"Object: "+currentText
         model:{0} //get all objects
         currentIndex:manager.currentEntitySelectedIndex==0 ? 0 : manager.currentEntitySelectedIndex;
     }} //end object display combobox

    TextField {{ //property name text field
         id:propertyNameInput;
         Layout.preferredWidth:parentW.width-20
         placeholderText:qsTr('property name e.g first name'); 
         font.pointSize:14
         maximumLength :30
         focus:true
    }} //end property textfield

    TextField {{ //property name text field
         id:propertyDescriptionInput;
         Layout.preferredWidth:parentW.width-20
         placeholderText:qsTr('Description...'); 
         font.pointSize:14
    }} //end property textfield
    
    GroupBox {{ //interface settings groupbox
        title:"Inteface settings"
        implicitWidth:parentW.width-20
        id:g1
     RowLayout{{ //row layout
       ComboBox {{ //object display combobox
         id:interfaceTypeCombobox;
         Layout.preferredWidth:g1.width/1.4
         displayText:"Interface: "+currentText
         model:['textbox (default)','combobox','checkbox']
       }} //end object display combobox
    
       Button {{ //property ui settings
          text:"settings"
          visible:interfaceTypeCombobox.currentText!="textbox (default)" ? true : false;
          onClicked:labelWin.show();
       }} //end property ui settings
     }}//end row layout

    }} //end interface settings groupbox

    RowLayout {{ //submit and cancel button layout
        Layout.alignment:Qt.AlignRight;

        Button {{ //done button
            Material.background:Material.Blue;
            text:qsTr("Done");
            onClicked:{{
            submit();
            if(propertyDescriptionInput.text.length==0) propertyDescriptionInput.text=""
            if(propertyNameInput.text.length>0){{
              manager.addEntityAttribute_String(objectComboBox.currentText,propertyNameInput.text,propertyDescriptionInput.text,interfaceTypeCombobox.currentText,counterList);
              parentW.destroy();
              }}
            else manager.triggerPropertyNameErrorDialog();
            }}
        }} //end button

        Button {{ //cancel button
            Material.background:Material.Blue;
            text:qsTr("Cancel");
            onClicked:parentW.destroy()
        }} //end cancel button

    }} //end submit and cancel button layout

    }} //end main layout

    function submit(){{ //invoked when user is done creating property/attribute
     if(interfaceTypeCombobox.currentText=='textbox (default)') counterList=[]; //set counterList to empty if textbox option is selected
     if(interfaceTypeCombobox.currentText!='textbox (default)' && counterList.length==0) interfaceTypeCombobox.currentIndex=0;
    }}

    //child window labels
    
ApplicationWindow {{
	Material.theme : Material.Light
	id:labelWin;
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
    
    ColumnLayout{{ //main layout for Label Window
    id:mainLayout2
    //anchors.horizontalCenter:labelWin.horizontalCenter
    anchors.fill:parent
    anchors.margins:10
RowLayout{{
	id:row1
    TextField {{ //property name text field
    	 id:labelInput
    	 Layout.preferredWidth:mainLayout.width-10-addButton.width
         placeholderText:qsTr('label name'); 
         font.pointSize:14 
         maximumLength:30 
    }} //end property textfield

    Button {{ //add button
    	    id:addButton
    		Material.background:Material.Blue;
    		text:qsTr("Add");
    		onClicked:addLabel();
    	}} //end add button


  }}//end row layout 1

  ListModel{{id:labelModel}}

  ScrollView {{ //listView GroupBox
  	Layout.preferredWidth:row1.width;
  	Layout.preferredHeight:((parent.height-row1.height)-40)-doneButton.height
   ListView {{ //labels listview
   	width:parent.width;
   	model:labelModel; 
   	delegate:RowLayout{{
   		width:parent.width
   		RadioButton{{text:name}}
   		Button {{text:"delete";Layout.alignment:Qt.AlignRight; 
   		onClicked:deleteLabel(name)}}
   	}}//end delegate for list view
   }} //and list view
  }}//end listview scrollview
  RowLayout{{ //row layout for cancel and done buttons
  	id:rFinal;
  	Layout.alignment:Qt.AlignCenter;
  Button {{
  	id:doneButton;text:qsTr("&Done");
  	onClicked:labelWin.close();
  }}
  Button {{
  	id:cancelButton;text:qsTr("&Cancel");
  	onClicked:{{labelWin.close();}}
  }}
 }}//end rowLayout for cancel done and cancel buttons

}}//end main layout




}}//end child window label window

function addLabel(){{ //add a label
	if(counterList.indexOf(labelInput.text)==-1) //find if label exists
	{{
	 if(labelInput.length!=0){{
	 labelModel.append({{"name":labelInput.text}});
	 counterList.push(labelInput.text)
	 labelInput.clear()
    }}
 }}
 else labelInput.clear();
}} //end add a label function

function deleteLabel(label_name){{ //delete label
 var getIndex=counterList.indexOf(label_name);
 labelModel.remove(getIndex);
 var temp=[];
 for(var x=0;x<counterList.length;++x){{
 	if(counterList[x]==counterList[getIndex])
 		continue;
    temp.push(counterList[x])
 }}
 counterList=temp
}} //end delete label
}} //end ApplicationWindow 

"""
#--------------------------------------------------------------------#


#create a boolean property
new_booleanPropertyDialog="""
/*
Author:miano
Project:sailFish engine
BooleanProperty_Skeleton -component file for creating boolean property
*/

import QtQuick 2.6
import QtQuick.Controls 2.6
import QtQuick.Layouts 1.12
import QtQuick.Controls.Material 2.6

ApplicationWindow {{
	title:"Create a Boolean property";
	modality:Qt.WindowModal;
	flags:Qt.Dialog;
	visible:true;
    width:400;
    height:mainLayout.height+40;
    id:parentW

    ColumnLayout{{ //main layout
    id:mainLayout
    anchors.horizontalCenter:parent.horizontalCenter

    ComboBox {{ //object display combobox
         id:objectComboBox
         Layout.preferredWidth:parentW.width-20
         displayText:"Object: "+currentText
         model:{0} //get all objects
        currentIndex:manager.currentEntitySelectedIndex==0 ? 0 : manager.currentEntitySelectedIndex; //set index according to selection

     }} //end object display combobox

    TextField {{ //property name text field
         id:propertyNameInput;
    	 Layout.preferredWidth:parentW.width-20
         placeholderText:qsTr('property name e.g first name'); 
         font.pointSize:14
         maximumLength:30
         focus:true
    }} //end property textfield

    TextField {{ //property name text field
         id:propertyDescriptionInput;
         Layout.preferredWidth:parentW.width-20
         placeholderText:qsTr('Description...(optional)'); 
         font.pointSize:14
    }} //end property textfield
    
    GroupBox {{ //interface settings groupbox
    	title:"Inteface settings"
        Layout.preferredWidth:parentW.width-20
        id:g1
  
       ComboBox {{ //object display combobox
         id:interfaceTypeCombobox;
         width:parentW.width-40
         displayText:"Interface: "+currentText
         model:['combobox (default)','radiobox']
       }} //end object display combobox
    

    }} //end interface settings groupbox

    RowLayout {{ //submit and cancel button layout
    	Layout.alignment:Qt.AlignRight;

    	Button {{ //done button
    		Material.background:Material.Blue;
    		text:qsTr("Done");
    		onClicked:{{
                if(propertyDescriptionInput.text.length==0) propertyDescriptionInput.text="" //end if 1
                if(propertyNameInput.text.length>0){{
                  manager.addEntityAttribute_Boolean(objectComboBox.currentText,propertyNameInput.text,propertyDescriptionInput.text,interfaceTypeCombobox.currentText);
                  parentW.destroy();
                }}
               else manager.triggerPropertyNameErrorDialog();
            }}//end onClicked
    	}} //end button

    	Button {{ //cancel button
    		Material.background:Material.Blue;
    		text:qsTr("Cancel");
    		onClicked:parentW.destroy();
    	}} //end cancel button

    }} //end submit and cancel button layout

    }} //end main layout
}} //end ApplicationWindow
"""
#end create new boolean property
#---------------------------------------------------------------------------------#
#create new Integer property window
new_integerPropertyDialog="""
/*
Author:miano
Project:sailFish engine
IntegerProperty_Skeleton -component file for creating integer property
*/

import QtQuick 2.6
import QtQuick.Controls 2.6
import QtQuick.Layouts 1.12
import QtQuick.Controls.Material 2.6

ApplicationWindow {{
    property var counterList:[];
	title:"Create an Integer property";
	modality:Qt.WindowModal;
	flags:Qt.Dialog;
	visible:show;
    width:400;
    height:mainLayout.height+40;
    id:parentW

    ColumnLayout{{ //main layout

    id:mainLayout
    anchors.horizontalCenter:parent.horizontalCenter

   
    ComboBox {{ //object display combobox
         id:objectComboBox;
         Layout.preferredWidth:parentW.width-20
         displayText:"Object: "+currentText
         model:{0} //get all objects
         currentIndex:manager.currentEntitySelectedIndex==0 ? 0 : manager.currentEntitySelectedIndex;
     }} //end object display combobox

    TextField {{ //property name text field
         id:propertyNameInput;
         Layout.preferredWidth:parentW.width-20
         placeholderText:qsTr('property name'); 
         font.pointSize:14
         maximumLength:30
         focus:true
    }} //end property textfield
    

    TextField {{ //property minimum int
         id:minimumInt
         Layout.preferredWidth:parentW.width-20
         placeholderText:qsTr('maximum integer (optional)'); 
         font.pointSize:14
    }} //end minimum int textfield

    TextField {{ //property maximum int
         id:maximumInt
         Layout.preferredWidth:parentW.width-20
         placeholderText:qsTr('minimum integer (optional)'); 
         font.pointSize:14
    }} //end minimum int textfield

    TextField {{ //property description field
         id:propertyDescriptionInput;
         Layout.preferredWidth:parentW.width-20
         placeholderText:qsTr('Description...'); 
         font.pointSize:14
    }} //end property description field
    

    RowLayout {{ //submit and cancel button layout
    	Layout.alignment:Qt.AlignRight;

    	Button {{ //done button
    		Material.background:Material.Blue;
    		text:qsTr("Done");
            onClicked:{{
                if(propertyDescriptionInput.text.length==0) propertyDescriptionInput.text="";
                if(propertyNameInput.text.length>0){{
                      manager.addEntityAttribute_Integer(objectComboBox.currentText,propertyNameInput.text,propertyDescriptionInput.text,minimumInt.text,maximumInt.text);
                      parentW.destroy();
                }} //end if 2
                else manager.triggerPropertyNameErrorDialog();
              
            }} //end onclicked
    	}} //end button

    	Button {{ //cancel button
    		Material.background:Material.Blue;
    		text:qsTr("Cancel");
            onClicked:parentW.destroy()
    	}} //end cancel button

    }} //end submit and cancel button layout

    }} //end main layout
}} //end ApplicationWindow
"""
#end new Integer property window
#--------------------------------------------------------------------------------------#
#create new Float property window
new_floatPropertyDialog="""
/*
Author:miano
Project:sailFish engine
IntegerProperty_Skeleton -component file for creating integer property
*/

import QtQuick 2.6
import QtQuick.Controls 2.6
import QtQuick.Layouts 1.12
import QtQuick.Controls.Material 2.6

ApplicationWindow {{
    property var counterList:[];
	title:"Create an Float property";
	modality:Qt.WindowModal;
	flags:Qt.Dialog;
	visible:show;
    width:400;
    height:mainLayout.height+40;
    id:parentW

    ColumnLayout{{ //main layout

    id:mainLayout
    anchors.horizontalCenter:parent.horizontalCenter

   
    ComboBox {{ //object display combobox
         id:objectComboBox;
         Layout.preferredWidth:parentW.width-20
         displayText:"Object: "+currentText
         model:{0} //get all objects
         currentIndex:manager.currentEntitySelectedIndex==0 ? 0 : manager.currentEntitySelectedIndex;
     }} //end object display combobox

    TextField {{ //property name text field
         id:propertyNameInput;
         Layout.preferredWidth:parentW.width-20
         placeholderText:qsTr('property name'); 
         font.pointSize:14
         maximumLength:30
         focus:true
    }} //end property textfield
    

    TextField {{ //property minimum int
         id:minimumF
         Layout.preferredWidth:parentW.width-20
         placeholderText:qsTr('maximum float (optional)'); 
         font.pointSize:14
    }} //end minimum int textfield

    TextField {{ //property maximum int
         id:maximumF
         Layout.preferredWidth:parentW.width-20
         placeholderText:qsTr('minimum float (optional)'); 
         font.pointSize:14
    }} //end minimum int textfield

    TextField {{ //property description field
         id:propertyDescriptionInput;
         Layout.preferredWidth:parentW.width-20
         placeholderText:qsTr('Description...'); 
         font.pointSize:14
    }} //end property description field
    

    RowLayout {{ //submit and cancel button layout
    	Layout.alignment:Qt.AlignRight;

    	Button {{ //done button
    		Material.background:Material.Blue;
    		text:qsTr("Done");
            onClicked:{{
                if(propertyDescriptionInput.text.length==0) propertyDescriptionInput.text="";
                if(propertyNameInput.text.length>0){{
                      manager.addEntityAttribute_Float(objectComboBox.currentText,propertyNameInput.text,propertyDescriptionInput.text,minimumF.text,maximumF.text);
                      parentW.destroy();
                }} //end if 2
                else manager.triggerPropertyNameErrorDialog();
              
            }} //end onclicked
    	}} //end button

    	Button {{ //cancel button
    		Material.background:Material.Blue;
    		text:qsTr("Cancel");
            onClicked:parentW.destroy()
    	}} //end cancel button

    }} //end submit and cancel button layout

    }} //end main layout
}} //end ApplicationWindow
"""
#end new float property dialog
#------------------------------------------------------------------------------#
oneToOneDialog="""
/*
Author:miano
Project:sailFish engine
MainWindow_Skeleton_menuBarSkeleton -component file for Relationship_OneToOneWindow activated by relationship
/one to one
*/

import QtQuick 2.6
import QtQuick.Controls 2.6
import QtQuick.Layouts 1.12
import QtQuick.Controls.Material 2.6

ApplicationWindow {{
	Material.theme:Material.Light;
	id:parentW;
	visible:true;
	flags:Qt.Dialog;
	modality:Qt.WindowModal;
	title:qsTr("create a one to one relationship");
    width:mainLayout.width;
    height:mainLayout.height
    maximumWidth:mainLayout.width 
    maximumHeight:mainLayout.height;
    
    	//Layout
    	ColumnLayout {{ //COlumnlayout starts here --main layout
    		id:mainLayout
    		GroupBox{{ //group box
    			Layout.margins:10;
    		RowLayout {{ //row layout
    			spacing:20;

    			Text {{ //text1
    			id:text1
    			text:qsTr("One")
    			font.pointSize:14;
                color:"Grey";
    		 }} //text1 ends here

    		 Button {{ //object1Button
    		        Material.background:Material.Blue;
    		 	id:object1Button;
    		 	Layout.preferredWidth:250
    		 	text:"{0}"
    		 }} //object1Button ends here

    		 Text {{ //text2
    		 	id:text2;
    		 	text:qsTr("To One");
    		 	font.pointSize:text1.font.pointSize;
                color:"Grey";
    		 }} //text2 ends here

    		 ComboBox {{ //combobox 2
    		        id:combobox2
    		 	Layout.preferredWidth:object1Button.Layout.preferredWidth;
    		 	model:{1}
    		 }} //combobox2 ends here
             
    		}} //row layout ends here
    	}}//groupbox ends here

    		RowLayout {{ //rowlayout
    			Layout.margins:10;
    			Layout.alignment:Qt.AlignRight;
    			Button {{Material.background:Material.Blue;text:qsTr("&Done"); onClicked:{{
    			manager.createOneToOne(object1Button.text,combobox2.currentText);parentW.close();
    			 }}
    			}}
    			Button {{Material.background:Material.Blue;text:qsTr("&Cancel"); onClicked:parentW.close();}}
    		}} //row layout ends here

    	}} //columnlayout ends here --main layout
    
}}
"""
#end one to one dialog
#-----------------------------------------------------------------------------#
oneToManyDialog="""
/*
Author:miano
Project:sailFish engine
MainWindow_Skeleton_menuBarSkeleton -component file for Relationship_OneToOneWindow activated by relationship
/one to one
*/

import QtQuick 2.6
import QtQuick.Controls 2.6
import QtQuick.Layouts 1.12
import QtQuick.Controls.Material 2.6

ApplicationWindow {{
	Material.theme:Material.Light;
	id:parentW;
	visible:true;
	flags:Qt.Dialog;
	modality:Qt.WindowModal;
	title:qsTr("create a one to Many relationship");
    width:mainLayout.width;
    height:mainLayout.height
    maximumWidth:mainLayout.width 
    maximumHeight:mainLayout.height;
    
    	//Layout
    	ColumnLayout {{ //COlumnlayout starts here --main layout
    		id:mainLayout
    		GroupBox{{ //group box
    			Layout.margins:10;
    		RowLayout {{ //row layout
    			spacing:20;

    			Text {{ //text1
    			id:text1
    			text:qsTr("One")
    			font.pointSize:14;
                color:"Grey";
    		 }} //text1 ends here

    		 Button {{ //object1Button
    		        Material.background:Material.Blue;
    		 	id:object1Button;
    		 	Layout.preferredWidth:250
    		 	text:"{0}"
    		 }} //object1Button ends here

    		 Text {{ //text2
    		 	id:text2;
    		 	text:qsTr("To Many");
    		 	font.pointSize:text1.font.pointSize;
                color:"Grey";
    		 }} //text2 ends here

    		 ComboBox {{ //combobox 2
    		        id:combobox2
    		 	Layout.preferredWidth:object1Button.Layout.preferredWidth;
    		 	model:{1}
    		 }} //combobox2 ends here
             
    		}} //row layout ends here
    	}}//groupbox ends here

    		RowLayout {{ //rowlayout
    			Layout.margins:10;
    			Layout.alignment:Qt.AlignRight;
    			Button {{Material.background:Material.Blue;text:qsTr("&Done"); onClicked:{{
    			manager.createOneToMany(object1Button.text,combobox2.currentText);parentW.close();
    			 }}
    			}}
    			Button {{Material.background:Material.Blue;text:qsTr("&Cancel"); onClicked:parentW.close();}}
    		}} //row layout ends here

    	}} //columnlayout ends here --main layout
    
}}
"""
#end one to many dialog
#----------------------------------------------------------------------------------------------------------------------------#
