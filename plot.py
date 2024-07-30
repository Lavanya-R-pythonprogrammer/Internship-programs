from matplotlib import pyplot as plt
x=["Kannad","Maths","English","Physics","Chemistry"]
y=[30,60,10,15,40]
plt.title("STUDENT SCORED IN PARTICULAR SUBJECTS")
colors=('tomato','cornflowerblue','gold','orchid','green')
plt.pie(
     y, labels=x, colors=colors,autopct='%1.2f%%',pctdistance=0.90,explode=[0.08,0.08,0.08,0.08,0.08],
     textprops={'fontsize':13}
)
hole = plt.Circle((0, 0), 0.65, color='white')
plt.gcf().gca().add_artist(hole)
plt.show()

