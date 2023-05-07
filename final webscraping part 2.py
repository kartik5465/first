import csv
import pandas as pd
from selenium import webdriver

file = pd.read_csv('D:\\result.csv', usecols = [2])
#file.dropna(inplace = True)
#file_dict = file.to_dict('index')
print(file[0])








