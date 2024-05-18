import openai

openai.api_key = "sk-proj-Fdtx4LwJpXlcFzdQWKWOT3BlbkFJLdpeyVJQX10wIPiaIwBN"

def chat_with_gpt(prompt)
    responce = openai.ChatCompletion.create(
        model=gpt-3.5-turbo
        messages=[{"role": "user", "content": prompt}]
    )

    return responce.choices[0].message.content.strip()

if __name__ == "_main_":
    while True:
        if user_input.lower()in["quit", "exit", "bye"]:
            break

            responce = chat_with_gpt(user_input)
            print("chatbot: ", response)

            
