import openai

openai.api_key = "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"

messages = []
system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready!")
while input != "quit()":
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")