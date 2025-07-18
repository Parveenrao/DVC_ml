import pandas as pd
import os

data = {'Name':['Parveen' , 'Savita' , 'Priyanka' , 'Nirmala'],
        
        'Age' : [20 , 21 , 22 ,23],
        
        'City' : ['Noida' , 'Alwar' , 'Rewari' , 'Gurugram']
        
    
}


df = pd.DataFrame(data)

data_dir = 'data'

os.makedirs(data_dir , exist_ok=True)

file_path = os.path.join(data_dir , 'sample_data.csv')

df.to_csv(file_path , index= False)

print(f"CSV file send to {file_path}")