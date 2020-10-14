from matplotlib import pyplot as plt

plt.xkcd()

# plt.style.use("fivethirtyeight")

slices = [
    59219, 55466, 47544, 36443, 35917, 31991, 27097,
    23030, 20524, 18523, 18017, 7920, 7331, 7201, 5833

]

labels = [
    'JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java',
    'Bash/Shell/PowerShell', 'C#', 'PHP', 'C++', 'TypeScript',
    'C', 'Other(s):', 'Ruby', 'Go', 'Assembly'
]

explode = [0, 0, 0, 0.1, 0]


plt.pie(
    slices[:5],
    labels=labels[:5],
    explode=explode,
    shadow=True,
    startangle=90,
    autopct='%1.1f%%'
    # colors=colors,
    # wedgeprops={'edgecolor': 'black'}, # black line between slices
)

plt.title("My awesome Pie Chart")
plt.tight_layout()
plt.show()
