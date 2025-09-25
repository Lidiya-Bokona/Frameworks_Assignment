# 📊 Frameworks_Assignment — CORD-19 Data Explorer

## Overview
This project analyzes the **CORD-19 metadata** dataset using Python frameworks. It demonstrates a basic data science workflow: loading, cleaning, exploring, visualizing, and building a simple Streamlit app.  
Because the full dataset (~1.5 GB) exceeds GitHub’s file size limit, this repository includes a **cleaned sample** for demonstration. Instructions are provided for downloading the full dataset if needed.

## Tools
- Python 3.7+
- pandas (data manipulation)
- matplotlib & seaborn (visualization)
- Streamlit (interactive app)
- Jupyter Notebook (exploration)

## Features
- Data cleaning (missing values, date parsing, word counts)
- Publication trends by year
- Top publishing journals
- Frequent title keywords
- Interactive dashboard with filters

## How to Run
1. Clone this repo and create a virtual environment.
2. Install requirements:
   ```bash
   pip install -r requirements.txt
3. Place the dataset inside the  folder:
  - Use the included  (recommended for quick testing), or
  - Download the full dataset from the CORD-19 Research Challenge and save it as  (note: very large file).
4.	Run the notebook for exploration:
    ```bash
    jupyter notebook Frameworks_Assignment.ipynb
5. Launch the Streamlit app:
   ```bash
   streamlit run app/app.py

## Reflection
This assignment strengthened skills in data wrangling, visualization, and framework integration.
The main challenge was handling the large dataset, which was solved by sampling and cleaning for efficient analysis.
Future improvements could include normalizing journal names, expanding keyword analysis, and supporting chunked processing of the full dataset.

    
