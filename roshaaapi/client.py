import requests
import json


# >>>>>>>>>>>>>>>>>>>>>> Using different function <<<<<<<<<<<<<<<<<<<<<<<<<<

    # >>>>>>>>>>>>>>>>>>>>>> GET request <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# native_type = {
#     "id" : 2
# }
# json_string = json.dumps(native_type)
# response = requests.get("http://127.0.0.1:8000/api/", data=json_string)
# print(response)
# print(response.json())



# >>>>>>>>>>>>>>>>>>>>>> POST request <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# native_type = {
#     "name" : "Vijay",
#     "salary" : 32000,
#     "address" : "Gurugram"
# }
# json_string = json.dumps(native_type)
# response = requests.post("http://127.0.0.1:8000/api/create/", data = json_string)
# print(response)
# print(response.json())


# >>>>>>>>>>>>>>>>>>>>>>>>> PUT request <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# native_type = {
#     "id" : 4,
#     "name" : "Ajay",
#     "salary" : 32000
# }
# json_string = json.dumps(native_type)
# response = requests.put("http://127.0.0.1:8000/api/update/", data = json_string)
# print(response)
# print(response.json())


# >>>>>>>>>>>>>>>>>>>>>>>> DELETE request <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# native_type = {
#     "id" : 4
# }
# json_string = json.dumps(native_type)
# response = requests.delete("http://127.0.0.1:8000/api/delete/", data = json_string)
# print(response)
# print(response.json())






# >>>>>>>>>>>>>>>>>>> using single function <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    # >>>>>>>>>>>>>>>>>>>>>> GET request <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# native_type = {
#     "id" : 2
# }
# json_string = json.dumps(native_type)
# response = requests.get("http://127.0.0.1:8000/api/", data=json_string)
# print(response)
# print(response.json())



# >>>>>>>>>>>>>>>>>>>>>> POST request <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# native_type = {
#     "name" : "Vijay",
#     "salary" : 32000,
#     "address" : "Gurugram"
# }
# json_string = json.dumps(native_type)
# headers = {
#     "content-Type" : "application/json"
# }
# response = requests.post("http://127.0.0.1:8000/api/", data = json_string, headers=headers)
# print(response)
# print(response.json())


# >>>>>>>>>>>>>>>>>>>>>>>>> PUT request <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# native_type = {
#     "id" : 7,
#     "name" : "Ajay",
#     "salary" : 32000
# }
# json_string = json.dumps(native_type)
# response = requests.put("http://127.0.0.1:8000/api/", data = json_string)
# print(response)
# print(response.json())


# >>>>>>>>>>>>>>>>>>>>>>>> DELETE request <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# native_type = {
#     "id" : 7
# }
# json_string = json.dumps(native_type)
# response = requests.delete("http://127.0.0.1:8000/api/", data = json_string)
# print(response)
# print(response.json())


