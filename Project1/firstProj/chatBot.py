import google.generativeai as genai

additional_prompt = """
prompt: 'Retinal Disease'
response: ' Conditions affecting the retina, the light-sensitive tissue at the back of the eye.
    Symptoms: Vary depending on the specific disease but may include vision loss, blurriness, distorted vision, floaters, or flashes of light.
    Treatments: Can include medication (such as anti-VEGF injections), laser therapy, surgery (such as vitrectomy or retinal detachment repair), or lifestyle changes (such as managing diabetes for diabetic retinopathy).'

prompt: 'treaments for pneumonia'
response: 'Treatment for Pneumonia:
    Bacterial Pneumonia:
    Antibiotics like azithromycin or amoxicillin.
    Viral Pneumonia:
    Antiviral medications for influenza, rest, and hydration.
    Fungal Pneumonia:
    Antifungal drugs like fluconazole.
    Other Treatments:
    Oxygen therapy if needed.
    Pain relievers for fever and discomfort.
    Hospitalization for severe cases.
    Hydration and respiratory therapy.
    Preventive Measures:
    Vaccination against pneumonia and influenza.
    Following healthcare provider's advice closely.
    Seeking medical attention if symptoms worsen.'

make sure to give just what the user wants in small concise points. if nothing is mentioned just reply with treatments and symptoms.
if anything is asked other than medical things, say i dont know.

And please reply with html tags so that it can be easily posted in front end
"""

def Gemini_Pro_PromptCall_getDiseaseDetails(prompt, temp=0.9):
    # print("apikey:", GOOGLE_API_KEY)
    genai.configure(api_key='AIzaSyDnDOPSKQWeSd5n_79XJu0ts6iiJCKjlXg')

    getDateRange = {'function_declarations': [
        {'name': 'getDiseaseDetails',
        'description': "Returns disease details in concise form",
        'parameters': {'type_': 'OBJECT',
        'properties': {
            'diseaseDetails': {'type_': 'STRING', 'description': 'Stores symptoms and treatments of disease'}},
        'required': ['diseaseDetails']}},
        ]}
    
    model = genai.GenerativeModel('gemini-pro')
    # model = genai.GenerativeModel('gemini-pro', tools=getDateRange, generation_config={"temperature": temp})
    chat = model.start_chat(history=[])

    prompt="Give the details of this prompt: '"+prompt+"'\nPrevious some of the examples include: \n"+additional_prompt
    response = chat.send_message(prompt)
    
    return response.text[7:-3] if response.text[:7]=="```html" else response.text

# print(Gemini_Pro_PromptCall_getDiseaseDetails("Retinal Disease"))


print(Gemini_Pro_PromptCall_getDiseaseDetails("Pneumonia"))
# print(Gemini_Pro_PromptCall_getDiseaseDetails("Retinal Disease treatments"))


# print(Gemini_Pro_PromptCall_getDiseaseDetails("footbal player essay"))