from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import csv
from collections import Counter

# plt.style.use("fivethirtyeight")
plt.xkcd()  # This is awesome

# print(plt.style.available)

data = pd.read_csv('data.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

language_counter = Counter()

for response in lang_responses:
    language_counter.update(response.split(";"))

languages = []
popularity = []
for item in language_counter.most_common(15):
    x, y = item
    languages.append(x)
    popularity.append(y)

languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)





plt.title("Most Popular Languages")
plt.xlabel("Number of Users")

plt.legend()

plt.tight_layout()


plt.show()
