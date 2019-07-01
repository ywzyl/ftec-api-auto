import requests

url = 'http://finance.cs.xiangqianpos.com/xdd-finance-web/config/getBaseConfig'
headers={
    'User-Agent': "PostmanRuntime/7.15.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "bb15189a-9b25-40a4-ab10-dae07168e3aa,c0a539eb-76e2-4373-b0cc-ae3e46f3de5c",
    'Host': "finance.cs.xiangqianpos.com",
    'cookie': "SERVERID=e98aa6e654c9fa4087fe9a140002da81|1561700850|1561700358",
    'accept-encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }
r = requests.get(url,headers=headers)
print(r.status_code)