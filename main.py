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
        for link in self.links:
            self.pages.append(requests.get(link))
        for page in self.pages:
            self.soups.append(BeautifulSoup(page.content,'html.parser'))
        for soup in self.soups : 
            self.columns.append(soup.find_all(class_="cBeditable"))
        self.size_dictionary.append({"2XS":0,"XS":1,"S":2,"M":3,"L":4,"XL":5,"2XL":6,"3XL":7})
        self.size_dictionary.append({"28":0,"29":1,"30":2,"31":3,"32":4,"33":5,"34":6,"35":7,"36":8,"37":9,"38":10,"39":11,"40":12,"41":13,"42":14,"43":15,"44":16,"45":17,"46":18,"47":19,"48":20,"49":21})
    def read_links(self):
        self.links=[]
        with open('./prod.csv','rb') as input_file:
            reader = csv.reader(input_file)
            for row in reader:
                if(row[1] not in self.links):
                    self.links.append(row[1])
            #self.links=random.sample(self.links)
            #self.links=list(set(self.links))    

    def checkProduct(self):
        with open('./prod.csv','rb') as input_file:
            reader = csv.reader(input_file)
            for row in reader:
                for i in range(len(self.links)):
                    if(row[1]==self.links[i]):
                        self.main_column=self.columns[i]
                        self.main_dictionary = self.size_dictionary[i]

                id_prod=row[0].split('/')[1]
                for single_column in self.main_column:
                    if id_prod==single_column.find(class_="color-name").get_text().replace("\t"," ").split(' ')[0]:
                        num=int(self.main_dictionary[row[0].split('/')[2]])
                        available=int((single_column.find(class_="cBsecondLine").find_all(class_="assortTypeFixed"))[num].get_text().replace("+","").strip())
                        if(available>0):
                            print(row[0]+" product is available "+str(available))
                        elif(available==0):
                            print(row[0]+" product is not available")
                            

inv = CheckInInventory();
inv.checkProduct();




# Size not found 
#Product Not found 
# Available