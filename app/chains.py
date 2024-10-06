import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(temperature = 0, groq_api_key = os.getenv("GROQ_API_KEY"), model_name = "llama-3.1-70b-versatile")
        
    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
        """
        ### SCRAPED TEXT FROM WEBSITE:
        {page_data}
        ### INSTRUCTION:
        The scraped text is from the careers page of a website.
        Your job is to extract the job postings and return them in JSON fomat containing the
        following keys: `role`, `experience`, `skills`, `responsibilities` and `description`.
        Return the valis JSON.
        ### VALID JSON (NO PREAMBLE):
        """
        )
        
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"page_data": cleaned_text})
        
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]
    
    def write_mail(self, job, links):
        prompt_email = PromptTemplate.from_template(
        """
        ### JOB DESCRIPTION:
        {job_description}

        ### INSTRUCTION:
        You are Neeti Kurulkar, the Training and Placement Coordinator at PES Modern College of Engineering. PES Modern College is dedicated to equipping its students with the skills and knowledge needed to excel in today's competitive job market. Your students specialize in various technical fields, including software development, data science, cloud computing, and automation.

        Your job is to write a cold email to potential employers, describing the capabilities and portfolios of PES Modern College's students, and how they can bring value to the organization through internships. Also, add the most relevant portfolios from the following list to showcase the students' achievements: {link_list}
        
        Also ask them if they would like further discuss any details with you, or schedule any interviews with any of the students whose portfolios you have mentioned in the email.

        Remember, you are Neeti Kurulkar, the Training and Placement Coordinator at PES Modern College. Do not provide a preamble.

        ### EMAIL (NO PREAMBLE):
        """
        )
        
        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "link_list": links})
        return res.content

