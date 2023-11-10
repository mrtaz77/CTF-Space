import zipfile
import os
import base64

def decrypt_comment(encrypted):
    text = base64.b64decode(encrypted).decode('utf-8')
    result = ""
    for char in text:
        if char.isalpha():
            # Determine whether the character is uppercase or lowercase
            is_upper = char.isupper()
            
            # Perform the Rot13 decryption
            decrypted_char = chr((ord(char) - ord('A' if is_upper else 'a') + 13) % 26 + ord('A' if is_upper else 'a'))
            
            result += decrypted_char
        else:
            # If the character is not a letter, keep it unchanged
            result += char
    
    return result
        
def zip_comment(zip_filename):
    try:
        with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
            return zip_ref.comment.decode('utf-8') 
    except zipfile.BadZipFile:
        print(f"The file {zip_filename} is not a valid ZIP archive.")
        return ""


    
def extract_zip(zip_filename, extract_path, password):
    try:
        with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
            # Set the password for the ZIP file
            if len(password) > 0:
                zip_ref.setpassword(password.encode('utf-8'))

            # Extract the contents of the ZIP file to the specified path
            zip_ref.extractall(extract_path)
            
            # print(f"Successfully extracted {zip_filename} to {extract_path} and got {zip_ref.namelist()}")
            
            
            return zip_ref.namelist()
            
    except zipfile.BadZipFile:
        print(f"The file {zip_filename} is not a valid ZIP archive.")
        
        return ""
        
    except RuntimeError:
        print(f"Failed to extract {zip_filename} with the provided password.")
        
        return ""


if __name__ == "__main__":
    script_directory = os.path.dirname(os.path.abspath(__file__))
    zip_file = os.path.join(script_directory, "task copy.zip")
    
    extraction_path = os.path.join(script_directory, "output")
    
    out = ""
    
    while zip_file.endswith(".zip"):        
        comment = zip_comment(zip_file)
        
        if comment.endswith("}"):
            out += "Zip file : "+zip_file+"\n"
            out += "Flag : "+comment+"\n"
            break

        else:
            password = decrypt_comment(comment)
            new_zip = extract_zip(zip_file,extraction_path,password)
            out += "Zip file : "+zip_file+"\n"
            out += "Comment : "+comment+"\n"
            out += "Password : "+password+"\n"
            if not zip_file.endswith("task copy.zip"):
                os.remove(zip_file)
            zip_file = os.path.join(script_directory, "output\\")+new_zip[0]
    
    with open('log.txt', 'a') as file:
        file.write(out)
        
