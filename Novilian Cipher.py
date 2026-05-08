import sys

def transform_text(text, encrypt=True):
    result = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for index, char in enumerate(text.lower()):
        if char in alphabet:
            word_pos = index + 1
            shift = word_pos * word_pos
            
            current_idx = alphabet.find(char)
            
            if encrypt:
                new_idx = (current_idx + shift) % 26
            else:
                new_idx = (current_idx - shift) % 26
                
            result += alphabet[new_idx]
        else:
            result += char
    return result

def main():
    print("--- Positional Multiplier Cipher ---")
    
    while True:
        print("\nChoose an option:")
        print("1. Encrypt text")
        print("2. Decrypt text")
        print("3. Exit")
        
        choice = input("\nSelection (1/2/3): ")
        
        if choice == '3':
            print("Goodbye!")
            break
            
        if choice in ['1', '2']:
            phrase = input("Enter your message: ")
            is_encrypting = (choice == '1')
            
            output = transform_text(phrase, encrypt=is_encrypting)
            
            label = "Encrypted" if is_encrypting else "Decrypted"
            print(f"\n{label} Result: {output}")
            print("-" * 30)
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
