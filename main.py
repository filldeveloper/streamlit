import streamlit as st
import pandas as pd
# import mymodel as m

data = {
    'Coluna 1': [1, 5, 9, 10, 11],
    'Coluna 2': [10, 20, 50, 60, 70]
}
df = pd.DataFrame(data)
st.title("Felipe Barreto da Silva")
st.subheader('Introducing Streamlit in Automate Everything with Python')
st.write("""
This is our first Web App.
Enjoy it!
""")
st.write(df)

st.line_chart(df)

myslider = st.slider('Celsius')
st.write(myslider, 'in Fahrenheit is', myslider * 9/5 +32)
st.button('Submit')
# st.write(m.run(window=15))