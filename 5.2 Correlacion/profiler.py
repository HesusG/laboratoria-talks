# %%
import pandas as pd
from ydata_profiling import ProfileReport

# %%
csv_folder_path = "/Users/d3r/Documents/Github/laboratoria-talks/5.2 Correlacion/dataset_banco"  # Replace with your actual folder path
csv_files = {
    "default": f"{csv_folder_path}/default.csv",
    "loans_detail": f"{csv_folder_path}/loans_detail.csv",
    "loans_outstanding": f"{csv_folder_path}/loans_outstanding.csv",
    "user_info": f"{csv_folder_path}/user_info.csv"
}

# %%
for name, filepath in csv_files.items():
    # Read the CSV file
    df = pd.read_csv(filepath)

    # Generate the profile report
    profile = ProfileReport(df, title=f"Profiling Report for {name}", explorative=True)

    # Save the report as an HTML file (replace with your desired extension)
    profile.to_file(f"{name}_profile_report.html")

    print(f"Generated profile report for {name} and saved to {name}_profile_report.html")

# %%
df = pd.read_csv("/Users/d3r/Documents/Github/laboratoria-talks/5.2 Correlacion/dataset_banco/loans_detail.csv")
# %%
df.info()
# %%
import plotly_express as px
fig = px.box(df, y='debt_ratio')
fig.show()
# %%
df = pd.read_csv("/Users/d3r/Documents/Github/laboratoria-talks/5.2 Correlacion/dataset_banco/user_info.csv")
fig = px.box(df, y='age')
fig.show()
# %%
