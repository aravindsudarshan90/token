import streamlit as st
from pymongo import MongoClient
import datetime 
import os
import json
import requests



mongo = MongoClient('mongodb+srv://aravind:aravind@cluster0-9tkxn.mongodb.net/test?retryWrites=true')
db = mongo.demo
JLPT = db.JLPT

def fetch(num):
    try:
        morn_already_ver = JLPT.find({'phone_num':str(num),'morn_verified':'1'})
        morn_result = JLPT.find({'phone_num':str(num),'morn_verified':'0'})
        if list(morn_already_ver):
            return -1
        return list(morn_result)
    except Exception:
        return {}


def main():
    st.set_page_config(page_title="JLPT Token Verification - Breakfast", page_icon="🤖")
    st.title("JLPT Token Verification - Breakfast")
    st.markdown("1.Kindly enter the registered mobile number in the field below.")
    st.markdown("2.Kindly refrain from submitting more than once.")
    with st.form("my_form"):
        number = st.number_input("Phone Number without +91", min_value=0, max_value=9999999999, key="index")
        # option = st.selectbox('Select the slot',('Breakfast', 'Lunch'))
        submitted = st.form_submit_button("Submit")

        if submitted:
            time = requests.get(url="http://worldtimeapi.org/api/timezone/Asia/Kolkata").json()['datetime']
            data= fetch(number)
            if data == -1:
                st.image('https://cdn.jsdelivr.net/gh/aravindsudarshan90/CDN/Verifie_Double.PNG', caption=f"Status: Token Already Verified")
            elif data:
                myquery = {'phone_num':str(number)}
                newvalues = {"$set":{'morn_verified':'1','morn_time':time}}
                st.write("Name: " + str(data[0]['name']))
                JLPT.update_one(myquery, newvalues)
                st.image('https://cdn.jsdelivr.net/gh/aravindsudarshan90/CDN/Verified.PNG', caption=f"Status: Verified")
                st.write("You are verified. Please proceed to the food counter")
            else:
                 st.image('https://cdn.jsdelivr.net/gh/aravindsudarshan90/CDN/nverified.PNG', caption=f"Status: Not Verified")
                 st.write("Kindly Check and Re-enter the phone number. If issue persists, kindly contact the venue incharge")

if __name__ == '__main__':
    main()