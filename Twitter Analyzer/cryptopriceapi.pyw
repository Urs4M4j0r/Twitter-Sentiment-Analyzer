from lxml import html
import requests

def getCryptoPriceChange24h(crypto):
    page = requests.get('https://coinmarketcap.com/currencies/' + crypto)
    tree = html.fromstring(page.content)
    prices = tree.xpath('//span[@class="sc-1v2ivon-0 fiaaIx"]/text()')
    #prices = tree.xpath('//span[@class="sc-1v2ivon-0 iQVSWO"]/text()')
    prices2 = tree.xpath('//span[@class="icon-Caret-up"]')
    prices3 = tree.xpath('//span[@class="icon-Caret-down"]')
    sing = ""
    if len(prices2) > 1:
        sign = '+'
    elif len(prices3) > 1:
        sign = '-'
        
    change = sign + str(prices[0])
    #print(change)
    return change

#getCryptoPriceChange24h('bitcoin')
