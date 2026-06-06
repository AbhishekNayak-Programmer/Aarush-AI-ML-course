import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

print(response.status_code)
# print(response.text)

users = response.json()
print(users[0]['email'])


res = requests.get("https://jsonplaceholder.typicode.com/posts/10")
# print(res.text)

github_response = requests.get("https://api.github.com/")
# print(github_response.text)

# POST DATA
user = {
    "name" : "Abhishek",
    "age" : 26,
    "address": "India"
}

post_res = requests.post("https://httpbin.org/post", user)
print(post_res.text)
data = post_res.json()["form"]
print(data)

patch_res = requests.patch("https://httpbin.org/patch", user)
print(patch_res.text)
data = patch_res.json()["form"]
print(data)

delete_res = requests.delete("https://httpbin.org/delete")
print(delete_res.text)
data = delete_res.json()["form"]
print(data)


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")


s1 = Student("Abhishek", 26)
s2 = Student("Adarsh", 16)

s1.introduce()
s2.introduce()