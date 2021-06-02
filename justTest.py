import time
import hashlib
import requests
s=requests.session()
import json
host="http://47.96.25.44:10010"
# login_url="/app/user/login"
# data={"sysParams":{"requestTime":1622443721000,"appKey":"8B6EA5A09B8DDAA9770EA340AE35D3BA","sign":"587A4626D4E6045E80A420363199C2ED"},"params":{"userName":"15906266923","password":"d9c37e748cd899191c661a7b0dbd62c3","isAlicloud":"1","deviceId":"46d7e35a80a9480f8771e30e8aea3dc1","systemContext":"/siweiApp","deviceType":1,"loginId":"yxyljg"}}
# s.post(host+login_url,json.dumps(data),headers={"Content-Type": "application/json"})

t=str(round(time.time()*1000))
str="deviceId=46d7e35a80a9480f8771e30e8aea3dc1latitude=31.39171longitude=120.920128orgIds=363,365,369,370,371,372,373,374,375,376,377,378,379,380,381,382,383,384,385,386,387,388,392,393requestTime=%ssecretKey=f39dbd1b383dc2461d5e3d4ba28febb7userName=15906266923"%t
sign=hashlib.md5(str.encode("utf-8")).hexdigest().upper()
url="/app/signIn/getNearestOrgByLocation"
params={'sysParams': '{"requestTime":%s,"appKey":"8B6EA5A09B8DDAA9770EA340AE35D3BA","sign":"%s"}'%(t,sign), 'params': '{"orgIds":"363,365,369,370,371,372,373,374,375,376,377,378,379,380,381,382,383,384,385,386,387,388,392,393","longitude":120.920128,"latitude":31.39171,"userName":"15906266923","deviceId":"46d7e35a80a9480f8771e30e8aea3dc1"}'}
print(s.get(host+url,params=params).json())