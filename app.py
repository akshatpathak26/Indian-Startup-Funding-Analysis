import pandas as pd
import streamlit as st





df = pd.read_csv('startup_funding.csv')

df['Investors Name'] = df['Investors Name'].fillna('Undisclosed')
st.dataframe(df)

st.sidebar.title('Startup Funding Analysis')

option = st.sidebar.selectbox('Select one', ['Overall Analysis', 'StartUp', 'Investor'])

if option == 'Overall Analysis':
    st.title('Overall Analysis')
elif option == 'StartUp':
    st.sidebar.selectbox('Select StartUp', sorted(df["Startup Name"].unique().tolist()))
    btn1 = st.sidebar.button('Find Startup Details')
    st.title('StartUp Analysis')
else:
    st.sidebar.selectbox('Select StartUp', sorted(df['Investors Name'].unique().tolist()))
    btn2 = st.sidebar.button('Find Investor Details')
    st.title('Investor Analysis')
    
