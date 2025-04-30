# File Name : location.py
# Student Name: Caitlin Hutchins
# email:hutchicu@mail.uc.edu
# Assignment Number: Final Project
# Due Date:  04/31/2025
# Course #/Section:   IS 4010-001
# Semester/Year:  Spring 2025
# Brief Description of the assignment: This assignment decrypts a campus meeting location and movie title then displays the team’s photo taken at that location.

# Brief Description of what this module does: this module decrypts the location for the group, Armstrong Exhibit
# Citations: Perplexity AI
import os
import json

class LocationDecryptor:
    def __init__(self, data_folder="Data", team_name="Wilbur (Shooter) Flatch"):
        """
        Initialize the LocationDecryptor with data folder and team name.
        
        Args:
            data_folder (str): Path to data folder containing encrypted files
            team_name (str): Name of the team to find location data for
        """
        self.data_folder = data_folder
        self.team_name = team_name
        self.encrypted_file = os.path.join(self.data_folder, "EncryptedGroupHints Spring 2025.json")
        self.english_file = os.path.join(self.data_folder, "UCEnglish.txt")  # Corrected path
            
    def load_encrypted_data(self):
        """Load encrypted data from JSON file."""
        try:
            with open(self.encrypted_file, 'r') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print(f"Error: Encrypted hints file not found at {self.encrypted_file}")
            return None
        except json.JSONDecodeError:
            print("Error: The encrypted hints file is not valid JSON.")
            return None
            
    def get_team_encrypted_location(self, encrypted_data):
        """Extract team-specific encrypted location data."""
        if self.team_name in encrypted_data:
            return encrypted_data[self.team_name]
        print(f"Team '{self.team_name}' not found in the encrypted data.")
        return None
    
    def load_english_file(self):
        """Load the UCEnglish.txt file."""
        try:
            with open(self.english_file, 'r', encoding='utf-8') as file:
                lines = file.readlines()
            return [line.strip() for line in lines]
        except FileNotFoundError:
            print(f"Error: English file not found at {self.english_file}")
            return None
            
    def decrypt_location(self, encrypted_indices, english_words):
        """
        Decrypt location using indices into english words.
        
        Args:
            encrypted_indices (list): List of indices (as strings)
            english_words (list): List of words from UCEnglish.txt
            
        Returns:
            str: Decrypted location text
        """
        if not encrypted_indices or not english_words:
            return None
            
        decrypted_location = []
        for index_str in encrypted_indices:
            try:
                index = int(index_str)
                if 0 <= index < len(english_words):
                    decrypted_location.append(english_words[index])
                else:
                    print(f"Index {index} is out of range for the English words file.")
            except ValueError:
                print(f"Invalid index value: {index_str}")
                
        return " ".join(decrypted_location)
        
    def get_location(self):
        """
        Main method to retrieve and decrypt location.
        
        Returns:
            str: Decrypted location or None if failed
        """
        encrypted_data = self.load_encrypted_data()
        if not encrypted_data:
            return None
            
        encrypted_indices = self.get_team_encrypted_location(encrypted_data)
        if not encrypted_indices:
            return None
            
        english_words = self.load_english_file()
        if not english_words:
            return None
            
        location = self.decrypt_location(encrypted_indices, english_words)
        return location
