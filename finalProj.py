import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import streamlit as st
from datetime import date

date_diff=0


st.write("""# USD->INR CALCULATOR!""")



def days_between(y,m,d):
    d0 = date(y,m,d)
    d1 = date(2023,1,31)
    delta = d1 - d0
    return abs(delta.days)

def literal_date_diff():
    from datetime import datetime

    date1 = datetime.now()
    date2 = datetime(day=31, month=1, year=2023)

    timedelta = date2 - date1
    #st.subheader("The DATE today is ",date1)
    return ((abs(timedelta)).days)

def user_input_features():
    
    st.sidebar.header("Select a Date")
    
    Day = st.sidebar.slider("Please input the Day", min_value=1, max_value=30, value=3)

    Month = st.sidebar.slider("Please input the month", min_value=1, max_value=12, value=5)

    Year = st.sidebar.slider("Please input the year",min_value=2023, max_value=2025, value=2023)

    
    print("day",Day)
    print("month",Month)
    print("yr",Year)
    
    date_diff=days_between(Year,Month,Day)
    print("date_diff",date_diff)
    
    df_train = pd.read_csv('train.csv')

    df_reqd = df_train[['Day', 'Price']]

    X= np.array(df_reqd['Day']).reshape(-1,1)
    y= np.array(df_reqd['Price']).reshape(-1,1)


    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    from sklearn.ensemble import RandomForestRegressor
    from sklearn.metrics import mean_squared_error

    rf = RandomForestRegressor(n_estimators = 300, max_features = 'sqrt', max_depth = 5, random_state = 18).fit(X_train, y_train)
    
    li=[]
    
    print("hhhhhhhhhhhhh",date_diff)
    date_diff=date_diff+834
    li.append(date_diff)
    
    
    X_cutu = np.asarray(li).reshape(-1, 1)
    
    print("X_Curu",X_cutu)
    prediction = rf.predict(X_cutu)
    
    td = date.today()
    
    st.write("Date Today : ",td)
    
    ok=literal_date_diff()
    print("ok ",ok)
    
    X_plot=rf.predict(X_cutu)
    
    st.write("--------------------------------------------------------------------------")
    st.write("The prediction of USD on the selected date ",X_plot[0])
    st.subheader("Analysis Graph")
    st.write("--------------------------------------------------------------------------")
    print(X_plot)
    
    
    
    ppx=np.array([ok+834,ok+835,ok+836,ok+837])
    
    print(ppx)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    ppy = rf.predict(ppx.reshape(-1,1))
    print(ppy)
    plt.scatter(X_test,y_test,color="black",label="last 3 years")
    plt.scatter(X_cutu,X_plot,color="red",label="selected date")
    plt.xlabel('Day Count')
    plt.ylabel('1USD in INR')
    plt.legend(bbox_to_anchor=(-0.35,0.5))
    plt.show()
    st.pyplot()
    
 
user_input_features()