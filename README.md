# 🎓 Student Performance Prediction App

A **Machine Learning–based Streamlit web application** that predicts a student's academic **Performance Index** using study habits, prior academic results, and lifestyle factors. The project demonstrates an **end‑to‑end ML workflow**: data analysis, model training, serialization, and cloud deployment.

---

## 🚀 Live Demo

🔗 **Deployed App:** [https://studentsperformancemodel-yrqk5zfpqvkpwi7rgff4gj.streamlit.app](https://studentsperformancemodel-yrqk5zfpqvkpwi7rgff4gj.streamlit.app)

---

## 📌 Problem Statement

Academic performance is influenced by multiple factors such as study time, previous scores, sleep habits, and extracurricular involvement. This project aims to **predict a continuous performance score (Performance Index)** for students based on these factors, helping identify performance levels and areas for improvement.

---

## 🧠 Solution Overview

* A **Linear Regression** model is trained on historical student data.
* Input features are **standardized** using `StandardScaler`.
* The trained model and scaler are saved as `.pkl` files.
* A **Streamlit web interface** allows users to input student details and receive real-time predictions.

---

## 🧾 Input Features

The model uses the following inputs:

| Feature                          | Description                              |
| -------------------------------- | ---------------------------------------- |
| Hours Studied                    | Number of hours spent studying           |
| Previous Scores                  | Past academic performance                |
| Extracurricular Activities       | Participation outside academics (Yes/No) |
| Sleep Hours                      | Average hours of sleep                   |
| Sample Question Papers Practiced | Number of practice papers solved         |

---

## 📊 Output

* **Performance Index**: A continuous numeric value estimating overall academic performance.
* Example output:

  > *Predicted Performance Index: 56.05*

This represents a **moderate performance level**, based on learned patterns from historical data.

---

## 🛠 Tech Stack

* **Programming Language:** Python
* **Web Framework:** Streamlit
* **Machine Learning:** Scikit-learn
* **Data Handling:** Pandas, NumPy
* **Deployment:** Streamlit Cloud

---

## 📂 Project Structure

```
students_performance_model/
│
├── app.py                         # Streamlit application
├── linear_regression_model.pkl    # Trained ML model
├── scaler.pkl                     # Feature scaler
├── requirements.txt               # Dependencies
├── student.ipynb                  # Model training notebook
└── Student_Performance.csv        # Dataset
```

---

## 📈 Model Details

* **Algorithm:** Linear Regression
* **Target Variable:** Performance Index
* **Evaluation Metrics:**

  * MAE (Mean Absolute Error)
  * RMSE (Root Mean Squared Error)
  * R² Score

The model was selected based on its interpretability and suitability for continuous prediction tasks.

---

## ▶️ How to Run Locally

1. Clone the repository:

```bash
git clone https://github.com/your-username/students_performance_model.git
cd students_performance_model
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:

```bash
streamlit run app.py
```

---

## ☁️ Deployment

The application is deployed on **Streamlit Cloud** directly from the GitHub repository. Dependency management is handled via `requirements.txt`, ensuring compatibility with the trained model.

---

## 🎓 Learning Outcomes

* End-to-end ML project implementation
* Model serialization and reuse
* Streamlit-based UI development
* Cloud deployment and dependency management

---

## 👤 Author

**Abeeba Abee**

---

## 📜 License

This project is for **educational and academic purposes**.

---

⭐ *If you find this project useful, feel free to star the repository!*
