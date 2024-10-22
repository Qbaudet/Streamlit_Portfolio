import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from streamlit_pages import exploration_page

st.set_page_config(page_title="Quentin Baudet's Dashboard", layout="wide", page_icon=":palm_tree:")


def show_experiences():
    st.write("")
    st.header("What I've done professionally so far 🗓️")
    st.write("")
    st.write("")

    timeline_data = [
        {
            "year": 2024,
            "title": "Humanitarian volunteering abroad for St. Vincent de Paul's charity",
            "description": "Went to Ireland to work as a volunteer in a charity shop:\n Managed the reception, sorting, and sale of the donations given by the Irish people. I got to use my engineering skills to put in place solutions to increase the efficiency of their processes and reduce waste.",
            "image": "./images/logo_SVP.png",
            "width": 150
        },
        {
            "year": 2023,
            "title": "Stock exchange summer auxiliary at Crédit Agricole Titres",
            "description": "Temporary member of the stock exchange team:\n Managed and kept updated critical Excel files for the service and handled operation rejection emails.",
            "image": "./images/logo_CA.svg",
            "width": 70
        },
        {
            "year": 2022,
            "title": "Sales intern at Boulanger",
            "description": "Assisted sales at the Opéra Paris shop of Boulanger:\n Directed and advised customers, provided information about the products, labeled, and maintained clean shelf visuals.",
            "image": "./images/logo_boulanger.png",
            "width": 120
        },
        {
            "year": 2021,
            "title": "Logistics and handling intern at O'CD",
            "description": "Assisted the manager with the logistic related to the stock of the company: Handled deliveries, received new merchandises, helped organise the stock and manage the inventory.",
            "image": "./images/logo_ocd.png",
            "width": 120
        },
        {
            "year": 2018,
            "title": "Internship at SNCF in the Data Team",
            "description": "Integrated for two weeks within the SNCF data team:\n Gained concrete insights on the way that SNCF handles its data, from the technical side to the decision-making.",
            "image": "./images/logo_sncf.png",
            "width": 80
        },
        {
            "year": 2017,
            "title": "Internship at Ubisoft",
            "description": "First contact with the professional world:\n Discovered the jobs related to video games, but also data which is where my passion comes from.",
            "image": "./images/logo_ubisoft.png",
            "width": 70
        },
    ]

    for milestone in timeline_data:
        with st.expander(f"**{milestone['year']} - *{milestone['title']}***"):
            st.markdown(milestone["description"])
            st.image(milestone['image'], width=milestone['width'])


def show_skills():
    st.write("")
    st.write("")
    st.header("A few of my qualities 💼")
    st.write("")
    st.write("")

    col1, col2 = st.columns(2)

    # Mask for the shape of the wordcloud
    brain_mask = np.array(Image.open("./images/brain_mask.png"))
    brain_mask = np.where(brain_mask == 0, 255, 0).astype(np.uint8)

    soft_skills = {
        "Rigorous": 80,
        "Detail-oriented": 65,
        "Team player": 55,
        "Warm": 50,
        "Responsible": 75,
        "Empathetic": 75,
        "Compromise": 50,
        "Collaboration": 50,
        "Problem-solver": 65,
        "Analytical thinker": 55,
        "Fast learner": 60,
        "Open-minded": 40,
        "Pedagogical": 65,
        "Patient": 60
    }

    # Creating the wordcloud of soft skills with the mask
    soft_wordcloud = WordCloud(
        colormap='Blues',
        max_font_size=100,
        min_font_size=10,
        mask=brain_mask,
        contour_color='white',
        contour_width=2
    ).generate_from_frequencies(soft_skills)

    hard_skills = {
        "Python": 80,
        "Machine Learning": 75,
        "Data Analysis": 65,
        "Deep Learning": 60,
        "NLP": 55,
        "SQL": 75,
        "Statistics": 65,
        "Data Visualization": 70,
        "Streamlit": 45,
        "Cloud Computing": 30,
        "Pandas": 60,
        "Scikit-Learn": 65,
        "GitHub": 55,
        "Web": 50,
        "Maths": 65
    }

    # Creating the wordcloud of hard skills with the mask
    hard_wordcloud = WordCloud(
        colormap='Blues',
        max_font_size=100,
        min_font_size=10,
        mask=brain_mask,
        contour_color='white',
        contour_width=2
    ).generate_from_frequencies(hard_skills)

    with col1:
        st.markdown('<h3 class="main-content">Soft skills 🤝</h3>', unsafe_allow_html=True)
        plt.imshow(soft_wordcloud)
        plt.axis("off")
        st.pyplot(plt)

    with col2:
        st.markdown('<h3 class="main-content">Hard skills 💻</h3>', unsafe_allow_html=True)
        plt.imshow(hard_wordcloud)
        plt.axis("off")
        st.pyplot(plt)


