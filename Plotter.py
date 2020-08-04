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

#makes heat map of correllations
def PlotCorr(data):
    """ Make heat map of correlation
    :param data: dataframe
    """
    corr = data.corr()
    #fig , ax = plt.figure( figsize = (6,6 ) )
    cmap = sns.diverging_palette( 220 , 10 , as_cmap = True )
    sns.heatmap(
        corr, cmap = cmap, square = True, cbar = False, cbar_kws = { 'shrink' : 1 }, 
     annot = True, annot_kws = { 'fontsize' : 14 }
    )
    plt.yticks(rotation = 0)
    plt.xticks(rotation = 90)

#plot top correlatins in a heat map
def TopCorr(dataFrame, lim):
    """ plot the top correlations in a heat map
    :param dataFrame: database file
    :param dataFrame: dataframe for correlation
    :param lim: limit of variable to be considered
    :param title: name of model to be applied
    :return: a tuple of the model and the summary of the model
    """
    corr = dataFrame.corr()
    cmap = sns.diverging_palette( 220 , 10 , as_cmap = True )
    #fig , ax = plt.subplots( figsize = (6,6 ) )
    sns.heatmap(corr[(corr >= lim) | (corr <= -lim)], 
         vmax = 1.0,  cmap = cmap, vmin = -1.0, square = True, cbar = False, linewidths = 0.2, annot = True, 
                annot_kws = {"size": 14})
    plt.yticks(rotation = 0)
    plt.xticks(rotation = 90)

def scatterPlot(x_Axis, y_Axis, DataFrame):
    plot_Title = "{0} vs {1}".format(x_Axis, y_Axis)
    plt.scatter(DataFrame[x_Axis], DataFrame[y_Axis])
    plt.xlabel(x_Axis)
    plt.ylabel(y_Axis)
    plt.title(plot_Title)

