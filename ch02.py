# _*_ coding:utf-8 _*_

import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import altair as alt

@st.cache_data #decorator,함수의 중급레벨 사용법
def load_data():
    #df = sns.load_dataset("iris")
    df = sns.load_dataset("tips")
    return df 

def main():
    st.write(st.__version__)
    st.write(sns.__version__)
    st.write(pd.__version__)

    tips = load_data()
    st.dataframe(tips, use_container_width = True)

    st.write("-" * 50)
    st.title("st.metric()")
    tip_max = tips['tip'].max() # 최대값
    tip_min = tips['tip'].min() # 최소값
    st.metric(label = "팁 최고금액", value = tip_max, delta = tip_max - tip_min)
    st.metric(label = "팁 최소금액", value = tip_min, delta = tip_min - tip_max)



    df = pd.DataFrame(np.random.randn(10, 20), columns=("col %d" % i for i in range(20)))
    st.dataframe(df.style.highlight_max(axis=0))





if __name__ == "__main__":
    main()