def show_projects():
    st.write("")
    st.write("")
    st.header("Some of the projects I worked on 🗂️")
    st.write("")
    st.write("")

    projects = [
        {"title": "Expl-AI",
         "description": "Expl-AI is an AI software that uses deep-learning to classify the category of patents based on their descriptions. This is a multi-label Bi-LSTM model, and the aim was to make the predictions understandable by the user by highlighting the words that influenced the decision.",
         "tools": "Python, Pandas, Sklearn, Tensorflow", "image": "./images/pj_explain.png"},
        {"title": "Kankei",
         "description": "Kankei is an application that aims to bring closer people with their most important relationships. The user dedicates the app to another user, and they can discuss, get AI propositions of activities to do together and other features like a shared photo gallery and games.",
         "tools": "Flutter, Figma, Android Studio, SQL", "image": "./images/pj_kankei.png"},
        {"title": "Real estate price predictor",
         "description": "This tool's aim is to predict the value of a real estate based on its characteristics like location, size and state. The tool uses a Random Forest model and the DVF dataset of French real estate values.",
         "tools": "Python, Jupyter Notebook, Pandas, Sklearn, Matplotlib", "image": "./images/pj_DVF.png"},
        {"title": "Traily",
         "description": "Traily is a website that allows you to find the closest trails to you based on a location you enter. It uses the Google places API and is a low-code website using Bubble.",
         "tools": "Bubble, Goodle Cloud Platform", "image": "./images/pj_traily.png"},
        {"title": "VaxCare",
         "description": "VaxCare is the prototype of a website which helps you keep on track with your medical needs. Things like recurrent appointments, vaccines and medication are easy to forget but VaxCare aims to track those for you and send reminders.",
         "tools": "Figma", "image": "./images/pj_vaxcare.png"},
        {"title": "Tipax",
         "description": "Tipax is a website which helps you keep track of your restaurant checks in the USA. You can calculate in advance your check including the taxes and tips. The website also keeps in memory the restaurants at which you ate and their associated checks so that the user can plan ahead.",
         "tools": "SQL, HTML/CSS/Javascript, express.js, node.js", "image": "./images/pj_tipax.png"},
        {"title": "Guidy",
         "description": "Guidy is the prototype of a website which helps you with your mental health by tracking your moods, giving advice and linking you with health professionals",
         "tools": "Figma", "image": "./images/pj_guidy.png"}
    ]

    for i, project in enumerate(projects):

        if i % 2 == 0:  # display the even projects with image on the left
            col1, col2 = st.columns([2, 5])
            with col1:
                st.image(project['image'], use_column_width=True)
            with col2:
                st.header(project['title'])
                st.write(project['description'])
                st.markdown(f"*{project['tools']}*")
        else:  # display the odd projects with image on the right
            col1, col2 = st.columns([5, 2])
            with col2:
                st.image(project['image'], use_column_width=True)

            with col1:
                st.header(project['title'])
                st.write(project['description'])
                st.markdown(f"*{project['tools']}*")
        st.write("")
        st.write("")


# Sidebar
with st.sidebar:
    placeholder_url = "https://www.linkedin.com/in/quentin-baudet/"

    st.title("Quentin Baudet's :blue[Dashboard] :sunglasses:")
    st.image("./images/Photo_CV.jpg", width=150)
    st.write("Hi ! I am a 21 years-old master's student at EFREI Paris majoring in Data & AI")

    st.header("Navigation")
    page = st.radio("Move to:", ["Profile", "High schools Added Value"])

    st.write("Feel free to contact me at:\nqtn.baudet@gmail.com")

    st.markdown(
        f"""
        <style>
        .linkedin-button {{
            display: inline-flex;
            align-items: center;
            background-color: #0077b5;
            color: white !important; 
            border: none;
            padding: 10px 20px;
            font-size: 16px;
            font-weight: bold;
            border-radius: 5px;
            cursor: pointer;
            text-decoration: none;
        }}
        .linkedin-button img {{
            margin-right: 10px;
        }}
        </style>
        <a href="{placeholder_url}" class="linkedin-button" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" width="20px" alt="LinkedIn Logo">
            My LinkedIn Profile
        </a>
        """, unsafe_allow_html=True
    )


# Page selection
if page == "Profile":

    # Main page:
    st.markdown('''<h1 class="main-content"> Hi, I'm <span style='color:#38b3fc;'>Quentin Baudet</span>! 👋</h1>''', unsafe_allow_html=True)
    st.write("")
    st.markdown("""
    I am currently pursuing a master's degree at <span style='color:#38b3fc; font-weight:bold;'>EFREI Paris</span>, specializing in the <span style='color:#38b3fc; font-weight:bold;'>Data & AI major</span>.  
    My passion for data started during my first internship at **Ubisoft**, where I was introduced to the role of a Data Scientist. Since then, I have been driven to apply my growing skills and knowledge to this field.
    
    Data science indeed combines two of my greatest childhood interests:
    - <span style='color:#38b3fc; font-weight:bold;'>Investigation</span>: The process of gathering evidence, uncovering patterns in data, and making critical decisions based on these insights. As a fan of scientific police TV shows, I was always drawn to investigations and I'm glad that working with data allows me to fulfill this need in a different way.
    - <span style='color:#38b3fc; font-weight:bold;'>Pedagogy</span>: The ability to clearly present findings to non-technical teams, ensuring that all necessary information is communicated effectively. This aspect resonates with my childhood dream of becoming a teacher and my love for helping friends overcome difficulties in school.
    
    I find these two parallels between my childhood aspirations and the world of data absolutely fascinating, and it only strengthens my conviction that I am truly meant for this field.
    """, unsafe_allow_html=True)

    # Section 1: Career Timeline
    show_experiences()

    # Section 2 : Word cloud of my skills (2 columns for hard and soft skills
    show_skills()

    # Section 3 : Projects
    show_projects()


# Navigation to the other page
if page == "High schools Added Value":
    exploration_page.show_data_exploration()

