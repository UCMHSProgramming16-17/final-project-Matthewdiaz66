#Import modules
import requests
import csv
import pandas as pd
from bokeh.charts import Bar, output_file, save

#open a new csv 
file = open("stat.csv", "w")
csv = csv.writer(file, delimiter = ",")

csv.writerow(["stats", "base"])

#create the URL
pokemonnum = input("input a pokemon's number ")
base = "http://pokeapi.co/api/v2/pokemon/"
url = base+pokemonnum

r = requests.get(url)
print(r)

#Label the CSV
dex = r.json()
hp = dex["stats"][5]["base_stat"]
df = dex["stats"][4]["base_stat"]
att = dex["stats"][4]["base_stat"]

csv.writerow(["attack", att])
csv.writerow(["hp",hp])
csv.writerow(["defense",df])

#CLose the CSV
file.close()

#Let bokeh read the data
data = pd.read_csv("stat.csv")

#Make the chart
bar = Bar(data, values="base", label="stats", legend=False, title= "Pokemon HP vs Attack vs Defence", bar_width=0.2, color="#000000")

#Save the chart
output_file("pokemon.html")
save(bar)
print("complete")