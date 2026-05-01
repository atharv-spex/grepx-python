#chatbot created using python basics
#variables and string 
bot_name = "chatbot"
user_name = input("What is your name? ")
question_count = 0
print("Hello, " + user_name + "! I am " + bot_name + ". Ask me about python basics!")


#knowledge base--------
knowledge = {
    "what is python": "Python is a high-level, interpreted programming language known for its simplicity and readability.",
    "who created python": "Python was created by Guido van Rossum and first released in 1991.",
    "what can you do": "I can answer basic questions about Python programming. Try asking me about data types, loops, or functions!",
    "data types": "Python has several built-in data types, including integers, floats, strings, lists, tuples, sets, and dictionaries.",
    "variables": "In Python, you can create a variable by simply assigning a value to a name. For example: x = 10 or name = 'Alice'.",
    "strings": "Strings in Python are sequences of characters enclosed in quotes. You can use single quotes (' '), double quotes (\" \"), or triple quotes (''' ''' or \"\"\" \"\"\").",
    "lists": "Lists in Python are ordered collections of items that can be of different types. They are defined using square brackets, like this: my_list = [1, 'hello', 3.14].",
    "tuples": "Tuples in Python are ordered collections of items that can be of different types. They are defined using parentheses, like this: my_tuple = (1, 'hello', 3.14).",
    "sets": "Sets in Python are unordered collections of unique items. They are defined using curly braces, like this: my_set = {1, 2, 3}.",
    "dictionaries": "Dictionaries in Python are unordered collections of key-value pairs. They are defined using curly braces, like this: my_dict = {'key': 'value'}.",
    "loops": "Python has two main types of loops: for loops and while loops.",
    "functions": "Functions in Python are defined using the 'def' keyword. They allow you to group code into reusable blocks.",
    "example of data types": "Here are some examples of Python data types:\n- Integer: 42\n- Float: 3.14\n- String: 'Hello'\n- List: [1, 2, 3]\n- Tuple: (1, 2, 3)\n- Set: {1, 2, 3}\n- Dictionary: {'key': 'value'}"
}

#main chatbot loop
#loop used to keep the chatbot running until the user decides to exit.
#  It checks the user's input against the knowledge base and responds accordingly. If the user types "exit", the chatbot will say goodbye and end the conversation. If the user's question is not in the knowledge base, it will prompt them to ask something else about Python basics.
while True:#creates and infinite loop
    question = input("You: ").lower()  #.lower()  this prevents case sensitivity from blocking valid questions.
    question_count += 1   #increments the question count each time the user asks a question

    if question in knowledge:
        print(bot_name + ": " + knowledge[question])
    elif "exit" in question:
        print(bot_name + ": Goodbye! It was nice chatting with you.")
        break
    else:
        print(bot_name + ": I'm sorry, I don't understand that question. Please ask something else about Python basics.")
