import csv

Explist = []
Preisliste = []
cardname = ''
sorted_name_to_price = {}

def dict_to_csv(sorted_name_to_price):
    with open('Cardlist.csv', 'a', newline='') as f: #ursprünglich w für write ( a ist adden/appendieren)
        writer = csv.writer(f)#, quoting=csv.QUOTE_ALL keine lösung
        for key, value in sorted_name_to_price.items():
            writer.writerow([key, value])

def dict_to_txt(sorted_name_to_price):
    with open('Cardlist.txt', 'a', newline='') as writer: #ursprünglich w für write ( a ist adden/appendieren)
        for key, value in sorted_name_to_price.items():
            writer.writelines([key, value])

def create_dict_cardinfo_cardprice(Explist, Preisliste):
    zaehler = 0
    Explist_new = []
    Preisliste_new = []
    for item in Explist:
        if zaehler > 0:
            Explist_new.append(item)
            #print(Explist_new)
        zaehler = zaehler + 1
    zaehler = 0
    for item in Preisliste:
        if zaehler > 0:
            Preisliste_new.append(item)
            #print(Preisliste_new)
        zaehler = zaehler + 1
    zip_iterator = zip(Explist_new, Preisliste_new) # zusammenführen von 2 listen
    name_to_price = dict(zip_iterator) # erstellung des dictionaries
    sorted_name_to_price = sorted(name_to_price.items(),key=lambda kv: kv[1]) # hierbei entsteht aus einem dict eine sortierte liste
    #cardname = cardname.strip('"[]')
    #del sorted_name_to_price[cardname]
    #print(cardname)
    print(sorted_name_to_price)
    return sorted_name_to_price

def dict_to_two_lists(sorted_name_to_price, cardname): # kann ich mir sparen da sorted_name_to_price eine liste ist und kein dict :D
    Explist = []
    Preisliste = []
    for key, value in sorted_name_to_price.items():
        Explist.append(key)
        Preisliste.append(value)
    Explist.insert(0, cardname)
    Preisliste(0, 'Preis:')
    return Explist, Preisliste

def convert_sorted_name_to_price_into_txt(sorted_name_to_price):
    sorted_name_to_price2 = []
    for string in sorted_name_to_price:
        sorted_name_to_price2 = str(sorted_name_to_price)

    with open('cardlist.txt', 'a') as writer: #ursprünglich w für write ( a ist adden/appendieren)
        writer.writelines('Sortiert nach günstigste zuerst')
        writer.writelines('\n')
        writer.writelines(sorted_name_to_price2)
        writer.writelines('\n')

def convert_sorted_name_to_price_into_csv(sorted_name_to_price):
    headline1 = ['Sortiert nach günstigste zuerst']
    Abstand = []
    with open('Cardlist.csv', 'a', newline='') as f: #ursprünglich w für write ( a ist adden/appendieren)
        writer = csv.writer(f)#, quoting=csv.QUOTE_ALL keine lösung
        writer.writerow(headline1)
        writer.writerow(sorted_name_to_price)
        writer.writerow(Abstand)

if __name__ == '__main__':
    create_dict_cardinfo_cardprice(Explist, Preisliste)
    dict_to_two_lists(sorted_name_to_price, cardname)
    dict_to_txt(sorted_name_to_price)
    dict_to_csv(sorted_name_to_price)
    convert_sorted_name_to_price_into_csv(sorted_name_to_price)
    convert_sorted_name_to_price_into_txt(sorted_name_to_price)