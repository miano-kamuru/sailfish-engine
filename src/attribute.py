from Backend import *

def create(name="",aType="",interface="",description="",labels=""):
    new=Attribute(name=name,type=aType,description=description,labels=labels)
    return new


