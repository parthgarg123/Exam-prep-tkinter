import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator, FormatStrFormatter

topics={'Algebra': [1, 3], 'Series Analysis': [0, 2],
        'Calculus': [2, 2], 'Matrices': [1, 1], 'Probability': [0, 2]}

def topics_composition_pie(topics):
        colors = ['#66b3ff','#99ff99','#ff9999','#c2c2f0','#ffcc99','#ff9770']
        values = [value[1] for value in topics.values()]
        fig1, ax1 = plt.subplots(figsize=(5,4))
        ax1.pie(values, colors = colors, labels=list(topics.keys()), autopct='%d%%', startangle=90)
        ax1.set_title("Sub-Topics Composition",weight='bold',pad=25)
        centre_circle = plt.Circle((0,0),0.70,fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)
        ax1.axis('equal')
        plt.tight_layout()
        return fig

def answer_ratio_bar(topics):
    names = list(topics.keys())
    wrng_answer = [value[1]-value[0] for value in topics.values()]
    corr_answer = [value[0] for value in topics.values()]
    pos1 = np.arange(len(names))
    pos2 = [x +0.2 for x in pos1]
    fig, ax = plt.subplots(figsize=(5.5,4))
    ax.bar(pos1, corr_answer, color='#3f72af', width=0.2, label='Correct Ans')
    ax.bar(pos2, wrng_answer, color='#f9a23c', width=0.2, label='Wrong Ans')
    ax.set_xlabel('Sub-Topics',labelpad=15)
    ax.set_ylabel('Number of Questions',labelpad=15)
    ax.set_title('Wrong vs Correct Answers',weight='bold',pad=25)
    ax.set_xticks(pos1)
    ax.set_xticklabels(names)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_color('#DDDDDD')
    ax.tick_params(bottom=False, left=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(True, color='#EEEEEE')
    ax.xaxis.grid(False)
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.yaxis.set_major_formatter(FormatStrFormatter('%d'))
    plt.tight_layout()

    return fig
