# 🎓 Student Performance Prediction App

![Status](https://img.shields.io/badge/Status-Deployed%20%26%20Stable-brightgreen)
![License](https://img.shields.io/badge/License-Academic-blue)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![ML](https://img.shields.io/badge/ML-scikit--learn-orange)
![Deployment](https://img.shields.io/badge/Deployment-Streamlit%20Cloud-red)

---

## 🎯 Overview

**Student Performance Prediction App** is a machine‑learning–powered web application that predicts a student’s **Performance Index** based on study habits, academic history, and lifestyle factors. The project demonstrates a **complete ML lifecycle** — from data analysis and model training to deployment on **Streamlit Cloud**.

This project is designed for **academic submission, internship evaluation, and portfolio demonstration**.

---

## 🚀 Live Application

👉 **Deployed Streamlit App:**
[[https://studentsperformancemodel-yrqk5zfpqvkpwi7rgff4gj.streamlit.app](https://studentsperformancemodel-dswcyf8jsftkr9rjvf34jx.streamlit.app/#ai-powered-student-performance-analyzer)]

---

## 📌 Problem Statement

Student academic performance depends on multiple factors such as:

* Time spent studying
* Previous academic results
* Sleep patterns
* Practice consistency
* Extracurricular involvement

This project aims to **predict a continuous Performance Index score** using these factors, enabling early performance assessment and data‑driven academic insights.

---

## 🧠 Solution Summary

* Performed **Exploratory Data Analysis (EDA)** on student performance data
* Trained a **Linear Regression model** for continuous prediction
* Applied **StandardScaler** for feature normalization
* Serialized the trained model and scaler using `.pkl` files
* Built an interactive **Streamlit UI** for real‑time predictions
* Deployed the application on **Streamlit Cloud**

---

## 🧾 Input Features

| Feature                          | Description                              |
| -------------------------------- | ---------------------------------------- |
| Hours Studied                    | Daily study time                         |
| Previous Scores                  | Past academic performance                |
| Extracurricular Activities       | Participation outside academics (Yes/No) |
| Sleep Hours                      | Average hours of sleep                   |
| Sample Question Papers Practiced | Number of practice papers solved         |

---

## 📊 Output

### 🎯 Performance Index

* A **continuous numeric score** predicting overall academic performance
* Example output:

```
Predicted Performance Index: 56.05
```

### Interpretation:

* **40–55** → Low to moderate performance
* **55–75** → Average performance
* **75+** → High performance

---

## 📈 Model Performance

The trained Linear Regression model was evaluated using standard regression metrics to assess accuracy and reliability.

- **R² Score:** **0.986 (98.6%)**
- **Root Mean Squared Error (RMSE):** **2.01**
- **Mean Absolute Error (MAE):** **≈ 1.6**

### Interpretation
- An R² score of **98.6%** indicates that the model explains nearly all the variance in student performance.
- Low RMSE and MAE values confirm minimal prediction error and strong model generalization.

---

## 🛠 Technology Stack

| Category        | Tools           |
| --------------- | --------------- |
| Language        | Python          |
| ML Library      | scikit-learn    |
| Data Processing | pandas, numpy   |
| Web Framework   | Streamlit       |
| Deployment      | Streamlit Cloud |
| Version Control | Git & GitHub    |

---

## 📂 Project Structure

```
students_performance_model/
│
├── app.py                         # Streamlit application
├── linear_regression_model.pkl    # Trained ML model
├── scaler.pkl                     # Feature scaler
├── requirements.txt               # Dependencies
├── student.ipynb                  # Training & EDA notebook
└── Student_Performance.csv        # Dataset
```

---

## ▶️ Run Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/students_performance_model.git
cd students_performance_model
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the App

```bash
streamlit run app.py
```

---

## ☁️ Deployment

* Platform: **Streamlit Cloud**
* Deployment Method: Direct GitHub integration
* Dependency management via `requirements.txt`
* Model loaded using serialized `.pkl` artifacts

---

## 🎓 Learning Outcomes

* End‑to‑end machine learning pipeline
* Model training and evaluation
* Feature scaling and preprocessing
* Streamlit UI development
* Cloud deployment and dependency management
* Debugging real‑world deployment issues

---

## 👤 Author

**Ummu Abeeba**
📧 Email: [abeeba2430@gmail.com](mailto:abeeba2430@gmail.com)

---

## 📜 License

This project is created for **educational and academic purposes**.

---

⭐ If you find this project useful, feel free to **star the repository** and try the live app!
