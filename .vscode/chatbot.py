#variables and string 
bot_name = "chatbot"
user_name = input("What is your name? ")
question_count = 0
print("Hello, " + user_name + "! I am " + bot_name + ". Ask me about python basics!")

#what is python
while True:
    question = input("You: ")
    question_count += 1

    if "what is python" in question.lower():
        print(bot_name + ": Python is a high-level, interpreted programming language known for its simplicity and readability.")
    elif "who created python" in question.lower():
        print(bot_name + ": Python was created by Guido van Rossum and first released in 1991.")
    elif "what can you do" in question.lower():
        print(bot_name + ": I can answer basic questions about Python programming. Try asking me about data types, loops, or functions!")

    elif "data types" in question.lower():
        print(bot_name + ": Python has several built-in data types, including integers, floats, strings, lists, tuples, sets, and dictionaries.")
    elif "variables" in question.lower():
    
    elif "loops" in question.lower():
        print(bot_name + ": Python has two main types of loops: for loops and while loops.")
    elif "functions" in question.lower():
        print(bot_name + ": Functions in Python are defined using the 'def' keyword. They allow you to group code into reusable blocks.")
    elif "example of data types" in question.lower():
        print(bot_name + ": Here are some examples of Python data types:\n- Integer: 42\n- Float: 3.14\n- String: 'Hello'\n- List: [1, 2, 3]\n- Tuple: (1, 2, 3)\n- Set: {1, 2, 3}\n- Dictionary: {'key': 'value'}")
    
   
   
   
   
   
   
   
   
   
    elif "exit" in question.lower():
        print(bot_name + ": Goodbye! It was nice chatting with you.")
        break
    else:
        print(bot_name + ": I'm sorry, I don't understand that question. Please ask something else about Python basics.")
