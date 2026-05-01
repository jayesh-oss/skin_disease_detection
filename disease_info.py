"""
Disease information knowledge base for the Skin Disease Detection system.
Contains detailed medical information for each detectable condition.
NOTE: This information is for educational purposes only and is NOT a substitute
for professional medical advice, diagnosis, or treatment.
"""

DISEASE_DATA = {
    "Eczema": {
        "full_name": "Eczema (Atopic Dermatitis)",
        "description": (
            "Eczema, also known as atopic dermatitis, is a chronic inflammatory skin condition "
            "that causes the skin to become red, itchy, and inflamed. It commonly appears in "
            "childhood but can occur at any age. Eczema is not contagious and is often linked "
            "to an overactive immune system response to environmental triggers. The condition "
            "tends to flare up periodically and may be accompanied by asthma or hay fever."
        ),
        "symptoms": [
            "Dry, scaly, or cracked skin",
            "Intense itching, especially at night",
            "Red or brownish-gray patches on the skin",
            "Small, raised bumps that may leak fluid when scratched",
            "Thickened or leathery skin from repeated scratching",
            "Raw, sensitive, or swollen skin",
        ],
        "treatment": [
            "Moisturizers & emollients — Apply fragrance-free moisturizers frequently to keep skin hydrated",
            "Topical corticosteroids — Prescription anti-inflammatory creams to reduce flare-ups",
            "Antihistamines — Over-the-counter medications to help control itching",
            "Calcineurin inhibitors — Non-steroid prescription creams (e.g., tacrolimus, pimecrolimus)",
            "Phototherapy (light therapy) — Controlled UV exposure under medical supervision",
            "Wet wrap therapy — Applying wet bandages over affected areas to soothe severe flare-ups",
        ],
        "prevention": [
            "Keep your skin well-moisturized daily, especially after bathing",
            "Identify and avoid personal triggers (certain fabrics, soaps, allergens, stress)",
            "Use mild, fragrance-free soaps and detergents",
            "Take lukewarm (not hot) baths and showers",
            "Wear soft, breathable fabrics like cotton",
            "Manage stress through relaxation techniques",
            "Use a humidifier in dry environments",
        ],
        "severity": "Moderate",
        "severity_description": "Manageable with proper skincare and medical treatment",
        "consult_urgency": "recommended",
        "consult_message": (
            "We recommend scheduling an appointment with a dermatologist for a thorough "
            "evaluation. A specialist can help identify your specific triggers, prescribe "
            "appropriate treatment, and create a personalized management plan to control "
            "flare-ups and improve your quality of life."
        ),
    },

    "Melanoma": {
        "full_name": "Melanoma (Malignant Skin Cancer)",
        "description": (
            "Melanoma is the most serious and potentially life-threatening type of skin cancer. "
            "It develops in the melanocytes — the cells that produce melanin, the pigment that "
            "gives skin its color. Melanoma can develop anywhere on the body, including areas "
            "not normally exposed to sunlight. While less common than other types of skin cancer, "
            "melanoma is far more dangerous because of its ability to spread (metastasize) to "
            "other parts of the body if not detected and treated early."
        ),
        "symptoms": [
            "A new, unusual growth or mole on the skin",
            "A change in an existing mole (size, shape, color, or texture)",
            "A mole that is asymmetrical — one half doesn't match the other",
            "Irregular, ragged, or blurred borders on a mole",
            "Uneven color distribution (shades of brown, black, red, white, or blue)",
            "A mole larger than 6mm in diameter (about the size of a pencil eraser)",
            "Itching, tenderness, or bleeding from a mole",
        ],
        "treatment": [
            "Surgical excision — Primary treatment to remove the melanoma and surrounding tissue",
            "Sentinel lymph node biopsy — To determine if the cancer has spread to lymph nodes",
            "Immunotherapy — Drugs that boost the immune system to fight cancer cells",
            "Targeted therapy — Medications targeting specific genetic mutations in melanoma cells",
            "Radiation therapy — Used in some cases to target remaining cancer cells",
            "Chemotherapy — May be used for advanced-stage melanoma",
        ],
        "prevention": [
            "Apply broad-spectrum sunscreen (SPF 30+) daily and reapply every 2 hours",
            "Avoid prolonged sun exposure, especially between 10 AM and 4 PM",
            "Wear protective clothing, wide-brimmed hats, and UV-blocking sunglasses",
            "Avoid tanning beds and artificial UV exposure completely",
            "Perform monthly self-examinations of your skin for new or changing moles",
            "Schedule annual skin check-ups with a dermatologist",
            "Follow the ABCDE rule: Asymmetry, Border, Color, Diameter, Evolving",
        ],
        "severity": "Serious",
        "severity_description": "Early detection is critical — seek immediate medical attention",
        "consult_urgency": "urgent",
        "consult_message": (
            "⚠️ URGENT: This analysis suggests a possible melanoma. Please seek medical "
            "attention as soon as possible. Early detection and treatment of melanoma "
            "significantly improves outcomes. Contact a dermatologist or visit a skin cancer "
            "specialist immediately for a professional biopsy and clinical evaluation. "
            "Do NOT delay — early-stage melanoma is highly treatable."
        ),
    },

    "Psoriasis": {
        "full_name": "Psoriasis (Chronic Autoimmune Condition)",
        "description": (
            "Psoriasis is a chronic autoimmune condition that causes the rapid buildup of skin "
            "cells, leading to thick, silvery-white scales and dry, red patches that can be "
            "itchy and sometimes painful. It occurs when the immune system mistakenly attacks "
            "healthy skin cells, accelerating their growth cycle from weeks to just days. "
            "Psoriasis is not contagious and tends to go through cycles, flaring for weeks or "
            "months and then subsiding. It can affect any part of the body but commonly appears "
            "on the scalp, elbows, knees, and lower back."
        ),
        "symptoms": [
            "Red patches of skin covered with thick, silvery scales",
            "Dry, cracked skin that may bleed or itch",
            "Soreness, burning, or itching around affected areas",
            "Thickened, pitted, or ridged nails",
            "Stiff and swollen joints (psoriatic arthritis)",
            "Small scaling spots (commonly seen in children)",
        ],
        "treatment": [
            "Topical treatments — Corticosteroid creams, vitamin D analogues, and retinoids",
            "Phototherapy — Controlled UVB or PUVA light therapy under medical supervision",
            "Systemic medications — Oral or injected medications for moderate to severe cases",
            "Biologic agents — Advanced injectable drugs targeting specific parts of the immune system",
            "Salicylic acid — Helps reduce scaling and smooth the skin",
            "Coal tar preparations — Reduce itching, scaling, and inflammation",
        ],
        "prevention": [
            "Manage stress levels through meditation, exercise, or counseling",
            "Avoid skin injuries (cuts, scrapes, sunburns) — they can trigger new patches",
            "Limit alcohol consumption, which can worsen symptoms",
            "Quit smoking — tobacco can increase severity and frequency of flare-ups",
            "Keep skin moisturized to prevent dryness and cracking",
            "Follow your treatment plan consistently, even during remission periods",
            "Maintain a healthy diet rich in anti-inflammatory foods",
        ],
        "severity": "Moderate",
        "severity_description": "Chronic condition requiring ongoing management",
        "consult_urgency": "recommended",
        "consult_message": (
            "We recommend consulting a dermatologist for a comprehensive evaluation and "
            "personalized treatment plan. Psoriasis management has advanced significantly "
            "with modern treatments including biologics. A specialist can determine the type "
            "and severity of your psoriasis and recommend the most effective therapy, helping "
            "you achieve clearer skin and better quality of life."
        ),
    },
}


def get_disease_info(disease_name):
    """
    Retrieve disease information by name.
    Returns the disease data dict or a default 'unknown' entry.
    """
    return DISEASE_DATA.get(disease_name, {
        "full_name": disease_name,
        "description": "No detailed information is available for this condition at this time.",
        "symptoms": [],
        "treatment": [],
        "prevention": [],
        "severity": "Unknown",
        "severity_description": "Please consult a healthcare professional for evaluation",
        "consult_urgency": "recommended",
        "consult_message": (
            "We recommend scheduling an appointment with a dermatologist for a "
            "professional diagnosis and personalized treatment plan."
        ),
    })
