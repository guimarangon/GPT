from flask import Flask
from database_connector import db, connect_db
from real_time_update import update_real_time_data
from external_data_link import fetch_external_data
from config import APP_CONFIG

app = Flask(__name__)
app.config.from_object(APP_CONFIG)

@app.before_first_request
def setup():
    connect_db(app)

@app.route('/update_data', methods=['POST'])
def update_data():
    update_real_time_data(db)
    return "Data updated successfully", 200

@app.route('/fetch_external_data', methods=['GET'])
def get_external_data():
    fetch_external_data(db)
    return "External data fetched successfully", 200

if __name__ == '__main__':
    app.run(debug=True)