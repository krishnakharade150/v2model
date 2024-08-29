import os
import pandas as pd
from dotenv import load_dotenv
from pandasai import SmartDataframe
from langchain_groq.chat_models import ChatGroq

load_dotenv()

llm = ChatGroq(model='llama3-70b-8192',api_key=os.environ['API_KEY'])

data = pd.read_csv('Perfetti_sample_data.csv')
# print(data.head())

df = SmartDataframe(data,config={'llm':llm})

# print(df.chat('Total number of records present in dataset'))                    # 40 Records
# print(df.chat('correlation between sales and spend'))                           # 0.21
# print(df.chat('plot a pie chart for sales for different platform'))             # Done
# print(df.chat('plot correlation matrix for the dataset'))                       # Done
# print(df.chat('plot trend for different platform over sales'))                  # Ask for trend gave bargraph
# print(df.chat('trendline for different platform over sales over weeks'))        # Done
# print(df.chat('trend line for sales for amazon platform.'))
# print(df.chat('correlation between sales and promotion'))                       # 0.36
# print(df.chat('total sales for amazaon platform'))                              # 30736.030000000002
# print(df.chat('Average sales for amazon platflorm'))                            # 1617.6857894736843
# print(df.chat('which week has the maximum sales for amazon paltform'))          # 202410
# print(df.chat('which week has the lowest sales for amazon paltform'))           # 202421    
# print(df.chat('Month wise sales for amazon platform'))                          # Return me a graph rather than values
# print(df.chat('which platform have the maximum sales'))                         # Blinkit
# print(df.chat('which platform have the maximum sales and value for the same'))  # Blinkit with a total sales of 138938.0.
# print(df.chat('how many features does this data have')) 
# print(df.chat('what is the average impression')) 
# print(df.chat('what is the relationship between promotion and sales'))            # 0.36 + scatter plot              
# print(df.chat('what is the relationship between promotion and sales for amazon platform')) # 0.62 
# print(df.chat('what is the relationship between position and sales for amazon platform')) 
# print(df.chat('total sales for year 2022'))                                      # Misslead