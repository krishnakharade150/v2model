# import os
# import pandas as pd
# import streamlit as st
# import matplotlib.pyplot as plt
# import seaborn as sns
# from dotenv import load_dotenv
# from langchain_groq.chat_models import ChatGroq
# from pandasai import SmartDataframe

# # Load environment variables
# load_dotenv()

# # Initialize the Groq client with your API key
# api_key = os.getenv('API_KEY')
# if api_key is None:
#     st.error("API Key not found. Please set your API key in the environment variables.")
# else:
#     llm = ChatGroq(model='llama3-70b-8192', api_key=os.environ['API_KEY'])

# # Streamlit app title
# st.title("Data Analysis Bot")

# # File uploader for CSV files
# uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

# # Process the uploaded file
# if uploaded_file is not None:
#     data = pd.read_csv(uploaded_file)
#     df = SmartDataframe(data, config={'llm': llm})
#     st.write(data.head(3))
    
#     prompt = st.text_area("Enter your prompt here:")
    
#     if st.button("Generate"):
#         if prompt:
#             with st.spinner("Generating response..."):
#                 try:
#                     response = df.chat(prompt)  # Adjust based on actual method to send a chat request
#                     st.write("Response from Llama model:")
#                     st.write(response)
                    
#                     # Assume you generate a heatmap and save it to a PNG
#                     file_path = "D:/12_GenAI/Chatbot_Lllama3_Groq/exports/charts/temp_chart.png"
#                     # Your visualization generation logic here
                    
#                     # Load and display the image
#                     if os.path.exists(file_path):
#                         st.image(file_path, caption='Visualization')
#                     else:
#                         st.error("Generated image not found.")
                    
#                 except Exception as e:
#                     st.error(f"An error occurred: {e}")
#         else:
#             st.warning("Please enter a prompt!")


#################################### 2 Approach #######################################

# import os
# import pandas as pd
# import streamlit as st
# import matplotlib.pyplot as plt
# import seaborn as sns
# from dotenv import load_dotenv
# from langchain_groq.chat_models import ChatGroq
# from pandasai import SmartDataframe

# # Load environment variables
# load_dotenv()

# # Initialize the Groq client with your API key
# api_key = os.getenv('API_KEY')
# if api_key is None:
#     st.error("API Key not found. Please set your API key in the environment variables.")
# else:
#     llm = ChatGroq(model='llama3-70b-8192', api_key=os.environ['API_KEY'])

# # Streamlit app title
# st.title("Data Analysis Bot")

# # File uploader for CSV files
# uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

# # Process the uploaded file
# if uploaded_file is not None:
#     data = pd.read_csv(uploaded_file)
#     df = SmartDataframe(data, config={'llm': llm})
#     st.write(data.head(3))
    
#     prompt = st.text_area("Enter your prompt here:")
    
#     if st.button("Generate"):
#         if prompt:
#             with st.spinner("Generating response..."):
#                 try:
#                     # Delete any existing heatmap images
#                     file_path = "D:/12_GenAI/Chatbot_Lllama3_Groq/exports/charts/temp_chart.png"
#                     if os.path.exists(file_path):
#                         os.remove(file_path)

#                     response = df.chat(prompt)  # Adjust based on actual method to send a chat request
#                     st.write("Response from Llama model:")
#                     st.write(response)
                    
#                     # Your visualization generation logic here
                    
#                     # Load and display the image
#                     if os.path.exists(file_path):
#                         st.image(file_path, caption='Visualization')
#                     else:
#                         st.error("Generated image not found.")
                    
#                 except Exception as e:
#                     st.error(f"An error occurred: {e}")
#         else:
#             st.warning("Please enter a prompt!")

############################## 3 Approach #####################################

import os
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from langchain_groq.chat_models import ChatGroq
from pandasai import SmartDataframe
import matplotlib.pyplot as plt
import seaborn as sns

# Load environment variables
load_dotenv()

# Initialize the Groq client with your API key
api_key = os.getenv('API_KEY')
if api_key is None:
    st.error("API Key not found. Please set your API key in the environment variables.")
else:
    llm = ChatGroq(model='llama3-70b-8192', api_key=os.environ['API_KEY'])

# Streamlit app title
st.title("InsightBOT: An Inhouse statistical tool")

# File uploader for CSV files
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

# Process the uploaded file
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    df = SmartDataframe(data, config={'llm': llm})
    st.write(data.head(3))
    
    prompt = st.text_area("Enter your prompt here:")
    
    if st.button("Generate"):
        if prompt:
            with st.spinner("Generating response..."):
                try:
                    # Delete any existing heatmap images
                    file_path = "D:/12_GenAI/Chatbot_Lllama3_Groq/exports/charts/temp_chart.png"
                    if os.path.exists(file_path):
                        os.remove(file_path)

                    response = df.chat(prompt)  # Adjust based on actual method to send a chat request
                    st.write("Response from Llama model:")
                    st.write(response)
                    
                    # Your visualization generation logic here
                    
                    # Check and display the image inline in Streamlit UI
                    if os.path.exists(file_path):
                        st.image(file_path, caption='Visualization')
                    else:
                        st.error("Generated image not found.")
                    
                except Exception as e:
                    st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter a prompt!")

