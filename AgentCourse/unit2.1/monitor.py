# import datetime
import os
from huggingface_hub import login
from smolagents import CodeAgent
from langfuse import get_client
from openinference.instrumentation.smolagents import SmolagentsInstrumentor

langfuse = get_client()
 
# Verify connection
if langfuse.auth_check():
    print("Langfuse client is authenticated and ready!")
else:
    print("Authentication failed. Please check your credentials and host.")
    exit

SmolagentsInstrumentor().instrument()

HF_TOKEN = os.environ.get("HF_TOKEN")
login(token=HF_TOKEN)


# Change to your username and repo name
alfred_agent = CodeAgent.from_hub('ArnaudBrun/AlfredAgent', trust_remote_code=True)
alfred_agent.run("Give me the best playlist for a party at Wayne's mansion. The party idea is a 'villain masquerade' theme")  
