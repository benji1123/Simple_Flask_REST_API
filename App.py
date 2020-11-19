"""
This project is based on:
towards data science.
The Right Way to Build an API with Python.
by James Briggs, Sept 11 2020.
"""

from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd

app = Flask(__name__)
api = Api(app)


def append_dict_to_csv(data, csv_filename):
    """Add a row to a csv"""
    data = pd.DataFrame(data, index=[0])
    data.to_csv(csv_filename, mode='a', header=False, index=False)


class Users(Resource):
    @staticmethod
    def get():
        data = pd.read_csv('users.csv')
        data = data.to_dict()
        return {'data': data}, 200

    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('userId', required=True)
        parser.add_argument('name', required=True)
        parser.add_argument('city', required=True)
        parser.add_argument('locations', required=True)
        args = parser.parse_args()  # dictionary
        append_dict_to_csv(data=args, csv_filename="users.csv")
        return {'data': args}, 200


api.add_resource(Users, '/users')

if __name__ == '__main__':
    app.run()
