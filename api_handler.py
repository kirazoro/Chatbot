from openai import OpenAI
import os

# NVIDIA API Configuration
API_KEY = "YOUR_API_KEY"
BASE_URL = "https://integrate.api.nvidia.com/v1"

# Initialize OpenAI client for NVIDIA API
client = OpenAI(
    base_url=BASE_URL,
    api_key=API_KEY
)

async def get_nemotron_response(prompt: str):
    try:
        completion = client.chat.completions.create(
            model="nvidia/llama-3.1-nemotron-70b-instruct",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
            top_p=1,
            max_tokens=1024,
            stream=True
        )

        response_text = ""
        for chunk in completion:
            if chunk.choices[0].delta.content is not None:
                response_text += chunk.choices[0].delta.content
        
        return response_text if response_text else "I couldn't generate a response."

    except Exception as e:
        return f"Error: {str(e)}"
