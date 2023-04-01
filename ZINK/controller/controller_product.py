from flask import Flask, request
from model.product import Product 


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/products", methods=['GET'] )
def get_products():
    # read products from db
    data = Product.get_product_by_user()
    print("Data send")
    return data


@app.route("/products", methods=['POST'] )
def post_product():
    # write products from db
    data = {

        'id' : 'id',
        'name_product' : 'name_product',
        'chasis_num' : 'chasis_num',
        'motor_num' : 'motor_num',
        'brand' : 'brand',
        'model' : 'model',
        'category' : 'category',
        'url_img' : 'url_img',
        'user_id' : 'user_id'
        }
    Product.save(data)
    
    print("Data save")
    return data
