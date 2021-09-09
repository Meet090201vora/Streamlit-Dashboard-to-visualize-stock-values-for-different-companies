import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt





def file_reader():
    '''

    Returns
    -------
    req_stocks_list : list of required values
        The function reads the complete .json file and returns a list of dictionaries, which contains only the useful
        attributes of the stocks.

    '''
    stock = pd.read_json('Stock List.json')
    req_stocks_list = stock[['open','high' ,'low','close','symbol','date']]

    
    return req_stocks_list


def candlestick(symbol):
    '''
    The function plots the candelstick graph for the company spacified by the input parameter.

    Parameters
    ----------
    symbol : String
        It is the symbol used for the identification of the company.

    Returns
    -------
    None.

    '''

    st.subheader("CandleStick")
    stockdata_df = models_used[symbol]
    fig = go.Figure(data=[go.Candlestick(x=stockdata_df['date'],
                    open=stockdata_df['open'],
                    high=stockdata_df['high'],
                    low=stockdata_df['low'],
                    close=stockdata_df['close'])])
    
    fig.update_layout(xaxis_title="TIME",yaxis_title="PRICE",width=900,height=600)
    
    st.plotly_chart(fig)

    
def OHLC(symbol):
    '''
    The function plots the OHLC graph for the company spacified by the input parameter.

    Parameters
    ----------
    symbol : String
        It is the symbol used for the identification of the company.

    Returns
    -------
    None.

    '''

    st.subheader("OHLC")
    stockdata_df = models_used[symbol]
    fig = go.Figure(data=[go.Ohlc(x=stockdata_df['date'],
                    open=stockdata_df['open'],
                    high=stockdata_df['high'],
                    low=stockdata_df['low'],
                    close=stockdata_df['close'])])
    
    fig.update_layout(xaxis_title="TIME",yaxis_title="PRICE",width=900,height=600)
    
    st.plotly_chart(fig)


def BAR(symbol):
    '''
    The function plots the bar graph for the company spacified by the input parameter.

    Parameters
    ----------
    symbol : String
        It is the symbol used for the identification of the company.

    Returns
    -------
    None.


    '''
    st.subheader("BAR CHART")
    stockdata_df = models_used[symbol]
    fig = px.bar(stockdata_df, x="date", y="high")

    st.plotly_chart(fig)
    


    
def vertical(symbol):
    '''
    The function plots the vertical graph for the company spacified by the input parameter.

    Parameters
    ----------
    symbol : String
        It is the symbol used for the identification of the company.

    Returns
    -------
    None.

    '''
    st.subheader("LINE CHART")
    stockdata_df = models_used[symbol]
    fig = px.line(stockdata_df, x="date", y="high")

    st.plotly_chart(fig)

df = file_reader()


st.markdown(
    """
<style>
.sidebar .sidebar-content {
    background-image: linear-gradient(#eab676,#eab676);
    color: black;
}
</style>
""",
    unsafe_allow_html=True,
)

st.markdown(f'<p style="background-color:#0066cc;color:#33ff33;font-size:24px;border-radius:2%;"></p>', unsafe_allow_html=True)


st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://cdn.nohat.cc/thumb/f/720/comvecteezy570382.jpg")
    }
    </style>
    """,
    unsafe_allow_html=True
)



st.markdown("""
<style>
div.stButton > button:first-child {
background-color: #00cc00;color:black;font-size:15px;height:3em;width:20em;border-radius:10px 10px 10px 10px;
}
.css-2trqyj:focus:not(:active) {
border-color: #81D66E;
box-shadow: none;
color: black;
background-color: #81D66E;
}
.css-2trqyj:focus:(:active) {
border-color: #81D66E;
box-shadow: none;
color: black;
background-color: #81D66E;
}
.css-2trqyj:focus:active){
background-color: #81D66E;
border-color: #81D66E;
box-shadow: none;
color: black;
background-color: #81D66E;
}
</style>""", unsafe_allow_html=True)


st.markdown("""
<style> 
.stButton>button {
    color: #4F8BF9;
    border-radius: 50%;
    height: 3em;
    width: 3em;
}

