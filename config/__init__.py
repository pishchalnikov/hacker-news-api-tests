from os import environ


staging = {
    "host": environ.get("STAGING_HOST", "hacker-news.firebaseio.com"),
    "port": environ.get("STAGING_PORT", 443)
}
