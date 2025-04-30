# File Name : decrypt.py
# Student Name: Josh Slocumb
# email:slocumjt@mail.uc.edu
# Assignment Number: Final Project
# Due Date:  04/31/2025
# Course #/Section:   IS 4010-001
# Semester/Year:  Spring 2025
# Brief Description of the assignment: This assignment decrypts a campus meeting location and movie title then displays the team’s photo taken at that location.

# Brief Description of what this module does: this module decrypts the json file using a key to give our movie title
# Citations: Perplexity AI

import os
import json
from cryptography.fernet import Fernet

class MovieDecryptor:
    def __init__(self, data_folder="Data"):
        """
        Initialize the MovieDecryptor with necessary configuration.
        
        Args:
            data_folder (str): Path to data folder with encrypted files
        """
        self.data_folder = data_folder
        self.file_path = os.path.join(self.data_folder, 'TeamsAndEncryptedMessagesForDistribution.json')
        self.team_name = "Wilbur (Shooter) Flatch"  # Your actual team name
        self.encryption_key = "rXpDo6eLx3UfvlWp7bNJ5fLBt3uBhOdd56mtJAm6Eao="  # Provided by professor
        
    def load_team_data(self):
        """Load team data from JSON file."""
        with open(self.file_path, 'r') as file:
            data = json.load(file)
        return data

    def find_team_message(self, data):
        """Find team's encrypted message in loaded data."""
        return data.get(self.team_name)

    def validate_encrypted_message(self, message):
        """Validate and normalize the encrypted message format."""
        if not message:
            raise ValueError("No encrypted message found")
        if isinstance(message, list):
            if len(message) == 0:
                raise ValueError("Empty encrypted message list")
            return message[0]
        return message

    def is_valid_fernet_key(self):
        """Check if the encryption key is a valid Fernet key."""
        try:
            Fernet(self.encryption_key)
            return True
        except ValueError:
            return False

    def decrypt_movie_title(self, encrypted_message):
        """
        Decrypt the movie title using Fernet.
        
        Args:
            encrypted_message (str): Encrypted message string
            
        Returns:
            str: Decrypted movie title or None if failed
        """
        f = Fernet(self.encryption_key)
        try:
            decrypted_bytes = f.decrypt(encrypted_message.encode())
            return decrypted_bytes.decode()
        except Exception as e:
            print(f"Decryption error: {type(e).__name__} - {str(e)}")
            return None
    
    def get_movie_title(self):
        """
        Main method to get and decrypt the movie title.
        
        Returns:
            str: Decrypted movie title or None if failed
        """
        try:
            teams_data = self.load_team_data()
            encrypted_message = self.find_team_message(teams_data)
            
            if not encrypted_message:
                print(f"Team '{self.team_name}' not found in the JSON file or no message present.")
                return None
            elif not self.is_valid_fernet_key():
                print("Invalid Fernet key format. Please check the key provided by your professor.")
                return None
            else:
                processed_message = self.validate_encrypted_message(encrypted_message)
                movie_title = self.decrypt_movie_title(processed_message)
                if movie_title:
                    return movie_title
                else:
                    print("Decryption failed after structural fixes. Double-check your key and message.")
                    return None
        except FileNotFoundError:
            print(f"Error: JSON file not found at {self.file_path}. Check if:")
            print("1. The 'Data' folder exists in your project directory")
            print("2. The JSON file is inside the 'Data' folder")
            print("3. The file name is spelled exactly as 'TeamsAndEncryptedMessagesForDistribution.json'")
            return None
        except json.JSONDecodeError:
            print("Error: The file is not valid JSON. Check its contents.")
            return None
        except Exception as e:
            print(f"Unexpected error: {type(e).__name__} - {str(e)}")
            return None

