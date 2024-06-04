import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import households


household_blp = Blueprint(
    "households",
    __name__,
    description="Operations on households"
    )


@household_blp.route("/households")
class HouseholdsList(MethodView):   
    """
    Represents a collection of households.
    """

    def get(self):
        """
        Retrieves a list of all households.
        
        Returns:
            dict: A dictionary containing the list of households.
        """
        return {"households": list(households.values())}

    def post(self):
        """
        Create a new household with the provided data.

        Returns:
            tuple: A tuple containing the new household data and the HTTP
            status code.

        Raises:
            HTTPException: If the request data is missing required keys or
            if the household already exists.
        """
        household_data = request.get_json()
        # Check if household_data contains the required keys
        if(
            "area" not in household_data
            or "address" not in household_data
        ):
            abort(
                400,
                message="Household must include area and address"
            )
        # Check if household_data["area"] is already in households
        for household_key in households.values():
            if(
                household_data["area"] == household_key["area"]
                and household_data["address"] == household_key["address"]
            ):
                abort(
                    400,
                    message="Household already exists"
                )
        # Create a new household
        household_id = uuid.uuid4().hex
        new_household = {
            "area": household_data["area"],
            "address": household_data["address"],
            "household_id": household_id
            }
        households[household_id] = new_household
        return new_household, 201


@household_blp.route("/households/<string:household_id>")
class Household(MethodView):
    """
    Represents a single household.
    """

    def get(self, household_id):
        """
        Retrieve a household by its ID.

        Args:
            household_id (int): The ID of the household to retrieve.

        Returns:
            dict: The household information.

        Raises:
            404: If the household is not found.
        """
        try:
            return households[household_id]
        except KeyError:
            abort(404, message="Household not found")
