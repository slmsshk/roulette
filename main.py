import pickle
import streamlit as st
import pandas as pd

st.title('Model Validation')
st.image('ConfusionMatrix.png')
model = pickle.load(open('test_model.pkl','rb'))
features = model.feature_names_in_
text = st.text_input('Enter the numbers seperated with , eg:1,2,3,4,5,.....')



d = {k:v for k,v in zip(features,text.split(','))}
pred = pd.DataFrame(d,index=['input']).astype(float)

st.markdown(f"""<h1> Model Prediction
            """,unsafe_allow_html=True)

predicted = model.predict(pred)

if predicted ==1:
    st.markdown(f"""<h1 style=color:red>Cheater</h1>🦹‍♀️🦹‍♂️""",unsafe_allow_html=True)
else:
    st.markdown(f"""<h1 style=color:red>Innocent</h1>😇🥺""",unsafe_allow_html=True)