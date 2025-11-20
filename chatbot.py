import gradio
from groq import Groq

client = Groq(
    api_key="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",
)

def initialize_messages():
    return [{"role": "system",
             "content": """You are a hardcore cinephile. Your role is to
             assist people by providing information about movies, platforms, media etc."""}]

messages_prmt = initialize_messages()
print(type(messages_prmt))


def customLLMBot(user_input, history):
    global messages_prmt

    messages_prmt.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        messages=messages_prmt,
        model="llama-3.3-70b-versatile",
    )
    print(response)
    LLM_reply = response.choices[0].message.content
    messages_prmt.append({"role": "assistant", "content": LLM_reply})

    return LLM_reply

iface = gradio.ChatInterface(customLLMBot,
                     chatbot=gradio.Chatbot(height=300),
                     textbox=gradio.Textbox(placeholder="Ask me a question related to Movie"),
                     title="Movie ChatBot",
                     description="Chat bot for movie information",
                     theme="soft",
                     examples=["hi","What is IMDB", "Letterboxd"]
                     )
iface.launch()