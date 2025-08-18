import streamlit as st
import pyqrcode

st.title("QR Code Generator")

name = st.text_input("Product name")
details = st.text_area("Product details")
url = st.text_input("Product URL")
years = st.selectbox("Number of years", list(range(1, 16)))
if st.button("Submit"):
    # Ensure the url starts with http:// or https://
    if url and not url.startswith(("http://", "https://")):
        url_display = "https://" + url
    else:
        url_display = url

    st.markdown(f"**Name:** {name}\n\n**Details:** {details}\n\n**Company Age:** {years}\n\n[Product Link]({url_display})")
    content = f"Product Name: {name}\nDetails: {details}\nCompany Age: {years} years\nURL: {url_display}"
    qr = pyqrcode.create(content, error='L')
    qr.png("myqr.png", scale=8)
    st.image("myqr.png", caption="Generated QR Code")
    with open("myqr.png", "rb") as f:
        st.download_button(
            label="Download QR Code",
            data=f,
            file_name="myqr.png",
            mime="image/png"
        )
else:
    st.write("Fill in the details and press Submit to create a QR code.")
