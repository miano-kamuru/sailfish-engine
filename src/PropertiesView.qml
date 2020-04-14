import QtQuick 2.6
import QtQuick.Controls 2.6
import QtQuick.Controls.Material 2.6
import QtQuick.Layouts 1.12
import QtQml.Models 2.12
import QtQuick.Controls 1.4 as PropertyTable
import QtQuick.Controls.Styles 1.4

PropertyTable.TableView { //table view for properties
              anchors.left:objectView.right
              width:parent.width-objectView.width*2;
              height:parent.height-190
              anchors.verticalCenter:parent.verticalCenter;
              id:propertyTable;

    PropertyTable.TableViewColumn { //start table view colum1
          role: "name"
          title: "Name"
          width: propertyTable.width/4
          elideMode :Text.ElideLeft;
          delegate:Item{
          RowLayout{
            anchors.fill:parent
            Button {
                flat:true
                icon.color:"#34b5e9";
                icon.source:"icons/ic_description_24px.svg"
            }
            Text{
                   id: itemText
                   text: styleData.value
                   Layout.preferredWidth:parent.width/1.25
                   Layout.alignment:Qt.AlignRight
                   font.pixelSize: 24
                   elide: Text.ElideRight
                   color:styleData.selected ? "#35b5e9" : "black";
                   opacity:0.5
                 }
               }
        } //end name item delegate

    }//end table view column 1

    PropertyTable.TableViewColumn { //colum 2
        elideMode :Text.ElideRight;
        role: "type"
        title: "Type"
        width: propertyTable.width/4
    } //end column 2

    PropertyTable.TableViewColumn { //column 3
        role: "interfaceType"
        title: "Interface"
        width: propertyTable.width/4
    } //end column 3

    PropertyTable.TableViewColumn { //last column
        role: "description"
        title: "Description"
        width: propertyTable.width/4
    } //end last column

    model: propertiesModel;

    rowDelegate:Item { //start row delegate
        id:xp
        height:50
        Rectangle {
        width:parent.width;height:parent.height; 
        color:styleData.selected ? "gray" : "white"; anchors.bottom:parent.bottom; opacity:0.1;
    }

    Rectangle {width:parent.width;height:1; color:"black"; anchors.bottom:parent.bottom; opacity:0.1;}
    } //end row delagate

    itemDelegate:Item{ 
        Text{
               id: itemText
               text: styleData.value
               anchors.fill:parent
               verticalAlignment: Text.AlignVCenter
               horizontalAlignment: Text.AlignHCenter
               font.pixelSize: 24
               wrapMode:Text.Wrap 
               elide: Text.ElideRight
               color:styleData.selected ? "#35b5e9" : "black";
               opacity:0.5
            }
        }
 
    onActivated:{
      manager.triggerEditAttribute(propertiesModel.get(currentRow).name); //on property activated slot
      //pass the name as argument
    }
} //end tableView 