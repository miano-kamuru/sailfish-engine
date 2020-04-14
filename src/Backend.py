#author:miano
#project:sailFish engine

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column,Integer,String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
import sqlalchemy.sql.default_comparator
from sqlalchemy.sql import exists
from sqlalchemy import and_,or_
import sys

project_file=""
for i in sys.argv:
    if(sys.argv.index(i)):
        project_file+=i
        project_file+=" "
if(project_file!=""):
 engine = create_engine(f"sqlite:///{project_file}",echo=False) #see all the generated sql produced
else:
 engine = create_engine("sqlite:///:memory:",echo=False) #see all the generated sql produced
 
Session = sessionmaker(bind=engine) #this class will serve as a factory for new session objects
Base = declarative_base() #declarative base class

class Project(Base): #store project info
    __tablename__='projects' 
    id = Column(Integer,primary_key=True) #<--PRIMARY KEY-->
    name = Column(String(50))   #the name of the project
    version = Column(String(50)) #project version is a string 
    developer = Column(String(80)) #maker of the project
    description = Column(String(140)) #a brief description of the project    
    def __repr__(self): #for nice formatting will be removed
        return f"{self.name} {self.version} {self.developer} {self.description}"

class Entity(Base): #objects 
    __tablename__="entities"
    id=Column(Integer,primary_key=True)
    name=Column(String(80)) #name of entity
    description=Column(String(140)) #a brief description of what the entity is about
    
    project_id=Column(Integer,ForeignKey('projects.id')) #relationship with project <!--many(entities) to one(project)-->
    project=relationship('Project',back_populates="entities")
    
    def __repr__(self):
        return f'{self.id} {self.name}'
    
Project.entities=relationship("Entity",order_by=Entity.id,back_populates="project",cascade="all, delete, delete-orphan") #relationship with entity <!--one(project) to many(entities)-->

class Attribute(Base): #object properties
    __tablename__="attributes"
    id=Column(Integer,primary_key=True)  #primary key
    name=Column(String(50))         #name of attribute
    type=Column(String(50))       #type of attribute
    interface=Column(String(50)) #[textbox (default),checkbox,combobox]
    labels=Column(String) #this will be a pickled list --optional
    description=Column(String(50)) #description of attribute (optional)
    
    entity_id=Column(Integer,ForeignKey('entities.id'))
    entity=relationship('Entity',back_populates="attributes")

    def __repr__(self):
        return f'{self.id} {self.name} {self.type} {self.interface}'
    
Entity.attributes=relationship('Attribute',back_populates="entity",cascade="all, delete, delete-orphan")

class Relationship(Base):
    __tablename__="relationships"
    id=Column(Integer,primary_key=True)
    type=Column(String) #[one to one,one to many]
    object1=Column(Integer) #primary key of object1
    object2=Column(Integer) #primary key of object2
    def __repr__(self): 
        return f'{self.object1} {self.object2}'
    
Base.metadata.create_all(engine) #generate schema
session=Session()
    

    
