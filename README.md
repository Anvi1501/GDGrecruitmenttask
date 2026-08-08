# Medicine Price Prediction

A machine learning project that predicts the price of medicines based on their features. The project includes data preprocessing, exploratory data analysis (EDA), model training, prediction, and a simple Flask web application for user interaction.

## Features

- Data preprocessing and cleaning
- Exploratory Data Analysis (EDA)
- Machine Learning model training
- Price prediction
- Flask web interface

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
│   └── Prediction.ipynb
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

## Installation

1. Clone the repository

```bash
git clone https://github.com/Anvi1501/GDGrecruitmenttask.git
```

2. Navigate to the project

```bash
cd GDGrecruitmenttask
```

3. Create a virtual environment

```bash
python -m venv .venv
```

4. Activate it

**Windows**

```bash
.venv\Scripts\activate
```

5. Install dependencies

```bash
pip install -r requirement.txt
```

## Running the Flask App

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Flask
- HTML
- CSS

## Note

The trained model (`medicine_price_model.pkl`) and label encoders (`label_encoders.pkl`) are not included in this repository because of GitHub's file size limitations.
