import argparse
import collections

import pandas as pd
import numpy as np

from monkey_model import Monkey
from utils import check_hexacolor, hexacolor_to_int, euclidean_distance, get_cli_args, VALID_OBS, patch_color_int

"""
2. In your file `monkey_classif.py`, implement the function `read_monkeys_from_csv(csv_path, strict)` that loads the CSV file `monkeys.csv` using the pandas library. **Read Part #4 carefully beforehand!**.
      1. The keyword argument `strict` defaults to `False`. When the function is called in `strict` mode, it should raise a `ValueError`if any row is missing any value (including for the column `species`)
      1. Make sure the header contains only the following keys: `fur_color`, `size`, `weight`, `species`, and raise a `ValueError` otherwise.
      1. Drop any row that contains invalid data: negative size and weights values, invalid hexadecimal color strings, rows with missing values...
      1. Add to the dataframe a column `monkey` of `Monkey` objects for each valid row. Use the `dataframe.apply` with a `lambda` function **Read Part #3 carefully beforehand!**.
      1. Add a column `fur_color_int`, where you convert hexadecimal color code strings into integers.
      1. Add a column `bmi`, where you store body mass indices for all your data points.
3. Implement the `test_bmi()` of the `MonkeyModelTestCase` class in `tests.py` to test whether `compute_bmi()` is working correctly

"""
def read_monkeys_from_csv(csv_filepath:str, strict:bool=False) -> pd.DataFrame:
    """Read a monkey data from a CSV file and produce and return a dataframe"""
    df=pd.read_csv(csv_filepath)
    if df[["size","weight","color"]].isna().any(axis=None):
        if strict:
            raise ValueError("Missing values in one or more required columns.")
 
    if not set(df.columns)=={"color","size","weight","species"}:
        raise ValueError("DataFrame must contain the columns: 'color', 'size', 'weight', and 'species'.")

    df = df[(df['size'] >= 0) | (df['weight'] >= 0) | (df['color'].apply(check_hexacolor))]
    df.dropna(subset=['color', 'size', 'weight', 'species'],inplace=True)
    df['monkey'] = df.apply(lambda row: Monkey(row['color'],row['size'],row['weight'],row['species']),axis=1)  
    df['fur_color_int'] = df['color'].apply(lambda x: int(x[1:], 16))
    df['bmi']=df['monkey'].apply(lambda row:row.compute_bmi() ) 
    return df
def compute_knn(df:pd.DataFrame, k:int=5, columns:list=["fur_color_int", "bmi"])->pd.DataFrame:
    """Update species information for a Monkey DataFrame using a KNN.
    Arguments:
        `df`: dataframe as obtained from `read_monkeys_from_csv`
        `k`: number of neighbors to consider
        `columns`: list of observations to consider. Are valid observations:
            - fur_color_int,
            - fur_color_int_r (for red hue of fur),
            - fur_color_int_g (for green hue of fur),
            - fur_color_int_b (for blue hue of fur),
            - weight
            - size
            - bmi
    Returns: the dataframe `df`, modified in-place
    """

    # Write your code here
    pass


def save_to_csv(dataframe:pd.DataFrame, csv_filename:str):
    """Save monkey dataframe to CSV file"""
    dataframe.drop(columns=["monkey", "fur_color_int", "bmi"]).to_csv(csv_filename, index=False)


def main():
    args = get_cli_args()
    if args.command == "knn":
        df = read_monkeys_from_csv(args.input_csv)
        df = compute_knn(df, k=args.k, columns=args.obs)
        save_to_csv(df, args.output_csv)
    elif args.command == "visualize":
        from monkey_visualize import scatter
        scatter(args.input_csv, args.obs_a, args.obs_b)
    else:
        # this should be dead code.
        raise RuntimeError("invalid command name")


# main entry point
if __name__ == "__main__":
    main()
