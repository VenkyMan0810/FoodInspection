import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv(r'D:\DADA BI\Datasets\MidTerm\Food_Inspections_Chicago.tsv', sep='\t')

# df = pd.read_csv(r'D:\DADA BI\Datasets\MidTerm\Food_Inspections_Chicago.csv')

profile = ProfileReport(df, title="Chicago Profiling Report")

profile.to_file("Chicago_Profiling_tsv_report.html")