import json

def buildURL(func, text, **kwargs):
    config_file = open('config.json')
    URL_list = json.load(config_file)

    if func == 'metrics':
        return URL_list.get('metrics', '')

    url = URL_list.get(func)
    if url is None:
        return ''  # Return a default value when func does not exist in URL_list

    if text is not None:
        url += text

    # Append additional query parameters
    for key, value in kwargs.items():
        url += f"&{key}={value}"

    return url