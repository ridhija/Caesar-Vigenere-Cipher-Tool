# Caesar and Vigenère Cipher Tool

A Python-based classical cryptography analysis tool developed as a cybersecurity/cryptography project.

## Features

- Caesar Cipher encryption
- Caesar Cipher decryption
- Vigenère Cipher encryption
- Vigenère Cipher decryption
- Letter frequency analysis
- Basic Caesar Cipher brute-force analysis using all 26 shifts
- Simple web interface using Streamlit

## Technologies Used

- Python
- Streamlit
- Classical Cryptography Concepts

## Project Structure

```
Caesar-Vigenere-Cipher-Tool/
├── app.py
├── caesar.py
├── vigenere.py
├── frequency_analysis.py
├── requirements.txt
└── README.md
```

## How to Run

1. Install Python 3.
2. Open a terminal in the project folder.
3. Install the required dependency:

```bash
python -m pip install -r requirements.txt
```

4. Start the Streamlit application:

```bash
streamlit run app.py
```

5. Open the local URL shown in the terminal, usually:

```
http://localhost:8501
```

## Example Tests

### Caesar Cipher
- Input: `HELLO WORLD`
- Shift: `3`
- Encrypted output: `KHOOR ZRUOG`

### Vigenère Cipher
- Input: `HELLO WORLD`
- Key: `KEY`
- Encrypted output: `RIJVS UYVJN`

## Purpose

The project demonstrates the implementation and practical testing of classical substitution and polyalphabetic ciphers, along with basic cryptanalysis techniques such as frequency analysis and Caesar brute force.

## Author

Ridhi Jain
