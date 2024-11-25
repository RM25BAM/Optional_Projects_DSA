import streamlit as st
from PIL import Image
import os
from binary_search import binary_search_flights
from flights_info import flights
from utils import navigate_to
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
ASSETS_DIR = os.path.join(BASE_DIR, "flight_io/assets")
destinations = [
    {"name": "Agra, India", "image": "agra.jpg", "description": "Home to the iconic Taj Mahal."},
    {"name": "Bali, Indonesia", "image": "bali.jpg", "description": "Known for its beautiful beaches and serene landscapes."},
    {"name": "Barcelona, Spain", "image": "barcelona.jpg", "description": "A city famous for art and architecture."},
    {"name": "Dubai, United Arab Emirates", "image": "dubai.jpg", "description": "Luxurious city with modern architecture and desert safaris."},
    {"name": "Istanbul, Turkey", "image": "istanbul.jpg", "description": "Historic city connecting Europe and Asia, rich in culture."},
    {"name": "London, England", "image": "london.jpg", "description": "A city with rich history and world-class museums and landmarks."},
    {"name": "New York City, United States", "image": "nyc.jpg", "description": "The city that never sleeps, known for iconic landmarks."},
    {"name": "Petra, Jordan", "image": "petra.jpg", "description": "Ancient city carved into rose-red cliffs."},
    {"name": "Prague, Czech Republic", "image": "prague.jpg", "description": "Charming city known for its Old Town and Gothic churches."},
    {"name": "Rome, Italy", "image": "rome.jpg", "description": "Historic city with ancient ruins and Renaissance art."},
    {"name": "Seoul, South Korea", "image": "seoul.jpg", "description": "Modern city blending tradition and high-tech culture."},
    {"name": "San Francisco, United States", "image": "sf.jpg", "description": "Home to the Golden Gate Bridge and scenic landscapes."},
    {"name": "Singapore, Singapore", "image": "singapore.jpg", "description": "Futuristic city with lush green spaces and modern architecture."},
    {"name": "Tokyo, Japan", "image": "tokyo.jpg", "description": "Vibrant city with a mix of skyscrapers, temples, and technology."},
]
for destination in destinations:
    destination["image"] = os.path.join(ASSETS_DIR, destination["image"])
    if not os.path.exists(destination["image"]):
        print(f"Warning: File not found for {destination['name']} at {destination['image']}")
