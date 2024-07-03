import os 
# api_key = "AIzaSyB-eP3rZwdXSNfTY2JrVO6XdkpV45NDCfs"
# GOOGLE_API_KEY = os.environ['AIzaSyB-eP3rZwdXSNfTY2JrVO6XdkpV45NDCfs']

import google.generativeai as genai
genai.configure(api_key="AIzaSyB-eP3rZwdXSNfTY2JrVO6XdkpV45NDCfs")
model = genai.GenerativeModel('gemini-pro')



response = model.generate_content("Write me a poem")
print(response.text)