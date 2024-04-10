import Brave_logic as Brave_logic
from Gpt_logic import GP_Generate

BRAVE_API_KEY = "YOUR KEY"
GPT_API_KEY = "YOUR KEY"

gpt = GP_Generate(api_key=GPT_API_KEY)
bl = Brave_logic.BR_gen(api_key=BRAVE_API_KEY)

class STAN:

    def __init__(self, query) -> None:
        self.query = query

    def do_magic(self):
        brave_result = bl.fetch_news(query= self.query)
        text_file_path = f"/YOUR?FOLDER?/{brave_result[1]}" # Replace with the path to your text file
        gpt.add_text_file_to_history(text_file_path)
        final_article = gpt.ask()
        with open(f"{brave_result[1]}", "w") as file:
            file.write(final_article)

        return text_file_path