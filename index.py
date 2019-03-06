#Nessecary Imports#
import csv 
from yattag import Doc, indent
import xml.etree.ElementTree as ET

doc, tag, text = Doc().tagtext()

    
class Product:
    def __init__(self,*args):
        args=args[0]
        self.sku=args[0]
        self.title=args[2]
        self.description=args[3]
        self.category=args[4]
        self.brand=args[5]



class Inventory:
    row=["sku",'title','description','category','brand']
    inventory=[]
    def read_file(self):
        with open('./products.csv') as file:
            csvfile= csv.reader(file,delimiter=',')
            next(csvfile)
            self.products=csvfile
            for rows in self.products:
                self.inventory.append(Product(rows))
    def get_xml(self):
        with tag('root'):
            with open('./products.csv') as file:
                csvfile= csv.reader(file,delimiter=',')
                next(csvfile)
                for rows in csvfile:
                    with tag('item'):
                        with tag(self.row[0]):
                            text(rows[0])
                        with tag(self.row[1]):
                            text(rows[2]) 
                        with tag(self.row[2]):
                            text(rows[3])
                        with tag(self.row[3]):
                            text(rows[4]) 
                        with tag(self.row[4]):
                            text(rows[5])
        result = indent(
        doc.getvalue(),
        indentation = ' '*4,
        newline = '\r\n'
        )
        with open('./products.xml','w') as file :
            file.write(result)


class Product_xml():
    def __init__(self,state,ids,sku,name,minimum,stock):
        self.state=state
        self.ids=ids
        self.sku=sku
        self.name=name
        self.minimum=minimum
        self.stock=stock
        if(stock==0):
            self.in_inventory=False
        else:
            self.in_inventory=True
    def __str__(self):
        return self.in_inventory
class inventory_xml():
    inventory=[]
    def __init__(self):
        with open("file.xml") as xmlfile:
            tree = ET.parse(xmlfile)   
            root = tree.getroot() 
            products=root.findall('./Product')
            j=0
            for i in products:
                print(j)
                j+=1
                state=i.find('State').text
                ids=i.find('Id').text
                sku=i.find('Sku').text
                stock=i.find('Stocks').find('Status').find("Active").text
                self.inventory.append(Product_xml(state,ids,sku,"name","minimum",stock))


a=inventory_xml()
a.inventory[0]