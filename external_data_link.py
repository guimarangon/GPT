import requests
from database_connector import db, FinancialData

FETCH_EXTERNAL_DATA = "FETCH_EXTERNAL_DATA"

def fetch_external_data():
    response = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vTGRs6Gx4xy7fSnganAALVC1hqzLw2Iyw9M0eOBkAMcVk2ypMmlP11ivuH9Df2PwA/pubhtml?gid=1728458610&single=true')
    data = response.json()

    for item in data:
        financial_data = FinancialData(
            date=item['date'],
            revenue=item['revenue'],
            expenses=item['expenses'],
            profit=item['profit']
        )
        db.session.add(financial_data)

    db.session.commit()
