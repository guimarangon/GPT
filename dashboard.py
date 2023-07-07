from flask import render_template, request
from database_connector import db, FinancialData
from data_visualization import visualize_data
from real_time_update import update_real_time_data
from external_data_link import fetch_external_data
from main import app

@app.route('/')
def dashboard():
    data = FinancialData.query.all()
    chart = visualize_data(data)
    return render_template('dashboard.html', chart=chart)

@app.route('/update', methods=['POST'])
def update_data():
    if request.form.get('update-button') == 'UPDATE_DATA':
        update_real_time_data(db)
    return redirect(url_for('dashboard'))

@app.route('/fetch', methods=['POST'])
def fetch_data():
    if request.form.get('update-button') == 'FETCH_EXTERNAL_DATA':
        fetch_external_data(db)
    return redirect(url_for('dashboard'))