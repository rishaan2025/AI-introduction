print("Hello, I am Chatbot 2.0")
print("Type'bye' to exit" )
def unknown():
    return "I don't understand the language you are speaking"
def greet():
    return "Hello, how are you?"
def school():
    return "School is amazing"
def age():
    return "I'm a chatbot, so I always stay young"
def sports():
    return "Sports are good for health and exercise and very exciting"
def name():
    return "My name is Chatbot 2.0"
def bye():
    return "See you later"
def coding():
    return "Coding is for geniuses and makes life way easier"
def ai():
    return "AI is good for doing work for you but don't use it for school purposes"
def sun():
    return "The sun provides energy and light to Earth and life would not exist on Earth without it, sadly"
def writing():
    return "Writing is a common form of communication where people read and write, like now"
def math():
    return "Math is just a lot of patterns that help with arithmetics and mathematical problems, it is so cool and hard"
def language():
    return "Language is a way of writing, there is a way to write in english, spanish, and hindi"
def home():
    return "Home is a lovely place where you can do whatever you want, there is nothing like home"
def get_intent(user_input):
    text=user_input.lower()
    if "hello" in text or "hi" in text:
        return "greet"
    elif "name" in text:
        return "name"
    elif "bye" in text:
        return "bye"
    elif "school" in text:
        return "school"
    elif "age" in text or "years old" in text:
        return "age"
    elif "sports" in text or "baseball" in text:
        return "sports" 
    elif "coding" in text:
        return "coding"
    elif "ai" in text:
        return "ai"
    elif "home" in text:
        return "home"
    elif "math" in text:
        return "math"
    elif "sun" in text:
        return "sun"
    elif "writing" in text:
        return "writing"
    elif "language" in text:
        return "language"
    else:
        return "unknown"
while True:
    user = input("You: ")
    if user.lower() in ["bye", "exit", "quit"]:
        print("ChatBuddy: Bye!👋")
        break
    intent=get_intent(user)
    if intent == "greet":
        print("ChatBuddy: ", greet())
    elif intent=="name":
        print("ChatBuddy: ",name())
    elif intent=="age":
        print("ChatBuddy: ",age())
    elif intent=="sports":
        print("ChatBuddy: ",sports())
    elif intent=="school":
        print("ChatBuddy: ",school())
    elif intent=="ai":
        print("ChatBuddy: ",ai())
    elif intent=="coding":
        print("ChatBuddy: ",coding())
    elif intent=="home":
        print("ChatBuddy: ",home())
    elif intent=="math":
        print("ChatBuddy: ",math())
    elif intent=="writing":
        print("ChatBuddy:",writing())
    elif intent=="language":
        print("ChatBuddy:",language())
    elif intent=="sun":
        print("ChatBuddy:",sun())
    else: 
        print("unknown intent",unknown())
