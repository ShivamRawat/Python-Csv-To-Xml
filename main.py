import requests
import csv
from bs4 import BeautifulSoup
page=[]
soup=[]
links =["https://seizoroi.com/product_api/0999/0999_dk.htm","https://seizoroi.com/product_api/0999_white.htm"]
class CheckInInventory:
    def __init__(self):
        page.append(requests.get(links[0]))
        page.append(requests.get(links[1]))
        soup.append(BeautifulSoup(page[0].content,'html.parser'))
        soup.append(BeautifulSoup(page[1].content,'html.parser'))
        self.all_columns=soup[0].find_all(class_="cBeditable")
        self.all_columns_sec=soup[1].find_all(class_="cBeditable")

        self.size_dictionary={"2XS":0,"XS":1,"S":2,"M":3,"L":4,"XL":5,"2XL":6,"3XL":7}
        self.size_dictionary_sec={"28":0,"29":1,"30":2,"31":3,"32":4,"33":5,"34":6,"35":7,"36":8,"37":9,"38":10,"39":11,"40":12,"41":13,"42":14,"43":15,"44":16,"45":17,"46":18,"47":19,"48":20,"49":21}
    def checkProduct(self):
        with open('./prod.csv','rb') as input_file:
            reader = csv.reader(input_file)
            for row in reader:
                if(row[1]==links[0]):
                    self.main_column=self.all_columns
                    self.main_dictionary = self.size_dictionary
                elif(row[1]==links[1]):
                    self.main_column=self.all_columns_sec
                    self.main_dictionary = self.size_dictionary_sec
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