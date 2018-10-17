from flask_restful import Resource
from flask import Flask, jsonify, make_response, request

sales = []
products = []


class SpecificSale(Resource):
    def get(self, id):
        return make_response(jsonify(
            {
                'Status': "OK",
                'Message': "Success",
                'specific sale': sales[id]
            }), 200)


class SpecificProduct(Resource):
    def get(self, id):
        return make_response(jsonify(
            {
                'Status': "OK",
                'Message': "Success",
                'specific product': products[id]
            }), 200)


class Products(Resource):
    def get(self):
        return make_response(jsonify(
            {
                'Status': "Ok",
                'Message': "Success",
                'My Products': products
            }), 200)

    def post(self):
        data = request.get_json()
        id = len(products) + 1
        productName = data['Product Name']
        category = data['Category']
        stockBalance = data['Stock Balance']
        minStockBalance = data['Minimum Inventory']
        price = data['Price']

        payload = {
            'id': id,
            'Description': {
                'Product Name': productName, 'Stock Balance': stockBalance,
                'Minimum Inventory': minStockBalance,
                'Category': category
                },
            'Price': price
        }
        products.append(payload)

        return make_response(jsonify(
            {
                'Message': 'Product created',
                'status': 'ok',
                'Data': products
            }), 201)
