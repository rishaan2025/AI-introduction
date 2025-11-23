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
    else: 
        print("unknown intent",unknown())
