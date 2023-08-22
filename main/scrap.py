from bs4 import BeautifulSoup
import requests


def get_valute(value):

    url = requests.get(url='https://www.cba.am/EN/SitePages/Default.aspx')

    soup = BeautifulSoup(url.text, 'html.parser')
    mylist = soup.find_all("em", class_="w_50")
    mydict = {}
    mylist = [i.text for i in mylist if i.text != '1']
    for i in range(0, len(mylist), 2):
        mydict[mylist[i]] = float(mylist[i + 1])

    return mydict[value]