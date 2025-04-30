

# File Name : main.py
# Student Name: Derick Bellofatto
# email:  Bellofdk@mail.uc.edu
# Assignment Number: Final Exam
# Due Date:   5/1/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  Decrypt a campus location and movie title, and display a team photo with a quote.

# Brief Description of what this module does. This module calls all functions and serves as the main entry point for the project.
# Citations: https://www.perplexity.ai/ - Perplexity AI

# Anything else that's relevant:

from locationPackage.location import LocationDecryptor
from decryptionPackage.decrypt import MovieDecryptor
from picturePackage.picture import PictureViewer
import os

def main():
    """
    Main entry point that orchestrates the complete project workflow:
    1. Decrypt the campus location
    2. Decrypt the movie title
    3. Display the team photo
    """
    print("===== UC Campus Location and Movie Decryption System =====\n")
    
    # Step 1-2: Decrypt location
    print("Decrypting campus location...")
    location_decryptor = LocationDecryptor()
    decrypted_location = location_decryptor.get_location()
    
    if decrypted_location:
        print(f"\nDecrypted Location: {decrypted_location}")
    else:
        print("Failed to decrypt the location.")
    
    # Step 3-4: Decrypt movie title
    print("\nDecrypting movie title...")
    movie_decryptor = MovieDecryptor()
    movie_title = movie_decryptor.get_movie_title()
    
    if movie_title:
        print(f"\nYour team's movie is: {movie_title}")
        
    else:
        print("Failed to decrypt the movie title.")
    
    # Step 6: Display the group photo
    print("\nDisplaying team photo with famous quote...")
    picture_viewer = PictureViewer()
    
    # Update this path with your actual team photo filename
    # Assuming your photo is stored in the Data folder
    picture_path = os.path.join("Data", "team_photo.jpg")
    picture_viewer.set_picture_path(picture_path)
    
    if not picture_viewer.load_and_display_photo():
        print("Failed to display the team photo.")
    
    print("\n===== Project Execution Complete =====")

if __name__ == "__main__":
    main()
