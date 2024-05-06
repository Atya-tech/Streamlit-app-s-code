import streamlit as st

def app():
    st.title("Login/Signup Form")

    # Display radio buttons for login/signup choice
    choice = st.radio("Choose an action:", ("Login", "Signup"))
    login=st.columns(2)
    if choice == "Login":
        with login[0]:
            login_form()
    elif choice == "Signup":
        with login[0]:
            signup_form()

def login_form():
    st.header("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "" or password == "":
            st.error("All fields are mandatory.")
        else:
            # Placeholder login logic
            st.success("Logged in as {}".format(username))
    
    # Forgot Password hyperlink
    st.markdown(
    """
    <style>
    button[kind="primary"] {
        background: none!important;
        border: none;
        padding: 0!important;
        color: black !important;
        text-decoration: none;
        cursor: pointer;
        border: none !important;
    }
    button[kind="primary"]:hover {
        text-decoration: none;
        color: black !important;
    }
    button[kind="primary"]:focus {
        outline: none !important;
        box-shadow: none !important;
        color: black !important;
    }
    </style>
    """,
    unsafe_allow_html=True)
    if st.button(':blue[forgot pasword]',type="primary"):
        st.session_state.page= forgot_password()

    if st.markdown("[Signup For Embed-View](https://www.example.com/forgot_password)"):
        st.session_state.page = "Signup For Embed-View"

def signup_form():
    st.header("Signup")
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Signup"):
        if username == "" or email == "" or password == "" or confirm_password == "":
            st.error("All fields are mandatory.")
        elif "@" not in email or "." not in email:
            st.error("Please enter a valid email address.")
        elif username == "" or "@" not in username or "." not in username:
            st.error("Please enter a valid username.")
        elif not validate_password(password):
            st.error("Password requirements not met.")
        elif password != confirm_password:
            st.error("Passwords do not match.")
        else:
            # Placeholder signup logic
            st.success("Signup successful for user: {}".format(username))
            

def validate_password(password):
    if len(password) < 12:
        return False
    if " " in password:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    return True
    
def forgot_password():
    new_password = st.text_input("New password",type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    if new_password!=confirm_password:
        st.warning("Password do not match")
    if st.button('update  Password'):
        st.write('password reset successful')
    