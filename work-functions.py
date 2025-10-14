# Define a function called create_mood_message.
# It should accept two parameters: name and mood.
# Make the mood parameter optional by giving it a default value of "neutral".
# Inside the function, use an if/elif/else block to check the value of mood:
# If mood is "happy", return a cheerful message like f"Hey {name}, great to see you smiling!".
# If mood is "sad", return a supportive message like f"I hope your day gets better, {name}.".
# If mood  is "neutral", return a message like f"Sometimes you have average days, {name}." .
# For any other mood (the else case), return a neutral message like f"Hi {name}, hope you're having a good day.".

def create_mood_message(name: str, mood="neutral"):
    if mood == "happy":
        return f"Hey {name}, gerat to see you smiling!"
    if mood == "sad":
        return f"lmao get better stop being sad"
    if mood == "mad":
        return f"reoerbbgrknjregkjegrkjgrekjegr"
    if mood == "neutral":
        return f"diddy blud"

print(create_mood_message("Julian", "happy"))     # Hey Julian, gerat to see you smiling!
print(create_mood_message("Mr. Ubial", "happy"))
print(create_mood_message("Mr. Ubial", "sad"))
print(create_mood_message("spiderman", "neutral"))



# def neutral_return():
#     print("glad to know youre neutral today")
#     return "neutral"





#     return_val = create_mood_message

#     print(f"hello {name}, nice to know youre" return_val "today.")
