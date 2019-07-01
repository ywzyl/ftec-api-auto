import requests

url = 'http://finance.cs.xiangqianpos.com/xdd-finance-web/userMerchant/queryUserMerchant'
headers={
    'userCookiesName': "64c9ef12817041bdeeb7c04f046a2877",
    'Content-Type': "application/json",
    'User-Agent': "PostmanRuntime/7.15.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "43ca36fa-8a5a-48a3-a6c2-115aedfa2e9c,6fd6da3e-0e7b-4fe4-b6af-aa99efe5e53b",
    'Host': "finance.cs.xiangqianpos.com",
    'cookie': "SERVERID=e98aa6e654c9fa4087fe9a140002da81|1561703339|1561702114",
    'accept-encoding': "gzip, deflate",
    'content-length': "28",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }
data = {
	"mobile": "13068281408"
}
r = requests.post(url,data=data,headers=headers)
print(r.status_code)