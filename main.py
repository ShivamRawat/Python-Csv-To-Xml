import requests
import csv
from bs4 import BeautifulSoup


class CheckInInventory:
    def __init__(self):
        page=requests.get('https://seizoroi.com/product_api/0999/0999_dk.htm?fbclid=IwAR1rBj-I_qp72HtiTmk0zdd9XCN6Qz_tfDrEKfVIFdAZR0HAq3M4qGTFQcs')
        soup= BeautifulSoup(page.content,'html.parser')
        self.all_columns=soup.find_all(class_="cBeditable")
        self.size_dictionary={"2XS":0,"XS":1,"S":2,"M":3,"L":4,"XL":5,"2XL":6,"3XL":7}
    def checkProduct(self):
        with open('./prod.csv','rb') as input_file:
            reader = csv.reader(input_file)
            for row in reader:
                id_prod=row[0].split('/')[1]
                for single_column in self.all_columns:
                    if id_prod==single_column.find(class_="color-name").get_text().split(' ')[0]:
                        num=int(self.size_dictionary[row[0].split('/')[2]])
                        available=int((single_column.find(class_="cBsecondLine").find_all(class_="assortTypeFixed"))[num].get_text().replace("+","").strip())
                        if(available>0):
                            print(row[0]+" product is available "+str(available))
                        if(available==0):
                            print(row[0]+" product is not available")
                            

inv = CheckInInventory();
inv.checkProduct();




# Size not found 
#Product Not found 
# Available