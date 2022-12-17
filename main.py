import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

products_list = []
prices_list = []
PhoneStatus_list = []
page_num = 1
while True:

    result = requests.get(f"https://www.ebay.com/sch/i.html?_from=R40&_nkw=iphone+13+pro+max&_sacat=0&LH_TitleDesc=0&_fsrp=1&_ipg=60&LH_BO=1&rt=nc&Color=Gold%7CSilver%7CGray%7CWhite%7CBlue%7CBlack&_oaa=1&_dcat=20349&_pgn={page_num}")
    # print(result.status_code)
    src = result.content
    soup = BeautifulSoup(src, 'html.parser')
    src = soup.find(id="mainContent")
    last_page = src.find_all('a', class_="pagination__item")

    # page=soup.find('h1',class_='srp-controls__count-heading')
    # page_limit=int(page.find('span',{'class':'BOLD'}).text)
    page_limit = len(last_page)
    # print(page_limit)
    if (page_limit < page_num):
        print("pages ended")
        break
    product = soup.find_all('div', {'class': 's-item__title'})
    pri = soup.find_all('span', {'class', 's-item__price'})
    phone_status = soup.find_all('span', {'class', 'SECONDARY_INFO'})
    for i in range(1, len(product)):
        products_list.append(product[i].text)
        prices_list.append(pri[i].text)
        PhoneStatus_list.append(phone_status[i].text)

    page_num += 1
    print("page switched")
# file_list = [products_list, prices_list,PhoneStatus_list]
# exported = zip_longest(*file_list)
# with open("Products.csv", "w", encoding='utf8') as h:
#     wr = csv.writer(h)
#     wr.writerow(["Product Name", "Price", "Phone_Status"])
#     wr.writerows(exported)
# g = {'name': products_list, 'price': prices_list}
# print(g)
print(products_list)
print(prices_list)
print(PhoneStatus_list)