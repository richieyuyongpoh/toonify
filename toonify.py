import streamlit as st 
import requests
from io import StringIO  
from tempfile import NamedTemporaryFile
 
st.title('Demo: AI Cartoonizer - Toonifying your face. ')

st.sidebar.write("""
This is a python based web app for toonifying your image.
""")

st.sidebar.write ("For more info, please contact:")

st.sidebar.write("<a href='https://www.linkedin.com/in/yong-poh-yu/'>Dr. Yong Poh Yu </a>", unsafe_allow_html=True)

key = st.sidebar.radio(
    "Choose a key",   
    ('Public', 'Default','User-defined'),
    index = 0
    
)

st.sidebar.write("<font color='blue'>Note: It is subject to the availability of license usage.</font>", unsafe_allow_html=True)
st.sidebar.write("<font color='blue'>      Once the license usage has been exceeded, the program will stop executing automatically.</font>", unsafe_allow_html=True)

if key=="Public":
   chosen_key = public_key

elif key=="Default":
   chosen_key = default_key

else:
     user_key = st.sidebar.text_input('Insert Key', 'the-key-is-key')
     chosen_key = user_key


uploaded_file = st.sidebar.file_uploader(
  "Upload an Image",
  type=['png', 'jpg','tiff','jpeg']    )
 
temp_file = NamedTemporaryFile(delete=False)

if st.sidebar.button('RUN'):

    if uploaded_file:

        temp_file.write(uploaded_file.getvalue())

        r = requests.post(
            API_init,
            files={
                'image': open(temp_file.name, 'rb'),
            },
            headers={'api-key': chosen_key}     
        )
        

        if r.json().get('err'):
           st.write("<font color='red'>Warning: An error occurred. Please ensure you have inserted a clear facial image.</font>", unsafe_allow_html=True)
        
        if r.json().get('status'):
           st.write("<font color='red'>Warning: You have either inserted wrong key or exceeded the maximum allowable license usage.</font>", unsafe_allow_html=True)

        if r.json().get('output_url'):
            st.write('Toonified Image')
            st.image(r.json()['output_url'])
            st.write('')
            st.write('')
            st.write('Original Image')
            st.image(temp_file.name)

    else:
          st.sidebar.write("<font color='red'>Please upload an image.</font>", unsafe_allow_html=True)