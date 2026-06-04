import pandas as pd
import os

folder_path =  "data/raw"

for file in os.listdir(folder_path):

    if file.endswith(".csv"):

        df = pd.read_csv(
            os.path.join(folder_path, file)
        )

        print(file, ":", df.shape)