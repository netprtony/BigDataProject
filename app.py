from flask import Flask, render_template
from pymongo import MongoClient
import pandas as pd
app = Flask(__name__)

# Kết nối tới MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['Sleep_heathy']
collection = db['Person']

@app.route('/')
def home():
    sleep_data_list = list(collection.find())

    # Tính toán các thống kê
    total_records = len(sleep_data_list)
    avg_sleep_duration = sum(d['Sleep Duration'] for d in sleep_data_list) / total_records
    avg_stress_level = sum(d['Stress Level'] for d in sleep_data_list) / total_records
    avg_physical_activity = sum(d['Physical Activity Level'] for d in sleep_data_list) / total_records

    # Thêm các thống kê vào context để truyền vào template
    return render_template('sleep_list.html', 
                           sleep_data=sleep_data_list, 
                           total_records=total_records, 
                           avg_sleep_duration=avg_sleep_duration, 
                           avg_stress_level=avg_stress_level,
                           avg_physical_activity=avg_physical_activity)




@app.route('/export_csv')
def export_csv():
    # Lấy dữ liệu từ MongoDB
    sleep_data_list = list(collection.find())
    
    # Tạo DataFrame từ dữ liệu MongoDB
    df = pd.DataFrame(sleep_data_list)
    
    # Xuất dữ liệu ra file CSV
    df.to_csv('sleep_data.csv', index=False)
    
    return "Data exported to CSV!"

if __name__ == '__main__':
    app.run(debug=True)