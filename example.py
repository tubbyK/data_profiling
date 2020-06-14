from dataprep.eda import plot, plot_correlation, plot_missing
from pandas_profiling import ProfileReport
import pandas as pd


class Example():
    def __init__(self, src=None):
        if src is None: src = 'https://www.openml.org/data/get_csv/1595261/phpMawTba'
        self.df = pd.read_csv(src)

    def run(self):
        df = self.df
        plot(df).save('dataprep_plot.html')
        plot_correlation(df).save('dataprep_correlation.html')
        plot_missing(df).save('dataprep_missing.html')
        ProfileReport(df, title='Pandas Profiling Report').to_file('pandas_profiling_report.html')


if __name__ == '__main__':
    e = Example()
    e.run()