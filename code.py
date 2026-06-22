import os
from google import genai

key = os.getenv("API_KEY")
client = genai.Client(api_key=key)

chat = client.chats.create(model="gemini-2.5-flash")

if __name__ == "__main__":
    print("Chat with Gemini: \n")

    while True:
        message = input("You: ")
        if message.lower() in ("quit", "exit"):
            break

        response = chat.send_message(message)
        print("\nGemini:", response.text, "\n")