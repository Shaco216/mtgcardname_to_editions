from Scrape_Card import card_search
from Scrape_Card import get_url
from Scrape_Card import get_card_information
from Scrape_Card import convert_list_into_txt

Terminate = False

while Terminate is False:
    cardname = card_search()
    url = get_url()
    Expansionlist = get_card_information(url, cardname)
    convert_list_into_txt(Expansionlist, cardname)
    Usereingabe = input('Möchtest du nach einer weiteren Karte suchen(Y/N): ')
    if Usereingabe == 'N':
        Terminate = True
