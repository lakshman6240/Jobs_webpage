import streamlit as st
import pandas as pd

# Sample data
data = [
    {
        "Job Title": "Data Engineer",
        "Company Name": "Microsoft",
        "Location": "Hyderabad",
        "Hrs Ago": 2,
        "Link": "https://careers.microsoft.com"
    },
    {
        "Job Title": "Data Analyst",
        "Company Name": "Google",
        "Location": "Bangalore",
        "Hrs Ago": 5,
        "Link": "https://careers.google.com"
    },
    {
        "Job Title": "ETL Developer",
        "Company Name": "Accenture",
        "Location": "Pune",
        "Hrs Ago": 10,
        "Link": "https://www.accenture.com/in-en/careers"
    }
]

# Convert to DataFrame
df = pd.DataFrame(data)

# App UI
st.set_page_config(page_title="Job Listings", layout="wide")
st.title("📊 Job Listings Dashboard")

# Show table with clickable links
st.dataframe(
    df,
    column_config={
        "Link": st.column_config.LinkColumn(
            "Apply Here",
            help="Click to open job posting",
            display_text="Open Job"
        )
    },
    use_container_width=True
)