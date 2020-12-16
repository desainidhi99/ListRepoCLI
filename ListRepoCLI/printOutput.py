import pandas as pd


def outputData(sortedData, keyvalue, noOfRecords):
    print('Top {0} repositories by {1}'.format(noOfRecords,keyvalue) +'\n' )
    df = pd.DataFrame(sortedData)
    df1 = df[['name', keyvalue]].head(int(noOfRecords))
    print(df1)
    print('\n')
              