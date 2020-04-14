/*
Author:miano
Project:sailFish engine
MainWindowSkeleton -this is a component file not main window
*/

import QtQuick 2.6
import QtQuick.Controls 2.6
import QtQuick.Controls.Material 2.6
import QtQuick.Layouts 1.12
import QtQml.Models 2.12
import QtQuick.Controls 1.4 as PropertyTable
import QtQuick.Controls.Styles 1.4

ApplicationWindow {

	title:manager.title
	visible:true;
	width:700;
	height:400;
    //static generation
    NewObjectWindow_Skeleton{id:newObjectWindow;} //new object window

    //relationships -dynamic generation
    Relationship_OneToOneWindow_Skeleton{id:relationship_OneToOneWindow;} //one to one relationship
    ROneToManyWindow_Skeleton{id:oneToManyWindow;} //one to many relationship
    ProjectPropertiesWindow_Skeleton{id:projectPropertiesWindow;} //project properties
    RManyToManyWindow_Skeleton{id:manyToManyWindow} //many to many relationship
    
    //delete -dynamic generation
    DeleteRelationshipWindow_Skeleton{id:deleteRelationshipWindow} //delete relationship
    DeleteEverythingWindow_Skeleton{id:deleteEverythingWindow} //delete everything
    
    //static generation
	AboutWindow_Skeleton{id:aboutWindow;} //about dialog
    
    //properties -dynamic generation
    StringProperty_Skeleton{id:stringPropertyWindow} //create a string property
    FloatProperty_Skeleton{id:floatPropertyWindow} //creating a float property 
    BooleanProperty_Skeleton{id:booleanPropertyWindow} //creating a bool property
    IntegerProperty_Skeleton{id:integerPropertyWindow} //creating an integer property

	menuBar:MainWindow_Skeleton_menuBarSkeleton{width:parent.width} //menubar component for main window 

    header:MainWindow_Skeleton_ToolBar{}



    background:Rectangle{ //background Rectangle N.B Use row layout for tableview and list view
        color:"#282828"
        width:parent.width;
        anchors.horizontalCenter:parent.horizontalCenter;
        

        ObjectView{id:objectView} //this view displays object folders;
        PropertiesView{id:propertiesView} //this view displays properties
        
    
} //end backgroundRectangle--------

footer:MenuBar{
Rectangle {anchors.fill:parent; color:"#282828"} //background 
 }//end footer
}