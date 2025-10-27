from utils.read_write_files.read_write_file import read_file, write_file
from dotenv import load_dotenv
from retrivals.vectorstore.chromadb_ops import ChromaDB
from openai import OpenAI
import json
import os
import configs

_ = load_dotenv()
chromadb_obj = ChromaDB()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
os.environ["ANONYMIZED_TELEMETRY"] = "false"

client = OpenAI(api_key=OPENAI_API_KEY)


def get_prompt(prompt_template_path, prompt_dir = None, mapped_data = None):
    prompt_template = read_file(file_path= prompt_template_path, directory = prompt_dir)
    if mapped_data:
        try:
            return prompt_template.format_map(mapped_data)
        except Exception as e:
            raise
    return prompt_template

def retrieve_contexts(query, top_k = 5):
    results = chromadb_obj.retrive_documenets(query, top_k)
    return results


def answer_generation(top_k = configs.top_k):
    print("enter 'q' to exit")
    while True:
        query = input("Enter your query: ")
        if query.lower() == "q":
            break
        contexts = retrieve_contexts(query, top_k= configs.top_k)
        prompt_dir = configs.prompt_dir
        system_prompt = get_prompt(prompt_template_path="system.txt", prompt_dir= prompt_dir)
        user_prompt = get_prompt(prompt_template_path="user.txt", prompt_dir= prompt_dir, mapped_data = {"query": query, "contexts": contexts})
        response = client.responses.create(
                model= configs.openai_llm,
                input=[{
                        "role": "system",
                        "content": system_prompt
                    },
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "input_text",
                                "text": user_prompt,
                            }]
                    }
                ]
            )
        llm_out = response.output_text
        llm_out_dictinary = json.loads(llm_out)
        try:
            llm_out_dictinary["contexts"] = contexts
            print(f"{json.dumps(llm_out_dictinary, indent= 4)}")
        except Exception as e:
            print(f"Issue occured while generating answer")
            raise

if __name__ == "__main__":
    answer_generation()

