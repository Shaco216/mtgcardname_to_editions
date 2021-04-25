from bs4 import BeautifulSoup
import requests
import csv
import time

url = ''
Preisliste = ['Preise:']
filetype = ''
Explist = []
url_cardname = ''

def create_cheapest_pricelist(url_cardname, Explist):
    core_link = 'https://www.cardmarket.com/de/Magic/Products/Singles/'
    ger_eng_filter = '?sellerCountry=7&language=1'#language=1,3 ist language=englisch,deutsch
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    zahl = 0
    Preisliste = []
    #cardname = cardname.replace('["', '')
    #cardname = cardname.replace('"]', '')
    Preistemp = ''
    for Exp in Explist:
        if zahl > 0 and zahl< len(Explist):
            Exp = str(Exp)
            Exp = Exp.strip() # entfernt leerzeichen
            cardname = url_cardname.strip()
            #print(cardname)
            link = core_link+Exp+'/'+url_cardname+ger_eng_filter
            link.strip()
            #print(link)
            #time.sleep(2)
            page = requests.get(link, headers=headers)
            soup = BeautifulSoup(page.content, 'html.parser')
            #print(link)
            Preis = []
            for prize in soup.findAll(class_='col-6 col-xl-7'):
                Preis.append(prize.text)
                #print(Preis)
            #print(Preis)
            if len(Preis) > 2:
                Preistemp = Preis[4] # 4 ist ab und 5 ist trend
                Preistemp = str(Preistemp)
                Preisliste.append(Preistemp)


        zahl = zahl + 1
    Preisliste.insert(0, 'Preis:')
    print(Preisliste)
    return Preisliste


def include_prices():

    inkl_preis2 = input('Mit Preisauflistung oder ohne(Y/N)? ')
    if inkl_preis2 == 'Y' or inkl_preis2 == 'y':
        inkl_preis = True
    if inkl_preis2 == 'N' or inkl_preis2 == 'n':
        inkl_preis = False
    return inkl_preis

def cheapest_price():
    cheapest_price2 = input('Mit gefiltertem Preis(Standort Deutschland Sprache ENG) von jeder Edition (Y/N)? ')
    if cheapest_price2 == 'Y' or cheapest_price2 == 'y':
        cheapest_price = True
    if cheapest_price2 == 'N' or cheapest_price2 == 'n':
        cheapest_price = False
    return cheapest_price

def get_price(url, filetype):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    Preis = []
    Preisliste = []
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
    cheapest_price()
    create_cheapest_pricelist(url_cardname, Explist)