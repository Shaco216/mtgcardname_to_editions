from bs4 import BeautifulSoup
import requests
import webbrowser
import pyautogui as py
import time
import csv
import tkinter as tk



url= ''
x = 0
keyword = 'Expansions'
cardname = ''
Expansionlist = []
cardname_exakt = ""
Explist = []
filetype = ''

def txt_or_csv():
    #print('Bitte in Capslock TXT bzw. CSV schreiben!')
    filetype = input('Soll die Liste als CSV oder TXT erstellt werden(CSV/TXT)? ')
    if filetype == 'csv':
        filetype = 'CSV'

    if filetype == 'Csv':
        filetype = 'CSV'

    if filetype == 'txt':
        filetype = 'TXT'

    if filetype == 'Txt':
        filetype = 'TXT'

    if filetype == 'CSV':
        headline = ['Kartenname', '$Expansionname']
        print('\nBeachte: Trennzeichen darf KEIN KOMMA sein und muss ein $-Zeichen sein')
        print('Zeichensatz muss UTF-8 sein!\n')
        with open('Cardlist.csv', 'a', newline='') as f:  # ursprünglich w für write ( a ist adden/appendieren)
            writer = csv.writer(f)
            writer.writerow(headline)

    return filetype
def card_search():
    #https://pyautogui.readthedocs.io/en/latest/
    cardname =''
    cardname = input("Bitte Kartenname eingeben: ")  #Exakter name ["cardname"]
    cardname_exakt = 'Y'
    if cardname_exakt == 'Y':
        cardname = '["' + cardname + '"]'
    webbrowser.open('https://www.cardmarket.com/de/Magic/')#https://www.cardmarket.com/de/Magic/
    time.sleep(3)
    py.write(cardname, interval=0.1) #suche nach kartenname
    py.press('return') # press enter
    time.sleep(2)
    py.hotkey('ctrl', 'l')
    py.sleep(1)
    py.hotkey('ctrl', 'c')
    py.sleep(1)
    py.hotkey('ctrl', 'r')
    py.sleep(1)
    py.hotkey('alt', 'tab')
    return cardname



def get_url():
    #url aus clipboard einfügen
    tempvariable = ''
    tempvariable = tk.Tk()
    # keep the window from showing
    tempvariable.withdraw()
    url = tempvariable.clipboard_get()
    #url = input("Bitte Url hier einfügen(nur STRG+V druecken): ")
    return url

def get_card_information(url, cardname, filetype):
    links = []
    linklistzaehler = 0

    #this is necessary to reset the list and to save the x>1nd try to the list
    Expansionlist= []
    Explist= []
    temp = ''


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
    cardname = cardname.replace('["', '')
    cardname = cardname.replace('"]', '')

    Expansionlist.insert(0, cardname)  # einfügen des kartennamens an erster stelle v. der liste
    # versuch liste in string zu convertieren und dann nur noch cardname und expansion darzustellen
    #for ele in Expansionlist:
        #Explist = Explist + ele
    #Explist.replace('/de/Magic/Expansions/', ' ')

    #replace /de/Magic/Expansions/
    if filetype == 'TXT' or filetype == 'txt' or filetype == 'Txt':

        for item in Expansionlist:
            temp = str(item)
            temp = temp.replace('/de/Magic/Expansions/', ' ')
            Explist.append(temp)
        print(Explist)
    else:
        for item in Expansionlist:
            temp = str(item)
            temp = temp.replace('/de/Magic/Expansions/', '$')
            Explist.append(temp)
        print(Explist)
    return Explist

def convert_list_into_txt(Explist, cardname):
    with open('cardlist.txt', 'a') as writer: #ursprünglich w für write ( a ist adden/appendieren)
        writer.writelines(Explist)
        writer.writelines('\n')
def convert_list_into_csv(Explist, cardname):

    with open('Cardlist.csv', 'a', newline='') as f: #ursprünglich w für write ( a ist adden/appendieren)
        writer = csv.writer(f)#, quoting=csv.QUOTE_ALL keine lösung
        writer.writerow(Explist)


if __name__ == '__main__':
    txt_or_csv()
    card_search()
    get_url()
    get_card_information(url, cardname, filetype)
    convert_list_into_txt(Explist, cardname)
    convert_list_into_csv(Explist, cardname)
#cardname = card_search()
#url = get_url()
#Expansionlist = get_card_information(url)
#convert_list_into_txt(Expansionlist, cardname)

