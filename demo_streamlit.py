import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io, os, sys, setuptools, tokenize

# Using menu
st.title("Trung Tâm Tin Học")
menu = ["Home", "Capstone Project"]
choice = st.sidebar.selectbox('Menu', menu)
if choice == 'Home':    
    st.subheader("[Trang chủ](https://csc.edu.vn)")  
elif choice == 'Capstone Project':    
    st.subheader("[Đồ án TN Data Science](https://csc.edu.vn/data-science-machine-learning/Data-Science-Capstone-Project-Hinh-thuc-2_225)")
    st.write("""### 3 chủ đề trong khóa học:
    - Topic 1: Regression & Time Series analysis
    - Topic 2: RFM & Clustering
    - Topic 3: Recommendation System
    - Prject Deployment
    - ...""")
