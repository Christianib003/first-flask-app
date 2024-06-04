from flask import Flask, request


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

@app.post("/households")
def create_household():
    """
    Creates a new household.

    Returns:
        dict: A dictionary containing the newly created household.
    """
    request_data = request.get_json()
    new_household = {
        "house_number": request_data["house_number"],
        "area": request_data["area"],
        "requests": []
    }
    households.append(new_household)
    return new_household