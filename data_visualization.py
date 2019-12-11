#Matplotlib: use for simple bar charts, line charts, and scatterplots.

matplotlib.pyplot
    #to save: savefig()
    #to display: show()
    
#(1) Bar Charts:
#good for showing how some quantity varies among some discrete set of items

#(A) Basic Exmaple

from matplotlib import pyplot as plt

movies = ['The Irishman', 'Requiem for a Dream', 'Casino']
num_oscars = [13, 5, 10]

# bars are by default width 0.8, so we'll add 0.1 to the left coordinates so that each bar is centered
xs = [i + 0.1 for i, _ in enumerate(movies)]

plt.ylabel("# of Academy Awards")
plt.title("My Favorite Movies")

# label x-axis with movie names at bar centers
plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)

plt.show()


#(B)histograms:

grades = [83, 84, 79, 100, 97, 91, 98, 81]
decile = lambda grade: grade // 10*10
histogram = Counter(decile(grade)) for grade in grades)

plt.bar([x - 4 for x in histogram.keys()],        # shift each bar to the left by 4
        histogram.values(),                       # give each bar its correct height
        8)                                        # give each bar a width of 8
        
plt.axis([-5, 105, 0, 5])                         # x-axis from -5 to 105,,,,,y-axis from 0-5

plt.xticks([10 * i foir i in range(11)]           # x-axis labels at 0, 10,...,100
plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distribution of Exam 1 Grades")
plt.show()

#(2) Line Charts:
# good for showing trends

variance      = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared  = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error   = [x + y, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]

# we can make mulitple calls to plt.plot to show multiple series on the same chart:
plt.plot(xs, variance,     'g-',  label = 'variance')       #green solid line
plt.plot(xs, bias_squared, 'r-.', label = 'bias_squared')   #red dot-dashed line
plt.plot(xs, total_error,  'b:',  label = 'total_error')    #blue dotted line

#becauae we've assigned labels to each series, we can get a legend for free:
plt.legend(loc=9)        #loc=9 means "top center"
plt.xlabel("Model Complexity")
plt.title("The Bias-Variance Tradeoff")
plt.show()

#(3) Scatterplots
# good for visualizing the relationship between two paired sets of data
# example: the relationship between the number of friends your users have and the number of minutes they spend on their phones each day

friends = [70, 75, 72, 63, 71]
minutes = [175, 170, 120, 220, 190]
labels = ['a', 'b', 'c', 'd', 'e']

plt.scatter(friends, minutes)

#label each point:
for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label,
                 xy = (friend_count, minute_count),     # put the label with its point
                 xytext = (5, -5),                      # but slightly offset
                 textscoords = 'offset points') 

plt.title("Daily Minutes vs. Number of Friends")
plt.xlabel("# of Friends")
plt.ylabel("daily minutes spent on the site")
plt.show()
           
  
# you can use plt.axis('equal') to more accurately disply any variation
           
#more visualization tools:
           #seaborn
           #D3.js
           #Bokeh
           #ggplot
