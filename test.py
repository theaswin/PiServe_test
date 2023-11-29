import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


class new():
    def Pie(self):
        self.df = pd.read_csv('.//DBExtracted/output.csv')
        self.Res1 = self.df['Response3'].mean()
        print(self.Res1)

v = new()
v.Pie()