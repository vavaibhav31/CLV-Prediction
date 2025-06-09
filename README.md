# 🧠 Customer Lifetime Value (CLV) Prediction App

A full-stack Machine Learning web application built using **Gradio** for the interface, **XGBoost** for CLV prediction, and **MongoDB** for secure user authentication. This app empowers business stakeholders with real-time insights into customer behavior and potential value, helping them make informed marketing and retention decisions.

---

## 🚀 Problem Statement

Many businesses struggle to measure the future value of customers accurately. Traditional CLV calculation methods are either too simplistic or too complex to be integrated into real-time decision-making. Moreover, there's often a disconnect between technical models and business users due to lack of usable interfaces.

**The Solution:**  
A no-code interactive platform where users can:
- Upload customer transaction data.
- Automatically clean, preprocess, and transform the data.
- Predict Customer Lifetime Value using a trained ML model.
- Explore interactive visual dashboards for strategic insights.
- Use secure login to protect business-sensitive data.

---

## 💡 Features

- 🔐 **User Authentication**  
  Sign-up and log-in using email/password credentials stored securely in MongoDB.

- 📁 **Dynamic File Upload**  
  Supports both `.csv` and `.xlsx` formats for ease of use across teams.

- 🧼 **Smart Data Preprocessing**  
  Automatically handles missing values, negative transactions, and date conversions.

- 🧠 **CLV Prediction**  
  Based on frequency, recency, T (tenure), and monetary value — powered by `XGBoost`.

- 📈 **Business Analytics Dashboards**  
  Visualizations include:
  - Revenue Trend (monthly)
  - Average Order Value (AOV)
  - Top Customers by Revenue

- ⚡ **Interactive Gradio UI**  
  Intuitive interface that’s shareable via public links and suitable for stakeholders.

---

## 🧠 Machine Learning Pipeline

- **Feature Engineering**:
  - Frequency: Number of repeat purchases
  - Recency: Time since last purchase
  - T: Time since first purchase
  - Monetary Value: Avg. order value

- **Model**:
  - `XGBoostRegressor` trained on engineered features
  - Output: Predicted CLV value per customer
  - Saved in `models/clv.pkl` using `joblib`

---

## 🛠️ MongoDB Integration

MongoDB Atlas is used to store user credentials securely. Upon signup or login:
- A new record is inserted into the `users` collection
- Passwords are hashed before storage for security
- Every time a new user signs up, data appears in real time in MongoDB

✅ **Example Document Format**:
```json
{
  "_id": ObjectId("..."),
  "email": "user@example.com",
  "password": "hashed_password"
}
