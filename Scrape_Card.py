from bs4 import BeautifulSoup
import requests
import webbrowser
import pyautogui as py
import time
import csv



url= ''
x = 0
keyword = 'Expansions'
cardname = ''
Expansionlist = []
cardname_exakt = ""


def card_search():
    #https://pyautogui.readthedocs.io/en/latest/
    cardname = input("Bitte Kartenname eingeben: ")  #Exakter name ["cardname"]
    cardname_exakt = input("Ist das der EXAKTE Kartenname (Y/N): ")
    if cardname_exakt == 'Y':
        cardname = '["' + cardname + '"]'
    webbrowser.open('https://www.cardmarket.com/de/Magic/')#https://www.cardmarket.com/de/Magic/
    time.sleep(5)
    py.write(cardname, interval=0.1) #suche nach kartenname
    py.keyDown('return') # press enter
    time.sleep(2)
    cardname_exakt = ""
    return cardname



def get_url():
    url = input("Bitte Url hier einfügen: ")
    return url

def get_card_information(url, cardname):
    links = []


    linklistzaehler = 0
    Explist = ''

    Substring = 'Expansion'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    for link in soup.findAll('a'):
        links.append(link.get('href'))
        linklistzaehler = linklistzaehler + 1

    #checking if list(links) contains a Substring
    Expansionlist = [link for link in links if Substring in str(link)] #https://www.kite.com/python/answers/how-to-check-if-a-list-contains-a-substring-in-python#:~:text=Use%20any()%20to%20check,the%20list%20contains%20the%20substring.&text=Alternatively%2C%20use%20a%20list%20comprehension,element%20that%20contains%20the%20substring.
    #WICHTIG: in dem link www.kite.com/... wird nicht erwähnt, dass (in diesem fall) link kein string ist und deshalb nicht mit einem substring
    #         verglichen werden kann! deshalb str(link) (s. https://stackoverflow.com/questions/47464211/what-does-the-x-for-x-in-syntax-mean )


    Expansionlist.insert(0, cardname) #einfügen des kartennamens an erster stelle v. der liste
    #versuch liste in string zu convertieren und dann nur noch cardname und expansion darzustellen
    #for ele in Expansionlist:
        #Explist = Explist + ele
    #Explist.replace('/de/Magic/Expansions/', ' ')
    print(Explist)




    return Expansionlist

def convert_list_into_txt(Expansionlist, cardname):
    with open('cardlist.txt', 'a') as writer: #ursprünglich w für write ( a ist adden/appendieren)
        writer.writelines(Expansionlist)
        writer.writelines('\n')
def convert_list_into_csv(Expansionlist, cardname):
    with open('Cardlist.csv', 'a', newline='') as f: #ursprünglich w für write ( a ist adden/appendieren)
        writer = csv.writer(f)
        writer.writerows(Expansionlist)

if __name__ == '__main__':
    card_search()
    get_url()
    get_card_information(url)
    convert_list_into_txt(Expansionlist, cardname)
    convert_list_into_csv(Expansionlist, cardname)
#cardname = card_search()
#url = get_url()
#Expansionlist = get_card_information(url)
#convert_list_into_txt(Expansionlist, cardname)
