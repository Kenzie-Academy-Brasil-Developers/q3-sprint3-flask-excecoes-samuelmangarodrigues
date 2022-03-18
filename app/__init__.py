import json
from turtle import st
from flask import Flask, jsonify, request
from app.services import reader_users,write_users


app=Flask(__name__)

@app.get('/users')
def user_data():
    return jsonify(reader_users()),200

@app.post('/users')
def register():
    data_body=request.get_json()
    return write_users(data_body),201