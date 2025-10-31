import streamlit as st
import csv
import os
from datetime import datetime

# -----------------------
# App Title and Intro
# -----------------------
st.set_page_config(page_title="Leadership on the Line", page_icon="✈️", layout="centered")
st.title("Leadership on the Line ✈️")
st.markdown("Welcome to the inspection tracker — enter your details below to begin.")

# -----------------------
# User Inputs
# -----------------------
who = st.text_input("Who is inspecting? (Enter full name)")
aircraft_number = st.text_input("Aircraft Tail Number (Two digits only)")
inspection_time = st.text_input("Time of Inspection (Military time, e.g. 1530)")

line_badge = st.selectbox("Do individuals have their line badge?", ["Yes", "No"])
badge_showing = st.selectbox("Is it showing?", ["Yes", "No"])
ppe = st.selectbox("PPE Worn Correctly?", ["Yes", "No", "N/A"])

st.markdown("---")
st.subheader("Score the following (1–5, with 5 being best):")

cleanliness = st.text_input("Cleanliness Inside/Outside")
safe_maint = st.text_input("Safe For Maintenance")
organized_storage = st.text_input("Organized Cargo/Storage")
organized_flightdeck = st.text_input("Organized Flight Deck")
forms = st.text_input("Forms 781s current/accurate/signed?")
fod_check = st.text_input("FOD Check?")
age_pos = st.text_input("AGE Positioned Safely?")
comments = st.text_area("Additional Comments", placeholder="Type 'No' if none")

# -----------------------
# Save Button
# -----------------------
if st.button("💾 Save Inspection"):
    # Validate required fields
    if not who or not aircraft_number or not inspection_time:
        st.error("Please fill out required fields: name, aircraft number, and inspection time.")
    else:
        # Format data
        date_now = datetime.now().strftime("%Y-%m-%d %H:%M")
        who_upper = who.upper()
        line_badge = line_badge.upper()
        badge_showing = badge_showing.upper()
        ppe = ppe.upper()

        filename = "Leadership_on_line.csv"
        save_path = os.path.join(os.getcwd(), filename)

        # Ensure CSV file exists
        file_exists = os.path.exists(save_path)

        with open(save_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            # Write header if new file
            if not file_exists:
                writer.writerow(["Question", "Answer"])

            # Write inspection data
            inspection_data = [
                ("Date of Inspection", date_now),
                ("Who spectated?", who_upper),
                ("What Aircraft?", aircraft_number),
                ("Time inspection was done", inspection_time),
                ("Line Badge?", line_badge),
                ("Showing?", badge_showing),
                ("PPE worn correctly?", ppe),
                ("Cleanliness Inside/Outside?", cleanliness),
                ("Safe For Maintenance?", safe_maint),
                ("Organized Cargo/Storage?", organized_storage),
                ("Organized Flight Deck?", organized_flightdeck),
                ("Forms?", forms),
                ("FOD Check?", fod_check),
                ("AGE Positioned correctly?", age_pos),
                ("Comments", comments),
                ("--- NEW ---", "")
            ]

            for q, a in inspection_data:
                writer.writerow([q, a])

        st.success("✅ Inspection saved successfully!")
        st.info(f"File saved at: {save_path}")

# -----------------------
# Display File
# -----------------------
if st.button("📄 View Saved Inspections"):
    save_path = os.path.join(os.path.expanduser("~"), "Documents", "Leadership_on_line.csv")
    if os.path.exists(save_path):
        import pandas as pd
        data = pd.read_csv(save_path)
        st.dataframe(data)
    else:
        st.warning("No saved inspections found yet.")
