import requests
from bs4 import BeautifulSoup
import openai, os

openai.organisation = os.environ['openai_organization_id']
openai.api_key = os.environ['openai_api_key']
#Model.list() returns information about all models available
openai.Model.list()


#the link we want to summarize
#url = "https://en.wikipedia.org/wiki/Alexandria_Ariana"
url = input("What wikipedia link do you want to have summarized: ")
print()

#below soup part identifies relevant content on the webpage and saves it in "text" variable
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")

#we know that by picking <p> from the page, we get the desired content
article = soup.find_all("p")

#and with below the overall text is of better quality
text = ""
for p in article:
    text += p.text

    
#openai part. text from above is sent to openai with a request to summarize. Neccessary identifications are above in beginning
#max_tokens can be updated, 200 seems to provide enough content
prompt = f"Summarize following text in 3 paragraphs or less: {text}"
response = openai.Completion.create(model="text-davinci-002", prompt=prompt, temperature=0, max_tokens=200)
    
print(response["choices"][0]["text"].strip())


#identifying references in wikipedia and listing those at the end
refs = soup.find_all("ol", {"class": "references"})
for ref in refs:
    print(ref.text.replace("^ ", ""))

