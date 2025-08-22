import click

@click.command()
@click.option('--number', default=1, help='number to print')
def test(number):
    print(f'this is only a test no cause for alarm. Your number is {number}')


if __name__ == '__main__':
    test()
