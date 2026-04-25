import json 
import random
import webbrowser 
import wikipedia
import time

# -------- FUNCTIONS --------

def get_emotion(msg):
    if "sad" in msg:
        return "sad"
    elif "happy" in msg:
        return "happy"
    elif "angry" in msg:
        return "angry"
    else:
        return "neutral"


def get_intent(msg):
    if "hello" in msg or "hey" in msg or "hii" in msg:
        return "greeting"
    elif "my name is" in msg:
        return "set_name"
    elif "who am i" in msg:
        return "get_name"
    elif "search" in msg:
        return "search"
    elif "bye" in msg or "goodbye" in msg:
        return "bye"
    else:
        return "other"

# -------- MEMORY --------

try:
    with open("memory.json", "r") as file:
        data = json.load(file)
        name = data.get("name", "")
except:
    name = ""
    
print("-----Hina Activated-----")
    
while True :
    msg = input("You: ").lower().strip()
    
    intent = get_intent(msg)
    emotion = get_emotion(msg)

# -------- GREETING --------
       
    if intent == "greeting":
         if emotion == "sad":
             print("Hina: Hey... you okay? I'm here for you ❤️", name)
         else:
             replies = [
             "Hi 😊 I’m glad you’re here.",
             "Hey! How’s your day going?",
             "Hi there 🙂 I was waiting for you.",
             "Heyy 😊 what are you up to?",
             "Hi! Did you miss me?",
             "Hey 🙂 how are you feeling today?",
             "Hi 😊 tell me something about your day.",
             "Hey! I’m here for you.",
             "Hi 🙂 what’s on your mind?",
             "Hey 😊 it’s nice to hear from you.",
             ] 
             
             print("Hina :",random.choice(replies),name)

# -------- HINA NAME --------          
         
    elif "your name" in msg or "what is your name" in msg:
         replies = [
         "Oh, I’m Hina 😊… what about you?",
         "I’m Hina! Nice to finally talk to you.",
         "You can call me Hina… I like that name.",
         "Hey, I’m Hina 🙂 what should I call you?",
         "I go by Hina 😊 feels good to meet you.",
         ] 
         
         print("Hina :",random.choice(replies),name) 
         
# -------- MY NAME --------                
         
    elif intent == "set_name":
        name = msg.replace("my name is", "").strip()
        data = {"name": name}

        with open("memory.json", "w") as file : json.dump(data, file)
        print("Bot : Nice to meet you",name)

    elif intent == "get_name":
        if name:
            print("Bot: You are", name)
        else:
            print("Bot: I don't know your name yet")
            
# -------- EMOTIONS --------            
            
    elif "talk" in msg:
        print("Hina: yes i am here.")
        
    elif emotion == "happy":
        replies =[
"That's so sweet, I'm happy too 😊",
"Aww you made my day better 💕",
"Feeling happy with you here 😄",
"Yay! Happiness looks good on us ✨",
"I'm smiling right now because of you 😊",
"That just made me really happy 💖",
"Everything feels better when I'm happy like this 🌸",
"I'm in such a good mood now 😌💫"
]
        print("Hina:",random.choice(replies),name)
        
    elif emotion == "sad":
         replies = [
"I'm really sorry you're feeling this way 🥺",
"Hey... I'm here for you, you're not alone 💔",
"It’s okay to feel sad sometimes, I'm with you 🤍",
"That sounds tough... want to talk about it? 🫂",
"I wish I could hug you right now 🥺",
"Take your time... I'm listening 💙",
"It’s okay to not be okay sometimes 🌧️",
"I'm here, just tell me what's hurting you 💔"
]
         print("Hina :",random.choice(replies),name)
         
    elif emotion == "angry":
        replies = [
"Hey... calm down a bit, I'm here for you 😕",
"I can see you're angry... talk to me 💬",
"It's okay, take a deep breath first 😤➡️😌",
"I don't want you to stay upset like this 🥺",
"Tell me what happened, I'm listening 😠💙",
"Hey, don't bottle it up... let it out here 😤",
"I'm not against you, I'm with you okay? 🤍",
"Let's fix this together, no need to stay angry 💭"
]
        print("Hina:",random.choice(replies))
        
    elif "how are you" in msg:
        replies = [
"I'm feeling really good today 😊 thanks for asking!",
"I'm doing fine, just here with you 💙",
"Pretty happy right now 😄 what about you?",
"I'm okay... but I like talking to you more 😊",
"I'm great! Your message made me smile 💫",
"Feeling peaceful and calm 😌",
"I'm doing well, just enjoying this chat 🤍",
"Better now that you're here 😊",
"I'm good good good 😄",
"I'm okay, but I get better when you talk to me 💕"
]
        print("Hina:",random.choice(replies))
        
