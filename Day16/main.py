from fastapi import FastAPI 

app = FastAPI()

# http://127.0.0.1:8000
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users")
async def get_users():
    return {"users": [
        {"id" : 1, "name": "Alice"},
        {"id" : 2, "name": "Bob"},
    ]}

arr = [
        {"id" : 1, "name": "Alice"},
        {"id" : 2, "name": "Bob"},
        {"id" : 3, "name": "Charlie"},
        {"id" : 4, "name": "David"},
        {"id" : 5, "name": "Eve"},
        {"id" : 6, "name": "Frank"},
        {"id" : 7, "name": "Grace"},
        {"id" : 8, "name": "Heidi"},
        {"id" : 9, "name": "Ivan"},
        {"id" : 10, "name": "Judy"},
    ]

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return {"user": {"id": user_id, "name": f"User {arr[user_id - 1]['name']}"}}


@app.get("/getusers")
async def get_users(limit: int = 2, search: str = "", aarush : str = "default"):
    return {"users": arr[:limit], "search": search, "aarush": aarush}