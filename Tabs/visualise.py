import warnings
import matplotlib.pyplot as plt
import seaborn as sns
'''from sklearn.metrics import plot_confusion_matrix'''
from sklearn import tree
import streamlit as st
from web_functions import train_model
def app(df, X, y):
    warnings.filterwarnings('ignore')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.title("Visualise the Stress Level")
    if st.checkbox("Show the correlation heatmap"):
        st.subheader("Correlation Heatmap")
        fig = plt.figure(figsize = (10, 6))
        ax = sns.heatmap(df.iloc[:, 1:].corr(), annot = True)   
        bottom, top = ax.get_ylim()                             
        ax.set_ylim(bottom + 0.5, top - 0.5)                   
        st.pyplot(fig)
    if st.checkbox("Show Scatter Plot"):
        figure, axis = plt.subplots(2, 2,figsize=(15,10))
        sns.scatterplot(ax=axis[0,0],data=df,x='bt',y='rr')
        axis[0, 0].set_title("Body Temperature vs Respiration Rate")
        sns.scatterplot(ax=axis[0,1],data=df,x='sr',y='lm')
        axis[0, 1].set_title("Snoring Rate vs Limb Movement")
        sns.scatterplot(ax=axis[1, 0],data=df,x='bo',y='bt')
        axis[1, 0].set_title("Blood Oxygen vs Body Temperature")
        sns.scatterplot(ax=axis[1,1],data=df,x='sh',y='hr')
        axis[1, 1].set_title("Sleeping Hour vs Heart Rate")
        st.pyplot()
    if st.checkbox("Display Boxplot"):
        fig, ax = plt.subplots(figsize=(15,5))
        df.boxplot(['sr', 'rr', 'bt','rem','bo','sh'],ax=ax)
        st.pyplot()
