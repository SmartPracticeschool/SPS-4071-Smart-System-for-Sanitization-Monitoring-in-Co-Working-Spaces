# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 21:12:47 2020

@author: Sai Nidhi
"""

from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    names = ['Shalini','deepti','sahas']
    date = []
    for i in names:
        url = "https://hqzkbqq5d2.execute-api.ap-south-1.amazonaws.com/sanitizerretrieve?Name="+i
        resp = requests.get(url)
        data = resp.json()
        print(data)
        #[{'name': 'sandeep', 'date': '31-09-2020'}]
        date.append(data['Date'])
    return render_template('stats.html', p1= names[0],d1=date[0], p2=names[1], d2=date[1])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)