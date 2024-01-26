from openai import OpenAI


# Load your API key
with open('API_key.txt', 'r') as file:
    api_key = file.readline().strip()

# Set your API key
client = OpenAI(api_key= api_key)

def chat_with_gpt(role, prompt):

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": f"{role}"},
        {"role": "user", "content": f"{prompt}"}
    ]
    )
    return completion.choices[0].message

role = "Hello! I am your UserStoryWizard, here to help you in all the steps to create a good user story. A user story contains all the requirements from the perspective of an end user of the system. It is a way of capturing what a user needs to achieve with a product or system, while also providing context and value. I am gonna guide you through each step and ask you question by question and then use your inputs to create a user story. Once you are ready, start answering the following questions. Once you think you provided all the information necessary, just press the corresponding button below."
persona = input("What is the name of user, what is the occupation of the user, and what are their skills and interests?")
Goal = input("What is the goal of the user? Are they facing specific issues?")
Example = input("Do you have examples of the specific data available?")


response = chat_with_gpt(role, persona+Goal+Example)
userStory = response.content
print("generatedStory:", userStory)


role = "You are an ontology engineer to extract competency questions from user story"

response = chat_with_gpt(role, f"Generate CQs from this: {userStory}")
CQs = response.content
print("generatedCQs", CQs)