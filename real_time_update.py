```python
from flask_socketio import SocketIO, emit
from database_connector import db, FinancialData, connect_db

socketio = SocketIO()

UPDATE_DATA = 'UPDATE_DATA'

@socketio.on(UPDATE_DATA)
def update_real_time_data():
    connect_db()
    financial_data = FinancialData.query.all()
    data = [data.serialize for data in financial_data]
    emit(UPDATE_DATA, {'data': data})
```