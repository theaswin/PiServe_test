import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import io
import warnings
warnings.filterwarnings('ignore')

class VisualisatioMaster():
    def __init__(self):
        self.df = pd.read_csv('./DBExtracted/output.csv')
        
    def LinePlot1(self):
        fig,ax = plt.subplots(figsize = (9,7))
        ax = sns.set_style(style="darkgrid")
        x = list(self.df['Response1'])
        y = list(self.df['Response2'])
        plt.xlabel('Response1')
        plt.ylabel('Response2')
        sns.lineplot(x,y)
        canvas = FigureCanvas(fig)
        fig.savefig('viz/lineplotRes1Res2.png')

    def LinePlot2(self):
        fig,ax = plt.subplots(figsize = (9,7))
        ax = sns.set_style(style="darkgrid")
        x = list(self.df['Response3'])
        y = list(self.df['Response4'])
        plt.xlabel('Response3')
        plt.ylabel('Response4')
        sns.lineplot(x,y)
        canvas = FigureCanvas(fig)
        fig.savefig('viz/lineplotRes3Res4.png')

    def Countplot1(self):
        # Create a pie plot using Seaborn and Matplotlib
        sns.set(style="whitegrid")  # Set the style (optional)

        # Create a count plot using Seaborn and Matplotlib
        sns.set(style="whitegrid")  # Set the style (optional)

        fig, ax = plt.subplots()
        sns.countplot(x='Response1', data=self.df, palette='pastel', ax=ax)
        

        fig.savefig("viz/CountplotResponse1")

    def Countplot2(self):
        # Create a pie plot using Seaborn and Matplotlib
        sns.set(style="whitegrid")  # Set the style (optional)

        # Create a count plot using Seaborn and Matplotlib
        sns.set(style="whitegrid")  # Set the style (optional)

        fig, ax = plt.subplots()
        sns.countplot(x='Response2', data=self.df, palette='pastel', ax=ax)
        fig.savefig("viz/CountplotResponse2")
    
    def Countplot3(self):
        # Create a pie plot using Seaborn and Matplotlib
        sns.set(style="whitegrid")  # Set the style (optional)

        # Create a count plot using Seaborn and Matplotlib
        sns.set(style="whitegrid")  # Set the style (optional)

        fig, ax = plt.subplots()
        sns.countplot(x='Response3', data=self.df, palette='pastel', ax=ax)
        fig.savefig("viz/CountplotResponse3")

    def Countplot4(self):
        # Create a pie plot using Seaborn and Matplotlib
        sns.set(style="whitegrid")  # Set the style (optional)

        # Create a count plot using Seaborn and Matplotlib
        sns.set(style="whitegrid")  # Set the style (optional)

        fig, ax = plt.subplots()
        sns.countplot(x='Response4', data=self.df, palette='pastel', ax=ax)
        fig.savefig("viz/CountplotResponse4")

    def Countplot5(self):
        # Create a pie plot using Seaborn and Matplotlib
        sns.set(style="whitegrid")  # Set the style (optional)

        # Create a count plot using Seaborn and Matplotlib
        sns.set(style="whitegrid")  # Set the style (optional)

        fig, ax = plt.subplots()
        sns.countplot(x='Response5', data=self.df, palette='pastel', ax=ax)
        
        fig.savefig("viz/CountplotResponse5")
    
    def Pie(self):
        self.Res1 = self.df['Response1'].mean()
        self.Res2 = self.df['Response2'].mean()
        self.Res3 = self.df['Response3'].mean()
        self.Res4 = self.df['Response4'].mean()
        self.Res5 = self.df['Response5'].mean()
        labels = ['Response1', 'Response2', 'Response3','Response4','Response5']
        sizes = [self.Res1,self.Res2,self.Res3,self.Res4,self.Res5]
        sns.set(style="whitegrid")

        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel'), wedgeprops=dict(width=0.3))
        ax.axis('equal')
        fig.savefig("viz/pie.png")






v = VisualisatioMaster()

v.Pie()