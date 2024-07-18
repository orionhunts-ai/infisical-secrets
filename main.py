import os
from quart import Quart
from infisical_client import ClientSettings, InfisicalClient, GetSecretOptions, AuthenticationOptions, UniversalAuthMethod
from dotenv import load_dotenv
load_dotenv()

app = Quart(__name__)
MACHINE_NAME=os.getenv("MACHINE_NAME")
ENVIRONMENT="dev" # or staging or production

client = InfisicalClient(ClientSettings(
    auth=AuthenticationOptions(
      universal_auth=UniversalAuthMethod(
        client_id=os.getenv("CLIENT_ID"),
        client_secret=os.getenv("CLIENT_SECRET"),
      )
    )
))

@app.route("/")
async def hello_world():
    # access value asynchronously
    name = await client.getSecret(options=GetSecretOptions(
       environment=ENVIRONMENT,
       project_id=os.getenv("PROJECT_ID"),
       secret_name=MACHINE_NAME))

    return f"Hello! My name is: {name.environment}"

if __name__ == "__main__":
    app.run()