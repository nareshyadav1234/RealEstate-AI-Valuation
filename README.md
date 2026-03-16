# 🏡 RealEstate AI - Valuation Engine

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![Flask](https://img.shields.io/badge/Framework-Flask-red.svg)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Random%20Forest-green.svg)
![Frontend](https://img.shields.io/badge/UI-Glassmorphism-purple.svg)

An industry-grade, end-to-end Machine Learning web application that predicts property valuations based on the California Housing Dataset. The project features a robust **Random Forest Regressor** backend and a premium **Glassmorphism-inspired UI** for a seamless user experience.

## ✨ Features
* **High-Accuracy ML Model:** Utilizes a Random Forest algorithm trained on 20,000+ data points for precise predictions.
* **RESTful API Backend:** Built with Python and Flask to handle asynchronous requests from the frontend.
* **Premium User Interface:** Modern, responsive "Glassmorphism" design using HTML, CSS, and JavaScript.
* **Localized Outputs:** Automatically converts raw predictions into properly formatted localized currency (e.g., Indian Rupees ₹ / US Dollars $).
* **Robust Error Handling:** Frontend validation and disable-on-submit buttons to prevent redundant API calls.

## 🛠️ Tech Stack
* **Machine Learning:** Scikit-Learn, Pandas, NumPy
* **Backend:** Python, Flask
* **Frontend:** HTML5, CSS3, Vanilla JavaScript
* **Data Visualization (EDA):** Seaborn, Matplotlib

## 🚀 How to Run the Project Locally

Since the trained Machine Learning model (`model.pkl`) is too large for GitHub, you need to generate it locally on your machine first. Follow these steps:

### 1. Clone the Repository
```bash
git clone [https://github.com/nareshyadav1234/RealEstate-AI-Valuation.git](https://github.com/nareshyadav1234/RealEstate-AI-Valuation.git)
cd RealEstate-AI-Valuation

RealEstate-AI-Valuation/
│
├── model.py               
├── app.py                 
├── Eda.ipynb              
├── requirements.txt
├── templates/
│   └── index.html      
│
└── static/
    ├── style.css          
    └── script.js

