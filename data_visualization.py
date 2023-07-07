import matplotlib.pyplot as plt
import pandas as pd
from database_connector import FinancialData

def visualize_data(db):
    # Fetch data from the database
    data = pd.read_sql(db.session.query(FinancialData).statement, db.session.bind)

    # Create a figure and a set of subplots
    fig, axs = plt.subplots(2)

    # Plot the data
    axs[0].plot(data['date'], data['revenue'], label='Revenue')
    axs[0].set_title('Revenue Over Time')
    axs[0].set_xlabel('Date')
    axs[0].set_ylabel('Revenue')
    axs[0].legend()

    axs[1].plot(data['date'], data['expenses'], label='Expenses')
    axs[1].set_title('Expenses Over Time')
    axs[1].set_xlabel('Date')
    axs[1].set_ylabel('Expenses')
    axs[1].legend()

    # Show the plot
    plt.show()