from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

# Kết nối tới MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['Sleep_heathy']
collection = db['Person']

@app.route('/')
def home():
    sleep_data_list = list(collection.find())
    return render_template('sleep_list.html', sleep_data=sleep_data_list)

if __name__ == '__main__':
    app.run(debug=True)