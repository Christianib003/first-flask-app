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

@app.route("/households")
def get_households():
    """
    Retrieves the list of households.
    
    Returns:
        dict: A dictionary containing the list of households.
    """
    return {"households": households}