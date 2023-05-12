
# importing the pandas library
import pandas as pd
  
# reading the csv file
df = pd.read_csv("countries.csv")

for i in range(195):

    # df.loc[i, 'Name'] = i % df.loc[i, 'Name']
    df.loc[i, 'Name'] = df.loc[i, 'Name'][:0] + f"{i}" + ',' + df.loc[i, 'Name'][0:]

  
    # writing into the file
    df.to_csv("countries.csv", index=False)


# for i in range(195):
#     df.loc[i, 'Name'] = df.loc[i, 'Name'][1:]
#     df.to_csv("countries.csv", index=False)

#     df.loc[i, 'Name'] = df.loc[i, 'Name'].rstrip(df.loc[i, 'Name'][-1])
#     df.to_csv("countries.csv", index=False)

