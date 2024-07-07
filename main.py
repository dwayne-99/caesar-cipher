# The list contains the alphabet twice so that letters at the end of the list are accounted for
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# Get the users inputs (encode or decode, text, amount to shift by)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# Define caeser function and intialize an empty string of text to store the text output
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  
  # If direction is decode multiply the shift amount by -1 to shift in the oppsoite direction  
  if cipher_direction == "decode":
      shift_amount *= -1
    
  # Find the position of the current character in the alphabet list if the user input is a letter of the alphabet
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)

      # Calculate the new position by adding the shift amount to the current position
      new_position = position + shift_amount

      # Append the letter at the new position to the end_text string      
      end_text += alphabet[new_position]

    # Append the actual character the user inputs to the end_text string    
    else:
      end_text += char
      
  print(f"Here's the {direction}d result: {end_text}")

caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