.stTextInput>div>div>input {
    color: black;
    border-color:black;
}
</style>
""",unsafe_allow_html=True)


st.title("OHLC analysis till May 2021:")
st.sidebar.title("OHLC analysis till May 2021:")
st.subheader("This application shows graphs for the following companies ")
st.sidebar.markdown("This application is a OHLC dashboard ")




unique_val = set(df["symbol"])
#print("Number of unique symbols : ",len(unique_val))

models_used = {}
for i in unique_val:
    models_used[i] = (df.loc[df.symbol == i])

    

st.sidebar.title("Companies")
button1 = st.sidebar.button("SONY")
button2 = st.sidebar.button("GOOGL")
button3 = st.sidebar.button("IBM")
button4 = st.sidebar.button("SNAP")
button5 = st.sidebar.button("AMZN")

st.sidebar.subheader("Graph")
select = st.sidebar.selectbox("",['OHLC', 'Candlestick', 'Bar graph','Vertical Line'], key='1')

text_entered = st.text_input("", "Search for companies...")
button_clicked = st.button("OK")




if button1:
    st.markdown("Sony Group Corporation commonly known as Sony and stylized as SONY) is a Japanese multinational conglomerate corporation headquartered in Kōnan, Minato, Tokyo, Japan. As a major technology company, it operates as one of the world's largest manufacturers of consumer and professional electronic products, the largest video game console company and the largest video game publisher.")
    st.title("SONY")
    

    if select == 'Candlestick':
        candlestick('SONY')
    if select == "OHLC":
        OHLC('SONY')
    if select == "Vertical Line":
        vertical('SONY')
    if select == "Bar graph":
        BAR('SONY')
        
    
if button2:
    st.markdown("Google LLC is an American multinational technology company that specializes in Internet-related services and products, which include online advertising technologies, a search engine, cloud computing, software, and hardware.")
    st.title("GOOGLE")
    
    
    if select == 'Candlestick':
        candlestick('GOOGL')
    if select == "OHLC":
        OHLC('GOOGL')
    if select == "Vertical Line":
        vertical('GOOGL')
    if select == "Bar graph":
        BAR('GOOGL')
        


    
if button3:
    st.markdown("International Business Machines Corporation is an American multinational technology corporation headquartered in Armonk, New York, with operations in over 171 countries.")
    st.title("IBM")

    if select == 'Candlestick':
        candlestick('IBM')
    if select == "OHLC":
        OHLC('IBM')
    if select == "Vertical Line":
        vertical('IBM')
    if select == "Bar graph":
        BAR('IBM')
        

        
        
if button4:
    st.markdown("Snapchat is an American multimedia instant messaging app and service developed by Snap Inc., originally Snapchat Inc. One of the principal features of Snapchat is that pictures and messages are usually only available for a short time before they become inaccessible to their recipients ");
    st.title("SNAP CHAT")

    if select == 'Candlestick':
        candlestick('SNAP')
    if select == "OHLC":
        OHLC('SNAP')
    if select == "Vertical Line":
        vertical('SNAP')
    if select == "Bar graph":
        BAR('SNAP')
        

        

if button5:
    st.markdown("Amazon.com, Inc. is an American multinational conglomerate which focuses on e-commerce, cloud computing, digital streaming, and artificial intelligence. It is one of the Big Five companies in the U.S. information technology industry, along with Google, Apple, Microsoft, and Facebook.");
    st.title("AMAZON")

    if select == 'Candlestick':
        candlestick('AMZN')
    if select == "OHLC":
        OHLC('AMZN')
    if select == "Vertical Line":
        vertical('AMZN')
    if select == "Bar graph":
        BAR('AMZN')



if button_clicked:
    text_entered = text_entered.strip().upper()

    if text_entered not in models_used.keys():
        st.subheader("COMPANY DOES NOT EXIST !")
    else:
        st.title(text_entered)

        if select == 'Candlestick':
            candlestick(text_entered)
        if select == "OHLC":
            OHLC(text_entered)
        if select == "Vertical Line":
            vertical(text_entered)
        if select == "Bar graph":
            BAR(text_entered)
        
    


    
        
    





