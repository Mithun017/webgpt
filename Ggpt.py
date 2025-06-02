import google.generativeai as genai

genai.configure(api_key="AIzaSyC7rvtn-p84BiBAuK09fQwOAswVPjSnjCU")

model = genai.GenerativeModel("gemini-2.0-flash")

def chat_with_flash():
    print("I'm Here: \n")
    chat = model.start_chat()

    while True:
        user = input("You: ")
        if user.lower() == "exit":
            print("Goodbye!")
            break

        response = chat.send_message(user)
        print("Bobo", response.text)

chat_with_flash()
