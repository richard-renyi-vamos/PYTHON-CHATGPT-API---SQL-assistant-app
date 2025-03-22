import openai

def text_to_sql(prompt_text):
    openai.api_key = "your-api-key-here"  # Replace with your OpenAI API key
    
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",  # Specify the model
        messages=[
            {"role": "system", "content": "You are an AI assistant that converts natural language to SQL queries."},
            {"role": "user", "content": f"Convert the following text into an SQL command: {prompt_text}"}
        ]
    )
    
    return response["choices"][0]["message"]["content"].strip()

if __name__ == "__main__":
    user_input = input("Enter a natural language query: ")
    sql_command = text_to_sql(user_input)
    print("Generated SQL Command:")
    print(sql_command)
