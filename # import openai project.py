import openai

API_KEY = "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"
openai.api_key = API_KEY

def generate_response(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=50
        )
        generated_text = response.choices[0].text
        return generated_text
    except Exception as e:
        print(f"Error in request: {e}")
        return None

def main():
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        generated_response = generate_response(user_input)
        if generated_response:
            print("ChatGPT:", generated_response)

if __name__ == "__main__":
    main()