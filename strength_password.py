import re
import streamlit as st
# project tittle
st.title("password strength meter")
st.write("Enter password below to check it's security level. ")


# function password strength check krny klie
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1 
    else:
        feedback.append("password should be atleast 8 character long.")
    
    if re.search(r"[A-Z]",password) and re.search (r"[a-z]", password):
        score += 1
        
    else:
      feedback.append("password should include both uppercase(A-z) and lowercase(a-z) letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("password should include atleast one number (0-9).")
    
    if re.search(r"[!@%&£$]", password):
        score += 1
    else:
        feedback.append("include atleast one special character (!@%&£$).")


# display
    if score == 4:
        st.success("strong password - your password is secure")
    elif score == 3:
        st.info("moderate password - consider improving security by adding more feature")
    else:
        st.error("weak password , follow the suggestion below.")

# feedback
    if feedback:
        with st.expander("improve your password"):
            for item in feedback:
                st.write(item)

 # user sy input lena
password = st.text_input("Enter your password", type="password", help= "Ensure your password is strong.")

# creat button
if st.button("check strength"): 
  if password:
      check_password_strength(password)
  else:
        st.warning("please enter a password first!")