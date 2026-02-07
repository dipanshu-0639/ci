import matplotlib.pyplot as plt  

fig, ax=plt.subplots()

fruits=['apple','blueberry','cherry','orange']
counts=[140,120,130,55]
bar_labels=['red','blue','_red','orange']
bar_colors=['tab:red','tab:blue','tab:red','tab:orange']

ax.bar(fruits,counts,label=bar_labels,color=bar_colors)

ax.set_ylabel('fruits supply')
ax.set_title("Fruits supply by kind and color")
ax.legend(title='Fruits color')

plt.savefig('bars.png',bbox_inches='tight')

cat=["bored","bored",'happy','happy','happy','bored']
dog=['bored','happy','bored','happy','happy','bored']
activity=["combing",'drinking','feeding','napping','playing','washing']

fig,ax=plt.subplots()
ax.plot(activity,dog,label="dog")
ax.plot(activity,cat,label="cat")
ax.legend()

plt.savefig('lines.png',bbox_inches='tight')