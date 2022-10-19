import requests
from fake_useragent import UserAgent
import json
ua = UserAgent()

url = 'https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?start=101&limit=100&sortBy=market_cap&sortType=desc&convert=USD,BTC,ETH&cryptoType=all&tagType=all&audited=false&aux=ath,atl,high24h,low24h,num_market_pairs,cmc_rank,date_added,max_supply,circulating_supply,total_supply,volume_7d,volume_30d,self_reported_circulating_supply,self_reported_market_cap'
result = []
def collect_data():

    url = f'https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?start=1&limit=100&sortBy=market_cap&sortType=desc&convert=USD,BTC,ETH&cryptoType=all&tagType=all&audited=false&aux=ath,atl,high24h,low24h,num_market_pairs,cmc_rank,date_added,max_supply,circulating_supply,total_supply,volume_7d,volume_30d,self_reported_circulating_supply,self_reported_market_cap'
    response = requests.get(url=url, headers={'user-agent': f'{ua.random}'})
    #with open('result.json', "w") as file:
        #json.dump(response.json(), file, indent=4, ensure_ascii=True)
    categories = response.json()['data']['cryptoCurrencyList']
    for crypto in categories:
        crypto_name = crypto.get('name').strip()
        quotes = crypto.get('quotes')

        for usd in quotes:
            usd_price = usd.get('price')
        result.append({
            'Name': crypto_name,
            'price': str(round((usd_price),4))
            })
        #print(f'Валюта {crypto_name}, цена {round((usd_price),4)}$')

    with open('result_data.json', 'w') as file:
        json.dump(result, file, indent=4, ensure_ascii=True)

def main():

    collect_data()



if __name__== "__main__":
    main()
