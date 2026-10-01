import ast
class Sherlock:

    def __init__(self):
        self.name = "Sherlock"

    def respond(self, message):

        try:
            ast.parse(message)
            
            return (
                "🕵️ Sherlock online.\n\n"
                "✅ Investigation complete!\n"
                "No syntax errors found."
            )
        except SyntaxError as error:

             return (
                "🕵️ Sherlock online.\n\n"
                "❌ Investigation complete!\n"
                f"Error Type: {type(error).__name__}\n"
                f"Problem: {error}"
            )
