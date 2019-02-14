from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = "https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html,"html.parser")

containers = page_soup.find_all("div",{"class":"bhgxx2 col-12-12"})
containers = containers[0]
#print(containers[0])

filename="product.csv"
f = open(filename,"w")
header = "product_name, Pricing, Ratings \n"
f.write(header)
for containers in containers:
    product_name = containers.div.img["alt"]

    price_container = containers.findAll("div",{"class":"bhgxx2 col-12-12"})
    price= price_container[0].text.strip()

    trim_price = ''.join(price.split(','))
    rm_rupee = trim_price.split("")

    split_price = add_rs_price.split('E')
    final_price = split_price[0]

    split_rating = rating.split("")
    final_rating = split_rating[0]

    print(product_name.replace(",","|" + "," + final_price + ", " + final_rating + "\n"))
    f.write(product_name.replace(",","|",+final_price + "," + final_rating + "\n"))
f.close()


