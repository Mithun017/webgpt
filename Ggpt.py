import google.generativeai as genai

genai.configure(api_key="AIzaSyC7rvtn-p84BiBAuK09fQwOAswVPjSnjCU")

model = genai.GenerativeModel("gemini-1.5-flash")

def chat_with_flash():
    print("Chatbot (Gemini 1.5 Flash) - type 'exit' to stop\n")
    chat = model.start_chat()

    while True:
        user = input("You: ")
        if user.lower() == "exit":
            print("Goodbye!")
            break

        response = chat.send_message(user)
        print("Gemini:", response.text)

chat_with_flash()
