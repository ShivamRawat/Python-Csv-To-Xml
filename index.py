#Nessecary Imports#
import csv 
from yattag import Doc, indent
doc, tag, text = Doc().tagtext()


class Product:
    def get_xml(self,inventory):
        with tag('root'):
            with open('./products.csv') as file:
                csvfile= csv.reader(file,delimiter=',')
                next(csvfile)
                for rows in csvfile:
                    with tag('item'):
                        with tag(inventory.row[0]):
                            text(rows[0])
                        with tag(inventory.row[1]):
                            text(rows[2]) 
                        with tag(inventory.row[2]):
                            text(rows[3])
                        with tag(inventory.row[3]):
                            text(rows[4]) 
                        with tag(inventory.row[4]):
                            text(rows[5])
        result = indent(
        doc.getvalue(),
        indentation = ' '*4,
        newline = '\r\n'
        )
        with open('./products.xml','w') as file :
            file.write(result)

class Inventory:
    row=["sku",'title','description','category','brand']
    inventory=''
    def read_file(self):
        with open('./products.csv') as file:
            csvfile= csv.reader(file,delimiter=',')
            next(csvfile)
            self.inventory=csvfile

a=Inventory()
a.read_file()
b=Product()
b.get_xml(a)