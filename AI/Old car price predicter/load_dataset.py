import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import RandomOverSampler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
    
def ld(filename):
    #removing lakhs and crores prefix in car_prices column and converting prices to NRS from INR
    df = pd.read_csv("car_price.csv", index_col='index')
     
    #removing km suffix from km driven columns
    df["kms_driven"] = df["kms_driven"].str.removesuffix("kms").str.replace(',','').astype(int)

    #cleaning fuel types
    fuels = {"Petrol":1,
         "Diesel": 2,
         "Cng": 3,
         "Lpg": 4,
         "Electric": 5
         } 
    df["fuel_type"] = df["fuel_type"].replace(fuels)

    #changing seats colums to int from str by removing suffix
    df["Seats"] = df["Seats"].str.removesuffix("Seats").astype(int)

    #conveting engine to cc in int
    df = df.rename({"engine": "engine_cc"}, axis="columns")
    df["engine_cc"] = df["engine_cc"].str.removesuffix("cc").astype(int)

    #giving tansmission a number for either manual or automatic
    transmissions = {"Manual": 0, "Automatic": 1}
    df['transmission'] = df['transmission'].replace(transmissions)

    #changing owner columns to int as well
    owners = {"1st":1, "2nd":2, "3rd":3, "4th":4, "5th":5, "0th": 0}
    df["ownership"] = df["ownership"].str.removesuffix("Owner").str.strip().replace(owners)

    # for label in df.columns:
    #     plt.hist(df[df["car_prices_in_lakh"] >= 10][label], color="blue", label="More than 10 lakhs", alpha=0.7, density=True)
    #     plt.hist(df[df["car_prices_in_lakh"] < 10][label], color="red", label="More than 10 lakhs", alpha=0.7, density=True)
    #     plt.show()

    #reordering prices at last cols
    cols = list(df.columns.values)
    price = cols.pop(1)
    seat = cols.pop(7)
    cols.insert(1, seat)
    cols.insert(8, price)
    df = df.reindex(columns = cols)


    #Removing car name
    df.pop("car_name")


    # maruti = df["car_name"].str.contains("Maruti")
    # df["car_name"] = (df["car_name"] * 0).where(maruti, other=df["car_name"])
    # print(df["car_name"].value_counts())


    df.loc[df["car_prices_in_lakh"] >= 10, "more_than_10"] = 'True'
    df.loc[df["car_prices_in_lakh"] < 10, "more_than_10"] = 'False'
    df["more_than_10"] = df["more_than_10"].replace({"True":1, "False":0})

    df.pop("car_prices_in_lakh")
    
    return df

    
    
def main():
    ld("car_price.csv")
        
if __name__ == 'main':
    main()