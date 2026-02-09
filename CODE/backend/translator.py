import ast

def translate_python_to_java(code):
    try:
        tree = ast.parse(code)
        func = tree.body[0]

        name = func.name
        params = [arg.arg for arg in func.args.args]

        return_stmt = func.body[0]
        left = return_stmt.value.left.id
        right = return_stmt.value.right.id

        params_java = ", ".join([f"int {p}" for p in params])

        return f"""
public class Main {{
    public static int {name}({params_java}) {{
        return {left} + {right};
    }}
}}
"""
    except:
        return "// Waiting for valid Python code..."
