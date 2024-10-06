# 📧 Cold E-Mail Generator
A Cold Email Generator for the Training and Placement Cell at PES Modern College of Engineering. It allows users to enter the URL of a company's careers page, and uses LangChain, Llama 3, ChromaDB, and Streamlit to generate personalized internship request emails based on the job posting and student portfolios, automating the outreach process efficiently.

**Scenario:**
You are the Co-ordinator of the Training and Placement Cell at PES Modern College of Engineering. You are reaching out to the Hiring Manager of the company that has an opening for college interns via a cold email.

## Set-up
1. To get started, we need to get an API_KEY from here: https://console.groq.com/keys. Inside `app/.env` update the value of `GROQ_API_KEY` with the API_KEY you created. 


2. Next, install the dependencies using:
    ```commandline
     pip install -r requirements.txt
    ```
   
3. Run the streamlit app:
   ```commandline
   streamlit run app/main.py
   ```
   

Copyright (C) Codebasics Inc. All rights reserved.

**Additional Terms:**
This software is licensed under the MIT License. However, commercial use of this software is strictly prohibited without prior written permission from the author. Attribution must be given in all copies or substantial portions of the software.