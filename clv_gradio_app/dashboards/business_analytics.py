
import pandas as pd
import plotly.express as px

def create_revenue_trend(df):
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
    monthly_revenue = df.groupby(df['InvoiceDate'].dt.to_period("M"))['TotalPrice'].sum()
    monthly_revenue.index = monthly_revenue.index.to_timestamp()
    return px.line(x=monthly_revenue.index, y=monthly_revenue.values, labels={"x": "Month", "y": "Revenue"}, title="Monthly Revenue")

def create_aov_chart(df):
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
    df['Month'] = df['InvoiceDate'].dt.to_period('M')
    aov = df.groupby('Month').apply(lambda x: x['TotalPrice'].sum() / x['InvoiceNo'].nunique())
    aov.index = aov.index.to_timestamp()
    return px.bar(x=aov.index, y=aov.values, labels={"x": "Month", "y": "AOV"}, title="Average Order Value (AOV)")

def create_top_customers(df):
    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
    top_customers = df.groupby('CustomerID')['TotalPrice'].sum().sort_values(ascending=False).head(10)
    return px.bar(x=top_customers.index.astype(str), y=top_customers.values, labels={"x": "CustomerID", "y": "Revenue"}, title="Top 10 Customers by Revenue")
