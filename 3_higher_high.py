import pandas as pd

def three_candles(path):
    df = pd.read_csv(path)
    df["Date"] = pd.to_datetime(df["Date"], format="%Y%m%d", errors="coerce")
    sorted_df = df.sort_values(by="Date", ascending=True).reset_index(drop=True)
    dates = []
    
    for i in range(len(sorted_df) - 3):
        if (
            (sorted_df["High"].iloc[i+3] > sorted_df["High"].iloc[i+2]) and
            (sorted_df["High"].iloc[i+2] > sorted_df["High"].iloc[i+1]) and
            (sorted_df["High"].iloc[i+1] > sorted_df["High"].iloc[i])
        ):
            dates.append(str(sorted_df["Date"].iloc[i+3]))
    
    return dates

print(three_candles("IRO9AHRM4681.csv"))
