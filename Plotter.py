import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

def demo():
    # Set data
    df = pd.DataFrame({
        'group': ['A','B','C','D'],
        'var1': [38, 1.5, 30, 4],
        'var2': [29, 10, 9, 34],
        'var3': [8, 39, 23, 24],
        'var4': [7, 31, 33, 14],
        'var5': [28, 15, 32, 14]
        })
 
    # number of variable
    categories=list(df)[1:]
    N = len(categories)
 
    # We are going to plot the first line of the data frame.
    # But we need to repeat the first value to close the circular graph:
    values=df.loc[0].drop('group').values.flatten().tolist()

    # to make sure the radar is fully form and close off the line at the end, we need to 
    # Make the first number match the last value of the array
    values += values[:1]
    values
 
    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]
 
    # Initialise the spider plot
    ax = plt.subplot(111, polar=True)
 
    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], categories, color='grey', size=8)
 
    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([10,20,30,], ["10","20","30"], color="grey", size=7)
    plt.ylim(0,100)
 
    # Plot data
    ax.plot(angles, values, linewidth=1, linestyle='solid')
 
    # Fill area
    ax.fill(angles, values, 'b', alpha=0.1)
    plt.show()


def Plot_Radar(DataFrame):
    """ Plotting a radar chart for a data frame
    :DataFrame: database file
    """

    # number of variable
    attributes = list(DataFrame)[1:]
    N = len(attributes)

    # We are going to plot the first line of the data frame.
    # But we need to repeat the first value to close the circular graph:
    values=DataFrame.loc[0].drop('id').values.flatten().tolist()
    values += values[:1]
    values

    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]

    # Initialise the spider plot
    ax = plt.subplot(111, polar=True)

    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], attributes, color='grey', size=8)
 
    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([10,20,30,40,50,60,70,80,90,100], ["10","20","30","40","50","60","70","80","90","100"], color="grey", size=7)
    plt.ylim(0,100)
 
    # Plot data
    ax.plot(angles, values, linewidth=1, linestyle='solid')
 
    # Fill area
    ax.fill(angles, values, 'b', alpha=0.1)
    plt.show()

def plot_Correlation(DataFrame):

    playerCorrelation = DataFrame.corr()
    # plt.matshow(playerCorrelation)
    # playerCorrelation.style.background_gradient(cmap='coolwarm')
    # plt.show()

    f, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(playerCorrelation, mask=np.zeros_like(playerCorrelation, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
        square=True, ax=ax)

    plt.show(sns)
        
    sns.heatmap(playerCorrelation, 
            xticklabels=playerCorrelation.columns.values,
            yticklabels=playerCorrelation.columns.values)

