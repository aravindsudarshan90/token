import streamlit as st
from pymongo import MongoClient
import datetime 
import os



mongo = MongoClient('mongodb+srv://aravind:aravind@cluster0-9tkxn.mongodb.net/test?retryWrites=true')
db = mongo.demo
JLPT = db.JLPT

def fetch(num,option):
    try:
        if option=='Breakfast':
            morn_already_ver = JLPT.find({'phone_num':str(num),'morn_verified':'1'})
            morn_result = JLPT.find({'phone_num':str(num),'morn_verified':'0'})
            if list(morn_already_ver):
                return -1
            return morn_result
        if option=='Lunch':
            aft_already_ver = JLPT.find({'phone_num':str(num),'aft_verified':'1'})
            aft_result = JLPT.find({'phone_num':str(num),'aft_verified':'0'})
            if list(aft_already_ver):
                return -1
            return aft_result
    except Exception:
        return {}


def main():
    st.set_page_config(page_title="JLPT Token Verification", page_icon="🤖")
    st.title("JLPT Token Verification")
    with st.form("my_form"):
        number = st.number_input("Phone Number without +91", min_value=0, max_value=9999999999, key="index")
        option = st.selectbox('Select the slot',('Breakfast', 'Lunch'))
        submitted = st.form_submit_button("Submit")

        if submitted:
            data = fetch(number,option)
            if data == -1:
                st.image('https://cdn.jsdelivr.net/gh/aravindsudarshan90/CDN/token_exp.PNG', caption=f"Status: Token expired")
            elif list(data):
                if option=='Breakfast':
                    myquery = {'phone_num':str(number)}
                    newvalues = {"$set":{'morn_verified':'1','morn_time': datetime.datetime.now()}}
                    JLPT.update_one(myquery, newvalues)
                elif option=='Lunch':
                    myquery = {'phone_num':str(number)}
                    newvalues = {"$set":{'aft_verified':'1','aft_time': datetime.datetime.now()}}
                    JLPT.update_one(myquery, newvalues)
                st.image('https://cdn.jsdelivr.net/gh/aravindsudarshan90/CDN/Verified.PNG', caption=f"Status: Verified")
                st.write("You are verified. Please proceed to the food counter")
            else:
                 st.image('https://cdn.jsdelivr.net/gh/aravindsudarshan90/CDN/nverified.PNG', caption=f"Status: Not Verified")
                 st.write("Kindly Check and Re-enter the phone number. If issue persists, kindly contact the venue incharge")

if __name__ == '__main__':
    main()