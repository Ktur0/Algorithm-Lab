import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

def show_parameter_search(arr,highlight = [],highlight_color = [],title = '',target='',speed = 1):
    plt.clf()
    plt.grid(axis='y')
    plt.bar(range(len(arr)),arr,color = 'lightblue',label='Target:'+str(target))
    plt.legend()

    if highlight is not None:
        for i in range(len(highlight)):
            plt.bar(highlight[i],arr[highlight[i]],color = highlight_color[i])

    ax = plt.gca()
    ax.yaxis.set_major_locator(MultipleLocator(2))
    plt.title(title)
    plt.pause(0.5*speed)
