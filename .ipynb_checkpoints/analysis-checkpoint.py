import numpy as np 
import pandas as pd 


spotify = pd.read_csv("./spotify-2023.csv", encoding='ISO-8859-1', skip_blank_lines=True)
#print(spotify.head())
print(spotify[['in_shazam_charts', 'key']].head())
print(spotify.describe())
print(spotify.isnull().sum())

# if __name__ == "__main__":
#     read_csv()