from dotenv import load_dotenv
import urllib.parse

load_dotenv()

def get_channel_access_token() -> str:
    return os.getenv('CHANNEL_ACCESS_TOKEN')

def get_channel_secret() -> str:
    return os.getenv('CHANNEL_SECRET')

def get_openai_api_key() -> str:
    return os.getenv('OPENAI_API_KEY')

def get_mongo_uri() -> str:
    host: str = get_mongo_host()
    port: str = get_mongo_port()
    username: str = urllib.parse.quote_plus(get_mongo_username())
    password: str = urllib.parse.quote_plus(get_mongo_passwd())
    return f"mongodb://{username}:{password}@{host}:{port}/"

def get_mongo_host() -> str:
    return os.getenv('MONGO_HOST')

def get_mongo_port() -> str:
    return os.getenv('MONGO_PORT')

def get_mongo_username() -> str:
    return os.getenv('MONGO_USERNAME')

def get_mongo_passwd() -> str:
    return os.getenv('MONGO_PASSWD')
