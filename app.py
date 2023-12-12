import pandas as pd
import streamlit as st





df = pd.read_csv('startup_cleaned.csv')

def load_investor_details(investor):
    st.title(investor)
    # Load the recent 5 investments of the investor
    last5_df = df[df['investors'].str.contains(investor)].head()[['date','startup','vertical','city', 'round', 'amount']]
    st.subheader('Most recent Investments')
    st.dataframe(last5_df)





st.sidebar.title('Startup Funding Analysis')

option = st.sidebar.selectbox('Select one', ['Overall Analysis', 'StartUp', 'Investor'])

if option == 'Overall Analysis':
    st.title('Overall Analysis')
elif option == 'StartUp':
    st.sidebar.selectbox('Select StartUp', sorted(df["startup"].unique().tolist()))
    btn1 = st.sidebar.button('Find Startup Details')
    st.title('StartUp Analysis')
else:
    selected_investor = st.sidebar.selectbox('Select StartUp', sorted(set(df['investors'].str.split(',').sum())))
    btn2 = st.sidebar.button('Find Investor Details')
    if btn2:
        load_investor_details(selected_investor)


    
