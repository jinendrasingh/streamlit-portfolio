import streamlit as st
import streamlit.components.v1 as components
from constant import *
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(page_title='Jinendra\'s portfolio' ,layout="wide",page_icon='👻')

st.caption("'Turning data into insights, one line of code at a time.'")

with st.sidebar:
    components.html(embed_component['linkedin'], height=275)

st.sidebar.caption("Wish to connect?")
st.sidebar.write("📧: jinendrasingh0007@gmail.com")
resume_pdf = open('MyResume.pdf', 'rb')
st.sidebar.download_button('Download Resume',resume_pdf, file_name='MyResume.pdf', mime='pdf')

st.subheader("Summary")
st.write(info['Brief'])

st.subheader('Skills & Tools ⚒️')
def skill_tab():
    rows, cols = len(info['skills'])//skill_col_size, skill_col_size
    skills = iter(info['skills'])
    if len(info['skills'])%skill_col_size!=0:
        rows+=1
    for x in range(rows):
        columns = st.columns(skill_col_size)
        for index_ in range(skill_col_size):
            try:
                columns[index_].button(next(skills))
            except:
                break

with st.spinner(text="Loading section"):
    skill_tab()

#st.subheader('Work Experience')

st.subheader('Education 📖')

fig = go.Figure(data=[go.Table(
    header=dict(values=list(info['edu'].columns),
                fill_color='white',
                align='left',height=65,font_size=20),
    cells=dict(values=info['edu'].transpose().values.tolist(),
               fill_color='white',
               align='left',height=40,font_size=15))])

fig.update_layout(width=750, height=400)
st.plotly_chart(fig)

st.subheader('Projects 👩🏻‍💻')
st.markdown('- **Flight Dashboard Creation using Python, SQL, and Streamlit** ')
st.write("""Developed a Flight Dashboard using Python, SQL, and Streamlit to visualize and analyze flight
data. Implemented two key features “City-to-City Flight Search” and “Airline Analysis and
Airport Traffic”.
Utilized Python for data manipulation, SQL for data storage, and Streamlit for interactive
web-based display. Demonstrated skills in data analysis, visualization, and user experience design.""")

st.markdown('- **NLP Analysis App using Python and Tkinter** ')
st.write("""Developed a Python-based NLP Analysis App with a Tkinter GUI. Employs Paralleldots API for
Sentiment, NER, and Emotion Analysis. Transforms complex NLP tasks into a user-friendly
interface, showcasing skills in Python, API integration, and UI design.
The technology stack includes:
Python for backend logic, API integration, and data manipulation.
Tkinter library for creating an intuitive and interactive graphical interface.""")

st.subheader("Work Experience")
st.markdown("- **Team-Lead @TELEPERFORMANCE** (Aug 2019- Fab 2021)")
st.write("Working as a team lead and managing a team of 15 professionals at Teleperformance, specializing in providing exceptional support to e-commerce website sellers. My role involves optimizing team performance, enhancing customer satisfaction, and driving operational efficiency. This experience has honed my leadership skills and deepened my understanding of the e-commerce industry.")

st.markdown("- **CCE @TaskUS** (Fab 2021-Till now)")
st.write("Currently employed as a Customer Care Executive at TaskUs, where I provide dedicated support to a prominent US-based e-commerce company.")

st.markdown("- ** Data Analyst Intern @The Spark Foundation, June 2023 - July 2023 ")
st.write("I completed a data science internship at The Spark Foundation, where I worked on supervised and unsupervised machine learning, conducted exploratory data analysis on various datasets, and implemented decision tree algorithms.")

st.subheader('Medium Blogs ✍️')
st.markdown("""- <a href={}> Statistics for Data Science </a>""".format(blogs['link1']), unsafe_allow_html=True)
st.markdown("""- <a href={}> Probability Distribution Function (PDF, PMF & CDF) </a>""".format(blogs['link2']), unsafe_allow_html=True)
st.markdown("""- <a href={}> Introduction of Machine Learning </a>""".format(blogs['link3']), unsafe_allow_html=True)
st.markdown("""- <a href={}> Gradient Descent From Scratch</a>""".format(blogs['link4']), unsafe_allow_html=True)
st.markdown("""- <a href={}> Database Fundamentals</a>""".format(blogs['link5']), unsafe_allow_html=True)
st.markdown("""<a href={}> Read more here </a>""".format(info['Medium']), unsafe_allow_html=True)

