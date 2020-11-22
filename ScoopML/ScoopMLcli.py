import click


@click.group()
def apis():
    """A CLI for managing ScoopML Cloud AI"""
    
def categories():
    """List all categories."""
    response = requests.post(url, data={payload: text})
    if response.status_code is 200:
        print('\n'.join(response.json()))
    else:
        print(f'Could not get the categories: {response.text}')


if __name__ == '__main__':
    apis(prog_name='apis')
