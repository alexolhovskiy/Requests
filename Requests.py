#Alex Olhovskiy
#################################################################
#Get report

import requests
url = "https://chirpstack-api.iotserv.ru/api/devices?limit=5&applicationId=0f516251-75bc-4699-919d-bcd398a50754"
headers = {
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjaGlycHN0YWNrIiwiaXNzIjoiY2hpcnBzdGFjayIsInN1YiI6IjVmM2FlZDdmLTA5NGItNDFhZC05NDdjLTBmMzE3NzAwNTVmMyIsInR5cCI6ImtleSJ9.3h3-YKpbUXvifb9kn8Rzvw6IVtezubrr6By2aZmhV-0'
}
response = requests.request("GET", url, headers=headers)
print(response.text)


###############################################################
#Delete 10 devices

# import requests
# import json

# url = "https://chirpstack-api.iotserv.ru/api/devices?limit=10&applicationId=0f516251-75bc-4699-919d-bcd398a50754"
# headers = {
#   'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjaGlycHN0YWNrIiwiaXNzIjoiY2hpcnBzdGFjayIsInN1YiI6IjVmM2FlZDdmLTA5NGItNDFhZC05NDdjLTBmMzE3NzAwNTVmMyIsInR5cCI6ImtleSJ9.3h3-YKpbUXvifb9kn8Rzvw6IVtezubrr6By2aZmhV-0'
# }
# response = requests.request("GET", url, headers=headers)
# print(response.text)

# arr=json.loads(response.text)

# for dev in arr['result']: 
#   url = f"https://chirpstack-api.iotserv.ru/api/devices/{dev['devEui']}"
#   headers = {
#     'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjaGlycHN0YWNrIiwiaXNzIjoiY2hpcnBzdGFjayIsInN1YiI6IjVmM2FlZDdmLTA5NGItNDFhZC05NDdjLTBmMzE3NzAwNTVmMyIsInR5cCI6ImtleSJ9.3h3-YKpbUXvifb9kn8Rzvw6IVtezubrr6By2aZmhV-0'
#   }
#   response = requests.request("DELETE", url, headers=headers)
#   print(response.text)


###############################################################
#Adding 10 devices

# import http.client
# import json
# #import time


# devEui=int("fa41a8fffe100000", 16)

# for i in range(10):

#   conn = http.client.HTTPSConnection("chirpstack-api.iotserv.ru")
#   payload = json.dumps({
#     "device": {
#       "applicationId": "0f516251-75bc-4699-919d-bcd398a50754",
#       "description": "oas-testDev",
#       "devEui": format(devEui+i, 'x'),
#       "deviceProfileId": "29d26ba4-2bf0-452e-9341-2671f442c7da",
#       "isDisabled": False,
#       "joinEui": "0000000000000000",
#       "name": "testDev_{}".format(i),
#       "skipFcntCheck": False
#     }
#   })
#   print(payload)
#   headers = {
#     'Content-Type': 'application/json',
#     'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjaGlycHN0YWNrIiwiaXNzIjoiY2hpcnBzdGFjayIsInN1YiI6IjVmM2FlZDdmLTA5NGItNDFhZC05NDdjLTBmMzE3NzAwNTVmMyIsInR5cCI6ImtleSJ9.3h3-YKpbUXvifb9kn8Rzvw6IVtezubrr6By2aZmhV-0'
#   }
  
#   conn.request("POST", "/api/devices", payload, headers)
#   res = conn.getresponse()
#   data = res.read()
#   print(data.decode("utf-8"))

#   #time.sleep(1)

#####################################################################
#Send to one device

# import http.client
# import json


# conn = http.client.HTTPSConnection("chirpstack-api.iotserv.ru")
# payload = json.dumps({
#     "queueItem": {
#       "data": "SGVsbG8gV29ybGQh",
#       "fPort": 8
#     }
# })

