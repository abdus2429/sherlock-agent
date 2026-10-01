class Sherlock:

    def __init__(self):
        self.name = "Sherlock"

    def respond(self, message):
        return (
            "🕵️ Sherlock online.\n\n"
            f"You said: {message}"
        )