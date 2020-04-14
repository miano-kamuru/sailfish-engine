from PyQt5.QtGui import *
from PyQt5.QtQml import *
from PyQt5.QtCore import *
from PyQt5.QtCore import QObject,pyqtSignal,pyqtSlot
import sys
import pickle
import project
import dialogs

if(project.project_file!=""):
 project.create(project.project_file)
else:
 project.create("")
 

class Manager(QObject):
    def __init__(self,object,parent=None):
        super().__init__(parent)
        self.object=object
        self._currentEntitySelected=None #store the name of the currently selected user object if none is selected return None
        self._currentEntitySelectedIndex=None #get the index of currently selected text in getEntityNames (to be used in combobox ONLY!)
        
        self._currentAttributeSelected=None #store the name of the currently selected attribute if none is selected return None
        
    @pyqtProperty(str)
    def title(self):      #set the title of window as project name
         return ("sailFish engine- {0}".format(project.getName()))
    
    @pyqtProperty(str)
    def currentEntitySelected(self):  #return currently selected entity
        return self._currentEntitySelected;
    
    @currentEntitySelected.setter
    def currentEntitySelected(self,selection): #setter of currently selected entity
        self._currentEntitySelected=selection

    @pyqtProperty(int)
    def currentEntitySelectedIndex(self):  #this fproperty holds the index of the currently selected entity/object by user which will be used in object dialog combobox 
        if(self._currentEntitySelected!=None): 
         self._currentEntitySelectedIndex=project.getEntityNames().index(self._currentEntitySelected) #get the index of currently selected entity in ui
         return self._currentEntitySelectedIndex;
        else:    #if no object/entity has been selected by user
            self._currentEntitySelectedIndex=0 #set the current object index to 0 (default)
            return self._currentEntitySelectedIndex; 
        
    @pyqtSlot()  #save the project
    def save(self):
        project.save()
        
    @pyqtSlot(str,str)
    def addEntity(self,name,description): #create a new entity/object
        if(project.getEntityIdThroughName(name)=="error"): #will return error if name does not exist
         project.addEntity(name=name,description=description)
         print(project.getEntities())
         msg=QVariant(name)
         QMetaObject.invokeMethod(self.object,"addObjectModel",Q_ARG(QVariant,msg)) #adds to the object model
         print(self._currentEntitySelected)
        else:
            QMetaObject.invokeMethod(self.object,"objectNameError") #if object name exists invoke objectNameError dialog

    @pyqtSlot() 
    def triggerObjectDelete(self): #this slot is called when user wants to delete object --INVOKE DIALOG
        if(project.getEntityCount()): #if object count > 0
          msg=QVariant(dialogs.deleteEntityDialog.format(project.getEntityNames()))  #pass entity names to delete objects dialog combobox
          QMetaObject.invokeMethod(self.object,"delObjectDialog",Q_ARG(QVariant,msg)) #invoke the delete window
        else:
            QMetaObject.invokeMethod(self.object,"noObjectExists") #invoke noObjectExists javascript function

    @pyqtSlot()
    def triggerObjectRename(self): #this slot is called when user wants to rename object 
        if(project.getEntityCount()): #if object count > 0
          msg=QVariant(dialogs.renameEntityDialog.format(project.getEntityNames()))  #pass entity names to rename objects dialog combobox
          QMetaObject.invokeMethod(self.object,"renameObjectDialog",Q_ARG(QVariant,msg)) #invoke the rename window
        else:
            QMetaObject.invokeMethod(self.object,"noObjectExists") #invoke noObjectExists javascript function
            
    @pyqtSlot(int)
    def triggerAtrributeDelete(self,row): #invoked when user wants to delete attribute
        if(project.getEntityCount()): #if object count > 0
            if(self._currentEntitySelected!=None):
                if(row==-1): #if no row is selected --Row is the currentRow in table view
                   QMetaObject.invokeMethod(self.object,"selectAttributeError") #invoked if no attribute is selected --Error
                else:
                    msg=QVariant(row) #pass properties view current row 
                    attributeName=QVariant()
                    attributeName=QMetaObject.invokeMethod(self.object,"getCurrentProperty", Q_RETURN_ARG(QVariant),Q_ARG(QVariant,msg))#get attribute name
                    attributeId=project.getAttributeIdThroughName(self._currentEntitySelected,attributeName)
                    edit=project.EditAttribute(attributeId)
                    edit.delete()
                    QMetaObject.invokeMethod(self.object,"removePropertiesModel",Q_ARG(QVariant,msg))
                   
            else:
              QMetaObject.invokeMethod(self.object,"selectObjectError")   #invoked if no object is selected
        else:
            QMetaObject.invokeMethod(self.object,"noObjectExists") #invoke noObjectExists javascript function

    @pyqtSlot(int)
    def triggerAtrributeRename(self,row): #invoked when user wants to rename attribute
        if(project.getEntityCount()): #if object count > 0
            if(self._currentEntitySelected!=None): #entity must be selected
                if(row==-1): #if no row is selected --Row is the currentRow in table view
                   QMetaObject.invokeMethod(self.object,"selectAttributeToRenameError") #invoked if no attribute is selected --Error
                else:
                     msg=QVariant(row) #pass properties view current row 
                     attributeName=QVariant()
                     attributeName=QMetaObject.invokeMethod(self.object,"getCurrentProperty", Q_RETURN_ARG(QVariant),Q_ARG(QVariant,msg))#get attribute name
                     msg=QVariant(dialogs.renamePropertyDialog.format(attributeName,row)) #pass entity names to rename objects dialog combobox
                     QMetaObject.invokeMethod(self.object,"renamePropertyDialog",Q_ARG(QVariant,msg)) #invoke the rename window
            else:
              QMetaObject.invokeMethod(self.object,"selectObjectErrorRename")   #invoked if no object is selected
        else:
            QMetaObject.invokeMethod(self.object,"noObjectExists") #invoke noObjectExists javascript function

                   
    @pyqtSlot(int,str,str)
    def renameSelectedAttribute(self,row,attributeName,newName): #handler for attribute rename 
        if(project.getAttributeIdThroughName(self._currentEntitySelected,newName)=='error'): #check if attribute exists
             attributeId=project.getAttributeIdThroughName(self._currentEntitySelected,attributeName)
             edit=project.EditAttribute(attributeId)
             edit.name(newName)
             arg1=QVariant(row);
             arg2=QVariant(newName)
             msg=QVariant([arg1,arg2])
             QMetaObject.invokeMethod(self.object,"setPropertiesModel",Q_ARG(QVariant,msg)) #---invoke JAVASCRIPT METHOD to update Model
        else:
            QMetaObject.invokeMethod(self.object,"attributeNameError")#invoked if attribute with that name exists
            
                     
        
            
    @pyqtSlot(str)
    def deleteSelectedObject(self,objectName): #delete the selected objects --HANDLE OBJECT DELETION
        if(project.getEntityIdThroughName(objectName)!="error"):
            if(self._currentEntitySelected==objectName):#if the currently selected object name==(Entity.name)
                QMetaObject.invokeMethod(self.object,"cleanPropertiesModel");
                self._currentEntitySelected=None         #set current entity selection to None
            msg=QVariant(project.getEntityNames().index(objectName)) #get index of entity using name
            QMetaObject.invokeMethod(self.object,"removeObjectItem",Q_ARG(QVariant,msg))#remove from listview
            project.EditEntity(project.getEntityIdThroughName(objectName)).delete() #delete object in database
            
    @pyqtSlot(str,str)
    def renameSelectedObject(self,objectName,newObjectName): #This function Renames an object ---HANDLE OBJECT RENAME
        if(newObjectName!=objectName):#if object name is not empty
           if(project.getEntityIdThroughName(objectName)!="error"):#if object exists
               if(project.getEntityIdThroughName(newObjectName)=="error"): #if object with a similiar name does not exist
                 obj=project.EditEntity(project.getEntityIdThroughName(objectName))
                 obj.name(newObjectName)
                                                          
                 index=project.getEntityNames().index(newObjectName)#get index 
                 arg1=QVariant(index);
                 arg2=QVariant(newObjectName)
                 msg=QVariant([arg1,arg2])
                 QMetaObject.invokeMethod(self.object,"setObjectModel",Q_ARG(QVariant,msg)) #---invoke JAVASCRIPT METHOD to update Model
                 
                 if(self._currentEntitySelected==objectName): #if current entity selected has the old object name
                     self._currentEntitySelected=newObjectName #update entity to new name
                     
               else: #if object with similar name exists
                 QMetaObject.invokeMethod(self.object,"objectNameError") #if object name exists invoke objectNameError dialog

                   
            
          
    @pyqtSlot()
    def triggerVisualizeEntity(self): 
        if(project.getEntityCount()): #if object count > 0
          msg=QVariant(dialogs.visualizeEntityDialog.format(project.getEntityNames()))  #pass entity names to delete objects dialog combobox
          QMetaObject.invokeMethod(self.object,"visualizeObjectDialog",Q_ARG(QVariant,msg)) #invoke the delete window
        else:
            QMetaObject.invokeMethod(self.object,"noObjectExists") #invoke noObjectExists javascript function

    @pyqtSlot(str)
    def visualizeSelectedObject(self,objectName):
        if(project.getEntityIdThroughName(objectName)!="error"): #if object exists
            if(project.getEntityAttributeCount(project.getEntityIdThroughName(objectName))>0): #at least one attribute is associated with entity
                msg=project.generateFakeForm(project.getEntityIdThroughName(objectName))
                QMetaObject.invokeMethod(self.object,"renderObjectDialog",Q_ARG(QVariant,msg))

             
    @pyqtSlot()
    def triggerNewStringProperty(self): #this function invokes the string property DIALOG
        if(project.getEntityCount()): #if object count > 0
          msg=QVariant(dialogs.new_stringPropertyDialog.format(project.getEntityNames()))  #pass entity names to new_stringPropertyDialog dialog combobox
          QMetaObject.invokeMethod(self.object,"newPropertyDialog",Q_ARG(QVariant,msg)) #invoke the newPropertyDialog function--Javascript function
        else:
            QMetaObject.invokeMethod(self.object,"noObjectExists") #invoke noObjectxists function --Javascript function

    @pyqtSlot()
    def triggerNewIntegerProperty(self): #this function invokes the integer property DIALOG
        if(project.getEntityCount()): #if object count > 0
          msg=QVariant(dialogs.new_integerPropertyDialog.format(project.getEntityNames()))  #pass entity names to new_stringPropertyDialog dialog combobox
          QMetaObject.invokeMethod(self.object,"newPropertyDialog",Q_ARG(QVariant,msg)) #invoke the newPropertyDialog function--Javascript function
        else:
            QMetaObject.invokeMethod(self.object,"noObjectExists") #invoke noObjectxists function --Javascript function
            
    @pyqtSlot()
    def triggerNewFloatProperty(self): #this function invokes the FLOAT property DIALOG
        if(project.getEntityCount()): #if object count > 0
          msg=QVariant(dialogs.new_floatPropertyDialog.format(project.getEntityNames()))  #pass entity names to new_stringPropertyDialog dialog combobox
          QMetaObject.invokeMethod(self.object,"newPropertyDialog",Q_ARG(QVariant,msg)) #invoke the newPropertyDialog function--Javascript function
        else:
            QMetaObject.invokeMethod(self.object,"noObjectExists") #invoke noObjectxists function --Javascript function

    @pyqtSlot()
    def triggerNewBooleanProperty(self): #invoke create BOOLEAN property DIALOG --invoke JAVASCRIPT FUNCTION
        if(project.getEntityCount()): #if object count > 0
            msg=QVariant(dialogs.new_booleanPropertyDialog.format(project.getEntityNames()))  #pass entity names to new_booleanPropertyDialog dialog combobox
            QMetaObject.invokeMethod(self.object,"newPropertyDialog",Q_ARG(QVariant,msg)) #invoke newPropertyDialog
        else:
            QMetaObject.invokeMethod(self.object,"noObjectExists") #invoke noObjectxists function --Javascript function

    @pyqtSlot(str,str,str,str)
    def addEntityAttribute_Boolean(self,objectName,property_name,property_description,property_interface): #add a boolean attribute
        if(project.getAttributeIdThroughName(objectName,property_name)=="error"): #attribute does not exist
            if(project.getEntityIdThroughName(objectName)!="error"): #if object exists
                objectId=project.getEntityIdThroughName(objectName) #get object id
                project.addEntityAttribute(id=objectId,name=property_name,aType="Boolean",interface=property_interface,description=property_description,labels=["true","false"])
                if(objectName==self._currentEntitySelected): #if the object is currently selected
                    object=project.getEntityById(objectId)
                    attrib=object.attributes[-1]
                    msg=QVariant([attrib.name,attrib.type,attrib.interface,str(attrib.description)])
                    QMetaObject.invokeMethod(self.object,"appendPropertiesModel",Q_ARG(QVariant,msg))
        


    @pyqtSlot(str,str,str,str,list)
    def addEntityAttribute_String(self,objectName,property_name,property_description,property_interface,plabels): #add a string attribute
        if(project.getAttributeIdThroughName(objectName,property_name)=="error"): #attribute does not exist
            if(project.getEntityIdThroughName(objectName)!="error"): #if object exists 
                objectId=project.getEntityIdThroughName(objectName) #get object id
                project.addEntityAttribute(id=objectId,name=property_name,aType="String",interface=property_interface,description=property_description,labels=plabels)
                if(objectName==self._currentEntitySelected): #if the object is currently selected
                    object=project.getEntityById(objectId)
                    attrib=object.attributes[-1]
                    msg=QVariant([attrib.name,attrib.type,attrib.interface,str(attrib.description)])
                    QMetaObject.invokeMethod(self.object,"appendPropertiesModel",Q_ARG(QVariant,msg))
        else:
            QMetaObject.invokeMethod(self.object,"attributeExistsError")
            
            
    @pyqtSlot(str,str,str,str,str) #objectName,property_name,property_description,[minimum int,maximum int] #DEFAULTS Attribute.type==integer,Attribute.interface=TextEdit
    def addEntityAttribute_Integer(self,objectName,property_name,property_description,minimum,maximum):#New integer attribute
         if(project.getAttributeIdThroughName(objectName,property_name)=="error"): #attribute does not exist
             if(project.getEntityIdThroughName(objectName)!="error"): #if object exists #will get object currently selected in comboBox
                 objectId=project.getEntityIdThroughName(objectName) #get object id
                 project.addEntityAttribute(id=objectId,name=property_name,aType="Integer",interface="textbox (default)",description=property_description,labels=[minimum,maximum])
                 if(objectName==self._currentEntitySelected): #if the object is currently selected
                        object=project.getEntityById(objectId)
                        attrib=object.attributes[-1]
                        msg=QVariant([attrib.name,attrib.type,attrib.interface,str(attrib.description)])
                        QMetaObject.invokeMethod(self.object,"appendPropertiesModel",Q_ARG(QVariant,msg))
         else:
            QMetaObject.invokeMethod(self.object,"attributeExistsError") #will be invoked if attribute with the same name exists --JAVASCRIPT FUNCTION
            
    @pyqtSlot(str,str,str,str,str) #objectName,property_name,property_description,[minimum int,maximum int] #DEFAULTS Attribute.type==integer,Attribute.interface=TextEdit
    def addEntityAttribute_Float(self,objectName,property_name,property_description,minimum,maximum):#New float attribute
         if(project.getAttributeIdThroughName(objectName,property_name)=="error"): #attribute does not exist
             if(project.getEntityIdThroughName(objectName)!="error"): #if object exists #will get object currently selected in comboBox
                 objectId=project.getEntityIdThroughName(objectName) #get object id
                 project.addEntityAttribute(id=objectId,name=property_name,aType="Float",interface="textbox (default)",description=property_description,labels=[minimum,maximum])
                 if(objectName==self._currentEntitySelected): #if the object is currently selected
                        object=project.getEntityById(objectId)
                        attrib=object.attributes[-1]
                        msg=QVariant([attrib.name,attrib.type,attrib.interface,str(attrib.description)])
                        QMetaObject.invokeMethod(self.object,"appendPropertiesModel",Q_ARG(QVariant,msg))
         else:
            QMetaObject.invokeMethod(self.object,"attributeExistsError") #will be invoked if attribute with the same name exists --JAVASCRIPT FUNCTION 

      
            
    @pyqtSlot()
    def triggerPropertyNameErrorDialog(self): #if property name is not specified --ERROR DIALOG
         QMetaObject.invokeMethod(self.object,"propertyNameError");

    @pyqtSlot()
    def triggerPropertyTableDisplay(self): #ACTIVATED WHEN OBJECT IS SELECTED
        object=project.getEntityById(project.getEntityIdThroughName(self._currentEntitySelected))#get object id through selected
        QMetaObject.invokeMethod(self.object,"cleanPropertiesModel"); #will clear the propertiesModel 
        for i in object.attributes: #get attributes associated with model 
          msg=QVariant([i.name,i.type,i.interface,str(i.description)]) #append to model attribute by attribute
          QMetaObject.invokeMethod(self.object,"appendPropertiesModel",Q_ARG(QVariant,msg)); #this method will append all attributes to properties model
          
    @pyqtSlot(str)
    def triggerEditAttribute(self,attributeName): 
        print("triggered edit attribute {0} objectName{1}".format(attributeName,self._currentEntitySelected))

    @pyqtSlot()
    def triggerRelationshipView(self):
        msg=QVariant(project.generateRelationshipView())
        QMetaObject.invokeMethod(self.object,"createRelationshipView",Q_ARG(QVariant,msg));

    @pyqtSlot()
    def triggerOneToOne(self):#invoke one to one relationship dialog
        if(project.getEntityCount()): #if object count > 0
            if(project.getEntityCount()>1):
                if(self._currentEntitySelected!=None): #entity must be selected
                    others=[]  #these are other entities excluding the currently selected entity
                    for i in project.getEntityNames(): 
                        if(i!=self._currentEntitySelected):
                            others.append(i)
                    msg=QVariant(dialogs.oneToOneDialog.format(self._currentEntitySelected,others))
                    QMetaObject.invokeMethod(self.object,"oneToOneDialog",Q_ARG(QVariant,msg)) #invoke one to one relationship dialog
                else:
                  QMetaObject.invokeMethod(self.object,"selectToCreateRelationshipErr")   #invoked if no object is selected
            else:
                QMetaObject.invokeMethod(self.object,"notEnoughObjectsError") #invoked if object count is <= 1
        else:
            QMetaObject.invokeMethod(self.object,"noObjectExists") #invoke noObjectExists javascript function

    @pyqtSlot(str,str)
    def createOneToOne(self,object1_name,object2_name):#invoke one to one relationship dialog
        object1=project.getEntityIdThroughName(object1_name)
        object2=project.getEntityIdThroughName(object2_name)
        if(project.addRelationship("one to one",object1,object2)!="relationship exists"): #create relationship
            pass #success
        else:
             QMetaObject.invokeMethod(self.object,"relationshipExistsError") #relationship exists error

    @pyqtSlot()
    def triggerOneToMany(self):#invoke one to many relationship dialog
        if(project.getEntityCount()): #if object count > 0
            if(project.getEntityCount()>1):
                if(self._currentEntitySelected!=None): #entity must be selected
                    others=[]  #these are other entities excluding the currently selected entity
                    for i in project.getEntityNames(): 
                        if(i!=self._currentEntitySelected):
                            others.append(i)
                    msg=QVariant(dialogs.oneToManyDialog.format(self._currentEntitySelected,others))
                    QMetaObject.invokeMethod(self.object,"oneToManyDialog",Q_ARG(QVariant,msg)) #invoke one to one relationship dialog
                else:
                  QMetaObject.invokeMethod(self.object,"selectToCreateRelationshipErr")   #invoked if no object is selected
            else:
                QMetaObject.invokeMethod(self.object,"notEnoughObjectsError") #invoked if object count is <= 1
        else:
            QMetaObject.invokeMethod(self.object,"noObjectExists") #invoke noObjectExists javascript function


    @pyqtSlot(str,str)
    def createOneToMany(self,object1_name,object2_name):#invoke one to one relationship dialog
        object1=project.getEntityIdThroughName(object1_name)
        object2=project.getEntityIdThroughName(object2_name)
        if(project.addRelationship("one to many",object1,object2)!="relationship exists"): #create relationship
            pass #success
        else:
             QMetaObject.invokeMethod(self.object,"relationshipExistsError") #relationship exists error
             
    @pyqtSlot()
    def node_ObjectExistsError(self):
        QMetaObject.invokeMethod(self.object,"objectNameError")

            

         



sys.argv+=['--style',"material"]

app=QGuiApplication(sys.argv);


engine=QQmlApplicationEngine();
component=QQmlComponent(engine,QUrl.fromLocalFile('MainWindow.qml'))
object=component.create()

#instance of the Manager object
manager=Manager(object)
#expose manager object to qml
context=engine.rootContext()
context.setContextProperty("manager",manager)

app.exec()
