import streamlit as st
from flights_info import flights


st.title("Confirm Your Booking")
selected_flight = st.session_state.get("selected_flight")
if not selected_flight:
    st.warning("No flight selected. Please search for and select a flight.")
   
st.subheader("Flight Details")
st.markdown(f"""
**From**: {flights[selected_flight]['origin']}  
**To**: {flights[selected_flight]['destination']}  
**Price**: ${flights[selected_flight]['price']}  
**Date**: {flights[selected_flight]['date']}  
**Departure**: {flights[selected_flight]['departure']}  
""")
st.subheader("Passenger Details")
with st.form("passenger_form"):
    name = st.text_input("Passenger Name")
    email = st.text_input("Passenger Email")
    phone = st.text_input("Passenger Phone Number")
    confirm = st.form_submit_button("Confirm Booking")

    if confirm:
        if not name or not email or not phone:
            st.error("All fields are required to confirm the booking.")
            
        st.session_state["booking_details"] = {
            "flight": selected_flight,
            "name": name,
            "email": email,
            "phone": phone,
        }
        st.success("Booking Confirmed! Navigating to confirmation page...")
        