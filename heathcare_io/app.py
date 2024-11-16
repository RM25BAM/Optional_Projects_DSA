# app.py

import streamlit as st
# from backend import add_patient, get_patient

st.image("logo.png", width)
st.title("Healthcare Information System")

# Sidebar Menu
menu = ["Add Patient", "View Patient", "Schedule Appointment"]
choice = st.sidebar.selectbox("Menu", menu)

# Add Patient Form
if choice == "Add Patient":
    st.subheader("Add a New Patient")
    id = st.text_input("Patient ID")
    name = st.text_input("Patient Name")
    age = st.number_input("Patient Age", min_value=0)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    contact = st.text_input("Contact Number")

    if st.button("Add Patient"):
        result = add_patient(id, name, age, gender, contact)
        st.success(result)

# View Patient Details
elif choice == "View Patient":
    st.subheader("View Patient Information")
    patient_id = st.text_input("Enter Patient ID")
    
    if st.button("Find Patient"):
        patient = get_patient(patient_id)
        if isinstance(patient, str):
            st.error(patient)
        else:
            st.write(f"Name: {patient.name}")
            st.write(f"Age: {patient.age}")
            st.write(f"Gender: {patient.gender}")
            st.write(f"Contact: {patient.contact}")

# Schedule Appointment (Dummy interface for now)
elif choice == "Schedule Appointment":
    st.subheader("Schedule an Appointment")
    st.text("Appointment scheduling feature to be implemented.")
