import hashlib

def get_token():
    str = "dealerCode=&kmMerchantId=0&merchantName=&mobile=13068281408&source=2&timestamp=1559814622065&userRegTime=1559814622065&version=1.0&weChatOpenId=odqQOw78x3Xt9Q9fuBDq3SINqqeQ&xinDaLuToken=&key=bd0df7edf2a11accb48c4b4eb2ed6175"
    m1 = hashlib.md5()
    m1.update(str.encode("utf-8"))
    token = m1.hexdigest()
    print(token)
    return token

get_token()