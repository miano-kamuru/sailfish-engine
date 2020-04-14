#author:miano
#project sailFish engine

from Backend import *
import attribute

#NOTE that the id parameter in this module is the id of the entity

def create(name="",description=""): #create a new object -use project.addEntity
    new=Entity(name=name,description=description)
    return new

def getNames(): #get all entity names
    entity_names=session.query(Entity.name).all()
    bucket=[]
    for i in entity_names:
        bucket.append(i.name)
    return bucket  #return a list of entity names

def count(): #return the number of entities
    number=session.query(Entity).count()
    return number

def getById(id): #get entity by id
    try:
     object=session.query(Entity).filter(Entity.id==id).one()
     return object
    except sqlalchemy.orm.exc.NoResultFound:
        return "error"

def getByName(name): #get entity by name if it exists return "error" else return the object ---will fix the logic later
    i=session.query(Entity).filter(Entity.name==name).first();
    if(i):
        return True
    else:
        return False

def attributeCount(id): #get entity count #ID is the id of the entity id->int
    if(getById(id)!="error"): #if the id exists
        return len(getById(id).attributes) #return the number of attributes associated with the object
    else:
        return "error" #return error if object is not found

def getAttributes(id): #pass id of entity
   try:
     object=session.query(Entity).filter(Entity.id==id).one()
     return object.attributes
   except sqlalchemy.orm.exc.NoResultFound:
       return "error"


    

