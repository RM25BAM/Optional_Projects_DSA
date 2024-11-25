import streamlit as st
import hashlib
from utils import navigate_to
from dashboard_page import dashboard, search_flights, view_reservations, confirmation_page

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def initialize_session_state():
    if "user_data" not in st.session_state:
        st.session_state["user_data"] = {"RM25BAM": hash_password("test123")}
    if "page" not in st.session_state:
        st.session_state["page"] = "sign_in"
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False
    if "user" not in st.session_state:
        st.session_state["user"] = None
    if "selected_flight" not in st.session_state:
        st.session_state["selected_flight"] = None
    if "booking_details" not in st.session_state:
        st.session_state["booking_details"] = None

# Sign-up page
def sign_up():
    st.title("Sign Up")
    user_data = st.session_state["user_data"]
    username = st.text_input("Create Username")
    password = st.text_input("Create Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Sign Up"):
        if username in user_data:
            st.error("User already exists!")
        elif password != confirm_password:
            st.error("Passwords do not match!")
        elif not username or not password:
            st.error("Username and Password cannot be empty!")
        else:
            user_data[username] = hash_password(password)
            st.session_state["user_data"] = user_data
            st.success("Account created successfully!")
            navigate_to("sign_in")

    if st.button("Go to Sign In"):
        navigate_to("sign_in")

# Sign-in page
def sign_in():
    st.title("Sign In")
    user_data = st.session_state["user_data"]
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Log In"):
        hashed_password = hash_password(password)
        if user_data.get(username) == hashed_password:
            st.success(f"Welcome back, {username}!")
            st.session_state["logged_in"] = True
            st.session_state["user"] = username
            navigate_to("dashboard")
        else:
            st.error("Invalid username or password!")

    if st.button("Go to Sign Up"):
        navigate_to("sign_up")

# Main function
def main():
    initialize_session_state()

    if st.session_state["logged_in"]:
        st.sidebar.title("Menu")
        menu = st.sidebar.radio(
            "Navigation",
            ["Dashboard", "Search Flights", "View Reservations","confirmation_page",  "Log Out"]
        )
        if menu == "Dashboard":
            navigate_to("dashboard")
        elif menu == "Search Flights":
            navigate_to("search_flights")
        elif menu == "View Reservations":
            navigate_to("view_reservations")
        elif page == "confirmation_page":
            confirmation_page() 
        elif menu == "Log Out":
            st.session_state["logged_in"] = False
            st.session_state["user"] = None
            navigate_to("sign_in")

    # Handle page routing
    page = st.session_state["page"]
    if page == "sign_in":
        sign_in()
    elif page == "sign_up":
        sign_up()
    elif page == "dashboard":
        if st.session_state["logged_in"]:
            dashboard()
        else:
            navigate_to("sign_in")
    elif st.session_state["page"] == "search_flights":
        search_flights()
    elif st.session_state["page"] == "view_reservations":
        view_reservations()
    elif st.session_state["page"] == "confirmation":
        confirmation_page()  # Add confirmation page handling
    else:
        st.error("Page not found. Redirecting to sign-in...")
        navigate_to("sign_in")

if __name__ == "__main__":
    main()
