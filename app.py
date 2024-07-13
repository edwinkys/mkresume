import typer
from src.content import Content
from typing_extensions import Annotated


def main(
    path: Annotated[str, typer.Option(help="Path to YML file")],
    template: Annotated[str, typer.Option(help="Template name")] = "default"
):
    Content(path=path)


if __name__ == "__main__":
    typer.run(main)
