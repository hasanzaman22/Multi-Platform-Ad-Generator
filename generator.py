from groq import Groq
import os
from prompts import get_system_prompt
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv('GROQ_API_KEY'))

def generate_ad_content(platform, business_name, product):
    system_instruction = get_system_prompt(platform)
    
    chat_completion = client.chat.completions.create(
        messages=[
            {'role': 'system', 'content': system_instruction},
            {'role': 'user', 'content': f'Biznes adı: {business_name}, Məhsul: {product}'}
        ],
        model='llama-3.3-70b-versatile',
    )
    return chat_completion.choices[0].message.content