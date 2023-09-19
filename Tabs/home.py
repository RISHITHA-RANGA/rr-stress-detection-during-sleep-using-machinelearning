import streamlit as st
def app():
    st.title("Stress Level Detector")
    st.image("./images/home stress image.jpg")
    st.markdown(
    """<p style="font-size:20px;">
              The SaYoPillow is designed to address the importance of sleep in our busy lives and promote the idea of "Smart-Sleeping." It incorporates an edge processor with a sleep analysis model to monitor physiological changes and sleep habits. Using this data, it predicts stress levels for the next day and securely stores it in the IoT cloud. Data can also be securely transferred to third-party apps. Users have control over data access through a user-friendly interface. This innovative pillow prioritizes sleep patterns to reduce stress, boasting an accuracy rate of up to 96%.
        </p>
    """, unsafe_allow_html=True)
