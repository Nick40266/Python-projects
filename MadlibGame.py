# In this game students are supposed to guess words without context.
# They will only know if a particular word is a noun, or whatever and thats it
import re
with open("story.txt", "r") as f:
    story = f.read()

# Make a copy to modify
modified_story = story

# Find all placeholders like <noun1>, <verb2>, etc
placeholder_list = re.findall(r"<.+?>", story)
for placeholder in placeholder_list:
    word = input(f"Guess the suitable word ({placeholder.strip("<>")}): ")
# Apply replacement to the CURRENT version of the text    
    modified_story = re.sub(placeholder, word, modified_story)    

print(modified_story)