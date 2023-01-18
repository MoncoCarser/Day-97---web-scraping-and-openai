import requests
from bs4 import BeautifulSoup
import openai, os

openai.organisation = os.environ['openai_organization_id']
openai.api_key = os.environ['openai_api_key']
#Model.list() returns information about all models available
openai.Model.list()

url = "https://en.wikipedia.org/wiki/Independence_of_Finland"

response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")
article = soup.find_all("p")

for text in article:
    task = text.text
    question = "When Finland became independent?"
    
    prompt = (f"In maximum three paragraphs. Answer {question} based on {task}")
    response = openai.Completion.create(model="text-davinci-002", prompt=prompt, temperature=0, max_tokens=50)
    print(response["choices"][0]["text"].strip())

#choose a wikipedia page
#use BS to extract relevant text form there
#request openai to summarize the text in max 3 paragraphs
#also print references at the end