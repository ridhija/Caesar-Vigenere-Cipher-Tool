import streamlit as st

from caesar import caesar_encrypt, caesar_brute_force
from vigenere import vigenere_encrypt, vigenere_decrypt
from frequency_analysis import frequency_analysis


# Page configuration
st.set_page_config(
    page_title="Classical Cryptography Tool",
    page_icon="🔐",
    layout="centered"
)

# Title
st.title("🔐 Classical Cryptography Tool")
st.write(
    "A Python-based tool for Caesar Cipher, Vigenère Cipher, "
    "Frequency Analysis and basic Caesar Cipher Brute Force."
)

st.divider()


# ---------------- Caesar & Vigenère ----------------

st.header("Cipher Operations")

cipher = st.selectbox(
    "Select Cipher",
    ["Caesar Cipher", "Vigenère Cipher"]
)

operation = st.selectbox(
    "Select Operation",
    ["Encrypt", "Decrypt"]
)

text = st.text_area(
    "Enter Text",
    placeholder="Enter your text here..."
)


if cipher == "Caesar Cipher":

    shift = st.number_input(
        "Enter Shift Value",
        min_value=0,
        max_value=25,
        value=3,
        step=1
    )

    if st.button("Process Cipher"):

        if text.strip():

            if operation == "Encrypt":
                result = caesar_encrypt(text, shift)

            else:
                result = caesar_encrypt(text, -shift)

            st.subheader("Result")
            st.code(result)

        else:
            st.warning("Please enter some text.")


else:

    key = st.text_input(
        "Enter Key",
        placeholder="Example: KEY"
    )

    if st.button("Process Cipher"):

        if not text.strip():
            st.warning("Please enter some text.")

        elif not key.isalpha():
            st.warning("Key must contain letters only.")

        else:

            if operation == "Encrypt":
                result = vigenere_encrypt(text, key)

            else:
                result = vigenere_decrypt(text, key)

            st.subheader("Result")
            st.code(result)


# ---------------- Frequency Analysis ----------------

st.divider()

st.header("📊 Frequency Analysis")

analysis_text = st.text_area(
    "Enter Text for Frequency Analysis",
    placeholder="Enter or paste text here..."
)

if st.button("Analyze Frequency"):

    if analysis_text.strip():

        frequency = frequency_analysis(analysis_text)

        if frequency:

            st.subheader("Letter Frequency")

            for letter, percentage in frequency.items():
                st.write(
                    f"**{letter}** → {percentage}%"
                )

        else:
            st.warning("No alphabetic characters found.")

    else:
        st.warning("Please enter text for analysis.")


# ---------------- Caesar Brute Force ----------------

st.divider()

st.header("🔓 Caesar Cipher Brute Force")

brute_text = st.text_input(
    "Enter Caesar Encrypted Text",
    placeholder="Example: KHOOR ZRUOG"
)

if st.button("Try All 26 Shifts"):

    if brute_text.strip():

        results = caesar_brute_force(brute_text)

        st.subheader("Possible Results")

        for shift, result in results:

            st.write(
                f"**Shift {shift}:** {result}"
            )

    else:
        st.warning("Please enter encrypted text.")


# ---------------- Footer ----------------

st.divider()

st.caption(
    "Classical Cryptography Analysis Tool | "
    "Developed using Python and Streamlit"
)
