import numpy as np
import pandas as pd
import glob, os

def clean_data(in_dir,out_name):

    # Retreive files
    files = glob.glob(os.path.join(in_dir,'*.txt'))

    # Read data from files
    dfs = []
    for file in files:
        df = pd.read_csv(file,sep='\t')
        dfs.append(df)

    # Combine all dataframes
    mort = pd.concat(dfs)

    # Remove unwanted columns
    mort = mort.drop(['Notes','County Code','Age Group','Gender','Race Code','Hispanic Origin Code'],axis=1)

    # Clean remaining columns
    unreliable = []
    states = []
    rates = []
    deaths = []
    pop = []
    for i in range(len(mort)):
        name = mort[i:i+1].County.to_string()
        states.append(name.split(', ')[-1])
        rate = mort[i:i+1]['Crude Rate'].to_string()
        if 'Unreliable' in rate:
            rates.append(float(mort[i:i+1]['Crude Rate'].to_string().split(' ')[-2]))
            unreliable.append(True)
        elif 'Not Applicable' in mort[i:i+1]['Crude Rate'].to_string():
            rates.append(np.nan)
            unreliable.append(True)
        elif 'Suppressed' in mort[i:i+1]['Crude Rate'].to_string():
            rates.append(np.nan)
            unreliable.append(True)
        else:
            rates.append(float(mort[i:i+1]['Crude Rate'].to_string().split(' ')[-1]))
            unreliable.append(False)
        if 'Suppressed' in mort[i:i+1]['Deaths'].to_string():
            deaths.append(np.nan)
        else:
            deaths.append(int(mort.Deaths[i:i+1].to_string().split(' ')[-1]))
        if 'Not Applicable' in mort[i:i+1]['Population'].to_string():
            pop.append(np.nan)
        elif 'Suppressed' in mort[i:i+1]['Population'].to_string():
            pop.append(np.nan)
        else:
            pop.append(int(mort[i:i+1]['Population'].to_string().split(' ')[-1]))
    mort['State'] = states
    mort['Crude Rate'] = rates
    mort['Unreliable'] = unreliable
    mort['Deaths'] = deaths
    mort['Population'] = pop

    print('Cleaning complete!\nTotal length of dataframe: ',len(mort))

    # Save dataframe to csv
    mort.to_csv(os.path.join(in_dir,out_name))
