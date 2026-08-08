from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load("notebook/medicine_price_model.pkl")
encoders = joblib.load("notebook/label_encoders.pkl")

original_df = pd.read_csv("data/data.csv")


df = original_df.copy()




columns_to_drop = [
    "product_id",
    "active_ingredients",
    "manufacturer_raw",
    "packaging_raw"
]


df = df.drop(
    columns=[c for c in columns_to_drop if c in df.columns]
)



if "pack_size" in df.columns:
    df["pack_size"] = df["pack_size"].fillna(
        df["pack_size"].median()
    )

if "pack_unit" in df.columns:
    df["pack_unit"] = df["pack_unit"].fillna(
        df["pack_unit"].mode()[0]
    )

if "primary_strength" in df.columns:
    df["primary_strength"] = df["primary_strength"].fillna(
        "Unknown"
    )


categorical_columns = [
    "brand_name",
    "manufacturer",
    "dosage_form",
    "pack_unit",
    "primary_ingredient",
    "primary_strength",
    "therapeutic_class"
]

for col in categorical_columns:
    if col in df.columns:
        df[col] = encoders[col].transform(
            df[col].astype(str)
        )




X = df.drop("price_inr", axis=1)

predicted_prices = model.predict(X)

original_df["predicted_price"] = predicted_prices




@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

     
        medicine = request.form["medicine"].strip()

      
        medicine_lower = medicine.lower()

      

      
        medicine_row = original_df[
            original_df["brand_name"]
            .astype(str)
            .str.strip()
            .str.lower()
            == medicine_lower
        ]

       
        if medicine_row.empty:

            medicine_row = original_df[
                original_df["brand_name"]
                .astype(str)
                .str.strip()
                .str.lower()
                .str.startswith(
                    medicine_lower,
                    na=False
                )
            ]

        

        if medicine_row.empty:

            result = {
                "error": "Medicine not found!"
            }

        else:

           
            searched_medicine = medicine_row.iloc[0]

           
            salt = searched_medicine["primary_ingredient"]

           
            dosage_form = searched_medicine["dosage_form"]

           

            same_salt = original_df[
                original_df["primary_ingredient"]
                .astype(str)
                .str.strip()
                .str.lower()
                ==
                str(salt).strip().lower()
            ]

           

            same_form = same_salt[
                same_salt["dosage_form"]
                .astype(str)
                .str.strip()
                .str.lower()
                ==
                str(dosage_form).strip().lower()
            ]

           
            if not same_form.empty:

                comparable_medicines = same_form

            else:

                comparable_medicines = same_salt

            

            cheapest = comparable_medicines.loc[
                comparable_medicines["predicted_price"].idxmin()
            ]

            

            result = {
                "searched": medicine,
                "salt": salt,
                "dosage_form": dosage_form,
                "brand": cheapest["brand_name"],
                "manufacturer": cheapest["manufacturer"],
                "price": round(
                    cheapest["predicted_price"],
                    2
                )
            }

    return render_template(
        "index.html",
        result=result
    )




if __name__ == "__main__":
    app.run(debug=True)