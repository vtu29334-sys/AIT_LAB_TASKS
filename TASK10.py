# --- Input: Predefined facts within the program ---
facts_database = {
    "the sun produces heat.": "VERIFIED (True)",
    "rain comes from clouds.": "VERIFIED",
    "snow is hot.": "INCORRECT (False)",
    "clouds contain water droplets.": "VERIFIED (True)"
}

statements_to_check = [
    "the sun produces heat.",
    "rain comes from clouds.",
    "snow is hot.",
    "clouds contain water droplets."
]

# --- Output: Weather Fact Verification System ---
print("WEATHER FACT VERIFICATION SYSTEM\n")

for statement in statements_to_check:
    # Normalize the statement to handle potential case mismatches gently
    lookup_key = statement.strip().lower()
    
    # Check against database and print the exact required formatting
    if lookup_key in facts_database:
        status = facts_database[lookup_key]
        print(f"Statement : {statement}")
        print(f"Status    : {status}\n")
