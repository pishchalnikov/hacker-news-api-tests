

class ClientAPIException(Exception):
    """
    Main Client API Error
    """


class ViewAPIException(ClientAPIException):
    """
    View error occurred
    """
