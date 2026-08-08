





## Model Details

For this project, I used a **Random Forest Regressor** to predict medicine prices.

### Data Preparation

- Removed columns that were not useful for prediction.
- Handled missing values using median and mode wherever required.
- Converted categorical features into numerical values using Label Encoding.

### Features Used

Some of the important features used by the model are:

- Brand Name
- Manufacturer
- Dosage Form
- Pack Size
- Pack Unit
- Primary Ingredient
- Primary Strength
- Therapeutic Class
- Number of Active Ingredients

### Model

- Algorithm: Random Forest Regressor
- Library: Scikit-learn

### Evaluation

The model was evaluated using **Mean Absolute Error (MAE)**.


Lower MAE indicates that the predicted prices are closer to the actual medicine prices.

### Working

The user enters the name of a medicine through the web interface.

The application:
1. Finds the medicine in the dataset.
2. Identifies its primary ingredient (salt).
3. Searches for medicines having the same salt.
4. Predicts their prices using the trained model.
5. Displays the cheapest available medicine.
