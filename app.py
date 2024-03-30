import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Nykaa_product dataset
@st.cache
def load_data(file_path):
    return pd.read_csv('Nykaa_product.csv')

def main():
    st.title('Nykaa Product Analysis')

    # Load data
    file_path = 'Nykaa_product.csv'  # Adjust the file path as needed
    df = load_data('Nykaa_product.csv')

    st.write(""" # My FIRST APP""")

    # Sidebar options
    st.sidebar.header('Visualization Options')

    # Display top categories by sales
    st.sidebar.subheader('Top Categories by Sales')
    top_categories = st.sidebar.checkbox('Show Top Categories by Sales')
    if top_categories:
        st.subheader('Top Categories by Sales')
        # Convert 'Product Price' column to numeric data type
        df['Product Price'] = pd.to_numeric(df['Product Price'], errors='coerce')

        # Replace NaN values with zeros
        df['Product Price'].fillna(0, inplace=True)

        category_sales = df.groupby('Product Category')['Product Price'].sum().reset_index()
        top_categories_data = category_sales.nlargest(10, 'Product Price')
        st.write(top_categories_data)

        

    # Display scatter plot for Price vs Rating
    st.sidebar.subheader('Price vs Rating')
    scatterplot = st.sidebar.checkbox('Show Scatter Plot: Price vs Rating')
    if scatterplot:
        st.subheader('Scatter Plot: Price vs Rating')
        # Ensure 'Rating' column is present in the DataFrame
        if 'Product Rating' not in df.columns:
            st.error("Rating column not found in the dataset.")
        else:
            # Drop rows with NaN values in 'Price' and 'Rating' columns
            df.dropna(subset=['Product Price', 'Product Rating'], inplace=True)

            # Convert 'Price' and 'Rating' columns to numeric data type
            df['Product Price'] = pd.to_numeric(df['Product Price'], errors='coerce')
            df['Product Rating'] = pd.to_numeric(df['Product Rating'], errors='coerce')

            # Check if sample size is greater than DataFrame size
            sample_size = min(1000, len(df))
            df_sample = df.sample(n=sample_size)

            # Plot scatter plot
            sns.scatterplot(data=df_sample, x='Product Price', y='Product Rating', alpha=0.5)
            plt.xlabel('Product Price')
            plt.ylabel('Product Rating')
            plt.title('Scatter Plot: Price vs Rating')
            st.pyplot()

    # Display pie chart option
    st.sidebar.subheader('Pie Chart: Top 10 Category-wise Sales')
    pie_chart = st.sidebar.checkbox('Show Pie Chart: Top 10 Category-wise Sales')
    if pie_chart:
        st.subheader('Pie Chart: Top 10 Category-wise Sales')
        # Convert 'Product Price' column to numeric data type
        df['Product Price'] = pd.to_numeric(df['Product Price'], errors='coerce')

        # Replace NaN values with zeros
        df['Product Price'].fillna(0, inplace=True)

        category_sales = df.groupby('Product Category')['Product Price'].sum().reset_index()
        top_categories_data = category_sales.nlargest(10, 'Product Price')
        st.write(top_categories_data)

        # Plot the pie chart for top categories
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.pie(top_categories_data['Product Price'], labels=top_categories_data['Product Category'], autopct='%1.1f%%', startangle=140)
        plt.axis('equal')
        plt.title('Pie Chart: Top 10 Category-wise Sales')
        st.pyplot(fig)

    # Display bar plot option
    st.sidebar.subheader('Bar Plot: Top 10 Products by Price')
    bar_plot = st.sidebar.checkbox('Show Bar Plot: Top 10 Products by Price')
    if bar_plot:
        st.subheader('Bar Plot: Top 10 Products by Price')

        # Convert 'Product Price' column to numeric data type
        df['Product Price'] = pd.to_numeric(df['Product Price'], errors='coerce')

        # Remove rows with NaN values in 'Product Price' column
        df.dropna(subset=['Product Price'], inplace=True)

        # Get top 10 products by price
        top_products = df.nlargest(10, 'Product Price')

        # Plot bar plot
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(data=top_products, x='Product Price', y='Product Name', ax=ax)
        ax.set_xlabel('Product Price')
        ax.set_ylabel('Product Name')
        ax.set_title('Bar Plot: Top 10 Products by Price')
        st.pyplot(fig)

    # Display heatmap option
    st.sidebar.subheader('Heatmap: Correlation Matrix')
    heatmap = st.sidebar.checkbox('Show Heatmap: Correlation Matrix')
    if heatmap:
        st.subheader('Heatmap: Correlation Matrix')
        # Remove non-numeric columns
        numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
        numeric_df = df[numeric_columns]

        # Calculate correlation matrix
        corr_matrix = numeric_df.corr()

        # Plot heatmap
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
        ax.set_title('Heatmap: Correlation Matrix')
        st.pyplot(fig)

if __name__ == '__main__':
    main()
