#Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file
import json

indian_states = {
    "Andhra Pradesh": "Hyderabad",
    "Bihar": "Patna",
    "Gujarat": "Gandhinagar",
    "Karnataka": "Bengaluru",
    "Maharashtra": "Mumbai",
    "Rajasthan": "Jaipur",
    "Tamil Nadu": "Chennai"
}

filename = "indian_states_and_capitals.json"
with open(filename, "w") as file:
    json.dump(indian_states, file, indent=4)

print("The data has been sucessfully written to:",filename)