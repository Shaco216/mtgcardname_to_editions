from Scrape_Card import card_search
from Scrape_Card import get_url
from Scrape_Card import get_card_information
from Scrape_Card import convert_cardlist_into_txt
from Scrape_Card import convert_cardlist_into_csv
from Scrape_Card import txt_or_csv
from scrape_price import get_price
from scrape_price import include_prices
from scrape_price import convert_preislist_into_txt
from scrape_price import convert_preislist_into_csv

Terminate = False
filetype = txt_or_csv()

inkl_preis = include_prices()
while Terminate is False:
    cardname = card_search()
    url = get_url()
    Explist = get_card_information(url, cardname, filetype)
    if inkl_preis == True:
        Preisliste = get_price(url, filetype)

    if filetype == 'TXT':
        convert_cardlist_into_txt(Explist, cardname)
        if inkl_preis == True:
            convert_preislist_into_txt(Preisliste)
    if filetype == 'CSV':
        convert_cardlist_into_csv(Explist, cardname)
        if inkl_preis == True:
            convert_preislist_into_csv(Preisliste)
    Usereingabe = input('Möchtest du nach einer weiteren Karte suchen(Y/N): ')
    if Usereingabe == 'N':
        Terminate = True
