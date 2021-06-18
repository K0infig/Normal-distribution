import random
import statistics
import plotly.figure_factory as ff


dice_result = []

for i in range(0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    dice_result.append(dice1+ dice2)

mean = sum(dice_result)/len(dice_result)
print("The mean value is: "+str(mean))

median = statistics.median(dice_result)
print("The median of Data is:"+str(median))

mode = statistics.mode(dice_result)
print("The mode value of the data is: "+str(mode));

std_dev = statistics.stdev(dice_result)
print("The standard deviation: "+ str(std_dev))

fig = ff.create_distplot([dice_result],["Result"], show_hist =False)
fig.show()


