from databricks import sql
import streamlit as st
import pandas as pd

# Connect
conn = sql.connect(
    server_hostname=st.secrets["DATABRICKS_HOST"],
    http_path=st.secrets["DATABRICKS_HTTP_PATH"],
    access_token=st.secrets["DATABRICKS_TOKEN"]
)

# Create cursor
cursor = conn.cursor()

# Run query
query = """
SELECT title, company, location, hrs_ago, url
FROM main_catalogue.jobs.curated_jobs
LIMIT 100
"""

cursor.execute(query)

# Fetch results
rows = cursor.fetchall()

# Convert to DataFrame
columns = ["title", "company", "location", "hrs_ago", "url"]
df = pd.DataFrame(rows, columns=columns)

# Show in Streamlit

df["title"] = df.apply(
    lambda row: f'<a href="{row["url"]}" target="_blank">{row["title"]}</a>',
    axis=1
)

st.write(
    df[["title", "company", "location", "hrs_ago"]].to_html(escape=False, index=False),
    unsafe_allow_html=True
)

# st.dataframe(
#     df,
#     column_config={
#         "url": st.column_config.LinkColumn(
#             "title",
#             help="Click to open job",
#             display_text="title",
#         ),
#         "Link": None  # 👈 hides the raw link column (optional)
#     },
#     use_container_width=True
# )
