# Simple AI-based diagnosis and treatment system

def diagnose_and_treat(symptoms):
    # Convert to lowercase for easier matching
    symptoms = [s.lower() for s in symptoms]

    # Rule-based diagnosis
    if "fever" in symptoms and "cold" in symptoms and "cough" in symptoms:
        diagnosis = "Flu"
        treatment = [
            "Rest well and stay hydrated",
            "Take paracetamol for fever",
            "Use cough syrup like Benadryl",
            "Consult a doctor if symptoms persist"
        ]
    elif "cold" in symptoms and "sneezing" in symptoms:
        diagnosis = "Common Cold"
        treatment = [
            "Drink warm fluids",
            "Use decongestant nasal sprays",
            "Take antihistamines",
            "Get adequate rest"
        ]
    elif "fever" in symptoms and "body pain" in symptoms:
        diagnosis = "Viral Fever"
        treatment = [
            "Take paracetamol every 6 hours",
            "Drink electrolyte-rich fluids",
            "Avoid exertion",
            "Consult a doctor if fever exceeds 102°F"
        ]
    else:
        diagnosis = "Unknown"
        treatment = ["Consult a healthcare professional for accurate diagnosis."]

    return diagnosis, treatment

# Example input
user_symptoms = ["Fever", "Cold", "Cough"]
diagnosis, treatment = diagnose_and_treat(user_symptoms)

# Output result
print("Diagnosis:", diagnosis)
print("Suggested Treatment:")
for step in treatment:
    print("-", step)
