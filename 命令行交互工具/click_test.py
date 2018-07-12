import click


@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name',prompt='Your name', help='the person to greet',hide_input=True,confirmation_prompt=True)

def hello(count, name):
    """Simple program that greets Name for a total of count times."""
    for x in range(count):
        click.echo('hello %s' %name)



if __name__ == '__main__':
	hello()
