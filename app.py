import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key="API_KEY")

st.title("Code Converter")

# Custom CSS to control the width of the input sections
st.markdown("""
    <style>
    .stTextInput, .stTextArea, .stSelectbox {
        width: 100% !important;
        height
        color:#092347;
    }

    .st-emotion-cache-qgowjl e1nzilvr4 {
        color:blue;
    }


    .st-emotion-cache-h4xjwg ezrtsby2 {
        background-color: aqua;
    }

    .stApp{
        background-color: #ccc;
    }

    h1 {
        color:#092347;
    }

    p{
        color:#092347;
        font-weight: bold;
        text-transform: uppercase;
    }

    .st-an{
    background-color: #092347;
    
    }


    .stButton>button {
        background-color: white;
        color: green;
    }

    .stButton>button:hover {
        border-color: #092347;
    }

    #stMarkdownContainer p{
        color: white;
    }

    .st-ak {
        background-color: #092347;
    }


    </style>
""", unsafe_allow_html=True)

# Create two columns
col1, col2 = st.columns([2, 2])

with col1:
    current_code_language = st.selectbox(
        "Enter your Current Code Language:",
        ["Python", "JavaScript", "Java", "C++", "C#", "Ruby", "Go", "Swift", "Kotlin"]
    )
    
code = st.text_area("Enter your code:")

with col2:
    language = st.selectbox(
        "Enter your desired Code Language:",
        ["Python", "JavaScript", "Java", "C++", "C#", "Ruby", "Go", "Swift", "Kotlin"]
    )

if st.button("Convert"):
    if current_code_language == language:
        st.error("The current code language and the desired code language are the same. Please select different languages.")
        st.stop()
    elif not code:
        st.error("Please enter the code to be converted.")
        st.stop()
    else:
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = f"""convert {code} to this {language} from {current_code_language} , 
            Provide only the code, no explanations or comments unless absolutely necessary.
        Don't include any delimiters at the beginning and the ending of the code.
        if header files are required, please include them in the code.
        if imports are required, please include them in the code.
        include brackets and semicolons if necessary mandatory for all other languages.
            EXAMPLE : 

            CURRENT CODE LANGUAGE  = PYTHON
            Code : print('Hello')
            IF THE DESIRED LANGUAGE IS jAVASCRIPT 

            OUTPUT SHOULD BE JUST:

            console.log('hello');

            *** IT MUST NOT BE : 
            '''javascript
            console.log('hello');
            '''
            Don't put any delimiters in the beginning and at the ending of the code.
        """

        response = model.generate_content(prompt)
        st.code(response.text)