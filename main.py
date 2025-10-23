#get
import requests

# user_input = input("Enter it:")
# get_url = f"https://jsonplaceholder.typicode.com/todos/{user_input}"


# get_response = requests.get(get_url)
# print(get_response.json())


#POST
to_do_item = {"userId": 1,"id": 1,"my_title": "delectus aut autem","completed": False}
post_url = f"https://jsonplaceholder.typicode.com/todos/"
post_response = requests.post(post_url, json=to_do_item, headers={"Content-Type": "application/json"})
# print(post_response.json())
print(post_response.headers)