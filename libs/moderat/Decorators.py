

def connected_to_server(function):
    '''
    Check If Moderator Connected To Server
    :param function:
    :return:
    '''
    def wrapper(moderat):
        if moderat.connected:
            return function(moderat)
    return wrapper


def is_administrator(function):
    '''
    Check If Moderator Privileges is highest
    :param function:
    :return:
    '''
    def wrapper(moderat):
        if moderat.privs == 1:
            return function(moderat)
    return wrapper


def client_is_selected(function):
    '''
    Check If Client Is Selected
    :param function:
    :return:
    '''
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except TypeError:
            pass
    return wrapper