#author:miano
#project sailfish engine

from Backend import *
import entity
import pickle
from jinja2 import Template
import nodeWindows

def create(name="",version="",developer="",description=""): #create a new project <!--PROJECT WILL BE PENDING-->
    new_project=Project(name=name,version=version,developer=developer,description=description) #create project instance
    session.add(new_project) #the project instance is pending
    session.commit()
    return new_project #return new project instance
    
def addEntity(name,description=""): #create a new entity (project id,name of object,description of object)
    project=session.query(Project).filter(Project.id==1).one() #the project id will always be 1
    if(not entity.getByName(name)): #check if entity exists 
     new=entity.create(name=name,description=description)
     session.add(new)
     project.entities.append(new) #add the entity to current project
    else:
        return "error" #return error is entity with the same name exists

def addEntityAttribute(id,name="",aType="",interface="",description="",labels=""): #add attribute to entity
     ent=session.query(Entity).filter(Entity.id==id).one()
     ent.attributes.append(Attribute(name=name,type=aType,interface=interface,labels=pickle.dumps(labels),description=description))
     session.add(ent)
     session.commit()
    
def getEntityAttributeCount(id): #get the number of attributes associated with entity --pass the id of entity
    return entity.attributeCount(id)
    
def getEntityCount(): #return the number of entities
    return entity.count()

def getEntityNames(): #return a list of entity names
    return entity.getNames()

def getEntityIdThroughName(name): #will return an entity id is exists
    if(entity.getByName(name)): #if entity exists
        object=session.query(Entity).filter(Entity.name==name).one()
        return object.id
    else:
        return "error"

def getEntityAttributes(id): #get attributes associates with an entity 
    return entity.getAttributes(id) #InstrumentedList -convert to list for use

def getAttributeIdThroughName(entityName,name): #return the id of attribute --pass the name of entity and attribute
    if(getEntityIdThroughName(entityName)!="error"):
        object_list=getEntityAttributes(getEntityIdThroughName(entityName))#get instrumented list of attributes
        for i in object_list:
            if(i.name==name):
                return i.id
        return "error" #attribute does not exist
    else:
        return "error" #entity does not exist
        

def getAttribute(id): #return the attribute object
    try:
     object=session.query(Attribute).filter(Attribute.id==id).one() #query for id
     return object #if id found return ATTRIBUTE OBJECT
    except sqlalchemy.orm.exc.NoResultFound: 
        return "error" #RETURN ERROR IF ID NOT FOUND

def getEntities(): #get all the entities associated with the project Entity Objects
    project=session.query(Project).filter(Project.id==1).one() #the project id will always be one
    return project.entities #return all the entities associated with the project

def getEntityById(id): #get one entity by id
    return entity.getById(id)
    
def relationshipExists(object1,object2): #check if relationship exists between two entities #ARGUMENTS ARE ENTITY IDs
    test1=session.query(Relationship).filter(and_(Relationship.object1==object1,Relationship.object2==object2)).first()
    test2=session.query(Relationship).filter(and_(Relationship.object1==object2,Relationship.object2==object1)).first()
    if(test1==None and test2==None):
        return False  #relationship does not exist
    else:
        return True #relationship exists

def addRelationship(typeOf,object1,object2): #create a new relationship note:entiy and object are the same thing , #ARGUMENTS ARE ENTITY IDs
    if(getEntityById(object1)!="error" and getEntityById(object2)!="error"): #both objects must be existing
         if(relationshipExists(object1,object2)): #will not create relationship if relationship with the same entity exists
             return "relationship exists" #will not create relationship if relationship with the same entity exists
         else:
             new=Relationship(type=typeOf,object1=object1,object2=object2) #create new relationship
             session.add(new)
             session.commit() #save automatically
    else:
        return "error" #if any or both entities do not exist return error
    
def getRelationships(): #return relationships
    objects=session.query(Relationship).all()
    return objects #return relationships as an instrumented list

def getEntitiesAndRelationships():
    objects=session.query(Relationship).all()
    for i in objects:
        return [getEntityById(i.object1).name,getEntityById(i.object2).name,i.type]

def entityInRelationship(id): #check if entity is in relationship --Return TRUE if entity has relationship False if entity has no relationship
    object=session.query(Relationship).filter(or_(Relationship.object1==id,Relationship.object2==id)).first()
    if(object):
        return True #entity has relationship
    else:
        return False #entity has no relationship

def deleteRelationship(id): #deletes relationship pass Relationship id
    try:
        object=session.query(Relationship).filter(Relationship.id==id).one()
        session.add(object) #add relationship to session
        session.delete(object) #delete relationship
        session.commit() #save
    except sqlalchemy.orm.exc.NoResultFound:
        return "error"     #return error if relationship does not exist

