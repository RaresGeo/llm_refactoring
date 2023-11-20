def generate_refactor_code_prompt(code, extra_prompt):
    return f"""
        Refactor the following code. {extra_prompt}
        
        CODE:
        {code}
    """