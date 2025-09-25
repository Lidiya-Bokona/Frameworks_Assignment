import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import re

st.set_page_config(page_title="CORD-19 Data Explorer", layout="wide")
sns.set(style="whitegrid")

@st.cache_data
def load_data():
    # Load the smaller, cleaned file you saved from your notebook
    df = pd.read_csv('data/metadata_clean_sample.csv', parse_dates=['publish_time'])
    return df

def top_words_in_titles(df, n=20):
    titles = df['title'].dropna().astype(str).str.lower().tolist()
    words = []
    for t in titles:
        words.extend(re.findall(r"[a-z]+", t))
    stop = set(["the","and","of","in","to","a","for","on","with","from","by","an","is","are","as","at","into","during","covid","sars","cov","coronavirus"])
    words = [w for w in words if w not in stop and len(w) > 2]
    return Counter(words).most_common(n)

df = load_data()

st.title("CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers")

# Sidebar filters
min_year = int(df['year'].min())
max_year = int(df['year'].max())
year_range = st.slider("Select year range", min_year, max_year, (max(min_year, 2019), max_year))

journal = st.selectbox("Select a journal (optional)", options=["All"] + sorted(df['journal'].unique().tolist()))
source_col = 'source_x' if 'source_x' in df.columns else None

# Filter data
mask = (df['year'] >= year_range[0]) & (df['year'] <= year_range[1])
if journal != "All":
    mask &= (df['journal'] == journal)
df_f = df[mask]

st.subheader("Sample of filtered data")
st.dataframe(df_f.head(20))

# Publications by year
st.subheader("Publications by year")
year_counts = df_f['year'].value_counts().sort_index()
fig, ax = plt.subplots(figsize=(8,4))
ax.bar(year_counts.index.astype(int), year_counts.values, color="#1f77b4")
ax.set_xlabel("Year")
ax.set_ylabel("Count")
ax.set_title("Publications by Year")
st.pyplot(fig)

# Top journals
st.subheader("Top publishing journals")
top_n = st.slider("How many top journals to show?", 5, 20, 10)
top = df_f['journal'].value_counts().head(top_n)
fig2, ax2 = plt.subplots(figsize=(8,6))
sns.barplot(x=top.values, y=top.index, ax=ax2, palette="Blues_d")
ax2.set_xlabel("Paper count")
ax2.set_ylabel("Journal")
ax2.set_title(f"Top {top_n} Journals")
st.pyplot(fig2)

# Source distribution
if source_col and source_col in df_f.columns:
    st.subheader("Paper counts by source")
    counts = df_f[source_col].fillna("Unknown").value_counts()
    fig3, ax3 = plt.subplots(figsize=(8,4))
    sns.barplot(x=counts.index, y=counts.values, ax=ax3, palette="Greens_d")
    ax3.set_xlabel("Source")
    ax3.set_ylabel("Count")
    ax3.set_title("Source distribution")
    plt.xticks(rotation=45, ha="right")
    st.pyplot(fig3)

# Top words
st.subheader("Most frequent words in titles")
n_words = st.slider("Number of words", 10, 40, 20)
words = top_words_in_titles(df_f, n=n_words)
st.table(pd.DataFrame(words, columns=["word", "count"]))