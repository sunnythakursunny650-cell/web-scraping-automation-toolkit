import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Scraped Data Analytics Hub", layout="wide")

st.title("📊 Web Scraping & Automation Dashboard")
st.markdown("Interactive exploration of real-time scraped web data.")

# Sidebar Navigation
dataset_choice = st.sidebar.radio(
    "Select Dataset to Explore:",
    ("Books Catalog Analysis", "Quotes Dataset")
)

# 1. Books Catalog Section
if dataset_choice == "Books Catalog Analysis":
    file_path = "books_catalog.csv"
    if os.path.exists(file_path):
        df_books = pd.read_csv(file_path)

        st.subheader("📚 Books Catalog Overview")
        
        # Metric KPI cards
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Books", len(df_books))
        col2.metric("Average Price", f"£{df_books['Price_GBP'].mean():.2f}")
        col3.metric("Top Rating Count (5★)", len(df_books[df_books["Rating"] == 5]))

        # Price Filter
        st.write("---")
        max_price = float(df_books["Price_GBP"].max())
        selected_price = st.slider("Filter by Maximum Price (£):", min_value=10.0, max_value=max_price, value=max_price)
        filtered_books = df_books[df_books["Price_GBP"] <= selected_price]

        # Two-column layout: Dataframe and Chart
        left_col, right_col = st.columns([3, 2])
        with left_col:
            st.write("### Filtered Books Table")
            st.dataframe(filtered_books, use_container_width=True)
            
        with right_col:
            st.write("### Rating Distribution")
            rating_counts = filtered_books["Rating"].value_counts().sort_index()
            st.bar_chart(rating_counts)

    else:
        st.warning("⚠️ `books_catalog.csv` not found. Please run `book_scraper.py` first.")

# 2. Quotes Dataset Section
elif dataset_choice == "Quotes Dataset":
    file_path = "all_quotes_data.csv"
    if os.path.exists(file_path):
        df_quotes = pd.read_csv(file_path)

        st.subheader("💬 Scraped Quotes Analysis")

        col1, col2 = st.columns(2)
        col1.metric("Total Quotes Scraped", len(df_quotes))
        col2.metric("Unique Authors", df_quotes["Author"].nunique())

        st.write("---")

        # Filter by author
        authors = ["All"] + sorted(df_quotes["Author"].unique().tolist())
        selected_author = st.selectbox("Filter quotes by Author:", authors)

        if selected_author != "All":
            display_quotes = df_quotes[df_quotes["Author"] == selected_author]
        else:
            display_quotes = df_quotes

        st.write(f"Displaying {len(display_quotes)} quotes:")
        for _, row in display_quotes.iterrows():
            st.info(f"“{row['Quote']}”\n\n— **{row['Author']}**  *(Page {row.get('Page', 'N/A')})*")

    else:
        st.warning("⚠️ `all_quotes_data.csv` not found. Please run `scraper.py` first.")

st.sidebar.markdown("---")
st.sidebar.markdown("### 👨‍💻 Developer & Author")
st.sidebar.markdown("**Sunny Thakur**")
st.sidebar.caption("Python & Machine Learning Developer")

# Quick Action Links
st.sidebar.markdown("""
[![GitHub](https://img.shields.io/badge/GitHub-Profile-181717?style=flat&logo=github)](https://github.com/sunnythakursunny650-cell)
[![Repo](https://img.shields.io/badge/Source_Code-Repository-blue?style=flat&logo=github)](https://github.com/sunnythakursunny650-cell/web-scraping-automation-toolkit)
[![Contact](https://img.shields.io/badge/Email-Contact_Me-EA4335?style=flat&logo=gmail&logoColor=white)](mailto:sunnythakursunny650@gmail.com)
""")

# Tech Stack Footnote
st.sidebar.markdown("---")
st.sidebar.markdown("**Tech Stack:** `Python` • `Playwright` • `BeautifulSoup4` • `Pandas` • `Streamlit`")