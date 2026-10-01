from PIL import Image
import os

def reverse_dict(i_dict):
    return {v: k for k, v in i_dict.items()}

def encrypt(text, i_dict):
    r_dict = reverse_dict(i_dict)
    encrypted_text = ""
    for char in text.upper():
        if char in r_dict:
            encrypted_text += str(r_dict[char]) + ' '
        else:
            encrypted_text += char + " "
    return encrypted_text.strip() 

def decrypt(text, i_dict):
    decrypted_text = ""
    for char in text:
        if char in i_dict:
            decrypted_text += i_dict[char]
        elif char == ' ':
            decrypted_text += char
        else:
            continue
    return decrypted_text.strip()

def order_dict(text, i_dict):
    remaining_values = list(i_dict.values())
    ordered = []
    for char in text.upper():
        if char in remaining_values:
            ordered.append(char)
            remaining_values.remove(char.upper())

    new_values = ordered + remaining_values
    new_dict = dict(enumerate(new_values))
    return new_dict

def encrypt_to_image(text, cipher_dict, output_file, symbol_folder=None):
    # Reverse dictionary so letters map to numbers
    reverse = {v: k for k, v in cipher_dict.items()}

    images = []

    for char in text.upper():
        if char in reverse:
            file_name = f"{reverse[char]}.jpg"

            if symbol_folder is not None:
                file_name = os.path.join(symbol_folder, file_name)

            images.append(Image.open(file_name))

        elif char == " ":
            images.append(None)

    if not any(images):
        print("No valid symbols found.")
        return
    
    # Determine dimensions
    symbol_width = max(img.width for img in images if img)
    symbol_height = max(img.height for img in images if img)

    spacer = 10

    total_width = 0
    for img in images:
        if img:
            total_width += img.width + spacer
        else:
            total_width += symbol_width

    output = Image.new(
        "RGB",
        (total_width, symbol_height),
        "white"
    )

    x = 0

    for img in images:
        if img:
            output.paste(img, (x, 0))
            x += img.width + spacer
        else:
            x += symbol_width

    output.save(output_file)
    print(f"Saved: {output_file}")

base_dict = { 0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z' }
encrypted_dict = order_dict(msg, base_dict)

msg = "Hello World"
encrypted_msg = encrypt(msg, encrypted_dict)  # Encrypted Message:  0 1 2 2 3   4 3 5 2 6
encrypt_to_image(encrypted_msg, encrypted_dict, "encypted_image.jpg", "symbols")
