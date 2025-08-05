import streamlit as st
import pandas as pd

# Load the cleaned dataset
@st.cache_data
def load_data():
    df = pd.read_csv("final_cleaned_recipes.csv")
    return df

df = load_data()

st.set_page_config(page_title="Recipe Finder", layout="centered")
st.title("🍽️ Recipe Finder App")
st.write("Enter a food title to get ingredients and instructions.")

# User input
user_input = st.text_input("Enter Recipe Title")

if user_input:
    user_input = user_input.strip().lower()

    # Search for the title
    matches = df[df['title'].str.lower().str.contains(user_input)]

    if not matches.empty:
        for idx, row in matches.iterrows():
            st.subheader(f"🍲 {row['title']}")
            st.markdown("#### 🧂 Ingredients:")
            st.write(row['ingredients'])

            st.markdown("#### 🧑‍🍳 Instructions:")
            st.write(row['instructions'])
            st.markdown("---")
    else:
        st.warning("No recipe found. Try a different title.")
