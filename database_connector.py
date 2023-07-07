from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Float, Date
from config import DATABASE_CONFIG

db = SQLAlchemy()

def connect_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONFIG['uri']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = DATABASE_CONFIG['track_modifications']
    db.init_app(app)

class FinancialData(db.Model):
    __tablename__ = 'financial_data'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    revenue = Column(Float)
    expenses = Column(Float)
    net_profit = Column(Float)

    def __init__(self, date, revenue, expenses, net_profit):
        self.date = date
        self.revenue = revenue
        self.expenses = expenses
        self.net_profit = net_profit