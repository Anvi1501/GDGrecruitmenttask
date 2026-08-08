# Medicine Price Prediction & Cheapest Alternative Recommendation

## About the Project

This project was built to help users find a cheaper alternative for a medicine. The user enters the name of a medicine, and the system identifies its primary ingredient (salt), compares medicines containing the same salt, predicts their prices using a trained Machine Learning model, and recommends the cheapest option.

The project also includes data preprocessing, model training, and a simple web interface built using Flask.

---

## Features

- Cleaned and preprocessed the medicine dataset
- Performed Exploratory Data Analysis (EDA)
- Trained a Random Forest Regression model for price prediction
- Search medicines using their brand name
- Automatically identify the medicine's primary ingredient (salt)
- Recommend the cheapest medicine with the same salt
- Simple Flask-based web interface

---

## Project Structure

```
GDGrecruitmenttask/
│
├── data/
│   └── data.csv
│
├── notebook/
│   ├── EDA.ipynb
│   ├── Model_Training.ipynb
│   ├── Prediction.ipynb
│   ├── medicine_price_model.pkl
│   └── label_encoders.pkl
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── requirement.txt
├── README.md
└── .gitignore
```

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Flask
- HTML
- CSS

---

## How to Run

### Clone the repository

```bash
git clone https://github.com/Anvi1501/GDGrecruitmenttask.git
```

### Move into the project folder

```bash
cd GDGrecruitmenttask
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the environment

**Windows**

```bash
.venv\Scripts\activate
```

### Install the required libraries

```bash
pip install -r requirement.txt
```

### Run the Flask application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

## Project Workflow

1. Load the medicine dataset.
2. Clean and preprocess the data.
3. Train the Random Forest model.
4. Save the trained model and label encoders.
5. User enters a medicine name through the website.
6. The application finds the medicine's primary ingredient.
7. All medicines containing the same salt are compared.
8. The model predicts their prices.
9. The medicine with the lowest predicted price is displayed.

---

## Future Improvements

- Filter recommendations based on dosage form (Tablet, Syrup, Injection, etc.)
- Improve prediction accuracy by trying different machine learning models.
- Add medicine search suggestions and autocomplete.
- Deploy the application online.

---

## Note

The trained model (`medicine_price_model.pkl`) and label encoders (`label_encoders.pkl`) are not included in this repository because of GitHub's file size limits.
