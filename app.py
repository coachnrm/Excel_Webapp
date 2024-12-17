import pandas as pd
import streamlit as st
import plotly.express as px

# Set Streamlit page configuration
st.set_page_config(page_title='Survey Results', page_icon="📊", layout="centered")

# Page header and subheader
st.header('Survey Results 2021')
st.subheader('Was the tutor helpful?')

# Read the Excel file
excel_file = 'Survey_Results.xlsx'
sheet_name = 'DATA'

# Load data into pandas DataFrame
try:
    df = pd.read_excel(excel_file, sheet_name=sheet_name, usecols='B:D', header=3)
    df_participants = pd.read_excel(excel_file, sheet_name=sheet_name, usecols='F:G', header=3)

    # Display data
    st.subheader("Survey Data")
    st.write("### Main Survey Data")
    st.dataframe(df)  # Display the DataFrame as a table

    # Group by Rating
    df_grouped = df.groupby(by=['Rating']).count()[['Age']]
    df_grouped = df_grouped.rename(columns={'Age':'Votes'}).reset_index()
    st.dataframe(df_grouped)


    # Visualization using Ploty Express
    st.subheader("Survey Results Visualization")
    fig = px.bar(df_grouped, x='Rating', y='Votes', color_discrete_sequence=['#F63366']*len(df_grouped), title='Tutor Ratings')
    st.plotly_chart(fig)

    st.write("### Participants Data")
    st.dataframe(df_participants)

    pie_chart = px.pie(df_participants,
                       title='Total No. of Participants',
                       values='Participants',
                       names='Departments')
    st.plotly_chart(pie_chart)



except FileNotFoundError:
    st.error("Error: File 'Survey_Results.xlsx' not found. Please ensure it exists in the same directory.")

except Exception as e:
    st.error(f"An error occurred: {e}")
