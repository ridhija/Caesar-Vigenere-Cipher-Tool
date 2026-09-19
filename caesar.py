def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char

    return result


def caesar_brute_force(text):
    results = []

    for shift in range(26):
        decrypted = caesar_encrypt(text, -shift)
        results.append((shift, decrypted))

    return results


# Run this section only when caesar.py is executed directly
if __name__ == "__main__":
    text = input("Enter text: ")
    shift = int(input("Enter shift value: "))

    encrypted_text = caesar_encrypt(text, shift)

    print("Encrypted text:", encrypted_text)