def search_flights():
    st.title("Search Flights")
    origin = st.text_input("Origin")
    destination = st.text_input("Destination")
    """ date = st.date_input("Travel Date") """
    if st.button("Search"):
        st.write(f"Searching flights from {origin} to {destination}...")
        origin = origin.strip().title()
        destination = destination.strip().title()
        sorted_flights = sorted(flights, key=lambda x: (x["origin"], x["destination"], x["price"], x["date"], x["departure"]))
        results, indexs = binary_search_flights(sorted_flights, origin, destination)
        if results and indexs:
            st.subheader("Direct Flights Found:")
            for flight, index in zip(results, indexs):
                with st.container():
                    st.markdown(
                        """
                        <style>
                        .flight-card {
                            background-color: #2c2c2c; /* Darker gray */
                            padding: 20px;
                            border-radius: 10px;
                            margin-bottom: 20px;
                            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.4); /* Stronger shadow */
                            display: flex;
                            align-items: center;
                            justify-content: space-between;
                        }
                        .flight-card-details {
                            flex-grow: 1;
                        }
                        .flight-card-details .from-to {
                            display: flex;
                            justify-content: space-between;
                            margin-bottom: 10px;
                        }
                        .flight-card-details h4 {
                            margin: 0;
                            color: #ffffff; /* White text */
                        }
                        .flight-card-details p {
                            margin: 5px 0;
                            color: #d3d3d3; /* Light gray text */
                            font-size: 14px;
                        }
                        </style>
                        """,
                        unsafe_allow_html=True,
                    )
                    st.markdown(
                        f"""
                        <div class="flight-card">
                            <div class="flight-card-details">
                                <div class="from-to">
                                    <h4><strong>From:</strong> {flight['origin']}</h4>
                                    <h4><strong>To:</strong> {flight['destination']}</h4>
                                </div>
                                <p><strong>Flight ID:</strong> {flight['flight_id']}</p>
                                <p><strong>Price:</strong> ${flight['price']}</p>
                                <p><strong>Date:</strong> {flight['date']}</p>
                                <p><strong>Departure:</strong> {flight['departure']}</p>
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
                    if st.button(f"Select Flight {flight['flight_id']}", key=f"select_{flight['flight_id']}"):
                        st.write(f"select_{flight['flight_id']}")
                        st.session_state["selected_flight"] = index
                        # navigate_to("booking_page") 
                        st.switch('booking.py')
        else:
            st.error("No direct flights found.")
    st.title("Explore Popular Destinations")

    cols = st.columns(1)  
    for i, dest in enumerate(destinations):
        with cols[i % 1]:  
            try:
                image = Image.open(dest["image"])
                st.image(image, use_container_width=True) 
            except Exception as e:
                st.error(f"Image not found for {dest['name']}")

            st.subheader(dest["name"])
            st.write(dest["description"])
def confirmation_page():
    st.title("Booking Confirmation")
    booking_details = st.session_state.get("booking_details")

    if not booking_details:
        st.warning("No booking details found. Please start over.")
        st.session_state["page"] = "search"
        st.experimental_rerun()
        return
    st.subheader("Your Booking Details")
    flight = booking_details["flight"]
    st.markdown(f"""
    **Flight ID**: {flight['flight_id']}  
    **From**: {flight['origin']}  
    **To**: {flight['destination']}  
    **Price**: ${flight['price']}  
    **Date**: {flight['date']}  
    **Departure**: {flight['departure']}  
    """)
    st.markdown(f"""
    **Passenger Name**: {booking_details['name']}  
    **Email**: {booking_details['email']}  
    **Phone**: {booking_details['phone']}  
    """)
    if st.button("Back to Search"):
        navigate_to("confirmation")
def view_reservations():
    st.title("Your Reservations")
    reservations = [{"Flight ID": "FL001", "Origin": "New York", "Destination": "Los Angeles", "Date": "2023-11-20"}]
    st.table(reservations)
def dashboard():
    st.title(f"Welcome, {st.session_state.get('user', 'Guest')}!")
    st.write("This is your dashboard.")
    st.write(f"Base directory: {BASE_DIR}")
    st.write(f"Assets directory: {ASSETS_DIR}")
    if st.button("Log Out"):
        st.session_state["logged_in"] = False
        st.session_state["user"] = None
        navigate_to("sign_in")
# import streamlit as st
# import hashlib
# import os
# BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))  # Adjust to root
# ASSETS_DIR = os.path.join(BASE_DIR, "assets/cities")
# destinations = [
#     {"name": "Agra, India",
#      "image": os.path.join(ASSETS_DIR, "agra.jpg"), 
#      "description": "Home to the iconic Taj Mahal."},
#     {
#         "name": "Bali, Indonesia",
#         "image": "flight_io/assets/cities/bali.jpg",
#         "description": "The city of love. Visit the Eiffel Tower, the Louvre, and enjoy French cuisine."
#     },
#     {
#         "name": "Barcelona, Spain",
#         "image": "flight_io/assets/cities/barcelona.jpg",
#         "description": "A bustling metropolis blending tradition and modernity. Don't miss Shibuya Crossing and ancient temples."
#     },
#     {
#         "name": "Dubai, United Arab Emirates",
#         "image": "flight_io/assets/cities/dubai.jpg",
#         "description": "Experience the beauty of Sydney Harbor, the Opera House, and Bondi Beach."
#     },
#     {
#         "name": "Istanbul, Turkey",
#         "image": "flight_io/assets/cities/istanbul.jpg",
#         "description": "Experience the beauty of Sydney Harbor, the Opera House, and Bondi Beach."
#     },
#     {
#         "name": "London, England/United Kingdom",
#         "image": "flight_io/assets/cities/buenos_aires.jpg",
#         "description": "Experience the beauty of Sydney Harbor, the Opera House, and Bondi Beach."
#     },
#     {
#         "name": "NYC, United States",
#         "image": "flight_io/assets/cities/nyc.jpg",
#         "description": "Experience the beauty of Sydney Harbor, the Opera House, and Bondi Beach."
#     },
#     {
#         "name": "Petra, Jordan",
#         "image": "flight_io/assets/cities/petra.jpg",
#         "description": "Experience the beauty of Sydney Harbor, the Opera House, and Bondi Beach."
#     },
#     {
#         "name": "Prague, Czech",
#         "image": "flight_io/assets/cities/prague.jpg",
#         "description": "Experience the beauty of Sydney Harbor, the Opera House, and Bondi Beach."
#     },
#     {
#         "name": "Rome, Italy",
#         "image": "flight_io/assets/cities/rome.jpg",
#         "description": "Experience the beauty of Sydney Harbor, the Opera House, and Bondi Beach."
#     },
#     {
#         "name": "Seoul, South Korea",
#         "image": "./assets/cities/seoul.jpg",
#         "description": "Experience the beauty of Sydney Harbor, the Opera House, and Bondi Beach."
#     },
#     {
#         "name": "San Francisco, Argentina",
#         "image": "flight_io/assets/cities/sf.jpg",
#         "description": "Experience the beauty of Sydney Harbor, the Opera House, and Bondi Beach."
#     },
#     {
#         "name": "Singapore, Singapore",
#         "image": "flight_io/assets/cities/singapore.jpg",
#         "description": "Experience the beauty of Sydney Harbor, the Opera House, and Bondi Beach."
#     },
#     {
#         "name": "Tokyo, Japan",
#         "image": "flight_io/assets/cities/tokyo.jpg",
#         "description": "Experience the beauty of Sydney Harbor, the Opera House, and Bondi Beach."
#     },
# ]
# def dashboard():
#     st.title(f"Welcome, {st.session_state.get('user')}!")
#     st.write("This is your dashboard.")

#     if st.button("Log Out"):
#         st.session_state["logged_in"] = False
#         st.session_state["user"] = None
#         navigate_to("sign_in")
# # Ensure absolute paths for local images
# for destination in destinations:
#     destination["image"] = os.path.abspath(destination["image"])

# # Function to display destinations
# def search_flights():
#     st.title("Search Flights")
#     origin = st.text_input("Origin")
#     destination = st.text_input("Destination")
#     date = st.date_input("Travel Date")

#     if st.button("Search"):
#         st.write(f"Searching flights from {origin} to {destination} on {date}...")

#     st.title("Explore Popular Destinations")
#     st.write("Click on a destination to learn more or include it in your flight search.")
#     for destination in destinations:
#         print(destination["image"])

#     # Display destinations in a grid
#     cols = st.columns(2)  # Two-column layout
#     for i, dest in enumerate(destinations):
#         with cols[i % 2]:  # Alternate between the two columns
#             try:
#                 st.image(dest["image"], use_container_width=True)
#             except Exception as e:
#                 st.error(f"Image not found for {dest['name']}: {e}")
#             st.subheader(dest["name"])
#             st.write(dest["description"])
#             if st.button(f"Select {dest['name']}", key=dest["name"]):
#                 st.session_state["selected_destination"] = dest["name"]
#                 st.success(f"Destination selected: {dest['name']}")
# def view_reservations():
#     st.title("Your Reservations")
#     reservations = [{"Flight ID": "FL001", "Origin": "New York", "Destination": "Los Angeles", "Date": "2023-11-20"}]
#     st.table(reservations)
