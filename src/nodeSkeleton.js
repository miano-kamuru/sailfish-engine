import QtQuick 2.6
import QtQuick.Controls 2.6
import QtQuick.Layouts 1.12
import QtQuick.Controls.Material 2.12
import QtQuick.Window 2.12
ApplicationWindow {
    property var entityList:{{entityList}};
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
                ToolButton { //create one to one relationship
                   icon.source:"icons/node-join-segment.svg"
                   icon.color:"transparent"
                   text:"one to one"
                   onClicked:manager.triggerOneToOne();
                  } //end create one to one relationship
                  ToolButton { //create one to  manyrelationship
                   icon.source:"icons/node-join-segment.svg"
                   icon.color:"transparent"
                   text:"one to many"
                   onClicked:manager.triggerOneToMany();
                  } //end create one to many relationship
            }
        }

        function createObjectNode(nodeName){
            var dynamicObject = Qt.createQmlObject(
                '
                import QtQuick 2.6
                import QtQuick.Controls 2.6
                import QtQuick.Layouts 1.12
                import QtQuick.Controls.Material 2.12
                import QtQuick.Window 2.12
                Rectangle { //start entity rectangle
                
                width:180;
                height:50
                radius:10;
                color:"#3d3d3d";
                x:(parent.width/5)-width
                y:parent.height/2
               
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
      }',
                        mainWindow,'newNodeObject')
        }
}//end ApplicationWindow