#Nessecary Imports#
import csv 
from yattag import Doc, indent
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

a=Inventory()
a.read_file()
a.get_xml()
for i in a.inventory:
    print(i.sku)