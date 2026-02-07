import matplotlib.pyplot as plt  

fig,ax=plt.subplot()

fruits=['apple','blueberry','cherry','orange']
counts=[140,10,30,55]
bar_labels=['red','blue','_red','orange']
bar_colors=['tab:red','tab:blue','tab:red','tab:orange']

ax.bar(fruits,counts,label=bar_labels,color=bar_colors)

ax.set_ylabel('fruits supply')
ax.set_title("Fruits supply by kind and color")
ax.legend(title='Fruits color')

plt.savefig('bars.png',bbox_inches='tight')

cat=["bored","happy",'happy','happy','happy','bored']
dog=['bored','bored','bored','happy','bored','bored']
activity=["combing",'drinking','feeding','napping','playing','washing']

fig,ax=plt.subplot()
ax.plot(activity,dog,label="dog")
ax.plot(activity,cat,label="cat")
ax.legend()

plt.savefig('lines.png',bbox_inches='tight')