from django.shortcuts import render
import requests
import psycopg2
import psycopg2.extras

class DbHelper:

    def category(self,id):
        response=requests.get(f'http://127.0.0.1:8000/category/?id={id}')
        return response.json()

    def product2(self,id):
        response=requests.get(f'http://127.0.0.1:8000/product/?id={id}')
        return response.json()








    def category_parent(self):
        response=requests.get('http://127.0.0.1:8000/category-list1/')
        return response.json()

    def category_child(self,id):
        response=requests.get(f'http://127.0.0.1:8000/category-list2/?id={id}')
        if response.json()!=[]:
            return response.json()


    def product_type(self,id):
        button=[]
        response=requests.get(f'http://127.0.0.1:8000/category-product/?id={id}')
        data=response.json()
        for i in data:
            response=requests.get(f"http://127.0.0.1:8000/category-type/?id={i['product_type']}")
            type=response.json()
            button.append(type[0])
        return button

    def product(self,category_id,type_id):
        response = requests.get(f'http://127.0.0.1:8000/category-product/?id={category_id}')
        data=response.json()
        for i in data:
            if i['product_type']==type_id:
                return i

    def product_image(self,id):
        x={}
        response = requests.get(f'http://127.0.0.1:8000/category-image/?id={id}')
        data=response.json()
        for i in data:
            if i['is_main']==True:
                x=i
                break
        return x



class DbHelper2:

    def __init__(self):
        self.conn=psycopg2.connect(
            host="127.0.0.1",
            database="loyiha",
            user="postgres",
            password="root"
        )

        self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    def insert_data(self,price,prise,product_name,user_id):
        self.cur.execute(f"""
        INSERT INTO orders(price,prise,product_name,user_id)
        VALUES({price},{prise},'{product_name}',{user_id})
        """)
        self.conn.commit()

    def read_product(self,id):
        self.cur.execute(f"""
        SELECT * FROM orders WHERE user_id={id}
        """)
        rows=self.cur.fetchall()
        return rows

    def remove(self, id):
        self.cur.execute(f"""
        DELETE FROM orders WHERE user_id={id}
        """)
        self.conn.commit()

    def remove_product(self, id):
        self.cur.execute(f"""
        DELETE FROM orders WHERE id={id}
        """)
        self.conn.commit()




