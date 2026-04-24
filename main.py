import json
import webbrowser
import wikipedia

try:
    with open("memory.json", "r") as file:
        data = json.load(file)
        name = data.get("name", "")
except:
    name = ""

while True:
    msg = input("You: ").lower().strip()

    if "hello" in msg or "hii" in msg:
        print("Bot: Hi!")
        
    elif "your name" in msg or "what is your name" in msg:
        print("Bot : My name is Hina")
        
    elif "my name is" in msg:
        name = msg.replace("my name is", "").strip()
        data = {"name": name}
    
        with open("memory.json", "w") as file : json.dump(data, file)
        print("Bot : Nice to meet you",name)
        
    elif "who am i" in msg:
        if name:
            print("Bot: You are", name)
        else:
            print("Bot: I don't know your name yet")   

    elif "time" in msg:
        import time
        print("bot : ",time.ctime())
        
    elif "how are you" in msg:
        print("Bot : I'm fine. Thanks for asking")
        
    elif "joke" in msg:
        print("Bot : Tune b tech liya ,and usme tune Cse liya yahi sbse bada joke hai tere liye.")
        
    elif "open youtube" in msg:
        webbrowser.open("https://www.youtube.com")
    
    elif "open google" in msg:
        webbrowser.open("https://www.google.com") 
        
    elif "search" in msg:
        query = msg.replace("search", "").strip()
        try:
            result = wikipedia.summary(query, sentences=2)
            print("Bot:", result)
        except:
            print("Bot: Sorry, I couldn't find anything")      
    
    elif "bye" in msg:
        print("Bot: Goodbye!")
        break
        
    elif "help" in msg:
        print("Bot: you can ask hello,name,time,bye")   

    else:
        print("Bot: I don't understand")
