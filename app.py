import streamlit as st
import os
import json



st.title("Image Classification (Pets)")
st.header(
    body= "Data Collection Section",
    divider= 'blue',
    width = "stretch"
    )

if "form_submitted" not in st.session_state:
    st.session_state.form_submitted = False

with st.form(key="id-form", enter_to_submit=False,border=True, width="stretch", height="content"):
    name = st.text_input(label = 'What\'s your name?', placeholder="Kuro")
    if name:
        st.write(f'Welcome, {name}!')
    age = st.slider('Select your age', 15, 80, 18)
    st.write(f'You are {age} years old.')
    residence = st.selectbox("Where do you stay", ["Ayeduase", "New Site", "Boadi", "Appiadu", "ON-campus"])
    submitted = st.form_submit_button("Submit Data")

if submitted:
    st.session_state.form_submitted = True
    new_user_data = {
        "username": name,
        "userage": age,
        "residence": residence }

    if not os.path.exists("data.json") or os.path.getsize("data.json") == 0:
        initial_data = [new_user_data]
        with open("data.json", "w") as data_file:
            json.dump(initial_data, data_file, indent=4)
    else:
        try:
            with open("data.json", "r") as data_file:
                existing_data = json.load(data_file)
            
            if not isinstance(existing_data, list):
                print("Error: The existing file content is not a list. Cannot append")
            existing_data.append(new_user_data)
            
            with open("data.json", "w") as data_file:
                json.dump(existing_data, data_file, indent=4)

        except Exception as e:
            print(f"ERROR!: {e}")

if st.session_state.form_submitted:
    # Image Upload Section
    st.header(
        body="Image Upload Section",
        anchor=False,
        help="Here, just upload image and await prediction",
        divider="blue",
        width="stretch"
    )

    user_upload = st.file_uploader("Upload an image file (JPG, JPEG, PNG)", type=["jpg", "jpeg", "png"])

    if user_upload:
        st.image(user_upload, caption="Uploaded image")
        st.balloons()

        st.header(
            body = "Prediction placeholder",
            divider = "blue",
            width = "stretch")
        
        with st.form(key="pred-form", enter_to_submit=False,border=True, width="stretch", height="content"):
            gender = st.radio("Enter your gender", ['Male', 'Female', "Mentally disabled"])
            edu = st.selectbox("Select your Parent's Education Level", ["Some high school", "High school(Completed)", "some college", "associate's degree", "bachelor's degree", "master's degree"])
            comp = st.selectbox("Did student complete a test prep course", ["Completed", "None"])
            final = st.form_submit_button("Make prediction")
        

