import json
import openai

MAX_RETRIES = 3

def create_chat_response(
    model="gpt-3.5-turbo", 
    client=None, 
    system_msg=None, 
    user_input=None,
    max_tokens=256, 
    temperature=1.0,
    top_p=0.95,
):
    retries = 0
    while retries < MAX_RETRIES:
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": system_msg},
                    {"role": "user", "content": user_input},
                ],
                max_tokens=max_tokens,
                temperature=temperature,
                top_p=top_p,
            )
            return response.choices[0].message.content
            
        except (TypeError, ValueError) as e:
            print(f"Error occurred: {e}. Retrying {retries + 1}/{MAX_RETRIES}...")
            retries += 1
    
    print("Max retries reached. Returning None.")
    return None


def create_chat_response_by_messages(
    model="gpt-3.5-turbo", 
    client=None, 
    messages=None, 
    headers=None,
    max_tokens=256, 
    temperature=1.0,
    top_p=0.95,
):
    retries = 0
    while retries < MAX_RETRIES:
        try:
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                max_tokens=max_tokens,
                temperature=temperature,
                top_p=top_p,
                extra_headers=headers,
            )            
            return response.choices[0].message.content

        except (TypeError, ValueError) as e:
            print(f"Error occurred: {e}. Retrying {retries + 1}/{MAX_RETRIES}...")
            retries += 1
    
    print("Max retries reached. Returning None.")
    return None


def create_json_mode_chat_response_by_messages(
    model="gpt-3.5-turbo", 
    client=None, 
    messages=None, 
    max_tokens=256, 
    temperature=1.0,
    top_p=0.95,
):
    retries = 0
    while retries < MAX_RETRIES:
        try:
            response = client.chat.completions.create(
                model=model,
                response_format={"type": "json_object"},
                messages=messages,
                max_tokens=max_tokens,
                temperature=temperature,
                top_p=top_p,
            )            
            return response.choices[0].message.content

        except (TypeError, ValueError) as e:
            print(f"Error occurred: {e}. Retrying {retries + 1}/{MAX_RETRIES}...")
            retries += 1
    
    print("Max retries reached. Returning None.")
    return None