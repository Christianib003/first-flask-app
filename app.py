from flask import Flask, request


app = Flask(__name__)

stores = [
    {
        "name": "My Wonderful Store",
        "items": [
            {
                "name": "My Item",
                "price": 15.99
            },
            {
                "name": "My Item 2",
                "price": 10.99
            }
        ]
    }
]

@app.route('/stores', methods=['GET'])
def get_stores():
    return {"stores": stores}

@app.route('/stores', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data['name'], "items": []}
    stores.append(new_store)
    return new_store, 201