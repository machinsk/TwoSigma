# Here's an example of loading the CSV using Pandas's built-in HDF5 support:
import pandas as pd

with pd.HDFStore("train.h5", "r") as train:
    # Note that the "train" dataframe is the only dataframe in the file
    df = train.get("train")

    df2 = df[df['id']==10]
    #df1 = df[['id','y']].groupby('id')

    writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')

    # Convert the dataframe to an XlsxWriter Excel object.
    df2.to_excel(writer, sheet_name='Sheet1')

    # Close the Pandas Excel writer and output the Excel file.
    writer.save()
