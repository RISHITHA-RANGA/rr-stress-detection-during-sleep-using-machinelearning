import warnings
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def app(df, X, y):
    warnings.filterwarnings('ignore')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.title("Visualise the Stress Level")

    if st.checkbox("Show the correlation heatmap"):
        st.subheader("Correlation Heatmap")
        # Create a correlation heatmap using Plotly
        fig = px.imshow(df.corr())
        st.plotly_chart(fig)

    if st.checkbox("Show Scatter Plot"):
        st.subheader("Scatter Plots")
        # Create scatter plots using Plotly Express
        scatter_fig = px.scatter(df, x='bt', y='rr', title="Body Temperature vs Respiration Rate")
        scatter_fig2 = px.scatter(df, x='sr', y='lm', title="Snoring Rate vs Limb Movement")
        scatter_fig3 = px.scatter(df, x='bo', y='bt', title="Blood Oxygen vs Body Temperature")
        scatter_fig4 = px.scatter(df, x='sh', y='hr', title="Sleeping Hours vs Heart Rate")

        # Display the scatter plots
        st.plotly_chart(scatter_fig)
        st.plotly_chart(scatter_fig2)
        st.plotly_chart(scatter_fig3)
        st.plotly_chart(scatter_fig4)

    if st.checkbox("Show 3D Scatter Plot"):
        st.subheader("3D Scatter Plot")
        # Create a 3D scatter plot using Plotly Express
        scatter_3d_fig = px.scatter_3d(df, x='bt', y='rr', z='hr', title="3D Scatter Plot")
        st.plotly_chart(scatter_3d_fig)

    if st.checkbox("Display Boxplot"):
        st.subheader("Box Plots")
        # Create box plots using Plotly Express
        box_fig = px.box(df, y=['sr', 'rr', 'bt', 'rem', 'bo', 'sh'], title="Box Plot of Features")

        # Display the box plot
        st.plotly_chart(box_fig)

    if st.checkbox("Show Histogram"):
        st.subheader("Histograms")
        # Create histograms using Plotly Express
        hist_fig = px.histogram(df, x='bt', title="Body Temperature Histogram")
        hist_fig2 = px.histogram(df, x='hr', title="Heart Rate Histogram")

        # Display the histograms
        st.plotly_chart(hist_fig)
        st.plotly_chart(hist_fig2)

    if st.checkbox("Show Violin Plot"):
        st.subheader("Violin Plot")
        # Create a violin plot using Plotly Express
        violin_fig = px.violin(df, y='rr', box=True, points="all", title="Violin Plot")
        st.plotly_chart(violin_fig)
