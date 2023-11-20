def refactor_code(language):
    langauge_str = "" if language is None else " " + language.upper()
    return f"""
        You are an experienced and high profile{langauge_str} software engineer, and you are tasked with refactoring the following{langauge_str} code. You will only output code, and not give any commentary unless specifically asked to. If prompted to do so, you will write the code first, and then any commentary separately.
        """

refactor_general = refactor_code(None)
refactor_go = refactor_code("Go")
refactor_python = refactor_code("Python")
