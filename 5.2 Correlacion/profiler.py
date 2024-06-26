# %%
import pandas as pd
from ydata_profiling import ProfileReport

# %%
csv_folder_path = "/Users/d3r/Documents/Github/laboratoria-talks/5.2 Correlacion/data"  # Replace with your actual folder path
csv_files = {
    "competition_data": f"{csv_folder_path}/track_in_competition - competition.csv",
    "technical_info": f"{csv_folder_path}/track_technical_info - technical_info.csv",
    "spotify_data": f"{csv_folder_path}/track_in_spotify - spotify.csv"
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
