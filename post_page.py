import pandas as pd 
import streamlit as st 
import plotly.express as px 
import data as dt

# Data Viz Pkgs
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg')


def analytics():
    st.subheader("Analytics")
    df = dt.fetch_all_task()

    with st.expander("View All Task"):
        st.write(df)

    with st.expander("Task Status Stats"):
        # Ensure the column names are correctly referenced
        new_df = df['task_status'].value_counts().reset_index()
        new_df.columns = ['task_status', 'count']  # Renaming columns
        st.dataframe(new_df)

        # Now use correct column names
        p1 = px.pie(new_df, names='task_status', values='count')
        st.plotly_chart(p1)

    with st.expander("Task Due Date"):
        task_df = df['task_due_date'].value_counts().reset_index()
        task_df.columns = ['task_due_date', 'count']  # Renaming columns
        st.dataframe(task_df)

        p2 = px.pie(task_df, names='task_due_date', values='count')
        st.plotly_chart(p2)