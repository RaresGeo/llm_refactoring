# Code Refactoring Script

## Description
This Python script uses OpenAI's GPT-4 model to refactor code snippets. It supports different programming languages and leverages specific roles for refactoring tasks. The script reads code and additional prompts from input files, processes them using OpenAI's API, and writes the refactored code to an output directory.

## Features
- **Multi-Language Support**: Handles 'Go' and 'Python', with a general fallback for other languages.
- **Customizable Prompts**: Allows extra prompts for tailored refactoring requests.
- **Organized Output**: Stores results in daily directories with unique IDs.

## Requirements
- Python 3.x
- OpenAI API key
- Required Python packages: `openai`, `dotenv`

## Setup
1. **Environment Variables**: Set your OpenAI API key in a `.env` file as `OPENAI_API_KEY`.
2. **Input Files**: Place your code snippet in `input/code_input.txt` and any extra prompt in `input/extra_prompt.txt`.

## Usage
Run the script with the desired language as an argument:
```bash
python script_name.py [language]
```
Supported languages are 'go' and 'python'. If no language is specified, it defaults to general refactoring.

## Output
Refactored code is saved in the output directory, organized into subfolders by date. Each output file is named with a unique ID based on its file type.

## Note
This script is designed for educational and development purposes. Ensure compliance with OpenAI's usage policies when using their API.