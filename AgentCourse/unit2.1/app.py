import datetime
# import numpy as np
import os
import time
from huggingface_hub import login
from smolagents import CodeAgent, DuckDuckGoSearchTool, InferenceClientModel, tool
from langfuse import get_client
from openinference.instrumentation.smolagents import SmolagentsInstrumentor

 


# Tool to suggest a menu based on the occasion
@tool
def suggest_menu(occasion: str) -> str:
    """
    Suggests a menu based on the occasion.
    Args:
        occasion (str): The type of occasion for the party. Allowed values are:
                        - "casual": Menu for casual party.
                        - "formal": Menu for formal party.
                        - "superhero": Menu for superhero party.
                        - "custom": Custom menu.
    """
    if occasion == "casual":
        return "Pizza, snacks, and drinks."
    elif occasion == "formal":
        return "3-course dinner with wine and dessert."
    elif occasion == "superhero":
        return "Buffet with high-energy and healthy food."
    else:
        return "Custom menu for the butler."

## You need a token from https://hf.co/settings/tokens, ensure that you select 'read' as the token type. If you run this on Google Colab, you can set it up in the "settings" tab under "secrets". Make sure to call it "HF_TOKEN"
## Check the .env file or run the export command (export HF_TOKEN=...)
HF_TOKEN = os.environ.get("HF_TOKEN")
login(token=HF_TOKEN)

agent = CodeAgent(
    tools=[DuckDuckGoSearchTool(), suggest_menu], 
    model=InferenceClientModel(),
    additional_authorized_imports=['datetime']
)

# # Preparing the playlist for tonight
# agent.run("Search for the best music recommendations for a party at the Wayne's mansion.")

# # Preparing the menu for the party
# agent.run("Prepare a formal menu for the party.")

# # Estimating the timing
# agent.run(
#     """
#     Alfred needs to prepare for the party. Here are the tasks:
#     1. Prepare the drinks - 30 minutes
#     2. Decorate the mansion - 60 minutes
#     3. Set up the menu - 45 minutes
#     4. Prepare the music and playlist - 45 minutes

#     If we start right now, at what time will the party be ready?
#     """
# )

# Change to your username and repo name
agent.push_to_hub('ArnaudBrun/AlfredAgent')