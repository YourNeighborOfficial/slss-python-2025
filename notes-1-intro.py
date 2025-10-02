# Notes - Introduction
# 16 September
# Julian Sauvageau

# Create an algorithm to solve a problem
# Problem: Create our own chatbot
#              MeGPT

#  1. Greet the user with a predetermined statement
greeting = "Hello! I am a chatbot"

# 1a. Print the greeting
print(greeting)

# 2. Introduce the bot
print("My name is MeGPT")
print("im not like the other guy")
print("i am completely deterministic")

# 3. Wow the user with some maths
print("I bet you dont know what 8x8 is")
print("I can do it")
print(f"8x8 is actuallt{8*8}.")
print(f"it is {3.14159265359 ** 2}")

# 4. make the bot crash out a little bit.
print("the quick brown fox jumps over the lazy dog" * 10)

# 5. get the name of the user, store it, and use it
user_name = input("whats your name")
print(f"its nice to meet you, {user_name}")

input("do you like juice")
print("sorry say that again i couldnt hear you")

input("do you like juice")
print("speak up you arent typing loud enough")

juice = input("do you like juice")
print(f"come back later with a proper answer that isnt {juice}")

# 8. see IF the user is someone specific
# 8a. if theyre someone specific, tell them a secret
if user_name == "jeffrey epstein":
    print("diddy ahh blud ☠️☠️☠️")
