# Import python packages
import streamlit as st



st.title('HARSHAVARDHAN REDDY')
st.write('Welcome to my portfolio')




for i in range(4):
    st.write('\n')



st.markdown("<h3> About ME </h3>",unsafe_allow_html=True)

st.write('I\'m a data professional with expertise in data analytics, data engineering, and automation, skilled in Power BI, SQL Server, PostgreSQL, Snowflake, Streamlit, and Python. I have experience building dynamic dashboards, writing complex SQL queries, and developing OCR-based solutions for extracting structured data. My projects include an automated JioCoin mining workflow using Appium and Python, a Bike Brand Analysis dashboard with Power BI and web scraping, and a Criminal Crime Case database design using SQL. I specialize in transforming complex data into actionable insights while leveraging Snowflake and Streamlit for end-to-end data solutions.')















cnx = st.connection("snowflake")
session = cnx.session()
