import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./01_unemp.csv", sep=",")

subset = df[['Country Name', "Country Code", "1991", "1992", "1993", "2006", "2007", "2008", "2009", "2019", "2020", "2021", "2022"]].copy()
subset.sort_values("Country Name")
subset.set_index("Country Code", inplace=True)

aut = subset.loc["AUT"]
aut = aut.apply(pd.to_numeric, errors='coerce')

aut_nn = aut[aut.notnull()]

threshold = 10
max_val = 10

aut_nn = aut_nn[aut_nn <= max_val]
mean_value = aut_nn.mean()

aut_nn.plot.line()

plt.legend()
plt.title('Unemployment Rates in Austria Over Time')
plt.xlabel('Year')
plt.ylabel('Unemployment Rate')
plt.show()
