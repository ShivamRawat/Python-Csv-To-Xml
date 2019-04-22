import requests
import csv
import random
from bs4 import BeautifulSoup
class CheckInInventory:
    def __init__(self):
        self.soups=[]
        self.pages=[]
        self.columns=[]
        #self.size_dictionary=[]
        self.read_links();
        for link in self.links:
            self.pages.append(requests.get(link))
        for page in self.pages:
            self.soups.append(BeautifulSoup(page.content,'html.parser'))
        for soup in self.soups : 
            self.columns.append(soup.find_all(class_="cBeditable"))
    def read_links(self):
        self.links=[]
        with open('./prod.csv','rb') as input_file:
            reader = csv.reader(input_file)
            for row in reader:
                if(row[1] not in self.links):
                    self.links.append(row[1])
            #self.links=random.sample(self.links)
            #self.links=list(set(self.links))    
    def checkSizes(self,webSize,size):
        if(size==webSize):
            return True
        elif(webSize=="XXXL" and size=="3XL"):
            return True
        elif(webSize=="XXL" and size=="2XL"):
            return True
        elif(webSize=="XXS" and size=="2XS"):
            return True                 
        else :  
            return False   
    def checkProduct(self):
        with open('./prod.csv','rb') as input_file:
            reader = csv.reader(input_file)
            for row in reader:
                for i in range(len(self.links)):
                    if(row[1]==self.links[i]):
                        self.main_column=self.columns[i]
                        #self.main_dictionary = self.size_dictionary[i]

                id_prod=row[0].split('/')[1]
                for single_column in self.main_column:
                    index_value  =-1
                    for sizes in single_column.find(class_="tableBackgroundBlack").find_all("td"):
                        index_value+=1
                        if id_prod==single_column.find(class_="color-name").get_text().replace("\t"," ").split(' ')[0]:
                            if(self.checkSizes(sizes.get_text(),row[0].split('/')[2])):
                                available=int((single_column.find(class_="cBsecondLine").find_all("td"))[index_value].get_text().replace("+","").strip())
                                if(available>0):
                                    print(row[0]+" product is available "+str(available))
                                elif(available==0):
                                    print(row[0]+" product is not available")

class ReadFromHtml:
    def __init__(self,sku,hmtllink):
        self.sku=sku
        self.pages=(requests.get(hmtllink))
        self.soups=(BeautifulSoup(self.pages.content,'html.parser')) 
        self.columns=(self.soups.find_all(class_="cBeditable"))
        self.checkProduct()
    def checkSizes(self,webSize,size):
        if(size==webSize):
            return True
        elif(webSize=="XXXL" and size=="3XL"):
            return True
        elif(webSize=="XXL" and size=="2XL"):
            return True
        elif(webSize=="XXS" and size=="2XS"):
            return True                 
        else :  
            return False               
    def checkProduct(self):
        for single_column in self.columns:
            index_value  =-1
            for sizes in single_column.find(class_="tableBackgroundBlack").find_all("td"):
                index_value+=1
                if self.sku.split('/')[1]==single_column.find(class_="color-name").get_text().replace("\t"," ").split(' ')[0]:
                    if(self.checkSizes(sizes.get_text(),self.sku.split('/')[2])):
                        available=int((single_column.find(class_="cBsecondLine").find_all("td"))[index_value].get_text().replace("+","").strip())
                        if(available>0):
                            print(self.sku+" product is available "+str(available))
                        elif(available==0):
                            print(self.sku+" product is not available")
#inv = CheckInInventory();
#inv.checkProduct();

inv = ReadFromHtml("302510/0099DKTEAM/2XS","https://seizoroi.com/product_api/0999/0999_dk.htm")


# Size not found 
#Product Not found 
# Available