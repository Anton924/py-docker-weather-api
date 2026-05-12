import requests
import pprint
import os


def get_weather(
        requested_info: str,
        q_param: str
) -> None:
    base_url = "http://api.weatherapi.com/v1"

    pprint.pprint(
        requests.get(
            f"{base_url}/{requested_info}"
            f"?key={os.getenv('API_KEY')}&q={q_param}"
        ).text
    )


if __name__ == "__main__":
    get_weather("current.json", "Paris")
