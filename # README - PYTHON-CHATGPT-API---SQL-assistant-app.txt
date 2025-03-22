CHATGPT CONVERSATION

***********

You said:
create a PYTHON code with a CHATGPT API that transforms a text to a SQL command
ChatGPT said:
Here's a Python script that uses OpenAI's ChatGPT API to transform a natural language text into an SQL command. You need to replace "your-api-key-here" with your actual OpenAI API key.


Answer in chat instead
This script takes a natural language input, sends it to ChatGPT, and retrieves an SQL query. Let me know if you need modifications! 🚀


***********

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




