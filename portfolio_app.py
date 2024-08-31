import streamlit as st
from PIL import Image

# Inject custom CSS for slanted gradient background, transparent header, content container, text color, progress bar color, and image caption color
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #87ab69, #75975e, #658354, #4b6043);
        background-image: url("https://www.ultraimagehub.com/wallpapers/tr:flp-false,gx-0.3,gy-0.2,q-75,rh-3264,rw-5824,th-1080,tw-1920/1273879709905850378.jpeg");
        background-size: cover;
    }

    [data-testid="stHeader"] {
        background-color: rgba(0,0,0,0);
    }

    [data-testid="stSidebar"] {
        background-image: url("https://i.pinimg.com/736x/a0/bb/61/a0bb61994d1be6895be1a887b16f1390.jpg");
        background-size: cover;
    }

    [data-testid="stAppViewBlockContainer"] {
        background-color: rgba(255, 255, 255, 0.8); /* White background with transparency */
        border-radius: 10px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        margin-top: 50px;
        margin-bottom: 50px;
        padding: 100px;
    }

    /* Custom font color for headers in main content */
    .stApp .stMarkdown h1, .stApp .stMarkdown h2, .stApp .stMarkdown h3 {
        color: #000000;  /* Black header text */
    }

    /* Custom font color for all text in main content */
    .stApp .stMarkdown, .stApp .stTextInput, .stApp .stTextArea, .stApp .stButton, .stApp .stImage, .stApp .stProgress {
        color: #4A4A4A;  /* Dark gray text */
    }

    /* Custom progress bar color */
    .st-at st-au st-aw st-av st-cc st-cd st-c6 st-ce st-cf {
        color: #b06500;  /* Custom progress bar color */
    }

    /* Custom caption color */
    [data-testid="stImageCaption"] {
        color: #000000;
        font-size: 18px; /* Optional: Change the font size */
    }

    [data-testid="stHeading"] {
        color: #000000;
    }

    </style>
    """, 
    unsafe_allow_html=True
)

# Header Section
st.title("Welcome to My Portfolio")
st.subheader("Denisse Claire G. Morales")

# Sidebar with Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About Me", "Portfolio", "Contact"])

# Home Page
if page == "Home":
    with st.container():
        st.header("Home")
        st.write("Welcome to my portfolio! Explore the sections to learn more about me and my work.")
        st.image("home_image.jpg", caption="This is me!", use_column_width=True)

# About Me Page
elif page == "About Me":
    with st.container():
        st.header("About Me")
        st.write("Hi, I'm Denisse Claire G. Morales, a 4th year BS Information Technology student of Cebu Institute of Technology-University (CIT-U). "
                 "I enjoy working on software projects and continuously learning new skills.")

        st.write("### My Skills")
        st.write("- **Programming Languages:** Python, JavaScript, Java")
        st.write("- **Web Development:** React.js, HTML, CSS")
        st.write("- **Databases:** MySQL")
        st.write("- **Tools & Technologies:** Git, Streamlit")

        # Progress bars to show skill levels
        st.write("### Skill Levels")
        st.write("Python")
        st.progress(75)  # Python
        st.write("JavaScript")
        st.progress(77)  # JavaScript
        st.write("Java")
        st.progress(77)  # Java
        st.write("React.js")
        st.progress(77)  # React.js

# Portfolio Page
elif page == "Portfolio":
    with st.container():
        st.header("Portfolio")
        st.write("Here are some of the projects I've worked on:")
        
        # Project 1
        st.write("### Project 1: MathMinds Software Project")
        st.write("A comprehensive application designed to enhance math learning for 3rd-grade students at CIT-U's elementary department. "
                 "Developed as a capstone project, it includes features such as lesson creation, quiz management, and user role administration.")
        st.image("project1_image.jpg", caption="MathMinds Software Project", use_column_width=True)


# Contact Page
elif page == "Contact":
    with st.container():
        st.header("Contact Me")
        st.write("Feel free to reach out to me through any of the following channels:")

        # Social media links
        st.write("### Connect with me:")
        st.write("[LinkedIn](https://www.linkedin.com/in/denisse-claire-morales-972055243/)")
        st.write("[GitHub](https://github.com/dedensyaaa)")
        st.write("[Facebook](https://www.facebook.com/dedensyaaa/)")

# Footer
st.write("---")
st.write("© 2024 Denisse Claire G. Morales. All rights reserved.")
