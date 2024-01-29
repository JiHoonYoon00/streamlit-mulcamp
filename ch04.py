# _*_ coding:utf-8 _*_
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import altair as alt
import matplotlib.pyplot as plt
import matplotlib as mpl
import plotly.graph_objects as go 
import plotly.express as px 
from plotly.subplots import make_subplots 
import plotly

@st.cache_data
def load_data():
    df = sns.load_dataset('tips')
    return df


def main():
    #st.write(mpl.__version__)
    st.title("Streamlit with Maplotlib")
    tips = load_data()
   
    st.write(tips)

    #st.pyplot(sns.barplot(x='tip', y='sex', data=tips))

   

    m_tips = tips.loc[tips['sex'] == 'Male', :]
    f_tips = tips.loc[tips['sex'] == 'Female', :]

    # 시각화 차트
    fig, ax = plt.subplots(ncols=2, figsize=(10, 6), sharex=True, sharey=True)
    ax[0].scatter(x = m_tips['total_bill'], y = m_tips['tip'])
    ax[0].set_title('Male')
    ax[1].scatter(x = f_tips['total_bill'], y = f_tips['tip'])
    ax[1].set_title('Female')

    st.pyplot(fig)

    # seaborn 진행
    fig, ax = plt.subplots(ncols=2, figsize=(10, 6), sharex=True, sharey=True)
    sns.scatterplot(data=m_tips, x = 'total_bill', y = 'tip', ax=ax[0])
    ax[0].set_title('Male')
    sns.scatterplot(data=f_tips, x = 'total_bill', y = 'tip', ax=ax[1])
    ax[0].set(xlabel=None, ylabel=None)
    ax[1].set_title('Female')
    ax[1].set(xlabel=None, ylabel=None)
    st.pyplot(fig)

    fig, ax = plt.subplots()
    sns.barplot(y='tip',x='sex',data=tips)
    st.pyplot(fig)

    #plotly 진행
    fig = make_subplots(rows = 1,
                        cols = 2,
                        subplot_titles=('Male', 'Female'),
                        shared_yaxes=True,
                        shared_xaxes=True,
                        x_title='Total Bill($)'
                        )
    fig.add_trace(go.Scatter(x = m_tips['total_bill'], y = m_tips['tip'], mode='markers'), row=1, col=1)
    fig.add_trace(go.Scatter(x = f_tips['total_bill'], y = f_tips['tip'], mode='markers'), row=1, col=2)
    fig.update_yaxes(title_text="Tip($)", row=1, col=1)
    fig.update_xaxes(range=[0, 60])
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)
if __name__ == "__main__":
    main()
