📊 Real-Time Financial Intelligence Platform

A production-grade real-time financial analytics platform built using FastAPI, PostgreSQL, ETL pipelines, and Streamlit.
This project fetches live cryptocurrency market data, processes it through an ETL pipeline, stores it in PostgreSQL, and visualizes insights through an interactive dashboard.

🌐 Live Demo
🚀 Live Dashboard

Real-Time Financial Intelligence Dashboard

⚡ Live API

FastAPI Backend Service

📄 Swagger API Documentation

Swagger Docs

💻 GitHub Repository

GitHub Repository

🚀 Features

✅ Real-time cryptocurrency market analytics
✅ Automated ETL pipeline
✅ PostgreSQL cloud database integration
✅ FastAPI backend APIs
✅ Interactive Streamlit dashboard
✅ Cloud deployment with Render & Streamlit Cloud
✅ REST API endpoints for analytics
✅ Data visualization and live metrics
✅ Production-ready architecture

🛠️ Tech Stack
Python
FastAPI
PostgreSQL
SQLAlchemy
Pandas
Streamlit
Requests
Render
Git & GitHub
📂 Project Structure
real-time-data-pipeline/
│
├── ingestion/
├── processing/
├── database/
├── api/
├── dashboard/
├── scheduler/
├── logs/
│
├── requirements.txt
├── README.md
└── test_db.py
⚙️ System Architecture
Live Crypto API
        ↓
Data Ingestion Pipeline
        ↓
PostgreSQL Database
        ↓
ETL Processing Layer
        ↓
FastAPI Backend APIs
        ↓
Streamlit Dashboard
📊 API Endpoints
Latest Market Data
/latest-data

Returns latest processed cryptocurrency market data.

Top Movers
/top-movers

Returns top performing cryptocurrencies based on price movement.

🚀 Local Setup
Clone Repository
git clone https://github.com/GMSKrishna/real-time-data-pipeline.git
Create Virtual Environment
python -m venv venv
Activate Virtual Environment
Windows
venv\Scripts\activate
Install Dependencies
pip install -r requirements.txt
🗄️ Configure PostgreSQL

Create a PostgreSQL database and update credentials in:

database/db.py
▶️ Run Project
Start FastAPI Backend
uvicorn api.main:app --reload
Start Streamlit Dashboard
streamlit run dashboard/app.py
📈 Dashboard Preview

The dashboard provides:

Live crypto market tracking
Top movers analysis
Price trend visualizations
Platform metrics
ETL processed insights
☁️ Deployment
Backend Deployment
Render
Frontend Deployment
Streamlit Community Cloud
Database Hosting
Render PostgreSQL
🎯 Resume Value

This project demonstrates:

✅ Backend Development
✅ Cloud Deployment
✅ Database Engineering
✅ ETL Pipelines
✅ REST APIs
✅ Data Analytics
✅ Production Architecture
✅ Real-Time Data Processing

👨‍💻 Author

Manikanta Sai Krishna Gadugoyyala

SAP + AI Enthusiast
Data Engineering & Analytics
Backend Development
Cloud & Real-Time Systems
⭐ Future Improvements
Kafka streaming integration
Docker containerization
Kubernetes deployment
Authentication & user management
Advanced analytics & forecasting
AI-powered market predictions
📜 License

This project is licensed under the MIT License.
