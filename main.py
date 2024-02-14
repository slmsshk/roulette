import pickle
import streamlit as st
import pandas as pd

# Add background color
def add_bg_from_local():
    st.markdown(
    f"""
    <style>
    .stApp {{
        background: rgb(2,0,36);
        background: linear-gradient(90deg, rgba(100,0,36,1) 0%, rgba(45,177,179,1) 35%, rgba(0,219,245,1) 100%);
    }}
    </style>
    """,unsafe_allow_html=True)
add_bg_from_local()

st.title('Model Validation')
st.image('ConfusionMatrix_WithAnnotations.png')
model = pickle.load(open('test_model.pkl','rb'))
features = model.feature_names_in_
text = st.text_input('Enter the numbers seperated with , eg:1,2,3,4,5,.....')


if bool(text):
    d = {k:v for k,v in zip(features,text.split(','))}
    
    pred = pd.DataFrame(d,index=['input']).astype(float)
    st.write(pred)

    st.markdown(f"""<h1> Model Prediction
                """,unsafe_allow_html=True)

    # st.write(pred)
    predicted = model.predict(pred)

    if predicted ==1:
        st.markdown(f"""<h1 style=color:red>Cheater</h1>🦹‍♀️🦹‍♂️""",unsafe_allow_html=True)
    else:
        st.markdown(f"""<h1 style=color:red>Innocent</h1>😇""",unsafe_allow_html=True)
else:
    st.write('enter text')