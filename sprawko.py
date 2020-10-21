import matplotlib.pyplot as plt

w = [0.024, 0.038, 0.048, 0.029, 0.048, 0.058]
M = [0.075, 0.113, 0.15, 0.075, 0.113, 0.15]

def average(nums):
    output = 0
    for num in nums:
        output += num

    output /= len(nums)
    return output

ws = average(w)
Ms = average(M)

value = 0
for wi in w:
    if value < abs(wi - ws):
        value = abs(wi - ws)
print(ws)
print(value)

value = 0
for Mi in M:
    if value < abs(Mi - Ms):
        value = abs(Mi-Ms)

print(value)

def u():
    output = 1 / Ms ** 2 * 0.017 + (ws / Ms ** 2) ** 2 * 0.038
    return output ** .5
print(u())


plt.scatter(M, w) # plot the data

# y = ax+b
a = 0.3537
b = 0.000098

x = [i/1000 for i in range(50, 200)]
y = [a * i + b for i in x ]


plt.plot(x, y)

plt.show()
