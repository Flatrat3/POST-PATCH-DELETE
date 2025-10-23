import requests

# to_do_item = {"userId": 3, "id": 6, "title": "Salam Asim", "completed": True}
# get_url = "https://jsonplaceholder.typicode.com/todos/3"
#
# put_response = requests.put(get_url, json=to_do_item)
# print(put_response.json())


#Delete

delete_url = f"https://jsonplaceholder.typicode.com/todos/4"
delete_response = requests.delete(delete_url)
print(delete_response)
print(delete_response.status_code)
