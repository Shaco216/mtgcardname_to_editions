from Scrape_Card import card_search
from Scrape_Card import get_url
from Scrape_Card import get_card_information
from Scrape_Card import convert_list_into_txt
from Scrape_Card import convert_list_into_csv

Terminate = False

while Terminate is False:
    cardname = card_search()
    url = get_url()
    Explist = get_card_information(url, cardname)
    convert_list_into_txt(Explist, cardname)
    #convert_list_into_csv(Explist, cardname)
    Usereingabe = input('Möchtest du nach einer weiteren Karte suchen(Y/N): ')
    if Usereingabe == 'N':
        Terminate = True

