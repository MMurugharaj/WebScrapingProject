import  requests
from bs4 import BeautifulSoup

#Different URL Examples
#URL = "https://www.amazon.in/Samsung-Emerald-Storage-Purchased-Separately/dp/B0B146VNMY/ref=sr_1_1_sspa?crid=1DH1H6ZXQSO19&keywords=mobile%2Bphone&qid=1673702619&sprefix=mo%2Caps%2C911&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"
#URL = "https://www.amazon.in/dp/B08VB57558/ref=sspa_dk_detail_0?psc=1&pd_rd_i=B08VB57558&pd_rd_w=hFpdb&content-id=amzn1.sym.1ab86ed4-e009-4190-bbae-77cbcace0264&pf_rd_p=1ab86ed4-e009-4190-bbae-77cbcace0264&pf_rd_r=577Y1RRVKAMNFV6W9XGK&pd_rd_wg=kZWCa&pd_rd_r=58c7e1b2-7b56-45f6-8c1f-50b17118229a&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWxfdGhlbWF0aWM&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzOTUyNEhIVzNHNVZSJmVuY3J5cHRlZElkPUEwMjk5NTYwMjE5WU1KNVAyWVNETiZlbmNyeXB0ZWRBZElkPUEwNDIzNDcyMlFKNTRHTUtGSjE2NSZ3aWRnZXROYW1lPXNwX2RldGFpbF90aGVtYXRpYyZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="


products_to_track = [
    {
        "product_url":"https://www.amazon.in/New-Apple-iPhone-12-128GB/dp/B0932MD32V/ref=sr_1_1_sspa?crid=3GQ7S4XZXOQNB&keywords=iphone%2B12&qid=1673958088&sprefix=%2Caps%2C395&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1",
        "Name":"iphone12",
        "Target":"65000"
    },
    {
        "product_url": "https://www.amazon.in/Apple-iPhone-13-128GB-Midnight/dp/B09G9HD6PD/ref=sr_1_1_sspa?crid=3ICN4PIIRT8YL&keywords=iphone%2B13&qid=1673959448&sprefix=iphone%2B1%2Caps%2C495&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1",
        "Name": "iphone13",
        "Target":"55000"
    },
{
        "product_url": "https://www.amazon.in/Apple-iPhone-128GB-Space-Black/dp/B0BDJ22G36/ref=sr_1_2_sspa?crid=3M2VWPHEBNBTW&keywords=iphone%2B14&qid=1673959482&sprefix=iphone%2B1%2Caps%2C344&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1",
        "Name": "iphone14",
        "Target":"150000"
    },
    {
        "product_url": "https://www.amazon.in/OnePlus-Moonstone-Black-128GB-Storage/dp/B0B5V47VK4/ref=sr_1_1_sspa?crid=20ZE9BHQA6JZ3&keywords=1%2B%2Bplus%2Bmobile&qid=1673959598&sprefix=1%2Caps%2C789&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1",
        "Name": "OnePlus 10T",
        "Target":"40000"
    },
{
        "product_url": "https://www.amazon.in/Apple-iPhone-Pro-Max-Gold/dp/B0BDJPZ4RC/ref=sr_1_11?crid=2NKVBK7DN2XBP&keywords=iphone+14&qid=1673970041&sprefix=ip%2Caps%2C3853&sr=8-11",
        "Name": "iphone 14 ProMax",
        "Target":"150000"
    }
]

def give_product_price(URL):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
               }
    page =requests.get(URL,headers=headers)
    soup=BeautifulSoup(page.content,'html.parser')

    product_price = soup.find("span",{"class":"a-price-whole"})
    if (product_price is None):
        product_price = soup.find("span",{"class":"a-price-whole"})

    return product_price.get_text()

    #print(product_price)
    #print(product_price.getText())

result_file = open("my_result_file.txt","w")
try:
    for every_products in products_to_track:
        product_price_returned = give_product_price(every_products.get("product_url"))
        print(product_price_returned + "--" + every_products.get("Name"))

        my_price = product_price_returned
        my_price = my_price.replace(',', '')
        my_price = int(float(my_price))

        print(my_price)
        if my_price < int(every_products.get("Target")):
            print("Available at required price")
            result_file.write(every_products.get("Name") + "\t" + "Available at target price" +"--" "Current price" + str(my_price)+"\n")
        else:
            print("The price is still at same price")

finally:
    result_file.close()

