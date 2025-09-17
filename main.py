import click
from TextRenderer import*

@click.command()
@click.option('--rows', default=768, help='number of rows in canvas. default 768')
@click.option('--cols', default=1080, help='number of columns in canvas. default 1080')
def test(rows, cols):
    print(f'canvas size r{rows} c{cols}')
    r = TextRenderer(rows=rows, cols=cols)
    r.printText()


if __name__ == '__main__':
    test()
