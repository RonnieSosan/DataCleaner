#Load packages
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib
import seaborn as sns
from IPython.display import display_html
from IPython.display import IFrame

# for inline plots
#%matplotlib inline

def PrintResults(model, X, y, title):
    """ Custom print function to display result of the model application on x and y test data
    :param model: database file
    :param x: an array of x variable(s)
    :param y: target variable
    :param title: name of model to be applied
    :return: a tuple of the model and the summary of the model
    """
    model, y_pred, Accuracy, Error, precision, recall, f1score = ApplyModel(X, y, model)
    
    _, Score_mean, Score_std = LearningCurve(X, y, model, cv, train_size)
    Score_mean, Score_std = Score_mean*100, Score_std*100
    
    
    print('Scoring Accuracy: %.2f %%'%(Accuracy))
    print('Scoring Mean: %.2f %%'%(Score_mean))
    print('Scoring Standard Deviation: %.4f %%'%(Score_std))
    print("Precision: %.2f %%"%(precision))
    print("Recall: %.2f %%"%(recall))
    print('f1-score: %.2f %%'%(f1score))
    
    Summary = pd.DataFrame({'Model': title,
                       'Accuracy': Accuracy, 
                       'Score Mean': Score_mean, 
                       'Score St Dv': Score_std, 
                       'Precision': precision, 
                       'Recall': recall, 
                       'F1-Score': f1score}, index = [0])
    return (model, Summary)

def PlotParams(Font, sizex, sizey):
    """ sets up the parameters for plotting, creating your own custom style
    :param font: set the font to be used for the labels, legend and axes
    :param sizex: figure size on x
    :param sizey: figure size on y
    """

    mpl.rcParams['figure.figsize'] = (sizex,sizey)
    plt.rcParams["legend.fontsize"] = Font
    plt.rcParams["axes.labelsize"] = Font
    mpl.rc('xtick', labelsize = Font) 
    mpl.rc('ytick', labelsize = Font)

#sets up Seaborn parametes for plotting
def snsParams(font, colour_scheme):
    """ set up the colour scheme for plotting on seaborn 
    :param font: set the font to be used for the labels, legend and axes
    :param colour_scheme: set the colour theme for the figure
    """
    #eaborn.set(context='notebook', style='darkgrid', palette='deep', font='sans-serif', font_scale=1, color_codes=True, rc=None)
    sns.set(style = 'whitegrid', palette = colour_scheme, font_scale = font)

#determined ht emissing data
def Missing (data):
    """ Identify missing values in the dataframe
    :param data: set the font to be used for the labels, legend and axes
    """
    total = data.isnull().sum().sort_values(ascending = False)
    percent = round(data.isnull().sum().sort_values(ascending = False)/len(data)*100, 2)
    missing = pd.concat([total, percent], axis = 1,keys= ['Total', 'Percent'])
    return(missing) 

#plots number of dataframes side by side
def SideSide(*args):
    html_str=''
    for df in args:
        html_str+=df.to_html()
    display_html(html_str.replace('table','table style="display:inline"'),raw = True)