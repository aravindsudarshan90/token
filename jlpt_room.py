import streamlit as st
from pymongo import MongoClient
import pandas as pd
import datetime 
import os
import json
import requests


d1 = {"N3":{45:{"level":"N3","Floor":"3","Wing":"Right_wing","Room_Number": "20"}}}
d1 = {"N2":{},
        "N4":{},
        "N5":{},
    "N1":{},
    "N3":{9900052603:{"Name":"Sneha","level":"N3","Floor":"3","Wing":"Right_wing","Room_Number": "20"}, 9900287638:{"Name":"Srividhya","level":"N3","Floor":"3","Wing":"Right_wing","Room_Number": "20"}, 8050347444:{"Name":"Geeta Menon","level":"N3","Floor":"3","Wing":"Right_wing","Room_Number": "38"}, 9663313052:{"Name":"Sowmini","level":"N3","Floor":"3","Wing":"Chapel_wing","Room_Number": "43"}, 9900211175: {"Name":"Savitha","level":"N3","Floor":"2","Wing":"Right_wing","Room_Number": "26"}}}
# mongo = MongoClient('mongodb+srv://aravind:aravind@cluster0-9tkxn.mongodb.net/test?retryWrites=true')
# db = mongo.demo
# JLPT = db.JLPT


# def fetch(num):
#     try:
#         morn_already_ver = JLPT.find({'phone_num':str(num),'morn_verified':'1'})
#         morn_result = JLPT.find({'phone_num':str(num),'morn_verified':'0'})
#         if list(morn_already_ver):
#             return -1
#         return list(morn_result)
#     except Exception:
#         return {}


def main():
    st.set_page_config(page_title="JLPT Room Finder", page_icon="🤖")
    st.title("JLPT Room Finder")
    # st.markdown("1.Kindly enter the registered mobile number in the field below.")
    # st.markdown("2.Kindly refrain from submitting more than once.")
    with st.form("my_form"):
        level =  st.selectbox('Select JLPT Level',('N5', 'N4', 'N3','N2','N1'))
        number = st.number_input("Kindly enter the last 4 digits of your Registration Number", min_value=0, max_value=9999999999, key="index")
        # option = st.selectbox('Select the slot',('Breakfast', 'Lunch'))
        submitted = st.form_submit_button("Submit")
        
        if submitted:
            if  number == 0:
                st.write("Kindly Enter the Mobile Number")
            else:
                st.write("The Number entered is ",number)
                st.write("The Level Selected is", level)
                # st.write(d1[level][number])
                if number in d1[level].keys():
                    st.write("Name: ",d1[level][number]['Name'])
                    st.write("Level: ",d1[level][number]['level'])
                    st.write("Floor: ",d1[level][number]['Floor'])
                    st.write("Wing: ",d1[level][number]['Wing'])
                    st.write("Room Number: ",d1[level][number]['Room_Number'])
                else:
                    st.write("The number is not registered for the selected level.")
            # time = requests.get(url="http://worldtimeapi.org/api/timezone/Asia/Kolkata").json()['datetime']
            # data= fetch(number)

            # if data == -1:
            #     st.image('https://cdn.jsdelivr.net/gh/aravindsudarshan90/CDN/Verifie_Double.PNG', caption=f"Status: Token Already Verified")
            # elif data:
            #     myquery = {'phone_num':str(number)}
            #     newvalues = {"$set":{'morn_verified':'1','morn_time':time}}
            #     st.write("Name: " + str(data[0]['name']))
            #     JLPT.update_one(myquery, newvalues)
            #     st.image('https://cdn.jsdelivr.net/gh/aravindsudarshan90/CDN/Verified.PNG', caption=f"Status: Verified")
            #     st.write("You are verified. Please proceed to the food counter")
            # else:
            #      st.image('https://cdn.jsdelivr.net/gh/aravindsudarshan90/CDN/nverified.PNG', caption=f"Status: Not Verified")
            #      st.write("Kindly Check and Re-enter the phone number. If issue persists, kindly contact the venue incharge")

if __name__ == '__main__':
    main()