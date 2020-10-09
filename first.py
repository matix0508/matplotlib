from matplotlib import pyplot as plt

# plt.style.use("fivethirtyeight")
plt.xkcd()  # This is awesome

# print(plt.style.available)

###DATA###
ages_x = [i for i in range(25, 36)]
dev_y = [
    38496, 42000, 46752, 49320, 53200,
    56000, 62316, 64928, 67317, 68748, 73752
]

py_dev_y = [
    45372, 48876, 53850, 57287, 63016,
    65998, 70003, 70000, 71496, 75370, 83640
]

js_dev_y = [
    37810, 42515, 46823, 49293, 53437,
    56373, 62375, 66674, 68745, 68746, 74583
]

###PLOT###


plt.plot(
    ages_x, py_dev_y,
    label="Python"
)

plt.plot(
    ages_x, js_dev_y,
    label="JavaScript"
)


plt.plot(
    ages_x, dev_y,
    linestyle='--',
    label="All devs",
)

plt.title("Median Salary (USD) by Age")
plt.xlabel("Ages")
plt.ylabel("Median Salary")

plt.legend()

plt.tight_layout()

plt.savefig('plot.png')

plt.show()