def relationshipEntityInstances(id): #get relationship instances associated with entity #PASS ENTITY ID AS ARGUMENT.
    if(entityInRelationship(id)): #if entity has relationship
        objects=session.query(Relationship).filter(or_(Relationship.object1==id,Relationship.object2==id)).all()
        return objects #return instrumented list of relationship objects
    else:
        return None #return none if entity is not in relationship
    
def save(): #commit the changes 
    session.commit() #persist the changes to the database

def rollback(): #rollback to last save
    session.rollback()
    
def getName(): #return the name of the project 
    project=session.query(Project).filter(Project.id==1).first()
    return project.name

def getVersion(): #return project version
    project=session.query(Project).filter(Project.id==1).first()
    return project.version

def getDeveloper(): #return name of developer
    project=session.query(Project).filter(Project.id==1).first()
    return project.developer

def getDescription(): #return description of project
    project=session.query(Project).filter(Project.id==1).first()
    return project.description

def getRecent(): #session.new -pending info
    pending=list(session.new)
    edited=list(session.dirty)
    all_={"pending":pending,"edited":edited}
    return all_

class EditProject(): #edit project after creating it- change name,version,developer,description
    def __init__(self):
        self.project=session.query(Project).filter(Project.id==1).one()
    def name(self,new): #change project name
        self.project.name=new
    def version(self,new):
        self.project.version=new
    def developer(self,new):
        self.project(developer=new)
    def description(self,new):
        self.project.description=new
        
class EditEntity(): #edit a pre-existing entity
    def __init__(self,id): #id is the id of the entity
        self.id=id
        self.entity=getEntityById(id)
    def name(self,new): #modify name
        if(self.entity!="error"):
          self.entity.name=new
          session.add(self.entity)
        else:
            print("error") #should invoke error window
    def description(self,new): #modify description
        if(self.entity!="error"):
         self.entity.description=new
         session.add(self.entity)
        else:
            print("error")
    def delete(self):
        save() #wont work without save
        #first delete associated relationship
        relationships=relationshipEntityInstances(self.id) #get relationships associated with entity
        if(relationships!=None):     #if relationships exist
            for item in relationships: 
                deleteRelationship(item.id) #delete each relationship
        session.delete(self.entity)
        save()

class EditAttribute(): #edit pre existing attribute pass id of attribute as arg
    def __init__(self,id): #id of the attribute
        self.id=id
        self.attribute=getAttribute(id)
    def name(self,new):
        if(self.attribute!="error"):
         self.attribute.name=new
        else:
            print("error")
    def type(self,new):
        self.attribute.type=new
    def interface(self,new): #should delete all labels associated with the previous interface after rename
        self.attribute.interface=new
    def description(self,new):
        self.attribute.description=new
    def delete(self): #delete attribute
        if(self.attribute!="error"):
          save()  #wont work without save
          session.delete(self.attribute)
    
        
