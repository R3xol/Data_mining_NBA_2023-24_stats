# Jak odpalasz pierwszy raz to odkomentuj pierwszą sekcję, potem zakomentuj ;)
'''import requests # make a request to the webpage to download it
import time

url = "https://www.basketball-reference.com/leagues/NBA_2024_totals.html"

# create a url
data = requests.get(url)
    
# W+ opens file in write mode and if it already exists it will just overwrite.
with open("Stats_2024.html", "w+", encoding = "utf-8") as f:
    time.sleep(3)
    f.write(data.text) #text saves files as html'''

# import beautiful soup
from bs4 import BeautifulSoup

# read the HTML data
with open("Stats_2024.html", encoding="utf-8") as f:
    page = f.read()

# create a parser class to extract table from the page
soup = BeautifulSoup(page, "html.parser")

# remove the top row of the table
'''soup.find("tr", class_="over_header").decompose()
print("Header row removed successfully")'''

# find the specific table we want using its id
mvp_table = soup.find(id="all_totals_stats")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Stats = pd.read_html(str(mvp_table))
print(Stats)

# Na tym chyba będziemy pracować, nie znam Pandasa
df = pd.DataFrame(Stats[0])

numeric_columns = ['Rk' ,'Age', 'G' , 'GS'  ,  'MP'  , 'FG'  , 'FGA' ,  'FG%'  , '3P' , '3PA' ,  '3P%' ,  '2P' , '2PA'  , '2P%' , 'eFG%',   'FT', 'FTA' ,  'FT%',  'ORB'  ,'DRB' , 'TRB',  'AST' ,'STL' ,'BLK',  'TOV'  , 'PF',   'PTS']
df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')

# Dalej już bez RK (Numer pożądkowy)
numeric_columns = ['Age', 'G' , 'GS'  ,  'MP'  , 'FG'  , 'FGA' ,  'FG%'  , '3P' , '3PA' ,  '3P%' ,  '2P' , '2PA'  , '2P%' , 'eFG%',   'FT', 'FTA' ,  'FT%',  'ORB'  ,'DRB' , 'TRB',  'AST' ,'STL' ,'BLK',  'TOV'  , 'PF',   'PTS']

string_columns = ['Player', 'Pos', 'Tm']
# Zamiana wybranych kolumn na typ string
df[string_columns] = df[string_columns].astype(str)

description = df.describe()

print(description )

print(df.dtypes)

# tu jest numpy arr, niewiem jescze po co ale xD
'''Stats_arr = df.to_numpy()
print(type(Stats_arr))
print(Stats_arr[0])'''

#print(df.loc[0])

print("\nŚrednia dla wybranych kolumn:")
print(df[numeric_columns].mean())  # średnia
print("\nMediana dla wybranych kolumn:")
print(df[numeric_columns].median())  # mediana
print("\nModa dla wybranych kolumn:")
print(df[numeric_columns].mode())  # moda
print("\nOdchylenie standardowe dla wybranych kolumn:")
print(df[numeric_columns].std())  # odchylenie standardowe

# Tworzenie wykresu box plot dla każdej kolumny
'''for i, column in enumerate(numeric_columns, 1):
    plt.figure(figsize=(12, 8))  # Ustawienie rozmiaru wykresu
    plt.plot(len(numeric_columns))  # Ustawienie pozycji subplotu
    sns.boxplot(y=df[column])
    plt.title(f'Box plot for {column}')
    plt.ylabel(column)
    plt.show()'''


# Znalezienie wartości NaN w DataFrame
nan_values = df.isna()
print("Wartości NaN w DataFrame:")
print(nan_values)

# Znalezienie wartości równych 0 w DataFrame
zero_values = df == 0
print("Wartości równe 0 w DataFrame:")
print(zero_values)

# Wartości NaN w wybranych kolumnach
print("\nWartości NaN w wybranych kolumnach:")
print(df[numeric_columns].isna())

# Wartości równe 0 w wybranych kolumnach
print("\nWartości równe 0 w wybranych kolumnach:")
print(df[numeric_columns] == 0)

# Wyświetlenie wierszy zawierających NaN w wybranych kolumnach
print("\nWiersze zawierające NaN w wybranych kolumnach:")
print(df[numeric_columns][df[numeric_columns].isna().any(axis=1)])

# Wyświetlenie wierszy zawierających wartości równe 0 w wybranych kolumnach
print("\nWiersze zawierające wartości równe 0 w wybranych kolumnach:")
print(df[numeric_columns][(df[numeric_columns] == 0).any(axis=1)])
