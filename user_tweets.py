from decouple import config
import requests
import os
import json

bearer_token = config("TWITTER_BEARER_TOKEN")
def create_url() :
    user_id = 47004493
    return "https://api.twitter.com/2/users/{}/tweets".format(user_id)

def get_params() :
    return {"tweet.fields" : "created_at"}

def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "Gejeclient"
    return r

def connect_to_endpoint(url, params):
    response = requests.request("GET", url, auth=bearer_oauth, params=params)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error : {} {}".format(
                response.status_code, 
                response.text
            )
        )
    return response.json()

def proc():
    url = create_url()
    params  = get_params()
    json_response = connect_to_endpoint(url, params)
    return json_response

def main():
    jsonO = proc()
    print(json.dumps(jsonO, indent=4, sort_keys=True))

if __name__ == "__main__":
    main()