# import streamlit as st
# import re
# import random


# # page style
# st.set_page_config(page_title='Password Strength Checker ', page_icon='🔑', layout='centered', initial_sidebar_state='auto')
# #custom css
# st.markdown("""
# <style>
#     .main {text-align: center;}
#     .stTextInput {width: 60% !imporoment; margin: auto;}
#     stButton button {width: 50%; background-color:#3f3f3f; color:white; font-size: 18px;  auto;}   
#     .stButton button {width: 50%; background-color:#3f3f3f; color:white; font-size: 18px;  auto;}         
# </style>
# """, unsafe_allow_html=True)
# #page title and decription
# st.title('Password Strength Checker 🔑')
# st.write('Enter a password and see how strong it is!')

# #func to check pasword strength
# def check_password_strength(password):
#     score = 0
#     feedback = []

#     if len(password) >= 8:
#         score +=1  # increase 
#     else:
#         feedback.append("❌ Pasword should be *atleast 8 or more*")
#     if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
#         score +=1
#     else:
#         feedback.append("❌ Pasword should include  *both uppercase nad (A-Z) lowercase (a-z)  8 or more*")
#     if re.search(r"\d", password):
#         score +=1
#     else:
#         feedback.append("❌ Pasword should include  *At least number  (0-9)*")
#     if re.search(r"[!@$%*&]", password):
#         score +=1
#     else:
#         feedback.append("❌ Include **atleast one special charachter (!@$%*&)")


#      # display pasword strength 
#     if score == 4:
#         st.success("**strong** Your password is secure")
#     elif score == 3 :
#         st.info(" **Mederate Password ** - consider improeving security by adding more secure password")
#     else:
#         st.error("**Week Password ** - Follow the suggestion below to stength")

#         # feedback
#         if feedback:
#             with st.expander("**Improve Your Passord**"):
#                 for item in feedback:
#                     st.write(item)
# password = st.text_input("Enter Your Password", type="password", help="Ensure Your password is strong")


# if st.button("Check strength"):
#     if password:
#         check_password_strength(password)
#     else:
#         st.warning("Please enter a password")


# yt


# import streamlit as st
# import re
# import random
# import string
# from pyperclip import copy

# # Page configuration
# st.set_page_config(
#     page_title='Password Strength Checker & Generator',
#     page_icon='🔐',
#     layout='centered',
#     initial_sidebar_state='collapsed'
# )

# # Custom CSS for improved styling
# st.markdown("""
# <style>
#     .main {padding: 2rem;}
#     .stTextInput input {font-size: 18px !important;}
#     .stButton>button {width: 100%; background-color: #4CAF50; color: white;}
#     .strength-meter {height: 10px; border-radius: 5px; margin: 10px 0;}
#     .weak {background-color: #ff4444;}
#     .medium {background-color: #ffd700;}
#     .strong {background-color: #00C851;}
#     .toggle-container {display: flex; justify-content: center; margin: 1rem 0;}
#     .generated-password {font-size: 20px; font-weight: bold; color: #4CAF50;}
# </style>
# """, unsafe_allow_html=True)

# # Common passwords list (partial example - should be expanded)
# COMMON_PASSWORDS = [
#     'password', '123456', 'qwerty', 'letmein', 'welcome',
#     'abc123', 'password1', 'admin', 'sunshine', 'iloveyou'
# ]

# def check_common_password(password):
#     return password.lower() in COMMON_PASSWORDS

# def generate_password(length=12):
#     characters = string.ascii_letters + string.digits + "!@$%*&"
#     return ''.join(random.choice(characters) for _ in range(length))

# def password_strength_visual(score):
#     colors = ['weak'] * 4
#     for i in range(score):
#         colors[i] = 'strong' if score > 2 else 'medium' if score == 2 else 'weak'
#     return f"""
#     <div style="display: flex; gap: 5px; margin: 10px 0;">
#         <div class="strength-meter {colors[0]}" style="width: 25%;"></div>
#         <div class="strength-meter {colors[1]}" style="width: 25%;"></div>
#         <div class="strength-meter {colors[2]}" style="width: 25%;"></div>
#         <div class="strength-meter {colors[3]}" style="width: 25%;"></div>
#     </div>
#     """

# def check_password_strength(password):
#     score = 0
#     feedback = []
    
#     # Length check
#     if len(password) >= 12:
#         score += 2
#     elif len(password) >= 8:
#         score += 1
#     else:
#         feedback.append("❌ Password should be at least 8 characters long (12+ recommended)")

#     # Character diversity
#     checks = {
#         'uppercase': re.search(r"[A-Z]", password),
#         'lowercase': re.search(r"[a-z]", password),
#         'digit': re.search(r"\d", password),
#         'special': re.search(r"[!@$%*&]", password)
#     }
    
#     for check, result in checks.items():
#         if not result:
#             feedback.append(f"❌ Missing {check} character")
#         else:
#             score += 0.5 if check in ['uppercase', 'lowercase'] else 1

#     # Common password check
#     if check_common_password(password):
#         score = 0
#         feedback.append("❌ This password is too common and easily guessable")

#     # Final scoring
#     score = min(int(score), 4)  # Cap score at 4 for visualization

#     return score, feedback

# # Main app layout
# st.title('🔐 Password Security Toolkit')
# tab1, tab2 = st.tabs(["Strength Checker", "Password Generator"])

# with tab1:
#     st.header("Check Password Strength")
#     password = st.text_input("Enter password:", type="password", key="checker_input")

#     if st.button("Analyze Password"):
#         if password:
#             score, feedback = check_password_strength(password)
#             st.markdown(password_strength_visual(score), unsafe_allow_html=True)
            
