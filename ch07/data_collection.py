
# _*_ coding:utf-8 _*_
import streamlit as st
import requests
import pandas as pd
from dotenv import load_dotenv
import os

#.env파일이 활성화됨
load_dotenv()

SERVICE_KEY =os.getenv('SEOUL_API_KEY')


data = None

for j in range(1,3):
    url = f'http://openapi.seoul.go.kr:8088/{SERVICE_KEY}/json/tbLnOpendataRtmsV/{1+((j-1)*1000)}/{j*1000}'
    # url = f'http://openapi.seoul.go.kr:8088/{service_key}/json/tbLnOpendataRentV/1/1000/2023/11560'
    print(url)
    
    #하나의 URL을 Json으로 받아 데이터 프레임으로 만듦
    req = requests.get(url)
    content = req.json()
    con = content['tbLnOpendataRtmsV']['row']
    result = pd.DataFrame(con)
    
    data = pd.concat([data, result])
    
data = data.reset_index(drop=True)
data.head()

data.to_csv('./seoul.csv',index =False)