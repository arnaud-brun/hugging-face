# import datetime
import os
from huggingface_hub import login
from smolagents import CodeAgent


## You need a token from https://hf.co/settings/tokens, ensure that you select 'read' as the token type. If you run this on Google Colab, you can set it up in the "settings" tab under "secrets". Make sure to call it "HF_TOKEN"
## Check the .env file or run the export command (export HF_TOKEN=...)
HF_TOKEN = os.environ.get("HF_TOKEN")
login(token=HF_TOKEN)

# Change to your username and repo name
alfred_agent = CodeAgent.from_hub('ArnaudBrun/AlfredAgent', trust_remote_code=True)

alfred_agent.run("Give me the best playlist for a party at Wayne's mansion. The party idea is a 'villain masquerade' theme")  