import tweepy
import json


def authorization(consumer_key, consumer_secret, token_key, token_secret):
    """
    Makes an authorization in Twitter account with the help of  API keys.
    """
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(token_key, token_secret)
    api = tweepy.API(auth)
    return api


def json_creator(api):
    """
    From the data of your own account create json file
    """
    data = api.me()
    dict_with_data = json.loads(json.dumps(data._json))
    with open("data.json", 'w', encoding='utf-8') as f:
        json.dump(dict_with_data, f, indent= 4)


def finder(path, key):
    """
    Find needed information from json.
    P.S. you should write your key word like root.
    For example: entities\\description\\urls.
    """
    with open(path) as f:
        dictionary = json.load(f)
    lst = key.split('\\')
    for i in range(len(lst)):
        dictionary = dictionary[lst[i]]
    return dictionary


if __name__ == "__main__":
    api = authorization("0PlKlKMbNYWL9UeVuC6DPxX4B", "dpvpCGjA9udpjsPkCVfdxZhmAOLMXFeZcZEVLbH3usRiv8fHfN",
                        "963011359737774080-mYiiiIGOarKbuYGVdVTJBPcYC39RkqC",
                        "f8031GVQo6dJXX35RRVbDlGxMcitrAt7uyAUVgKuO1E0R")
    # if yo wish you can use your API key.
    json_creator(api)
    key = input("Enter your key words: ")
    print(finder("C:\\Users\\Home\\hi.json", key))
    # if it does not work please enter correct path to json file.
