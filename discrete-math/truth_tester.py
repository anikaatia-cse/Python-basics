# --- STEP 1: Set up my true or false facts ---
i_study_hard = True
i_get_4_cgpa = True

# --- STEP 2: Let the computer check the math rules ---

# Rule 1: The AND rule (Both things must happen)
and_result = i_study_hard and i_get_4_cgpa

# Rule 2: The OR rule (At least one thing must happen)
or_result = i_study_hard or i_get_4_cgpa

# Rule 3: The NOT rule (Flip the truth)
not_result = not i_study_hard


# --- STEP 3: Print the answers on the screen ---
print("Did both happen?")
print(and_result)

print("Did at least one happen?")
print(or_result)

print("What is the opposite of studying hard?")
print(not_result)