def generateRelationshipView():
    view="""
import QtQuick 2.6
import QtQuick.Controls 2.6
import QtQuick.Layouts 1.12
import QtQuick.Controls.Material 2.12
import QtQuick.Window 2.12
ApplicationWindow {
    property var entityList:{{entityList}};
    property var newEntityList:[]
    width:Screen.desktopAvailableWidth/2;
    height:600
    title:"node view"
    modality:Qt.WindowModal;
    visible:true
    id:mainWindow

        Canvas { //start canvas
            anchors.fill:parent
            id:canvas;
            {%for item in entities%}

            Rectangle { //start entity rectangle
                id:e{{item.id}}
                width:180;
                height:nodeL{{item.id}}.height;
                radius:10;
                color:"#3d3d3d";
                x:parent.width/3
                y:{% if item.id!=1 and entities.index(item)!=0 %} (e{{entities[entities.index(item)-1].id}}.height+e{{entities[entities.index(item)-1].id}}.y)+20 {%else%} {{item.id*10}} {%endif%}
                ColumnLayout
                { //start main layout
                    id:nodeL{{item.id}}
                RowLayout{ //start row layout image+entity name
                Image {
                    source:"icons/document-open-recent.svg"
                }
                Text{
                    text:"{{item.name}}"
                    font.pointSize:12
                    color:"#dfdfdf"
                }
              } //end row layout image + entity name
              {%for a in item.attributes %}
              RowLayout{
                Button {
                    id:ic{{a.id}}
                    Layout.alignment:Qt.AlignLeft;
                    icon.source:"icons/ic_description_24px.svg"
                    icon.color:"#00c7b5"
                    flat:true;
                } //end button
                Rectangle {
                     implicitWidth:180-(ic{{a.id}}.width+10);
                     implicitHeight:ic{{a.id}}.height;
                     color:"transparent"
                Text {
                    width:parent.width
                    text:"{{a.name}}"
                    elide:Text.ElideRight
                    color:"white"
                    font.pointSize:12
                    anchors.verticalCenter:parent.verticalCenter
                }
            }
               } //row
              {%endfor%}
          } //end main layout
                MouseArea { 
                    anchors.fill:parent;
                    drag.target:parent
                    onPositionChanged:canvas.requestPaint()
                    onPressed:{parent.border.width=2;parent.border.color="#00c7b5";}
                    onReleased:{parent.border.color="transparent"}
                    onDoubleClicked:manager.visualizeSelectedObject("{{item.name}}")
                }
            } //end entity rectangle
            
            {%endfor%}

            {%for item in relationships%}
            Rectangle { //start relationship rectangle
                id:r{{item.id}}
                width:250;
                height:50;
                color:"#3d3d3d";
                radius:10;
                x:(parent.width/2)+width
                y:(height*{{item.id}})+{{item.id*10}}
                RowLayout{
                    spacing:20
                Button {
                    icon.source:"icons/node-join-segment.svg"
                    icon.color:"#00c7b5"
                    flat:true
                }
                Text{
                    text:"{{item.type}}" //type of relationship
                    font.pointSize:14;
                    color:"#00c7b5"
                }
            }
                MouseArea { 
                    anchors.fill:parent;
                    drag.target:parent;
                    onPositionChanged:canvas.requestPaint()
                    onPressed:{
                        parent.border.color="#00c7b5"; 
                        e{{item.object1}}.border.width=2;
                        e{{item.object1}}.border.color="#00c7b5";
                        e{{item.object2}}.border.width=2;
                        e{{item.object2}}.border.color="#00c7b5";
                    }
                    onReleased:{
                        parent.border.color="transparent"
                        e{{item.object1}}.border.color="transparent";
                        e{{item.object2}}.border.color="transparent";
                    }
                }
            } //end entity rectangle
            {%endfor%}
        onPaint:{painter();}
        }//end Canvas

        function painter(){
            var context=canvas.getContext('2d');
            context.fillStyle="#282828"
            context.fillRect(0,0,canvas.width,canvas.height);
            context.fillStyle="#282828"
            context.beginPath()
            {%for item in relationships%}
            context.moveTo(e{{item.object1}}.x+e{{item.object1}}.width,e{{item.object1}}.y)
            context.lineTo(r{{item.id}}.x,r{{item.id}}.y+10)

            context.moveTo(e{{item.object2}}.x+e{{item.object2}}.width,e{{item.object2}}.y)
            context.lineTo(r{{item.id}}.x,r{{item.id}}.y+40)
            context.strokeStyle="#00c7b5"
            context.stroke()
            {%endfor%}
        }
        {{newObjectWindow}}
        footer:ToolBar {//start footer toolbar
            Rectangle {anchors.fill:parent; color:"#3d3d3d"} //background rect
            RowLayout { //row layout for toolbar
                spacing:10;
                ToolButton { //new object toolbutton
                   icon.source:"icons/folder_new.svg"
                   icon.color:"transparent"
                   text:"new object"
                   onClicked:parent_w1.show();
                  } //end new object toolbutton  
            }
        }

        function createObjectNode(nodeName){
            var first_code=`
                import QtQuick 2.6
                import QtQuick.Controls 2.6
                import QtQuick.Layouts 1.12
                import QtQuick.Controls.Material 2.12
                import QtQuick.Window 2.12
                Rectangle { //start entity rectangle
                `
            var id="id:nodeObject_"+newEntityList.length
            var second_code=
            `
                width:180;
                height:50
                radius:10;
                color:"#3d3d3d";
                x:(parent.width/5)-width
                y:(newEntityList.length*60)
               
                ColumnLayout
                { //start main layout
                    
                RowLayout{ //start row layout image+entity name
                Image {
                    source:"icons/document-open-recent.svg"
                }
                Text{
                    text:entityList[entityList.length-1]
                    font.pointSize:12
                    color:"#dfdfdf"
                }
              } //end row layout image + entity name,
          }
          MouseArea { 
                    anchors.fill:parent;
                    drag.target:parent
                    onPositionChanged:canvas.requestPaint()
                    onPressed:{parent.border.width=2;parent.border.color="#00c7b5";}
                    onReleased:{parent.border.color="transparent"}
                }
      }`
      var qmlCode=first_code+id+second_code
    var dynamicObject = Qt.createQmlObject(qmlCode,mainWindow,'newNodeObject')
        }
}//end ApplicationWindow
"""
    template=Template(view)
    viewer=template.render(entities=getEntities(),relationships=getRelationships(),newObjectWindow=nodeWindows.new_objectDialog,entityList=getEntityNames())
    return viewer

