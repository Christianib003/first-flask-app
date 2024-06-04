from flask import Flask


app = Flask(__name__)


households = [
    {
        "house_number": "KK 123",
        "area": "Kicukiro",
        "requests": [
            {
                "amount": 5,
                "is_completed": False
            }
        ]
    }
]
