import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import streamlit as st

# Page title
st.title('Nifty Stocks Explorer 📈')

# Load the dataset
@st.cache_data
def load_data():
    df = pd.read_csv('Nifty_Stocks.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    return df

df = load_data()

# Show unique categories
categories = df['Category'].unique()
selected_category = st.selectbox('Select a Category:', categories)

# Filter by selected category
filtered_by_category = df[df['Category'] == selected_category]

# Show unique symbols within the selected category
symbols = filtered_by_category['Symbol'].unique()
selected_symbol = st.selectbox('Select a Symbol:', symbols)

# Filter by selected symbol
filtered_data = filtered_by_category[filtered_by_category['Symbol'] == selected_symbol]

# Plot
st.subheader(f'Closing Price Over Time for {selected_symbol}')
fig, ax = plt.subplots(figsize=(10, 5))
sb.lineplot(data=filtered_data, x='Date', y='Close', ax=ax)
plt.xticks(rotation=90)
st.pyplot(fig)
