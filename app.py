import uuid

from flask import Flask, request
from flask_smorest import abort
from db import households, requests


app = Flask(__name__)


@app.get("/households")
def get_households():
    pass

@app.get("/households/<string:household_id>")
def get_household(household_id):
    pass


@app.post("/households")
def create_household():
    pass


@app.post("/requests")
def create_request():
    pass


@app.get("/requests/<string:request_id>")
def get_request(request_id):
    pass