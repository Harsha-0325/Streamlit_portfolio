# Import python packages
import streamlit as st
import base64


# background

# import streamlit as st
# import base64


# st.markdown(
#     f"""
#     <style>
#     .stApp {{
#         background-color:#032500 ;
#         background-size: cover;
#         background-repeat: no-repeat;
#         background-position: center;
#     }}
#     </style>
#     """,
#     unsafe_allow_html=True
# )

#image function
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# title
st.markdown(
    """
    <style>
        .ctitle {
            font-size: 50px;
            font-weight: bold;
        }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown("""<div class = 'ctitle' >HI</div>
            <div class = 'ctitle' >I'M HARSHAVARDHAN</div>""",unsafe_allow_html = True) 


st.write('Welcome to my portfolio')


# gap
for i in range(4):
    st.write('\n')


#about me 
st.markdown("<h2> About ME </h2>",unsafe_allow_html=True)

st.write('I\'m a data professional with expertise in data analytics, data engineering, and automation, skilled in Power BI, SQL Server, PostgreSQL, Snowflake, Streamlit, and Python. I have experience building dynamic dashboards, writing complex SQL queries, and developing OCR-based solutions for extracting structured data. My projects include an automated JioCoin mining workflow using Appium and Python, a Bike Brand Analysis dashboard with Power BI and web scraping, and a Criminal Crime Case database design using SQL. I specialize in transforming complex data into actionable insights while leveraging Snowflake and Streamlit for end-to-end data solutions.')


st.markdown("""
        <style>
        .five_year_old {
            margin-left: 43%;  /* Adjust the percentage to control left alignment */
            text-align: right;
            font-style: italic;
        }
        </style>""",unsafe_allow_html=True)



st.markdown("""<div class = 'five_year_old'>
            <p>for 5 year old:</p><p>"i love data and i like to play with it🧑‍💻"</p>
            </div>""",unsafe_allow_html=True)


for i in range(4):
    st.markdown('<br>',unsafe_allow_html=True)


# experience


st.markdown("<h2>Experience</h2>",unsafe_allow_html=True)

# st.markdown("""
# <style>
# .experience-container {
#     display: flex;
#     justify-content: left;
#     align-items: flex-start;
#     gap: 20px;
#     margin-top: 20px;
# }

# .experience-card {
#     background-color: #f4f4f9;
#     color: #333;
#     padding: 15px;
#     border-radius: 12px;
#     box-shadow: 0 4px 6px rgba(0,0,0,0.1);
#     width: 250px;
    
            
# }

# .company-name {
#     font-weight: bold;
#     color: #032500;
#     margin-bottom: 5px;
    
    
# }

# .role {
#     font-style: italic;
#     margin-bottom: 8px;
# }
# .skills {
#     background-color: #e8f5e9;
#         padding: 8px;
#         border-radius: 10px;
#         margin-top: 10px;
#         color: #032500;
#         font-weight: 500;
# }
# </style>
# """, unsafe_allow_html=True)

st.markdown("""
<div class="experience-container">
    <!-- Experience 1 -->
    <div class="experience-card_1">
        <p class="company-name_1">Broadridge</p>
        <p class="role">Role: Trainee</p>
        <p>Duration: Jan 2025 - Present</p>
        <p class  ='skills'>Skills: Power BI, SQL Server, PostgreSQL</p>
    </div>
    <div class="experience-card_2">
        <p class="company-name">SimplyFI Softtech</p>
        <p class="role">Role: Python Developer Intern</p>
        <p class = 'duration'>Duration: Sep 2024 - Dec2024</p>
        <p class = 'skills'>Skills: Python, OCR</p>
    </div>  
</div>
        

""", unsafe_allow_html=True)

st.markdown("""
<style>
.experience-container {
    display: flex;
    justify-content: left;
    align-items: flex-start;
    gap: 20px;
    margin-top: 20px;
}

.experience-card_1 {
    background-color: #00568f;
    color: #ede8e8;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    width: 340px;   /* Fixed box width */
    height: 220px;  /* Fixed box height */
    font-size: 18px !important; /* Ensure base font size applies */
    display: flex;
    flex-direction: column;
}
            
.experience-card_2 {
    background-color: #76ffa5;
    color: #26233b;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    width: 340px;   /* Fixed box width */
    height: 220px;  /* Fixed box height */
    font-size: 18px !important; /* Ensure base font size applies */
    display: flex;
    flex-direction: column;

}

.company-name {
    font-weight: bold;
    color: #032500;
    font-size: 20px !important; /* Forced larger font size for company name */
}
            
.company-name_1 {
    font-weight: bold;
    color: #ede8e8;
    font-size: 20px !important; /* Forced larger font size for company name */
}


.role {
    font-style: italic;
    font-size: 18px !important; /* Slightly larger for role */
}
            
</style>
""", unsafe_allow_html=True)

for i in range(2):
    st.markdown('<br>',unsafe_allow_html=True)

st.markdown("""<div class = 'five_year_old'>
            <p>for 5 year old:</p><p>"i did my first job, now doing second😁"</p>
            </div>""",unsafe_allow_html=True)





# ----------------------------------------------------------------------------------------------------------------------------------------------------------
#skills

for i in range(4):
    st.markdown('<br>',unsafe_allow_html=True)
st.markdown("<h2>My Skills</h2>",unsafe_allow_html=True)

# st.markdown("""

# <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">

# <style>

# .skills-container {
#     display: flex;
#     flex-wrap: wrap;
#     gap: 10px;
#     justify-content: left;
#     margin-top: 10px;
# }

# .skill-box{
   
#     color: #333;
#     padding: 8px;
#     border-radius: 8px;
#     box-shadow: 0 4px 6px rgba(0,0,0,0.1);
#     width: 200px; /* Adjust width as needed */
#     text-align: center;
#     margin-bottom: 10px;
#     font-size: 17px;
#     ffont-family: 'Inter', sans-serif;
# }

# .category-1 {
#     background-color: #b8d8f5; /* Light Blue */
#     }
    
# .category-2 {
#     background-color: #fdfd96; /* Light Yellow */
# }

# .category-3 {
#     background-color: #d4f1c5; /* Light Green */
# }
# </style>""",unsafe_allow_html=True)


# st.markdown("""
#         <div class="skills-container">
#             <!-- Category 1 -->
#             <div class="skill-box category-1">Python</div>
#             <div class="skill-box category-1">PostgreSQL</div>
#             <div class="skill-box category-1">R</div>
#             <div class="skill-box category-1">My SQL</div>
#             <div class="skill-box category-1">SQL Server</div> <!-- 5th item in a new row -->
#         </div>
#         <br>
#         <div class="skills-container">
#             <div class="skill-box category-2">Snowflake</div>
#             <div class="skill-box category-2">Streamlit</div>
#             <div class="skill-box category-2">MS-Word</div>
#             <div class="skill-box category-2">MS-Excel</div>
#             <div class="skill-box category-2">VS Code</div>
#             <div class="skill-box category-2">Power BI</div>
#         </div>
#         <br>
#         <div class="skills-container">
#             <div class="skill-box category-3">Data Analytics</div>
#             <div class="skill-box category-3">Web Scraping</div>
#             <div class="skill-box category-3">DBMS</div>
#             <div class="skill-box category-3">Machine Learning</div>
#         </div>
#         """,unsafe_allow_html=True)


for i in range(2):
    st.markdown('<br>',unsafe_allow_html=True)
st.image('https://raw.githubusercontent.com/Harsha-0325/Streamlit_portfolio/main/skills_2.png',  use_container_width=True)
# ----------------------------------------------------------------------------------------------------------------------------------------------------------
for i in range(4):
    st.markdown('<br>',unsafe_allow_html=True)
# projects
st.markdown("<h2>My Projects</h2>",unsafe_allow_html=True)

# jio coin
st.markdown("""
    <style>
        .project_1 {
            font-size: 20px;
            font-weight: bold;
            color: #80ccff;
            margin-bottom: 10px;
        }
        .project_1_info {
            background-color: ##0e1117;
            padding: 10px;
            border-left: 5px solid #80ccff;
            border-radius: 5px;
            font-size: 16px;
            color: #DDDDDD;
        }
        .s1{
            font-style:italic;
            color:#ffbf80}
    </style>
""", unsafe_allow_html=True)

# Project Title
st.markdown("<div class='project_1'>Automated Search Engine Workflow for JioCoin Mining</div>", unsafe_allow_html=True)

# Project Details
st.markdown("""
    <div class='project_1_info'>
    <div>To streamline web searches in the Jio browser, I developed an automation system using Appium and Python.  
    The project eliminated manual intervention by leveraging mobile automation techniques.</div>  
    <br>
    <div>• Configured <span class = 's1'>Appium</span> and <span class = 's1'>Android Studio</span> to automate mobile browser operations.</div>  
    <div>• Used ADB commands to identify the app package and launch activities.</div>  
    <div>• Created a <span class = 's1'>Python</span> script that runs dynamic search queries using NLTK.</div>  
    <div>• Implemented an optimized automation workflow, reducing manual effort.</div>  
    </div>
""", unsafe_allow_html=True)

for i in range(2):
    st.markdown('<br>',unsafe_allow_html=True)

st.markdown("<p>The workflow image👀</p>",unsafe_allow_html=True)   
# # Display Flowchart Image
st.image(r"C:\Users\GurralaH\OneDrive - Broadridge Financial Solutions, Inc\Desktop\my_files\pro1_flowchart.png",  use_container_width=True)

for i in range(2):
    st.markdown('<br>',unsafe_allow_html=True)

st.markdown("""<div class = 'five_year_old'>
            <p>for 5 year old:</p><p>"i connected my mobile with my laptop and controlled it😎"</p>
            </div>""",unsafe_allow_html=True)



for i in range(4):
    st.markdown('<br>',unsafe_allow_html=True)


# bike brank analysis.

st.markdown("""
    <style>
        .project_2 {
            font-size: 20px;
            font-weight: bold;
            color: #80ff80;
            margin-bottom: 10px;
        }
        .project_2_info {
            background-color: ##0e1117;
            padding: 10px;
            border-left: 5px solid #80ff80;
            border-radius: 5px;
            font-size: 16px;
            color: #DDDDDD;
        }
        .s2{
            font-style:italic;
            color:#ff80ff;
            }
        .s2_1{
            font-style:italic;
            color:#ffbf80;
            }
    </style>
""", unsafe_allow_html=True)

# Project Title
st.markdown("<div class='project_2'> Bike Brand Analysis</div>", unsafe_allow_html=True)

# Project Details
st.markdown("""
    <div class='project_2_info'>
    <div>Developed a comprehensive Bike Specs Analysis project by <span class = 's2_1'>scraping web data</span> and analyzing 200+ bike records.</div>  
    <br>
    <div>• Scraped bike data from online sources using <span class = 's2_1'>Python</span>. </div>  
    <div>• Extracted key attributes like brand, price, engine capacity, and mileage. </div>  
    <div>• Performed data analysis in Python and published findings on Kaggle. </div>  
    <div>• Built an interactive <span class = 's2_1'>Power BI</span> dashboard focusing on:  
        <span class = 's2'>Mileage vs. Price Analysis</span>, 
        <span class = 's2'>Brand-wise Comparisons</span></div>  
            
    <br>
    <div>Dataset: <a href="https://www.kaggle.com/datasets/harshared236/bikes-information-dataset/data" target="_blank">Bikes Information Dataset</a> </div>
    Dash Board: <a href="https://github.com/Harsha-0325/POWERBI-PROJECTS/blob/main/Bike%20Analysis/POWER%20BI%20Dashboards.pdf" target="_blank">Bike Analysis</a>  
    </div>
            
    </div>
""", unsafe_allow_html=True)

for i in range(2):
    st.markdown('<br>',unsafe_allow_html=True)

st.markdown("""<div class = 'five_year_old'>
            <p>for 5 year old:</p><p>"i pulled the data from website and showed it as graphs📊"</p>
            </div>""",unsafe_allow_html=True)


for i in range(4):
    st.markdown('<br>',unsafe_allow_html=True)
# powerbi analysis

st.markdown("""
    <style>
        .project_3 {
            font-size: 20px;
            font-weight: bold;
            color: #FF8A8A;
            margin-bottom: 10px;
        }
        .project_3_info {
            background-color: ##0e1117;
            padding: 10px;
            border-left: 5px solid #FF8A8A;
            border-radius: 5px;
            font-size: 16px;
            color: #DDDDDD;
        }
        .s3{
            font-style:italic;
            color:#ff80ff;
            }
        .s3_1{
            font-style:italic;
            color:#ffbf80;
            }
    </style>
""", unsafe_allow_html=True)

# Project Title
st.markdown("<div class='project_3'>Power BI Data Analysis</div>", unsafe_allow_html=True)

# Project Details
st.markdown("""
    <div class='project_3_info'>
    <div>Conducted in-depth exploratory data analysis (EDA) on 100,000+ hotel bookings to uncover customer behavior trends.  </div>  
    <br>
    <div>• Developed regression models in R to estimate housing prices & salaries. </div>  
    <div>• Analyzed streaming data from Netflix, Amazon Prime, and Disney+ Hotstar using Power BI dashboards.</div>  
    <div>• Designed and implemented three interactive dashboards to highlight:  
        <span class = 's2'>User behavior insights</span>, 
        <span class = 's2'>Market trends & predictions</span>,
        <span class = 's2'>Actionable business intelligence</span></div>   
            
    <br>
    Dash Boards: <a href="https://github.com/Harsha-0325/POWERBI-PROJECTS/tree/main" target="_blank">All dashboard links</a>  
    </div>
            
    </div>
""", unsafe_allow_html=True)

for i in range(2):
    st.markdown('<br>',unsafe_allow_html=True)

st.markdown("""<div class = 'five_year_old'>
            <p>for 5 year old:</p><p>"I did some dashboards👀"</p>
            </div>""",unsafe_allow_html=True)



for i in range(4):
    st.markdown('<br>',unsafe_allow_html=True)
# CCC

st.markdown("""
    <style>
        .project_4 {
            font-size: 20px;
            font-weight: bold;
            color: #ffff99;
            margin-bottom: 10px;
        }
        .project_4_info {
            background-color: ##0e1117;
            padding: 10px;
            border-left: 5px solid #ffff99;
            border-radius: 5px;
            font-size: 16px;
            color: #DDDDDD;
        }
        .s4{
            font-style:italic;
            color:#ff80ff;
            }
        .s4_1{
            font-style:italic;
            color:#ffbf80;
            }
    </style>
""", unsafe_allow_html=True)

# Project Title
st.markdown("<div class='project_4'>Criminal Crime Case Database Design </div>", unsafe_allow_html=True)

# Project Details
st.markdown("""
    <div class='project_4_info'>
    <div>Designed & developed a robust Criminal Crime Case (CCC) database, incorporating Entity-Relationship (ER) diagrams & <span class = 's4_1'>advanced SQL queries</span>.</div>  
    <br>
    <div>• Populated the database with simulated crime data, reflecting real-life scenarios in Andhra Pradesh.</div>  
    <div>• Optimized performance & integrity using database normalization techniques.</div>  
    <div>• Implemented indexing & query tuning for fast & efficient data retrieval.</div>   
            
    <br>
    Document: <a href="https://github.com/Harsha-0325/Criminal-Crime-Case" target="_blank">CCC</a>  
    </div>
            
    </div>
""", unsafe_allow_html=True)

for i in range(2):
    st.markdown('<br>',unsafe_allow_html=True)

st.markdown("""<div class = 'five_year_old'>
            <p>for 5 year old:</p><p>"i made my own sample database🛢️"</p>
            </div>""",unsafe_allow_html=True)



# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# education
for i in range(4):
    st.markdown('<br>',unsafe_allow_html=True)


st.markdown("<h2>Education</h2>",unsafe_allow_html=True)

st.markdown("""
<style>
        
.education-section {
    display: flex;
    justify-content: flex-start;  /* Align to the left */
     margin-right: 47%;
}
            
/* Outer Frame */
.frame-container {
    background-color: #8d893c; 
    padding: 20px;
    border-radius: 15px;
    width: 400px;
    margin: auto;
    text-align: left;
}

/* Inner White Box */
.education-box {
    background-color: #fff;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

/* Text Styling */
.education-name {
    font-weight: bold;
    font-size: 18px;
    color: black;
    margin-bottom: 8px;
}

.education-degree {
    font-size: 16px;
    font-style: italic;
    color: #D18800; /* Golden color */
    margin-bottom: 10px;
}

.info{
    color :#333;
}

.cgpa {
    font-weight: bold;
    color: black;
}
</style>
""", unsafe_allow_html=True)


st.markdown("""
<div class ="education-section">
    <div class="frame-container">
        <div class="education-box">
            <p class="education-name">SRM University AP</p>
            <p class = 'info'>B.Tech in CSE with a specialization in <span class="education-degree">Big Data Analytics</span></p>
            <p class="cgpa">CGPA: 8.81</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

# certifications
for i in range(4):
    st.markdown('<br>',unsafe_allow_html=True)

st.markdown("<h2>Licenses & Certifications</h2>",unsafe_allow_html=True)
st.markdown("<br>",unsafe_allow_html=True)

# snowflake
st.markdown("""
    <style>
        .certificate-box {
            display: flex;
            flex-direction: column; /* Stack logo and text vertically */
            align-items: center; /* Center align content */
            background-color: #ffffff;
            border: 2px solid ;
            border-radius: 15px;
            padding: 20px;
            width: 640px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        .certificate-box img {
            width: 170px; /* Adjust logo size */
            height: auto;
            margin-bottom: 10px;
            margin-right:67%;
        }
        .cer_details {
            display: flex;
            flex-direction: column; /* Keep entries stacked */
            width: 100%;
            padding: 0 15px; /* Adds spacing inside */
            box-sizing: border-box; /* Ensures padding doesn't overflow */
        }
        .cer_row {
            display: flex;
            justify-content: space-between; /* Pushes name left & link right */
            align-items: center;
            width: 100%;
            margin-bottom: 10px;
        }
        .cer_name {
            font-size: 18px;
            font-weight: bold;
            color: #000;
        }
        .link {
            font-size: 16px;
            font-weight: bold;
            text-decoration: none;
            color: #0056b3;
        }
        .link:hover {
            text-decoration: underline;
        }
    </style>
    
    <div class="certificate-box">
        <img src="https://upload.wikimedia.org/wikipedia/commons/f/ff/Snowflake_Logo.svg" alt="Snowflake Logo">
        <div class="cer_details">
            <br>
            <div class="cer_row">
                <span class="cer_name">Data Warehousing Workshop</span>
                <span><a class="link" href="https://achieve.snowflake.com/78d5f6a3-0a8e-4f07-b5c0-a7c3a921e419#acc.NML5wnOA" target="_blank">View Certificate</a></span>
            </div>
            <div class="cer_row">
                <span class="cer_name">Collaboration, Marketplace & Cost Estimation Workshop</span>
                <span><a class="link" href="https://achieve.snowflake.com/57ecb77b-827f-4b25-9d4a-5745bac5cc22#acc.dSq6P40h" target="_blank">View Certificate</a></span>
            </div>
            <div class="cer_row">
                <span class="cer_name">Data Application Builders Workshop</span>
                <span><a class="link" href="https://achieve.snowflake.com/a20549fd-51b2-443c-ae92-fede83af51c3#acc.ge1EwxNT" target="_blank">View Certificate</a></span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


for i in range(2):
    st.markdown('<br>',unsafe_allow_html=True)


# hackerrank

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Encode the local image (Make sure the image file is in the same directory or provide the full path)
image_base64_1 = get_base64_image("hackerranlogo.jpg")

# Render HTML with Base64-embedded image
st.markdown(f"""
    <style>
        .certificate-box_1 {{
            display: flex;
            flex-direction: column; /* Stack logo and text vertically */
            align-items: center; /* Center align content */
            background-color: #050f1b;
            border: 2px solid;
            border-radius: 15px;
            padding: 20px;
            width: 640px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            text-align: center;
        }}
        .certificate-box_1 img {{
            width: 180px; /* Adjust logo size */
            height: auto;
            margin-bottom: 10px;
            margin-right:70%;
        }}
        .cer_details_1 {{
            display: flex;
            flex-direction: column; /* Keep entries stacked */
            width: 100%;
            padding: 0 15px; /* Adds spacing inside */
            box-sizing: border-box; /* Ensures padding doesn't overflow */
        }}
        .cer_row_1 {{
            display: flex;
            justify-content: space-between; /* Pushes name left & link right */
            align-items: center;
            width: 100%;
            margin-bottom: 10px;
        }}
        .cer_name_1 {{
            font-size: 18px;
            font-weight: bold;
            color: #ffffff;
        }}
        .link_1 {{
            font-size: 16px;
            font-weight: bold;
            text-decoration: none;
            color: #2bc862;
        }}
        .link_1:hover {{
            text-decoration: underline;
        }}
    </style>
    
    <div class="certificate-box_1">
        <img src="data:image/jpg;base64,{image_base64_1}" alt="Hacker Rank logo" width="150px">
        <div class="cer_details_1">
            <br>
            <div class="cer_row_1">
                <span class="cer_name_1">SQL (Basic)</span>
                <span><a class="link_1" href="https://www.hackerrank.com/certificates/iframe/335e232cb55c" target="_blank">View Certificate</a></span>
            </div>
            <div class="cer_row_1">
                <span class="cer_name_1">SQL (Intermediate)</span>
                <span><a class="link_1" href="https://www.hackerrank.com/certificates/iframe/08584e09c320" target="_blank">View Certificate</a></span>
            </div>
            <div class="cer_row_1">
                <span class="cer_name_1">SQL (Advanced)</span>
                <span><a class="link_1" href="https://www.hackerrank.com/certificates/iframe/dc9b4e9ccb27" target="_blank">View Certificate</a></span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)



for i in range(2):
    st.markdown('<br>',unsafe_allow_html=True)



# coursera

image_base64_2 = get_base64_image("coursera logo.png")

# Render HTML with Base64-embedded image
st.markdown(f"""
    <style>
        .certificate-box_2 {{
            display: flex;
            flex-direction: column; /* Stack logo and text vertically */
            align-items: center; /* Center align content */
            background-color: #0056d2;
            border: 2px solid;
            border-radius: 15px;
            padding: 20px;
            width: 640px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            text-align: center;
        }}
        .certificate-box_2 img {{
            width: 170px; /* Adjust logo size */
            height: auto;
            margin-bottom: 10px;
            margin-right:71%;
        }}
        .cer_details_2 {{
            display: flex;
            flex-direction: column; /* Keep entries stacked */
            width: 100%;
            padding: 0 15px; /* Adds spacing inside */
            box-sizing: border-box; /* Ensures padding doesn't overflow */
        }}
        .cer_row_2 {{
            display: flex;
            justify-content: space-between; /* Pushes name left & link right */
            align-items: center;
            width: 100%;
            margin-bottom: 10px;
        }}
        .cer_name_2 {{
            font-size: 18px;
            font-weight: bold;
            color: #ffffff;
        }}
        .link_2 {{
            font-size: 16px;
            font-weight: bold;
            text-decoration: none;
            color: #333;
        }}
        .link_2:hover {{
            text-decoration: underline;
            color : #050f1b;
        }}
        .linkname {{
            color :#ffffff;
        }}
    </style>
    
    <div class="certificate-box_2">
        <img src="data:image/jpg;base64,{image_base64_2}" alt="Hacker Rank logo" width="150px">
        <div class="cer_details_2">
            <br>
            <div class="cer_row_2">
                <span class="cer_name_2">Google Data Analytics</span>
                <span><a class="link_2" href="https://github.com/Harsha-0325/CERTIFICATES/blob/main/google%20analytics.pdf" target="_blank"><span class = 'linkname'>View Certificate</span></a></span>
            </div>
            <div class="cer_row_2">
                <span class="cer_name_2">Excel Skills for Business: Essentials</span>
                <span><a class="link_2" href="https://github.com/Harsha-0325/CERTIFICATES/blob/main/EXCEL%20BASIS.pdf" target="_blank"><span class = 'linkname'>View Certificate</span></a></span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

for i in range(2):
    st.markdown('<br>',unsafe_allow_html=True)

st.markdown("""<div class = 'five_year_old'>
            <p>for 5 year old:</p><p>"i have done there many - REALLY !! I DID😁"</p>
            </div>""",unsafe_allow_html=True)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------


#contact box

for i in range(4):
    st.markdown('<br>',unsafe_allow_html=True)
st.markdown("""
    <style>
        .contact-box {
            background-color: #0e1117;
            border-radius: 15px;
            padding: 20px;
            width: 640px;
            text-align: center;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            color: #ffffff;
            font-size: 18px;
        }
        .contact-box a {
            color: #2bc862;
            text-decoration: none;
            font-weight: bold;
        }
        .contact-box a:hover {
            text-decoration: underline;
        }
    </style>

    <div class="contact-box">
        <p><strong>Contact Me</strong></p>
        <p>📧 Email: <a href="mailto:gurralaharshavardhanreddy363@gmail.com">gurralaharshavardhanreddy363@gmail.com</a></p>
        <p>🔗 LinkedIn: <a href="https://www.linkedin.com/in/harshavardhanreddy-gurrala/" target="_blank">Harshavardhan G</a></p>
    </div>
    """, unsafe_allow_html=True)




# ----------------------------------------------------------------------------------------------------------------------------------------------------------



#count

import os

# File to store visitor count
counter_file = "visits.txt"

# Initialize visitor count
if not os.path.exists(counter_file):
    with open(counter_file, "w") as f:
        f.write("0")

# Read current count
with open(counter_file, "r") as f:
    count = int(f.read())

# Use session state to track if the user has already been counted
if "visited" not in st.session_state:
    st.session_state["visited"] = True  # Mark user as visited
    count += 1  # Increase count only if it's a new session

    # Save updated count
    with open(counter_file, "w") as f:
        f.write(str(count))


