# import openai project
import openai

k = open("key.txt", "r")
openai.api_key = k.read().strip("\n")


messages = [ 
        {"role": "system", "content": "you are a software engineer, use words with some emojis"},
]
while True:
    message = input("user : ")
    if not (message == "thank you"):
        messages.append(
            {"role" : "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model = " gpt-3.5-turbo", messages=messages
        )
    else:
        break
    reply = chat.choices[0]