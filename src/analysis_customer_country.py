import pandas as pd
from pathlib import Path

TABLES_DIR = Path("outputs") / "tables"
TABLES_DIR.mkdir(parents=True, exist_ok=True)

def top_customers(df: pd.DataFrame, n: int = 10) -> pd.DataFrame:
    df_valid = df.dropna(subset=["Customer ID", "Revenue"])
    top_cust = (
        df_valid.groupby("Customer ID", as_index=False)["Revenue"]
        .sum()
        .sort_values(by="Revenue", ascending=False)
        .head(n)
    )
    top_cust.to_csv(TABLES_DIR / "top_customers.csv", index=False)
    return top_cust

def revenue_by_country(df: pd.DataFrame) -> pd.DataFrame:
    df_valid = df.dropna(subset=["Country", "Revenue"])
    rev_country = (
        df_valid.groupby("Country", as_index=False)["Revenue"]
        .sum()
        .sort_values(by="Revenue", ascending=False)
    )
    rev_country.to_csv(TABLES_DIR / "revenue_by_country.csv", index=False)
    return rev_country

def items_per_invoice(df: pd.DataFrame) -> pd.DataFrame:
    df_valid = df.dropna(subset=["Invoice", "Quantity"])
    items_per = (
        df_valid.groupby("Invoice", as_index=False)["Quantity"]
        .sum()
        .rename(columns={"Quantity": "TotalItems"})
    )
    items_per.to_csv(TABLES_DIR / "items_per_invoice.csv", index=False)
    return items_per

def top_revenue_by_country(df: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    df_valid = df.dropna(subset=["Country", "Revenue"])
    top_country = (
        df_valid.groupby("Country", as_index=False)["Revenue"]
        .sum()
        .sort_values(by="Revenue", ascending=False)
        .head(n)
    )
    top_country.to_csv(TABLES_DIR / "top_revenue_by_country.csv", index=False)
    return top_country
