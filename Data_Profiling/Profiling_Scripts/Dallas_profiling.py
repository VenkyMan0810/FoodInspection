import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv(r'D:\DADA BI\Datasets\MidTerm\Food_Inspection_Dallas.tsv', sep='\t')

# df = pd.read_csv(r'D:\DADA BI\Datasets\MidTerm\Food_Inspection_Dallas.csv')

profile = ProfileReport(df, title="Dallas Profiling Report")

profile.to_file("Dallas_Profiling_tsv_report.html")