import json
from datetime import datetime
from doc_reader import *
import ollama

class CoverLetter_Ollama():
    def __init__(self, model = "mistral"):
        self.__parser_prompt_json = "./json_prompt/parser_prompt.json"
        self.load_config(self.__parser_prompt_json, model)

    def load_json(self, api_json_file):
        with open(api_json_file, 'r') as json_file:
            return json.load(json_file)

    def load_config(self, __parser_prompt_json, model):
        self.model = model
        self.resume_api_content = self.load_json(__parser_prompt_json)

    def add_to_prompt(self):
        self.resume_api_content['messages'][0]['content'] += '\n Resume:' + self.resume + '\n Date(Month day, year):' + self.curr_date + '\n Company Name:' + self.company_name + '\n Company Description:' + self.company_description + '\n Job Position:' + self.job_position + '\n Job Description:' + self.job_description

    def query_ollama(self, prompt):
        response = ollama.chat(model=self.model,
                               messages=[
                                   {'role': 'user', 'content': prompt}
                                   ]
                                )
        return response['message']['content']
    
    def read_input(self, resume_file_path, job_description, company_name, job_position, company_description):
        self.resume_file_path = resume_file_path
        self.resume = read_document(self.resume_file_path)
        # print("Extracted Resume:", self.resume)
        print("Resume Extracted, Processing...")
        self.company_name = company_name
        self.job_position = job_position
        self.job_description = job_description
        self.company_description = company_description
        self.curr_date = datetime.today().strftime("%B %d, %Y")
        self.add_to_prompt()

    def generate_cover_letter(self):
        prompt = self.resume_api_content['messages'][0]['content']
        query_response = self.query_ollama(prompt)
        # print("Ollama response:", query_response)
        print("Finished!")
        return query_response