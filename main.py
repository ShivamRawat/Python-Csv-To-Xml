import sys
import requests
import csv
import random
from bs4 import BeautifulSoup
class CheckInInventory:
    def __init__(self):
        self.soups=[]
        self.pages=[]
        self.columns=[]
        self.size_dictionary=[]
        self.read_links();

        self.size_dictionary.append({"2XS":0,"XS":1,"S":2,"M":3,"L":4,"XL":5,"2XL":6,"3XL":7})
        self.size_dictionary.append({"28":0,"29":1,"30":2,"31":3,"32":4,"33":5,"34":6,"35":7,"36":8,"37":9,"38":10,"39":11,"40":12,"41":13,"42":14,"43":15,"44":16,"45":17,"46":18,"47":19,"48":20,"49":21})
    def get_inventory_info(self,sku,link):
     print("Now getting inventory info for: "+str(sku))
     content = requests.get(link).content
     soup = BeautifulSoup(content,'html.parser')
     column = soup.find_all(class_="cBeditable")

     id_prod = sku
# TODO
# Write your logic here to get the inventory info for an SKU from the HTML content

     for single_column in column:
      if id_prod==single_column.find(class_="color-name").get_text().replace("\t"," ").split(' ')[0]:
       num = int(self.main_dictionary[row[0].split('/')[2]])
       inventory_info = int((single_column.find(class_="cBsecondLine").find_all(class_="assortTypeFixed"))[num].get_text().replace("+","").strip())
       return inventory_info

    def read_links(self):
        self.links=[]
        with open('./prod.csv','rb') as input_file:
            reader = csv.reader(input_file)
            for row in reader:
              print(str(self.get_inventory_info(row[0],row[1])))
        sys.exit(1)
            
            #self.links=random.sample(self.links)
            #self.links=list(set(self.links))    


                            

inv = CheckInInventory();




# Size not found 
#Product Not found 
# Available
