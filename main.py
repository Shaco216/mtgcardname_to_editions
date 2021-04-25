from Scrape_Card import card_search
from Scrape_Card import get_url
from Scrape_Card import get_card_information
from Scrape_Card import convert_cardlist_into_txt
from Scrape_Card import convert_cardlist_into_csv
from Scrape_Card import txt_or_csv
from scrape_price import include_prices
from scrape_price import convert_preislist_into_txt
from scrape_price import convert_preislist_into_csv
from scrape_price import create_cheapest_pricelist
from scrape_price import get_price
from scrape_price import cheapest_price
from dict_cardinfo_cardprice import create_dict_cardinfo_cardprice
from dict_cardinfo_cardprice import dict_to_csv
from dict_cardinfo_cardprice import dict_to_txt
from dict_cardinfo_cardprice import dict_to_two_lists
from dict_cardinfo_cardprice import convert_sorted_name_to_price_into_txt
from dict_cardinfo_cardprice import convert_sorted_name_to_price_into_csv
from Scrape_Card import cardname_with_space


Terminate = False
filetype = txt_or_csv()

inkl_preis = include_prices()
if inkl_preis == True:
    cheapest_price = cheapest_price()


while Terminate is False:
    cardname = card_search()
    url = get_url()
    url_cardname = cardname_with_space(cardname, url)
    #print(url_cardname)
    Explist = get_card_information(url, cardname, filetype)
    if inkl_preis == True:

        if cheapest_price == True:
            Preisliste = create_cheapest_pricelist(url_cardname, Explist)
        else:
            Preisliste = get_price(url, filetype)
        #print(cardname)
        sorted_name_to_price = create_dict_cardinfo_cardprice(Explist, Preisliste)
        #dict_to_two_lists(sorted_name_to_price, cardname)
    if filetype == 'TXT':
        convert_cardlist_into_txt(Explist, cardname)
        if inkl_preis == True:
            convert_preislist_into_txt(Preisliste)
            #dict_to_txt(sorted_name_to_price)
            convert_sorted_name_to_price_into_txt(sorted_name_to_price)
    if filetype == 'CSV':
        convert_cardlist_into_csv(Explist, cardname)
        if inkl_preis == True:
            convert_preislist_into_csv(Preisliste)
            #dict_to_csv(sorted_name_to_price)
            convert_sorted_name_to_price_into_csv(sorted_name_to_price)
    Usereingabe = input('Möchtest du nach einer weiteren Karte suchen(Y/N): ')
    if Usereingabe == 'N':
        Terminate = True
