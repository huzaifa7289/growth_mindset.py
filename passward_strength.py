import streamlit as st
import re

def check_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r"[A-Z]", password))
    lowercase_criteria = bool(re.search(r"[a-z]", password))
    number_criteria = bool(re.search(r"[0-9]", password))
    special_char_criteria = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])

    if score == 5:
        return "🟢 Strong", "green"
    elif score >= 3:
        return "🟡 Medium", "orange"
    else:
        return "🔴 Weak", "red"

st.title("🔐 Password Strength Meter")

password = st.text_input("Enter your password", type="password")

if password:
    strength, color = check_password_strength(password)
    st.markdown(f"### Strength: <span style='color:{color}'>{strength}</span>", unsafe_allow_html=True)
    st.progress(sum([len(password) >= 8, any(c.isupper() for c in password), any(c.islower() for c in password), any(c.isdigit() for c in password), any(c in '!@#$%^&*(),.?":{}|<>' for c in password)]) / 5)
