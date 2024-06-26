from fastapi import FastAPI

app = FastAPI(
    title="Tradding App"
)

fake_users = [
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "investor", "name": "John"},
    {"id": 3, "role": "trader", "name": "Matt"},
]


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return [user for user in fake_users if user.get("id") == user_id]


fake_trades = [
    {"id": 1, "user_id": 1, "currency": "BTC", "side": "buy", "price": 121, "amount": 2.12},
    {"id": 2, "user_id": 1, "currency": "BTC", "side": "sell", "price": 122, "amount": 2.12},
    {"id": 3, "user_id": 1, "currency": "BTC", "side": "buy", "price": 123, "amount": 2.12},
    {"id": 4, "user_id": 1, "currency": "BTC", "side": "sell", "price": 124, "amount": 2.12},
    {"id": 5, "user_id": 1, "currency": "BTC", "side": "buy", "price": 125, "amount": 2.12},
    {"id": 6, "user_id": 1, "currency": "BTC", "side": "sell", "price": 126, "amount": 2.12},
    {"id": 7, "user_id": 1, "currency": "BTC", "side": "buy", "price": 127, "amount": 2.12},
    {"id": 8, "user_id": 1, "currency": "BTC", "side": "sell", "price": 128, "amount": 2.12},

]


@app.get("/trades")
def get_trades(limit: int, offets: int):
    return fake_trades[offets:][:limit]


fake_users2 = [
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "investor", "name": "John"},
    {"id": 3, "role": "trader", "name": "Matt"},
]


@app.post("/users/{user_id}")
def change_user_name(user_id: int, new_name: str):
    current_name = list(filter(lambda user: user.get("id") == user_id, fake_users2))[0]
    current_name["name"] = new_name
    return {"status": 200, "data": current_name}
