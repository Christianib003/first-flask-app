import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import households, requests


request_blp = Blueprint(
    "requests",
    __name__,
    description="Operations on collection requests"
    )


request_blp.route("/requests")
class Request(MethodView):
    def get(self, request_id):
        """
        Retrieve a request by its ID.

        Args:
            request_id (int): The ID of the request to retrieve.

        Returns:
            dict: The request object.

        Raises:
            NotFound: If the request with the given ID is not found.
        """
        try:
            return requests[request_id]
        except KeyError:
            abort(404, message="Request not found")


    def post(self):
        """
        Create a new request with the provided data.

        This function creates a new request based on the data provided in
        the request payload.

        Returns:
            tuple: A tuple containing the newly created request and
            the HTTP status code.
        """
        request_data = request.get_json()
        # Check if request_data contains the required keys
        if(
            "household_id" not in request_data
            or "amount" not in request_data
        ):
            abort(
                400,
                message="Request must include household_id and amount"
            )
        # Check if request_data["household_id"] is already in requests
        for request_key in requests.values():
            if(
                request_data["household_id"] == request_key["household_id"]
            ):
                abort(
                    400,
                    message="Request already exists for this household"
                )
        # Check if request_data["household_id"] is in households
        if request_data["household_id"] not in households:
            abort(404, message="Household not found")
        # Create a new request
        request_id = uuid.uuid4().hex
        new_request = {
            "household_id": request_data["household_id"],
            "request_id": request_id,
            "amount": request_data["amount"],
            "status": "pending"
        }
        requests[request_id] = new_request
        return new_request, 201
