import google.generativeai as genai
import textwrap

genai.configure(api_key="AIzaSyC7rvtn-p84BiBAuK09fQwOAswVPjSnjCU")

model = genai.GenerativeModel("gemini-1.5-flash")

def chat_with_flash():
    print("I'm Here Hello There - \n")
    chat = model.start_chat()

    while True:
        user = input("You: ")
        if user.lower() == "exit":
            print("Goodbye!")
            break

        response = chat.send_message(user)
        print("Bobo:\n")
        
        # Print line-by-line preserving line breaks
        for line in response.text.splitlines():
            print(textwrap.fill(line, width=100, replace_whitespace=False))

chat_with_flash()
