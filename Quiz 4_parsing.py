import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint
f = open('bags.csv', 'w', newline='\n', encoding='utf-8_sig')
f_obj = csv.writer(f)
f_obj.writerow(['Brand Name', 'Item Description', 'Price'])
index = 1
h = {'Accept-language': '*', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'}
dict = {'Gucci': 25354, 'Prada': 34624, 'Bottega Veneta': 2450, 'Dolce & Gabanna': 3440, 'Valentino Garavani': 534369}
#შერჩეულია ისეთი ბრენდები, რომლებსაც მინიმუმ 5 გვერდზე აქვთ პროდუქცია განთავსებული
try:
    designer = input("Hello, we have Gucci, Prada, Dolce & Gabanna, Bottega Veneta and Valentino Garavani."
                     " Which designer bags do you want to add in the file? ").title()
    if dict.get(designer) == None:
        raise ValueError
    while index < 6:
        url = "https://www.farfetch.com/ge/shopping/women/bags-purses-1/items.aspx?page=" + str(index) + "&view=50&sort=3&designer="
        + str(dict.get(designer))
        r = requests.get(url, headers=h)
        soup = BeautifulSoup(r.text, 'html.parser')
        soup_sub = soup.find('div', class_="css-1h2x2st elu6vcm2")
        all_items = soup_sub.find_all('div', class_="css-1veh5kh-ProductCard e19e7out0")
        index += 1
        sleep(randint(2, 7))
        for item in all_items:
            item_brand = item.find('p', class_="e17j0z620 css-14ahplz-Body-BodyBold-ProductCardBrandName eq12nrx0").text
            #მართალია, ეს ისედაც ვიცი, ვინაიდან მომხმარებელმა შეიყვანა, მაგრამ გადამოწმებისთვის მაინც დავტოვე
            item_desc = item.find('p', class_="css-4y8w0i-Body e1s5vycj0").text
            item_price = item.find('p', class_="css-hmsjre-Body-Price e15nyh750").text
            #რამდენიმე p იყო, html-თან მუშაობის საწყისი დონიდან გამომდინარე, რთულიც კი აღმოჩნდა და კლასით ძებნა დამჭირდა,
            #თუმცა ყველაფერს სწორად პოულობს
            f_obj.writerow([item_brand, item_desc, item_price])
except ValueError: print('Enter the brand name correctly')

f.close()



