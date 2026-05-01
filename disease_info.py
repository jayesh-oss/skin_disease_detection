"""
Disease information knowledge base for the Skin Disease Detection system.
Contains detailed medical information for each detectable condition.
NOTE: This information is for educational purposes only and is NOT a substitute
for professional medical advice, diagnosis, or treatment.
"""

DISEASE_DATA = {
    "Nail_psoriasis": {
        "full_name": "Nail Psoriasis",
        "description": (
            "Nail psoriasis is an autoimmune condition that alters the way fingernails and toenails grow. "
            "It is closely related to psoriasis of the skin. It causes cells in the nails to multiply too quickly, "
            "leading to a buildup of cells under the nail, pitting on the surface, and changes in the nail's shape, "
            "thickness, and color. It is not a fungal infection and is not contagious."
        ),
        "symptoms": [
            "Tiny dents or pits on the surface of the nail",
            "Yellow or brown discoloration (oil drop spots)",
            "Nails separating from the nail bed (onycholysis)",
            "Chalky white buildup under the nail (subungual hyperkeratosis)",
            "Crumbling or thickening of the nail",
        ],
        "treatment": [
            "Topical treatments — Corticosteroids or vitamin D analogues applied to the nail bed",
            "Corticosteroid injections directly into the nail matrix",
            "Phototherapy — Targeted light therapy",
            "Systemic medications or biologics for severe or widespread cases",
            "Laser therapy to treat affected blood vessels",
        ],
        "prevention": [
            "Keep nails trimmed extremely short to prevent lifting and trauma",
            "Wear gloves when cleaning or doing manual labor",
            "Moisturize nails and cuticles daily",
            "Avoid aggressively cleaning under the nails",
            "Do not bite or pick at nails or cuticles",
        ],
        "severity": "Moderate",
        "severity_description": "Can cause discomfort and cosmetic concern but is highly manageable.",
        "consult_urgency": "recommended",
        "consult_message": (
            "We recommend consulting a dermatologist. Nail psoriasis can mimic fungal infections, "
            "so a professional diagnosis is important. A dermatologist can prescribe targeted treatments "
            "that are much more effective than over-the-counter options."
        ),
    },

    "SJS-TEN": {
        "full_name": "Stevens-Johnson Syndrome / Toxic Epidermal Necrolysis",
        "description": (
            "Stevens-Johnson Syndrome (SJS) and Toxic Epidermal Necrolysis (TEN) are rare, severe, and "
            "life-threatening skin reactions. They are typically triggered by an unpredictable adverse "
            "reaction to certain medications. The condition causes the epidermis (the outer layer of skin) "
            "to separate from the dermis, resulting in extensive blistering and peeling. SJS involves less "
            "than 10% of the body surface area, while TEN involves more than 30%."
        ),
        "symptoms": [
            "Widespread skin pain and tenderness",
            "A red or purplish rash that spreads quickly",
            "Large blisters on the skin and mucous membranes (mouth, nose, eyes, genitals)",
            "Shedding or peeling of skin in large sheets",
            "Flu-like symptoms (fever, sore throat, fatigue) preceding the rash",
            "Severe eye irritation, sensitivity to light, and swelling",
        ],
        "treatment": [
            "Immediate hospitalization, often in an intensive care or burn unit",
            "Discontinuation of the suspected trigger medication",
            "Intravenous fluids and electrolytes to replace lost fluids",
            "Pain management and wound care (similar to severe burn treatment)",
            "Systemic immunosuppressants or intravenous immunoglobulin (IVIG)",
        ],
        "prevention": [
            "Strictly avoid medications that have previously caused a severe allergic reaction",
            "Inform all healthcare providers of your medical allergy history",
            "Wear a medical alert bracelet indicating severe drug allergies",
            "Genetic testing (e.g., HLA-B*1502) before starting certain high-risk medications",
        ],
        "severity": "Critical",
        "severity_description": "A severe, life-threatening medical emergency requiring immediate hospitalization.",
        "consult_urgency": "urgent",
        "consult_message": (
            "⚠️ URGENT MEDICAL EMERGENCY: This analysis suggests a high risk for SJS/TEN. "
            "Stop taking any new medications immediately and GO TO THE NEAREST EMERGENCY ROOM. "
            "This is a life-threatening condition that requires immediate intensive care. "
            "Do NOT wait for a standard dermatology appointment."
        ),
    },

    "Vitiligo": {
        "full_name": "Vitiligo",
        "description": (
            "Vitiligo is a long-term autoimmune disorder in which patches of skin lose their pigment (color). "
            "It occurs when the immune system mistakenly attacks and destroys melanocytes—the cells responsible "
            "for producing skin pigment. The condition can affect any part of the body, including the inside "
            "of the mouth and hair. It is not contagious, life-threatening, or painful, but it can cause "
            "significant psychological distress."
        ),
        "symptoms": [
            "Patchy loss of skin color, which usually first appears on the hands, face, and areas around body openings",
            "Premature whitening or graying of the hair on the scalp, eyelashes, eyebrows, or beard",
            "Loss of color in the tissues that line the inside of the mouth and nose",
            "Symmetrical or asymmetrical depigmentation patterns",
        ],
        "treatment": [
            "Topical corticosteroids or calcineurin inhibitors to reduce inflammation and encourage repigmentation",
            "Phototherapy (Narrowband UVB) — highly effective for restoring pigment",
            "Excimer laser therapy for small, targeted areas",
            "Depigmentation therapy (lightening unaffected skin to match) for extensive cases",
            "Micropigmentation (medical tattooing) for small patches",
            "Surgical skin grafting in stable, non-spreading cases",
        ],
        "prevention": [
            "Vitiligo cannot be prevented as it is an autoimmune condition",
            "Protect affected areas from severe sunburn using high-SPF sunscreen, as depigmented skin burns easily",
            "Avoid skin trauma (cuts, severe sunburns), which can trigger new patches (Koebner phenomenon)",
        ],
        "severity": "Mild",
        "severity_description": "Non-life-threatening autoimmune condition affecting skin pigmentation.",
        "consult_urgency": "recommended",
        "consult_message": (
            "We recommend scheduling an appointment with a dermatologist. Early treatment "
            "often yields the best results for halting pigment loss and encouraging repigmentation. "
            "A specialist can discuss medical, surgical, and cosmetic options tailored to your needs."
        ),
    },

    "acne": {
        "full_name": "Acne Vulgaris",
        "description": (
            "Acne is a highly common skin condition that occurs when hair follicles become plugged with "
            "oil (sebum) and dead skin cells. This creates an environment where bacteria can thrive, "
            "leading to inflammation. It most commonly appears on the face, forehead, chest, upper back, "
            "and shoulders. While most common in teenagers due to hormonal changes, it can affect people "
            "of all ages."
        ),
        "symptoms": [
            "Whiteheads (closed plugged pores)",
            "Blackheads (open plugged pores)",
            "Small red, tender bumps (papules)",
            "Pimples (pustules), which are papules with pus at their tips",
            "Large, solid, painful lumps under the skin (nodules)",
            "Painful, pus-filled lumps under the skin (cystic lesions)",
        ],
        "treatment": [
            "Over-the-counter topical treatments (Salicylic acid, Benzoyl peroxide)",
            "Prescription topical retinoids (e.g., Tretinoin, Adapalene)",
            "Topical or oral antibiotics to reduce bacteria and inflammation",
            "Hormonal therapies (for female patients)",
            "Oral isotretinoin for severe, cystic, or treatment-resistant acne",
            "Light therapy or chemical peels",
        ],
        "prevention": [
            "Wash your face twice daily with a gentle, non-comedogenic cleanser",
            "Avoid scrubbing the skin aggressively, which can worsen inflammation",
            "Use oil-free, non-comedogenic makeup and moisturizers",
            "Always remove makeup before going to sleep",
            "Avoid picking, popping, or squeezing pimples to prevent scarring and infection",
            "Shower after heavy sweating",
        ],
        "severity": "Mild to Moderate",
        "severity_description": "Common condition ranging from mild breakouts to severe painful cysts.",
        "consult_urgency": "recommended",
        "consult_message": (
            "If over-the-counter products haven't cleared your acne, or if you have painful cysts "
            "or are developing scars, we recommend consulting a dermatologist. Prescription "
            "treatments are highly effective and can prevent permanent skin damage."
        ),
    },

    "hyperpigmentation": {
        "full_name": "Hyperpigmentation",
        "description": (
            "Hyperpigmentation is a common, usually harmless condition in which patches of skin become "
            "darker in color than the normal surrounding skin. This darkening occurs when an excess of "
            "melanin, the brown pigment that produces normal skin color, forms deposits in the skin. "
            "Common types include sunspots (liver spots), melasma (often triggered by hormonal changes "
            "like pregnancy), and post-inflammatory hyperpigmentation (occurring after skin injury or acne)."
        ),
        "symptoms": [
            "Flat, darkened patches of skin that can vary in size and color",
            "Spots appearing on areas frequently exposed to the sun (face, hands, arms)",
            "Darkened patches appearing symmetrically on the face (typical of melasma)",
            "Dark spots remaining after an acne breakout or skin injury heals",
        ],
        "treatment": [
            "Topical skin-lightening creams containing hydroquinone or cysteamine",
            "Topical retinoids or vitamin C serums to increase cell turnover",
            "Chemical peels containing AHAs or BHAs (glycolic acid, salicylic acid)",
            "Laser therapies (e.g., IPL, Q-switched lasers) targeting melanin deposits",
            "Microdermabrasion for superficial pigmentation",
        ],
        "prevention": [
            "Consistent daily use of broad-spectrum sunscreen (SPF 30 or higher) is critical",
            "Reapply sunscreen every 2 hours when outdoors",
            "Wear protective clothing and wide-brimmed hats",
            "Treat inflammatory skin conditions (like acne or eczema) promptly to prevent post-inflammatory marks",
            "Avoid picking at spots, scabs, or acne",
        ],
        "severity": "Mild",
        "severity_description": "Cosmetic condition that does not pose a physical health threat.",
        "consult_urgency": "recommended",
        "consult_message": (
            "While hyperpigmentation is generally harmless, a dermatologist can help determine "
            "the specific type you have and prescribe professional-grade treatments that are "
            "much more effective than over-the-counter options. They can also rule out any "
            "serious conditions that mimic dark spots."
        ),
    },
}

def get_disease_info(disease_name):
    """
    Retrieve disease information by name.
    Returns the disease data dict or a default 'unknown' entry.
    """
    return DISEASE_DATA.get(disease_name, {
        "full_name": disease_name.replace("_", " ").title(),
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
