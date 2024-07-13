import typer
from typing_extensions import Annotated


def main(
    path: Annotated[str, typer.Option(help="Path to markdown file")],
    template: Annotated[str, typer.Option(help="Template name")] = "default"
):
    pass


if __name__ == "__main__":
    typer.run(main)
