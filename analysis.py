import pandas as pd

# load data

df_policy = pd.read_csv("data/policy_sales.csv")
df_claims = pd.read_csv("data/claims_data.csv")

# -----------------------------
# 1 Total premium 2024
# -----------------------------

total_premium = df_policy["Premium"].sum()

print("Total Premium:", total_premium)


# -----------------------------
# 2 Claim cost per year
# -----------------------------

df_claims["Claim_Date"] = pd.to_datetime(df_claims["Claim_Date"])

df_claims["Year"] = df_claims["Claim_Date"].dt.year

claim_by_year = df_claims.groupby("Year")["Claim_Amount"].sum()

print("\nClaim by year")
print(claim_by_year)


# -----------------------------
# 3 Claim / Premium ratio by tenure
# -----------------------------

premium_by_tenure = df_policy.groupby(
    "Policy_Tenure"
)["Premium"].sum()

merged = df_claims.merge(
    df_policy,
    on=["Customer_ID", "Vehicle_ID"]
)

claim_by_tenure = merged.groupby(
    "Policy_Tenure"
)["Claim_Amount"].sum()

ratio = claim_by_tenure / premium_by_tenure

print("\nRatio by tenure")
print(ratio)


# -----------------------------
# 4 Ratio by month sold
# -----------------------------

df_policy["Policy_Purchase_Date"] = pd.to_datetime(
    df_policy["Policy_Purchase_Date"]
)

df_policy["Month"] = df_policy[
    "Policy_Purchase_Date"
].dt.month

premium_month = df_policy.groupby(
    "Month"
)["Premium"].sum()

merged["Month"] = pd.to_datetime(
    merged["Policy_Purchase_Date"]
).dt.month

claim_month = merged.groupby(
    "Month"
)["Claim_Amount"].sum()

ratio_month = claim_month / premium_month

print("\nRatio by month")
print(ratio_month)