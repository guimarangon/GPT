import requests
from database_connector import db, FinancialData

FETCH_EXTERNAL_DATA = "FETCH_EXTERNAL_DATA"

def fetch_external_data():
    response = requests.get('https://external-data-source.com/financial-data')
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