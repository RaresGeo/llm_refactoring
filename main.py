import os
import sys
from openai import OpenAI
from prompts import generate_refactor_code_prompt
from roles import refactor_general, refactor_go, refactor_python
from dotenv import load_dotenv
import time

def query_llm(role_content, messages, openai_client, response_parser):
    history=[{"role": "system", "content": role_content}]
    
    for message in messages:
        history.append(message)
        

    response = openai_client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=history,
        temperature=0
    )

    return response_parser(response)


def refactor_code(code, extra_prompt, language, openai_client, get_response):
    match language:
        case 'go':
            role_content = refactor_go
            print("Go")
        case 'python':
            role_content = refactor_python
            print("Python")
        case _:
            role_content = refactor_general
            print("General")
            
    refactor_code_prompt = generate_refactor_code_prompt(code, extra_prompt)
    
    user_prompt = {"role": "user", "content": refactor_code_prompt}
    
    return query_llm(role_content, [user_prompt], openai_client, get_response)


def get_response(response):
        return response.choices[0].message.content
    
load_dotenv()

import os
import time
import sys

def get_next_id(day_output_dir, extension):
    """Get the next ID for the output file, based on extension."""
    if not os.path.exists(day_output_dir):
        return 0
    existing_files = os.listdir(day_output_dir)
    max_id = -1
    for file in existing_files:
        if file.endswith(extension):
            parts = file.split('_')
            if len(parts) > 0 and parts[0].isdigit():
                max_id = max(max_id, int(parts[0]))
    return max_id + 1

if __name__ == '__main__':
    load_dotenv()
    client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

    input_dir = 'input'
    output_base_dir = 'output'
    
    if len(sys.argv) > 1:
        language = sys.argv[1]
    else:
        language = ""

    with open(os.path.join(input_dir, 'code_input.txt')) as f:
        code = f.read()
        
    with open(os.path.join(input_dir, 'extra_prompt.txt')) as f:
        extra_prompt = f.read()
        
    start_time = time.time()
    print(f'Refactoring code in...')
    response = refactor_code(code, extra_prompt, language, client, get_response)
    
    extension = {
        'python': '.py',
        'go': '.go'
    }.get(language, '.txt')

    # Create subdirectory for the current day
    current_date = time.strftime("%d_%m_%Y")
    day_output_dir = os.path.join(output_base_dir, current_date)
    os.makedirs(day_output_dir, exist_ok=True)

    # Generate the output file name without the date
    file_id = get_next_id(day_output_dir, extension)
    output_file_name = f'{file_id}_output{extension}'

    with open(os.path.join(day_output_dir, output_file_name), 'w') as f:
        f.write(response)
        elapsed_time = time.time() - start_time
        minutes = int(elapsed_time // 60)
        seconds = elapsed_time % 60
        print(f'Wrote output to {output_file_name} in {minutes} minutes and {seconds:.2f} seconds')
        