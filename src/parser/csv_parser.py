import pandas as pd


def parse_csv(path):
    df = pd.read_csv(path)

    row = df.iloc[0]

    return {
        "full_name": row["name"],
        "emails": [row["email"]],
        "phones": [str(row["phone"])],
        "headline": row["title"]
    }