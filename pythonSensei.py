import ollama
# pip install ollama
# if its not installed

# Ensure the model is pulled if not already
try:
    ollama.pull('tulu3:latest')
except Exception as e:
    print(f"Model tulu3:latest might already be installed or an error occurred: {e}")

# A simple starting code snippet or context for the AI to work on
initial_code = """
def greet(name):
    return f"Hello, {name}!"
"""

messages = [
    {"role": "system", "content": "You are a helpful coding assistant specialized in improving Python code."},
    {"role": "user", "content": f"Here is some code: {initial_code}. Keep improving this code and add more important features to it. Think step by step."}
]

while True:
    try:
        # Get response from Ollama
        response = ollama.chat(model='tulu3:latest', messages=messages)
        
        # Print the AI's response
        print(response['message']['content'])
        
        # Append the AI's response to the conversation history
        messages.append({"role": "assistant", "content": response['message']['content']})
        
        # Continue the conversation by asking for further improvements
        messages.append({"role": "user", "content": "Keep improving the code and add more important features to it. Think step by step."})

        # You might want to add some delay here or a condition to stop the loop
        # For example, you can break the loop if the user presses a key or after a certain number of iterations
        input("Press Enter to continue, or Ctrl+C to quit...")

    except KeyboardInterrupt:
        print("\nStopping the chat...")
        break
    except Exception as e:
        print(f"An error occurred: {e}")
        break

print("Chat session ended.")
