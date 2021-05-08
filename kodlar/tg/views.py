from django.shortcuts import render
import requests

class DbHelper:

    def category_parent(self):
        print("request")
        json=requests.get('http://127.0.0.1:8000/category-list1/')
        return json