#             if score == 4:
#                 st.success("💪 Excellent! This is a strong, secure password")
#             elif score >= 2:
#                 st.info("🔍 Good start, but could be improved")
#                 with st.expander("🔧 Recommendations"):
#                     for item in feedback:
#                         st.markdown(item)
#             else:
#                 st.error("⚠️ Weak password - High risk of compromise")
#                 with st.expander("🔧 Critical Improvements Needed"):
#                     for item in feedback:
#                         st.markdown(item)
#         else:
#             st.warning("Please enter a password to analyze")

# with tab2:
#     st.header("Generate Strong Password")
#     col1, col2 = st.columns(2)
#     length = col1.slider("Password length", 8, 24, 12)
#     use_special = col2.toggle("Include special characters", value=True)
    
#     if st.button("Generate Secure Password"):
#         chars = string.ascii_letters + string.digits
#         if use_special:
#             chars += "!@$%*&"
#         generated = ''.join(random.choice(chars) for _ in range(length))
#         st.markdown(f'<p class="generated-password">{generated}</p>', unsafe_allow_html=True)
        
#         if st.button("📋 Copy to Clipboard"):
#             copy(generated)
#             st.success("Password copied to clipboard!")

# # Footer
# st.markdown("---")
# st.markdown("🔒 *Always use strong, unique passwords for each account*")




# fixed 

import streamlit as st
import re
import random
import string
import streamlit.components.v1 as components  # Added for JavaScript clipboard copy

# Page configuration
st.set_page_config(
    page_title='Password Strength Checker & Generator',
    page_icon='🔐',
    layout='centered',
    initial_sidebar_state='collapsed'
)

# Custom CSS for improved styling
st.markdown("""
<style>
    .main {padding: 2rem;}
    .stTextInput input {font-size: 18px !important;}
    .stButton>button {width: 100%; background-color: #4CAF50; color: white;}
    .strength-meter {height: 10px; border-radius: 5px; margin: 10px 0;}
    .weak {background-color: #ff4444;}
    .medium {background-color: #ffd700;}
    .strong {background-color: #00C851;}
    .toggle-container {display: flex; justify-content: center; margin: 1rem 0;}
    .generated-password {font-size: 20px; font-weight: bold; color: #4CAF50;}
</style>
""", unsafe_allow_html=True)

# Common passwords list
COMMON_PASSWORDS = ['password', '123456', 'qwerty', 'letmein', 'welcome', 'abc123', 'password1', 'admin', 'sunshine', 'iloveyou']

def check_common_password(password):
    return password.lower() in COMMON_PASSWORDS

def generate_password(length=12, use_special=True):
    characters = string.ascii_letters + string.digits
    if use_special:
        characters += "!@$%*&"  # Add special characters only if use_special is True
    return ''.join(random.choice(characters) for _ in range(length))

def password_strength_visual(score):
    colors = ['weak'] * 4
    for i in range(score):
        colors[i] = 'strong' if score > 2 else 'medium' if score == 2 else 'weak'
    return f"""
    <div style="display: flex; gap: 5px; margin: 10px 0;">
        <div class="strength-meter {colors[0]}" style="width: 25%;"></div>
        <div class="strength-meter {colors[1]}" style="width: 25%;"></div>
        <div class="strength-meter {colors[2]}" style="width: 25%;"></div>
        <div class="strength-meter {colors[3]}" style="width: 25%;"></div>
    </div>
    """

def check_password_strength(password):
    score = 0
    feedback = []
    
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long (12+ recommended)")

    checks = {'uppercase': re.search(r"[A-Z]", password), 'lowercase': re.search(r"[a-z]", password), 'digit': re.search(r"\d", password), 'special': re.search(r"[!@$%*&]", password)}
    
    for check, result in checks.items():
        if not result:
            feedback.append(f"❌ Missing {check} character")
        else:
            score += 0.5 if check in ['uppercase', 'lowercase'] else 1

    if check_common_password(password):
        score = 0
        feedback.append("❌ This password is too common and easily guessable")

    score = min(int(score), 4)

    return score, feedback

st.title('🔐 Password Security Toolkit')
tab1, tab2 = st.tabs(["Strength Checker", "Password Generator"])

with tab1:
    st.header("Check Password Strength")
    password = st.text_input("Enter password:", type="password", key="checker_input")

    if st.button("Analyze Password", key="analyze_btn"):
        if password:
            score, feedback = check_password_strength(password)
            st.markdown(password_strength_visual(score), unsafe_allow_html=True)
            
            if score == 4:
                st.success("💪 Excellent! This is a strong, secure password")
            elif score >= 2:
                st.info("🔍 Good start, but could be improved")
                with st.expander("🔧 Recommendations"):
                    for item in feedback:
                        st.markdown(item)
            else:
                st.error("⚠️ Weak password - High risk of compromise")
                with st.expander("🔧 Critical Improvements Needed"):
                    for item in feedback:
                        st.markdown(item)
        else:
            st.warning("Please enter a password to analyze")

with tab2:
    st.header("Generate Strong Password")
    col1, col2 = st.columns(2)
    length = col1.slider("Password length", 8, 24, 12)
    use_special = col2.toggle("Include special characters", value=True)

    # Unique Key Added for Button
    if st.button("Generate Secure Password", key="generate_btn"):
        generated = generate_password(length, use_special)
        st.success("✅ Strong password generated!")

        # Display password in text box for easy copy
        generated_password = st.text_input("Generated Password:", generated, key="generated_password", disabled=False)

        # Copy button with a unique key
        if st.button("📋 Copy to Clipboard", key="copy_btn"):
            st.write("📋 Select & Copy the password manually!")
            st.warning("⚠️ Auto-copy doesn't work on Streamlit Cloud. Use the textbox above to copy.")

st.markdown("---")
st.markdown("🔒 *Always use strong, unique passwords for each account*")
