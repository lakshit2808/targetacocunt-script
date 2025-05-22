from Functions import csv_to_json, verify_data

if __name__ == "__main__":
    import streamlit as st
    import tempfile
    import os
    st.title("CSV to API Uploader & Verifier")

    st.write("Upload a CSV file and provide your email to send data to the API.")

    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
    email = st.text_input("Enter your email")

    if uploaded_file is not None and email:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_csv_path = tmp_file.name

        if st.button("Send Data to API"):
            with st.spinner("Sending data to API..."):
                csv_to_json(tmp_csv_path, email)
            st.success("All data sent to API.")

        if st.button("Verify Data in API"):
            with st.spinner("Verifying data in API..."):
                count = verify_data(email, tmp_csv_path)
            st.info(f"API returned {count} records for this email.")

        os.remove(tmp_csv_path)
    elif uploaded_file is not None:
        st.warning("Please enter your email.")
    elif email:
        st.warning("Please upload a CSV file.")