import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

def main():
    st.title("안녕하세요!")
    st.header("This is Header")
    st.subheader("파이썬 문법을 사용 할 수 있어요!!!")
    st.write("-" * 50) #print와 유사
    a = 1
    b = 2
    st.write(a+b)
    st.write("-" * 50) 

    st.write(1234)
    st.write(pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40],
    })) # 사전의 형식으로 들어감


    data_frame = pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40],
    })
    st.write('Below is a DataFrame:', data_frame, 'Above is a dataframe.')

#차트객체 허용 
    df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])

    c = alt.Chart(df).mark_circle().encode(
        x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
        #컬러 c는 c값에따라 색상이 지정, 툴팁은 마우스를 가져다 놓을때 보게될 값들을 입력
    
    st.write(df)
    st.write(c)

    st.write("-" * 50) 
    '''
    # 마크다운 문법이 사용가능하게 진행
    ## 소제목 
    ### 마크다운 사용
    - 항목1
    - 항목2
    '''

if __name__ == "__main__":
    main()