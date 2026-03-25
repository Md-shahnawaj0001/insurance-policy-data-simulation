import pandas as pd
import numpy as np

n = 1000000

dates = pd.date_range("2024-01-01", "2024-12-31")

tenure_choices = [1, 2, 3, 4]
tenure_probs = [0.2, 0.3, 0.4, 0.1]

customer_id = np.arange(1, n+1)
vehicle_id = np.arange(1, n+1)

purchase_dates = np.random.choice(dates, n)

tenure = np.random.choice(
    tenure_choices,
    size=n,
    p=tenure_probs
)

premium = tenure * 100

start_dates = pd.to_datetime(purchase_dates) + pd.Timedelta(days=365)

end_dates = start_dates + pd.to_timedelta(tenure * 365, unit="D")

df = pd.DataFrame({
    "Customer_ID": customer_id,
    "Vehicle_ID": vehicle_id,
    "Vehicle_Value": 100000,
    "Premium": premium,
    "Policy_Purchase_Date": purchase_dates,
    "Policy_Start_Date": start_dates,
    "Policy_End_Date": end_dates,
    "Policy_Tenure": tenure
})

df.to_csv("data/policy_sales.csv", index=False)

print("Policy data created")

# -------------------
# CLAIMS DATA
# -------------------

df["Policy_Start_Date"] = pd.to_datetime(df["Policy_Start_Date"])

claim_rows = []

claim_days = [7,14,21,28]

for i, row in df.iterrows():

    start_date = row["Policy_Start_Date"]

    if start_date.year == 2025 and start_date.day in claim_days:

        if np.random.rand() < 0.3:

            claim_rows.append([
                row["Customer_ID"],
                row["Vehicle_ID"],
                start_date,
                10000,
                1
            ])

df_claims = pd.DataFrame(
    claim_rows,
    columns=[
        "Customer_ID",
        "Vehicle_ID",
        "Claim_Date",
        "Claim_Amount",
        "Claim_Type"
    ]
)

df_claims.insert(0,"Claim_ID",range(1,len(df_claims)+1))

df_claims.to_csv("data/claims_data.csv",index=False)

print("Claims data created")