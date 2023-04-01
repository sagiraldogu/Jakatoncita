from config.mysqlconnection import connectToMySQL
from flask import flash
from datetime import *


class Product:
    def __init__(self,data):
        self.id = data['id']
        self.name_product = data['name_product']
        self.cha_num = data['chasis_num']
        self.motor_num = data['motor_num']
        self.brand = data['brand']
        self.model = data['model']
        self.category = data['category']
        self.url_img = data['url_img']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    def time_validator(self):
        now = datetime.today()
        return now
    
    @classmethod
    def save (self, form ):
        query = "INSERT INTO product (name_product, cha_num, motor_num, brand, model, category, url_img, created_at, update_at, user_id ) VALUES( %(name_product)s,%(cha_num)s, %(motor_num)s, %(brand)s, %(model)s, %(category)s, %(url_img)s, %(created_at)s, %(update_at)s, %(user_id)s );"
        newId = connectToMySQL('ZINK').query_db(query,form)
        return newId
    
    @classmethod
    def get_product_by_user(self, form ):
        query = "SELECT product.*,name_product FROM product LEFT JOIN user ON user.id = product.user_id WHERE user_id = %(id)s;"
        result = connectToMySQL('ZINK').query_db(query,form)
        products = []
        for product in result:
            products.append(self(product))
        return products

   
