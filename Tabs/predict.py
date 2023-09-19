import streamlit as st
from web_functions import predict
def app(df, X, y):
    st.title("Prediction Page")
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:blue">Decision Tree Classifier</b> for the Prediction of Stress Level.
            </p>
        """, unsafe_allow_html=True)
    st.subheader("Select Values:")
    sr = st.slider("Snoring Rate", int(df["sr"].min()), int(df["sr"].max()))
    rr = st.slider("Respiration Rate", int(df["rr"].min()), int(df["rr"].max()))
    bt = st.slider("Body Temperature (in °F)", int(df["bt"].min()), int(df["bt"].max()))
    lm = st.slider("Limb Movement", float(df["lm"].min()), float(df["lm"].max()))
    bo = st.slider("Blood Oxygen(%)", float(df["bo"].min()), float(df["bo"].max()))
    rem = st.slider("Rapid Eye Movement", float(df["rem"].min()), float(df["rem"].max()))
    sh = st.slider("Sleeping Hour", float(df["sh"].min()), float(df["sh"].max()))
    hr = st.slider("Heart Rate", float(df["hr"].min()), float(df["hr"].max()))
    
    features = [sr,rr,bt,lm,bo,rem,sh,hr]

    if st.button("Predict"):
      
        prediction, score = predict(X, y, features)
        st.info("Stress level detected...")

        if (prediction == 1):
            st.success("The person has low stress level 🙂")
        elif (prediction == 2):
            st.warning("The person has medium stress level 😐")
        elif (prediction == 3):
            st.error("The person has high stress level! 😞")
        elif (prediction == 4):
            st.error("The person has very high stress level!! 😫")
        else:
            st.success("The person is stress free and calm 😄")

        st.write("The model has an accuracy of ", (score*100),"%")
