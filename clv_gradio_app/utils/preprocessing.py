
import pandas as pd

def preprocess_uploaded_file(file):
    if file.name.endswith('.csv'):
        df = pd.read_csv(file.name, encoding='ISO-8859-1')
    else:
        df = pd.read_excel(file.name)

    df.dropna(subset=['CustomerID'], inplace=True)
    df = df[df['Quantity'] > 0]
    df = df[df['UnitPrice'] > 0]
    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

    summary = df.groupby("CustomerID").agg({
        "InvoiceDate": [lambda x: (x.max() - x.min()).days, lambda x: (df["InvoiceDate"].max() - x.max()).days],
        "InvoiceNo": "nunique",
        "TotalPrice": "sum"
    }).reset_index()

    summary.columns = ["CustomerID", "recency", "T", "frequency", "monetary_value"]
    summary = summary[summary["monetary_value"] > 0]
    X = summary.set_index("CustomerID")[["frequency", "recency", "T", "monetary_value"]]
    return X, summary