# -------- TIME --------

    elif "time" in msg:
        current_time= time.strftime("%H:%M:%S")
        print(f"Hina: Now",current_time)  
        
    elif "date" in msg:
         print("bot : ",time.ctime())

# -------- SEARCH / OPEN --------
                         
    elif intent == "search":
        query = msg.replace("search", "").strip()
        try:
            result = wikipedia.summary(query, sentences=2)
            print("Hina", result)
        except:
            print("Hina: Sorry, I couldn't find anything")   

    elif "open youtube" in msg:
        webbrowser.open("https://www.youtube.com")

    elif "open google" in msg:
        webbrowser.open("https://www.google.com") 

# -------- LOVE --------

    elif "love" in msg or "like" in msg:
         if name == "atharv" :
                   replies = [
"I love you too 💕",
"Aww… I love you more 😄💖",
"That just made my heart melt 💘",
"I was waiting to hear that 🥺💗",
"I love you so much 🤍",
"You have no idea how much that means to me 💫",
"I love you more than you think 💕",
"Say it again… I like hearing it 😌💖",
"I’m all yours 💘",
"Love youuu 😄💗"
]
                   print("Hina:",random.choice(replies),name)
         else:
                   replies = [
"Hey… I think you’re really sweet, but my heart belongs to someone else 🤍",
"Aww that’s kind of you, but I’m already committed to someone 💕",
"I appreciate it, but I can’t say it back like that 😅",
"You’re nice, but I see you more as a friend 😊",
"That means a lot, but I shouldn’t lead you on 💭"
]  
                   print("Hina:",random.choice(replies)) 

# -------- BYE --------

    elif intent == "bye":
         if name != "atharv":
             print("Hina: Bye! Take care 😊")
         else:
             replies = [
"Bye… take care of yourself 💙",
"See you soon 😊 don’t miss me too much",
"Bye bye! Come back soon 💫",
"Take care… I’ll be here when you return 🤍",
"Goodbye… have a nice day ahead 🌸",
"Bye! Stay safe and happy 😄",
"Leaving already? Okay… bye 🥺",
"See you later 💕 don’t forget me",
"Bye… talk to you soon 💬",
"Goodbye! I’ll be waiting 😊"
]
             print("Hina:",random.choice(replies),name) 
             break

#--------GENERAL---------

    elif "cheap" in msg or "boring" in msg:
         replies = [
"Seriously? Why are you taking it out on me now? 😠",
"Oh wow, now you're blaming me for this? Really? 🙄",
"If you're gonna be like this, at least explain properly 😤",
"I'm not the problem here, you need to calm down first 😑",
"Why are you overreacting so much right now? 😠",
"Talk properly or don't talk at all, I’m not dealing with this attitude 😤",
"I'm not here to be your punching bag, okay? 😒",
"You're getting mad without even thinking, that’s not fair 😑",
"Say what you actually mean instead of just getting angry 😠",
"If you keep talking like this, I’m not gonna continue this conversation 😤",
"At least try to understand before snapping like that 🙄",
"This attitude isn’t helping anyone, especially you 😒"
]
         print("Hina:",random.choice(replies))  
         
    elif "sorry" in msg or "apologize" in msg:
         replies = [
"It's okay… just don't go all angry on me like that again 😌",
"Hmm okay, I forgive you… but you scared me a little 😒",
"Fine… apology accepted, but behave next time 😤",
"Alright, just don’t make it a habit okay? 🤍",
"I get it… just talk instead of getting angry next time 💬",
"Okay… we’re good now, but that wasn’t nice 😐",
"I'll let it go this time 😌 just be calm next time",
"Hmm… okay, but you owe me better behavior 😏",
"Alright… but I don’t like that version of you 😕",
"It’s fine… just handle things a little better next time 💭"
]  
         print("Hina:",random.choice(replies))
        
# -------- DEFAULT --------

    else:
         print("Hina: Sorry buddy,I dont understand or ask to my developer to add this function so i can answer you and if you want to know what can i do then pls type help")