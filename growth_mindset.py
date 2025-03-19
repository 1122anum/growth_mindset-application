import streamlit as st
st.title("growth mindset challenge project")
st.header("mood checker app")

# user sy mood ka input lety hain
mood = st.text_input("How is your mood today?",)

# mood k hisab sy text dekhaty hain
if mood == "happy":
    st.header("Your day is wonderful!")
    st.write("Enjoy your day and spread positivity")
elif mood == "sad":
    st.header("You are a little cheerful")
    st.write("It doesn't matter, everything will be fine, take out some time for yourself too.")
elif mood == "angry":
    st.header("Relax")
    st.write("Take deep breaths to cool down your anger")

# apka mood thk krny k lie kuch motivational quotes
st.subheader("Today's motivational quote")
quotes = ["It always seems impossible until it's done.",
         "Every day is a new biginnig. take a deep breath and start again.",
         "Your attitude determines your direction."]
import random
st.write(random.choice(quotes))




