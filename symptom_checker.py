import datetime

"""
Medical Symptom Checker + Medication Guide
------------------------------------------
Author: Swasti Jain
Email: swasti1030@gmail.com

This program analyzes user-input symptoms, identifies possible medical conditions,
suggests medications, provides side effects, and can generate a printable report.

DISCLAIMER: This is for educational use only. Always consult a licensed healthcare provider.
"""

# --- Symptom-to-condition mapping ---
symptom_conditions = {
    "fever": ["Flu", "COVID-19", "Dengue"],
    "cough": ["Cold", "Flu", "COVID-19", "Bronchitis", "Pneumonia"],
    "headache": ["Migraine", "Tension Headache"],
    "fatigue": ["Anemia", "Hypothyroidism", "Depression"],
    "sore throat": ["Strep Throat", "Cold"],
    "nausea": ["Food Poisoning", "Stomach Flu"],
    "diarrhea": ["E. coli", "Salmonella", "Lactose Intolerance", "Rotavirus"],
    "rash": ["Allergic Reaction", "Eczema", "Ringworm", "Contact Dermatitis"],
    "bodyache": ["COVID-19", "Viral Infection", "Exhaustion"]
}

# --- Symptom-to-medications mapping ---
symptom_medications = {
    "fever": ["Tylenol", "Advil (Ibuprofen)", "Motrin"],
    "nausea": ["Pepto-Bismol", "Dramamine", "Emetrol"],
    "headache": ["Excedrin", "Tylenol", "Advil (Ibuprofen)"],
    "sore throat": ["Cepacol", "Chloraseptic", "Throat lozenges", "Honey-lemon tea"],
    "diarrhea": ["Loperamide", "Bismuth Subsalicylate", "Electrolyte solutions"],
    "rash": ["Hydrocortisone cream (1%)", "Calamine lotion", "Clotrimazole (antifungal cream)", "Oral antihistamines (Benadryl)"],
    "bodyache": ["Hydroxyurea", "Pantoprazole"]
}

# --- Medication side effects ---
medication_info = {
    "Tylenol": ["Liver damage if overdosed"],
    "Advil (Ibuprofen)": ["Stomach upset", "Kidney risk if long-term"],
    "Motrin": ["Stomach upset", "Dizziness"],
    "Pepto-Bismol": ["Black tongue", "Dark stool"],
    "Dramamine": ["Drowsiness", "Dry mouth"],
    "Emetrol": ["Upset stomach (rare)"],
    "Excedrin": ["Contains caffeine", "Can cause insomnia"],
    "Chloraseptic": ["Numbness in mouth", "Allergic reaction"],
    "Cepacol": ["Mouth dryness", "Tingling"],
    "Clotrimazole (antifungal cream)": ["Itching", "Mild burning"],
    "Hydrocortisone cream (1%)": ["Thinning skin if overused"],
    "Calamine lotion": ["Minimal side effects", "Dry skin"],
    "Oral antihistamines (Benadryl)": ["Drowsiness", "Dry mouth"],
    "Loperamide": ["Constipation", "Abdominal cramps"],
    "Bismuth Subsalicylate": ["Black stool", "Reye’s syndrome risk in kids"],
    "Electrolyte solutions": ["None if taken correctly"],
    "Throat lozenges": ["Mild numbness", "Sugar content"],
    "Hydroxyurea": ["Black nails", "Constipation"],
    "Pantoprazole": ["Headache", "Bloating", "Vitamin B12 deficiency (long-term use)"]
}

# --- Symptom matcher ---
def match_symptoms(user_input):
    input_lower = user_input.lower()
    return [symptom for symptom in symptom_conditions if symptom in input_lower]

# --- Show and optionally save results ---
def show_results(symptoms, user_input):
    if not symptoms:
        print("\n❌ No matching symptoms found in our database.")
        print("🧑‍⚕️ Please consult a licensed medical professional.\n")
        return ""

    report_lines = []
    report_lines.append("SYMPTOM CHECKER REPORT")
    report_lines.append(f"User Input: {user_input}")
    report_lines.append(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report_lines.append("")

    for symptom in symptoms:
        report_lines.append(f"🩺 Symptom Detected: {symptom.capitalize()}")
        report_lines.append("🔍 Possible Conditions:")
        for cond in symptom_conditions[symptom]:
            report_lines.append(f"  - {cond}")

        report_lines.append("💊 Suggested Medications:")
        for med in symptom_medications.get(symptom, []):
            report_lines.append(f"  - {med}")
            side_fx = medication_info.get(med, ["No known side effects"])
            report_lines.append(f"     ⚠️ Side Effects: {', '.join(side_fx)}")

        report_lines.append("")

    report_lines.append("⚠️ DISCLAIMER:")
    report_lines.append("This tool is for educational use only.")
    report_lines.append("It is not a substitute for professional medical advice, diagnosis, or treatment.")
    report_lines.append("Please consult a doctor or pharmacist before taking any medications.")

    # Print to console
    print("\n" + "\n".join(report_lines))

    # Ask to save report
    save = input("\nWould you like to save this report? (yes/no): ").strip().lower()
    if save == "yes":
        filename = f"symptom_report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, "w") as file:
            file.write("\n".join(report_lines))
        print(f"✅ Report saved as '{filename}'")

# --- Main app runner ---
def main():
    print("🩺 Welcome to the Medical Symptom Checker + Medication Guide")
    user_input = input("\nPlease describe your symptoms (e.g., 'I have a fever and nausea'): ")
    matched = match_symptoms(user_input)
    show_results(matched, user_input)

# --- Execute ---
if __name__ == "__main__":
    main()