# headers = {
#   'Content-Type': 'application/json',
#   'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjaGlycHN0YWNrIiwiaXNzIjoiY2hpcnBzdGFjayIsInN1YiI6IjVmM2FlZDdmLTA5NGItNDFhZC05NDdjLTBmMzE3NzAwNTVmMyIsInR5cCI6ImtleSJ9.3h3-YKpbUXvifb9kn8Rzvw6IVtezubrr6By2aZmhV-0'
# }
# conn.request("POST", "/api/devices/fa41a8fffe100004/queue", payload, headers)
# res = conn.getresponse()
# data = res.read()
# print(data.decode("utf-8"))

###########################################################################
#Send data for 10 devices

# import http.client
# import json


# url = "https://chirpstack-api.iotserv.ru/api/devices?limit=10&applicationId=0f516251-75bc-4699-919d-bcd398a50754"
# headers = {
#   'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjaGlycHN0YWNrIiwiaXNzIjoiY2hpcnBzdGFjayIsInN1YiI6IjVmM2FlZDdmLTA5NGItNDFhZC05NDdjLTBmMzE3NzAwNTVmMyIsInR5cCI6ImtleSJ9.3h3-YKpbUXvifb9kn8Rzvw6IVtezubrr6By2aZmhV-0'
# }
# response = requests.request("GET", url, headers=headers)
# print(response.text)

# arr=json.loads(response.text)

# for dev in arr['result']: 

#   conn = http.client.HTTPSConnection("chirpstack-api.iotserv.ru")
#   payload = json.dumps({
#       "queueItem": {
#         "data": "SGVsbG8gV29ybGQh",
#         "fPort": 8
#       }
#   })

#   headers = {
#     'Content-Type': 'application/json',
#     'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjaGlycHN0YWNrIiwiaXNzIjoiY2hpcnBzdGFjayIsInN1YiI6IjVmM2FlZDdmLTA5NGItNDFhZC05NDdjLTBmMzE3NzAwNTVmMyIsInR5cCI6ImtleSJ9.3h3-YKpbUXvifb9kn8Rzvw6IVtezubrr6By2aZmhV-0'
#   }
#   conn.request("POST", f"/api/devices/{dev['devEui']}/queue", payload, headers)
#   res = conn.getresponse()
#   data = res.read()
#   print(data.decode("utf-8"))
  

#############################################################################
#Rename

import http.client
import json


url = "https://chirpstack-api.iotserv.ru/api/devices?limit=10&applicationId=0f516251-75bc-4699-919d-bcd398a50754"
headers = {
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjaGlycHN0YWNrIiwiaXNzIjoiY2hpcnBzdGFjayIsInN1YiI6IjVmM2FlZDdmLTA5NGItNDFhZC05NDdjLTBmMzE3NzAwNTVmMyIsInR5cCI6ImtleSJ9.3h3-YKpbUXvifb9kn8Rzvw6IVtezubrr6By2aZmhV-0'
}
response = requests.request("GET", url, headers=headers)
print(response.text)

arr=json.loads(response.text)

i=1

for dev in arr['result']: 

  conn = http.client.HTTPSConnection("chirpstack-api.iotserv.ru")
  payload = json.dumps({
    "device": {
      "applicationId": "0f516251-75bc-4699-919d-bcd398a50754",
      "deviceProfileId": "29d26ba4-2bf0-452e-9341-2671f442c7da",
      "name": f'new_dev_{i}'
    }
  })

  i+=1
 
  headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjaGlycHN0YWNrIiwiaXNzIjoiY2hpcnBzdGFjayIsInN1YiI6IjVmM2FlZDdmLTA5NGItNDFhZC05NDdjLTBmMzE3NzAwNTVmMyIsInR5cCI6ImtleSJ9.3h3-YKpbUXvifb9kn8Rzvw6IVtezubrr6By2aZmhV-0'
  }
  conn.request("PUT", f"/api/devices/{dev['devEui']}", payload, headers)
  res = conn.getresponse()
  data = res.read()
  print(data.decode("utf-8"))

########################################################################
