import numpy as np
import pandas as pd

revenues = pd.Series([5555, 7000, 1980])
print(revenues)
city_revenues = pd.Series([5000, 6000, 7000], index = ['Jakarta', 'Bandung', 'Surabaya'])
print(city_revenues)
city_employee = pd.Series({'Jakarta':10, 'Bandung':5, 'Surabaya':15})
print(city_employee)
city_data = pd.DataFrame({'revenues':city_revenues, 'employee':city_employee})
print(city_data)
city_data.loc['Bandung':'Surabaya', 'revenues']
print(city_data.loc)