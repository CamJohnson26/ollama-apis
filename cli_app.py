from cmd import Cmd

from dotenv import load_dotenv
from ollama_apis.run_prompt import chat, embed

load_dotenv()
# token = os.environ.get("")


class CLIApp(Cmd):
    """A simple CLI app."""
    prompt = '>>> '

    def do_greet(self, args):
        """Greet a person."""
        first_name, last_name = args.rsplit(" ", 1)
        print(f"Hello, {last_name}, {first_name}!")

    def do_exit(self, args):
        """Exit the app."""
        raise SystemExit()

    def do_chat(self, prompt):
        chat(prompt)

    def do_embed(self, prompt):
        embed(prompt)


if __name__ == '__main__':
    CLIApp().cmdloop("Enter a command (greet, exit):")