def generateFakeForm(id):#the id is the id of the entity  #NO CHECKS FOR ID --MAKE SURE THAT Entity ID EXISTS
    entity=getEntityById(id)
    attributes=getEntityAttributes(id) #instrumented list of attributes
    bucket=[]
    for i in attributes:
        bucket.append({"name":i.name,"type":i.type,"interface":i.interface,"labels":pickle.loads(i.labels)})
    #template for the fake form
    form="""  
    /*
Author:miano
Project:sailFish engine
Fake Form template
*/

import QtQuick 2.6
import QtQuick.Controls 2.6
import QtQuick.Layouts 1.12
import QtQuick.Controls.Material 2.6
import QtQml.Models 2.12
import QtQuick.Controls 1.4 as PropertyTable
import QtQuick.Controls.Styles 1.4
import QtQuick.Window 2.12

ApplicationWindow  //This is the main window
{
id:mainWindow
title:"{{name}}"; //name of entity
visible:true
width:Screen.desktopAvailableWidth/2;
height:400;

PropertyTable.TableView { //tableView
 anchors.fill:parent
 id:propertyTable
 {%for item in bucket%}
 PropertyTable.TableViewColumn{
 //role:"{{item["name"]}}"
 title:"{{item["name"]}}"
 width:mainWindow.width/{{len(bucket)}}
 }
 {%endfor%}
}//end tableview

ApplicationWindow {
    title:"{{name}}"; {# name of the entity #}
    modality:Qt.WindowModal;
    flags:Qt.Dialog;
    visible:true;
    width:400;
    height:mainLayout.height+40;
    id:parentW

    ColumnLayout { //this is the main layout
    id:mainLayout
    anchors.horizontalCenter:parent.horizontalCenter

    {%for item in bucket%} {#list of attribute dicts#}

    {%if item['interface']=='textbox (default)'%}  {#start with the textbox type#}
    TextField {
    Layout.preferredWidth:parentW.width-20
    placeholderText:"{{item['name']}}"
    font.pixelSize:24
    }
    {%endif%} {#end textbox type#}

    {%if item['interface']=='combobox' and item['type']!='Boolean'%} {#display combobox with associated model#}
    ComboBox{
    Layout.preferredWidth:parentW.width-20
    displayText:"{{item['name']}}: "+currentText
    model:{{item['labels']}}
    }//end combobox
    {%endif%} {#end combobox display#}

    {%if item['interface']=='checkbox'%} {#display checkbox with associated labels#}
    GroupBox{
    title:"{{item['name']}}"
    Layout.preferredWidth:parentW.width-20
     ColumnLayout {
     {%for i in item['labels']%}
      CheckBox{
      text:"{{i}}"
      }
     {%endfor%}
     }//end columnlayout for groupbox
    }//end groupbox
    {%endif%} {#end checkbox display#}

    {%if item['type']=='Boolean' and item['interface']=='combobox (default)'%} {#boolean combobox display#}
    ComboBox{
    Layout.preferredWidth:parentW.width-20
    displayText:"{{item['name']}}: "+currentText
    model:{{item['labels']}} {#will display true and false#}
    }
    {%endif%} {#end boolean combobox display#}

    {%if item['type']=='Boolean' and item['interface']=='radiobox'%}
     GroupBox{
     title:"{{item['name']}}"
     Layout.preferredWidth:parentW.width-20
     ColumnLayout {
     {%for i in item['labels']%}
      RadioButton{
      text:"{{i}}"
      }
     {%endfor%}
     }//end columnlayout for groupbox
    }//end groupbox
    {%endif%}
     
    
    {%endfor%} {#end attribute iteration#}

     RowLayout { //Button row layout
            Layout.alignment:Qt.AlignRight;

            Button { //button 1
            	Material.background:Material.Blue;
            	text:qsTr("Add");
            	onClicked:{
            	//parentW.destroy();
            	mainWindow.destroy();
            	}
            } //button 1 ends here

            Button { //button cancel
            	Material.background:Material.Blue;
            	text:qsTr("&Cancel");
            	onClicked:{
            	//parentW.destroy();
            	mainWindow.destroy();}
            } //button cancel ends here

          } //Button Row Layout ends here
    
    } //end mainLayout
 }
}//end mainWindow
"""
    template=Template(form)
    output=template.render(name=entity.name,bucket=bucket,len=len)
    return output
    
   
    



    
