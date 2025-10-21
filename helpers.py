import pandas as pd
from scipy import stats
import numpy as np
import pandas as pd




def find_outliers(df,threshold,columName):
    

    # avikelse från medelvärde
    z = np.abs(stats.zscore(df[columName].dropna()))

    print("z",z)

    # find indices
    outliers_indices = df[columName].dropna().index[z > threshold]

    print(outliers_indices)

    # Remove outliners
    no_outliers = df.drop(index=outliers_indices)

    mean = no_outliers[columName].mean().round(2)
    print("medelvärde",mean)
   
    no_outliers[columName].fillna(mean, inplace=True)
    

    


    return no_outliers


def findNan(df):
    nan_counts = df.isna().sum()
    cols_with_nan = nan_counts[nan_counts > 0]
    return cols_with_nan.index.tolist()

    


    

def remove_outliers_iqr(df, columns):
    df_clean = df.copy()
    for col in columns:
        if not pd.api.types.is_numeric_dtype(df[col]):
            continue
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        df_clean = df_clean[(df_clean[col] >= lower) & (df_clean[col] <= upper)]
        print(f"{col}: removed {len(df) - len(df_clean)} outliers")
    return df_clean

   




