from bs4 import BeautifulSoup
import requests
import csv

url = ''
Preisliste = []
filetype = ''
def include_prices():

    inkl_preis2 = input('Mit Preisauflistung oder ohne(Y/N)? ')
    if inkl_preis2 == 'Y' or inkl_preis2 == 'y':
        inkl_preis = True
    if inkl_preis2 == 'N' or inkl_preis2 == 'n':
        inkl_preis = False
    return inkl_preis

def get_price(url, filetype):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    Preis = []
    for prize in soup.findAll(class_='col-price pr-sm-2'):

        Preis.append(prize.text)
    del Preis[0]
    #Preis.sort()
    Preis.insert(0, 'Preise:')
    if filetype == 'TXT':
        for item in Preis:
            temp = str(item)
            temp = temp + '\t'
            Preisliste.append(temp)
        print(Preisliste)
    if filetype == 'CSV':
        for item in Preis:
            temp = str(item)
            #temp = '$'+ temp
            Preisliste.append(temp)
        print(Preisliste)

    return Preisliste

def convert_preislist_into_txt(Preisliste):
    with open('cardlist.txt', 'a') as writer: #ursprünglich w für write ( a ist adden/appendieren)
        writer.writelines(Preisliste)
        writer.writelines('\n')
def convert_preislist_into_csv(Preisliste):

    with open('Cardlist.csv', 'a', newline='') as f: #ursprünglich w für write ( a ist adden/appendieren)
        writer = csv.writer(f)#, quoting=csv.QUOTE_ALL keine lösung
        writer.writerow(Preisliste)

if __name__ == '__main__':
    get_price(url, filetype)
    include_prices()
    convert_preislist_into_txt(Preisliste)
    convert_preislist_into_csv(Preisliste)