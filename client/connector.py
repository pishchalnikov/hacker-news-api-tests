import requests
import urllib.parse


class Connector:
    def __init__(self, host, port):
        self.host = host
        self.port = int(port)
        self.schema = "https" if self.port == 443 else "http"
        self.base_url = f"{self.schema}://{self.host}:{self.port}"
        self.headers = {}
        self.cookies = {}
        self.proxies = {}

    def do_get(self, path, params=None, **kwargs):
        return requests.get(
            url=urllib.parse.urljoin(self.base_url, path),
            params=params,
            proxies=self.proxies,
            headers=self.headers,
            cookies=self.cookies,
            **kwargs
        )

    def do_post(self, path, data=None, **kwargs):
        return requests.post(
            url=urllib.parse.urljoin(self.base_url, path),
            proxies=self.proxies,
            headers=self.headers,
            cookies=self.cookies,
            json=data,
            **kwargs
        )
