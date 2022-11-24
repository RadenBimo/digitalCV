from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"
whatsapp_pic= current_dir / "assets" / "Whatsapp.png"
gmail=current_dir / "assets" / "gmail.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | R. Bimo"
PAGE_ICON = ":wave:"
NAME = "R.Bimo Mandala Putra"
DESCRIPTION = """
Entry-level data scientist capable using predictive modeling, data processing, data visualization, and data mining algorithms to solve challenging business problems.
Have knowledge and experience in deep learning such as NLP, image classification, and time-series forecasting. 
Able collect internal or external data using scraping technique, SQL and ETL process. 
Able work in team, responsible and fast learner person who passionate about solving problems.
"""
EMAIL = "rbimomandalaputra@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/radenbimo/",
    "GitHub": "https://github.com/RadenBimo",
}
SOCIAL_MEDIA_PATH ={
    "LinkedIn" : current_dir / "assets" / "Link.png",
    "GitHub": current_dir / "assets" / "Git.png"
}    
PROJECTS = {
    "🏆 Bank Customers Credit Card Approval ": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    #st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    
st.write(DESCRIPTION)

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns([2,2,2,3])
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    with cols[index]:
        pic = Image.open(SOCIAL_MEDIA_PATH[platform])
        st.image(pic, width=50)
        st.write(f"[{platform}]({link})",align_text='center')
with cols[2]:
        pic = Image.open(whatsapp_pic)
        st.image(pic, width=50)
        st.write('+6281234503388')
with cols[3]:
    pic = Image.open(gmail)
    st.image(pic, width=50)
    st.write(EMAIL)

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ Have Knowledge of application of data analysis, machine learning, data mining, and statistical analysis.
- ✔️ Strong hands on experience and knowledge in Python, Excel and, SQL. 
- ✔️ Knowledgeable in ML Framework such as Tensorflow and Sklearn.
- ✔️ Capable collect internal or external data using scraping technique, SQL and ETL process.
- ✔️ Able work in team, responsible and fast learner person who passionate about solving problems
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python, SQL
- 🕵️‍♂️ Scrapping: Beautiful Soup, Selenium, Requests
- 📊 Data Visulization: Tableau, MS Excel, Plotly, Matplotlib
- 📚 Machine Learning: ScikitLearn, Hyperopt
- ✨ Deep Learning: TensorFlow, Keras
- 🗄️ Databases: MySQL, DBeaver
- 💻 ETL tools: Talend
"""
)

# --- Education ---
st.subheader("Education")
st.write('___')

#-- Education 1
st.write("**Dibimbing.id** ( 02/2022 - 07/2022 )")
st.text("Data Science Bootcamp | score: 86.24/100.00 ")


#-- Education 2
st.write('**Universitas Pembangunan Nasional "V" Yogyakarta** ( 09/2015 - 02/2021 )')
st.text("Bachelor Degree of Chemical Enginering | GPA: 3.29/4.00 ")

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Staff Production and Quality at POPA div | PT. Honda Prospect Motor**")
st.write("08/2021 - 01/2022")
st.write(
    """
-	Managed and Supervised production team of total ±120 manpower with 5 Leader and, 1 Foremen.
-	Controlled production in order to meet daily targets and quality in accordance with company standards.
-	Made monthly report Production and Quality of POPA.
-	Made production planning at POPA, consist: raw material import & local part, quantity and model to process, delivery planning and, planning simulation, which produce 410 parts each shift.
"""
)

# --- JOB 2
st.write("🚧", "**Process Engineer, Student Intern | PT. Pupuk Kujang Cikampek**")
st.write("09/2021 - 10/2022")
st.write(
    """
-	Learned to ensure plant runs well with most efficient and keep the NPK fertilizer quality always in good shape particularly in forming granular at NPK-01.
-	Make report which include indicating problem and reasons, then way to find the solutions.
"""
)

# --- JOB 3
st.write("🚧", "**Surveyor| PT. losta institute**")
st.write("02/2019")
st.write(
    """
-	Conducted interviews with respondents in Solo, at locations that had been determined. Used the survey method provided by the Losta Institute.
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")

# --- Project 1
st.write("🏆", "[**Bank Customers Credit Card Approval**](https://github.com/RadenBimo/Bank-Customers-Credit-Card-Approval-XGB-CatBoost-GridcvHyperparametertune)")
st.write("Pandas, ScikitLearn, Seaborn, NumPy")
st.write(
    """
-	Scraping project to get data from mamikos.com, an HTML website with some Java script code.
-	Data gained from the project consists of price, location, specification, rules, etc.
"""
)

# --- Project 2
st.write("🏆", "[**Scraping Mamikos.com**](https://github.com/RadenBimo/Scraping_Mamikos.comScrape)")
st.write("Pandas, Beautifulsoup, Selenium")
st.write(
    """
-	Scraping project to get data from mamikos.com, an HTML website with some Java script code.
-	Data gained from the project consists of price, location, specification, rules, etc.
"""
)

# --- Project 3
st.write("🏆", "[**Animals Classification**](https://github.com/RadenBimo/DL-IMGClassification-TransferLearning-AnimalsDataset)")
st.write("TensorFlow, Keras, Pandas, NumPy, Matplotlib")
st.write(
    """
-	Deep Learning Image classification project to identify image contain various animals.
-	The models using CNN with Transfer Learning technique using VGG-16 as base model. 
-	The model has 98% accuracy on test data.
"""
)

# --- Project 4
st.write("🏆", "[**Kimia Farma ETL & SQL**](https://github.com/RadenBimo/ETL-SQL-kimiafarma)")
st.write("Talend, MYSQL, Tableau")
st.write(
    """
-	Designed snowflake schema into local MYSQL database using TALEND as ETL process tools.
-	Designed star schema into local MYSQL database using SQL.
-	Dashboard visualization with Tableau data visualization tools.
"""
)

# --- Project 5
st.write("🏆", "[**Unilever Stock Forecasting**](https://github.com/RadenBimo/DL_TimeSeries_UnileverStockPricePrediction_CNN)")
st.write("Pandas, NumPy, yfinance, Plotly")
st.write(
    """
-	The data set are realtime Unilever stock price downloaded using yfinance package.
-	The prediction is based on data 60 days before the prediction date.
-	The model used LSTM layer.
-	The model has MAE score of 0.457, indicating that it deviates by only 0.79%.
"""
)

# --- Project 5
st.write("🏆", "[**Classification Spotify Review**](https://github.com/RadenBimo/NLP-Spotify-Review-Classify)")
st.write("TensorFlow, nltk, Pandas, NumPy, Plotly")
st.write(
    """
-	The data set obtained from Kaggle used for classification deeplearning NLP project.
-	The model used LSTM and Embedding layer.
-	The model has accuracy with 0.86% score both from test and validations set.
"""
)

st.write("More project at my","[github](https://github.com/RadenBimo)")


