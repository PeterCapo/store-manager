from flask_restful import Resource
from flask import Flask, jsonify, make_response, request

sales = []
products = []


class SpecificProduct(Resource):
    def get(self, id):
        return make_response(jsonify(
            {
                'Status': "OK",
                'Message': "Success",
                'specific product': products[id]
            }), 200)
