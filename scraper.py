from bs4 import BeautifulSoup
import requests
import subprocess

def getItems(subSec):
    url = (f"https://www.jumia.co.ke/catalog/?q={subSec}&sort=lowest-price&shipped_from=country_local#catalog-listing")
    site = requests.get(url)

    soup = BeautifulSoup(site.text,'html.parser')
    products = soup.find_all(class_='core')
    gathered = []
    for product in products:
        itemPrice = product.find(class_='prc')
        fillPrice = itemPrice.get_text()
        gathered.append(fillPrice)

    notifyText = f"Price is at {gathered[0]}"
    print(notifyText)
    subprocess.run(["notify-send", "-t", "5", "--action=Okay", str(notifyText)])

