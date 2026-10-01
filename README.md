Pigpen Cipher Image Encoder
A Python implementation of a Pigpen-inspired cipher that supports:

Traditional text encryption and decryption
Keyword-based cipher alphabet generation
Conversion of encrypted messages into images using custom symbol sets
User-defined symbol mappings for all 26 letters of the alphabet
What is a Pigpen Cipher?
The Pigpen Cipher is a simple substitution cipher that replaces letters with geometric symbols rather than standard text characters.

Historically, the cipher uses a collection of grid and X-shaped patterns with optional dots to represent letters of the alphabet.

For example:

A → ⌜
B → ⊓
C → ⌝
...
Because the cipher uses symbols instead of letters, messages appear as drawings rather than readable text.

This project takes a modernized approach by:

Assigning each letter a numeric index.
Generating a keyed alphabet based on a keyword or phrase.
Mapping each index to a custom image file.
Producing an image containing the encrypted symbols.
Features
Basic Encryption
Convert plaintext into a sequence of cipher indexes.

Example:

HELLO WORLD

↓

0 1 2 2 3 4 3 5 2 6
Basic Decryption
Convert a sequence of cipher indexes back into readable text.

Keyword-Based Cipher Generation
A custom cipher alphabet can be generated from a word or phrase.

Example:

Keyword:
HELLO WORLD
Generated alphabet:

H E L O W R D A B C F G I J K M N P Q S T U V X Y Z
Resulting dictionary:

{
    0:'H',
    1:'E',
    2:'L',
    3:'O',
    4:'W',
    5:'R',
    6:'D',
    7:'A',
    ...
}
This makes every encrypted message dependent on the selected keyword.

Image-Based Encryption
Instead of displaying numbers, encrypted values can be represented using image files.

Example:

0.jpg
1.jpg
2.jpg
...
25.jpg
The program loads the corresponding image for each encrypted character and combines them into a single encrypted image.

Requirements
pip install pillow
Required imports:

from PIL import Image
import os
Project Structure
Option 1: Images in the Same Directory
project/
│
├── cipher.py
├── 0.jpg
├── 1.jpg
├── 2.jpg
├── ...
└── 25.jpg
Usage:

encrypt_to_image(
    encrypted_msg,
    encrypted_dict,
    "encrypted_image.jpg"
)
Option 2: Images in a Subfolder
project/
│
├── cipher.py
│
└── symbols/
    ├── 0.jpg
    ├── 1.jpg
    ├── 2.jpg
    ├── ...
    └── 25.jpg
Usage:

encrypt_to_image(
    encrypted_msg,
    encrypted_dict,
    "encrypted_image.jpg",
    "symbols"
)
Example
Create a base alphabet:

base_dict = {
    0:'A', 1:'B', 2:'C', 3:'D', 4:'E',
    5:'F', 6:'G', 7:'H', 8:'I', 9:'J',
    10:'K', 11:'L', 12:'M', 13:'N',
    14:'O', 15:'P', 16:'Q', 17:'R',
    18:'S', 19:'T', 20:'U', 21:'V',
    22:'W', 23:'X', 24:'Y', 25:'Z'
}
Generate a keyword cipher:

msg = "Hello World"

encrypted_dict = order_dict(
    msg,
    base_dict
)
Encrypt the message:

encrypted_msg = encrypt(
    msg,
    encrypted_dict
)

print(encrypted_msg)
Output:

0 1 2 2 3 4 3 5 2 6
Create an encrypted image:

encrypt_to_image(
    encrypted_msg,
    encrypted_dict,
    "encrypted_image.jpg",
    "symbols"
)
Output:

Saved: encrypted_image.jpg
Functions
reverse_dict()
Creates a reversed version of a dictionary.

reverse_dict(i_dict)
Example:

{
    0:'A'
}
becomes:

{
    'A':0
}
encrypt()
Encrypts plaintext using a cipher dictionary.

encrypt(text, i_dict)
decrypt()
Decrypts text using a cipher dictionary.

decrypt(text, i_dict)
order_dict()
Generates a keyword-based cipher alphabet.

order_dict(keyword, i_dict)
Duplicate letters are removed automatically while preserving order.

encrypt_to_image()
Converts encrypted output into a composite image made from symbol files.

encrypt_to_image(
    text,
    cipher_dict,
    output_file,
    symbol_folder=None
)
Arguments:

Parameter	Description
text	Message to encrypt
cipher_dict	Cipher alphabet dictionary
output_file	Output image filename
symbol_folder	Optional folder containing symbol images
Future Improvements
Potential enhancements include:

Graphical user interface (Tkinter)
Multi-line encrypted output
PNG transparency support
Image decryption using OCR or symbol recognition
Multiple Pigpen alphabet styles
Save and load custom cipher keys
Random cipher generation
License
This project is provided for educational purposes and experimentation with classical substitution ciphers.
