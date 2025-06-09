
import gradio as gr
import pandas as pd
import joblib
import os

from auth.auth import signup_user, login_user
from utils.preprocessing import preprocess_uploaded_file
from dashboards.business_analytics import (
    create_revenue_trend,
    create_aov_chart,
    create_top_customers
)

model = joblib.load("models/clv.pkl")

session = {"authenticated": False}

def signup(email, password):
    return signup_user(email, password)

def login(email, password):
    if login_user(email, password):
        session["authenticated"] = True
        return "Login successful! Go to the 'Upload & Predict' tab."
    else:
        return "Invalid credentials."

def predict_clv(file):
    if not session["authenticated"]:
        return "Please log in first.", None, None, None, None

    features, customer_summary = preprocess_uploaded_file(file)
    clv_pred = model.predict(features)
    result = features.copy()
    result['Predicted CLV'] = clv_pred
    result.reset_index(inplace=True)

    if file.name.endswith(".csv"):
        df = pd.read_csv(file.name, encoding='ISO-8859-1')
    else:
        df = pd.read_excel(file.name)

    fig1 = create_revenue_trend(df)
    fig2 = create_aov_chart(df)
    fig3 = create_top_customers(df)

    return "CLV prediction completed!", result, fig1, fig2, fig3

with gr.Blocks(theme=gr.themes.Soft()) as app:
    gr.Markdown("## 🧠 Customer Lifetime Value (CLV) Prediction App")
    with gr.Tabs():
        with gr.TabItem("👤 Login / Sign Up"):
            with gr.Row():
                with gr.Column():
                    gr.Markdown("### 🔐 Sign Up")
                    email_signup = gr.Textbox(label="Email")
                    password_signup = gr.Textbox(label="Password", type="password")
                    signup_btn = gr.Button("Sign Up")
                    signup_output = gr.Textbox(label="Signup Status")
                    signup_btn.click(fn=signup, inputs=[email_signup, password_signup], outputs=signup_output)
                with gr.Column():
                    gr.Markdown("### 🔑 Log In")
                    email_login = gr.Textbox(label="Email")
                    password_login = gr.Textbox(label="Password", type="password")
                    login_btn = gr.Button("Log In")
                    login_output = gr.Textbox(label="Login Status")
                    login_btn.click(fn=login, inputs=[email_login, password_login], outputs=login_output)

        with gr.TabItem("📁 Upload & Predict"):
            file_upload = gr.File(label="Upload Transaction Data (.csv or .xlsx)")
            run_btn = gr.Button("Predict CLV")
            result_text = gr.Textbox(label="Status")
            result_df = gr.Dataframe(label="Predicted CLV")
            revenue_plot = gr.Plot(label="Revenue Trend")
            aov_plot = gr.Plot(label="AOV Chart")
            top_cust_plot = gr.Plot(label="Top Customers")
            run_btn.click(fn=predict_clv, inputs=file_upload,
                          outputs=[result_text, result_df, revenue_plot, aov_plot, top_cust_plot])

app.launch(share=True)
