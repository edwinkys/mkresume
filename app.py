import typer
from src.content import Content
from src.template import Template
from typing_extensions import Annotated

app = typer.Typer()


@app.command()
def main(
    input: Annotated[str, typer.Option(help="Path to YML file")],
    output: Annotated[str, typer.Option(help="Directory to output PDF")],
    template: Annotated[str, typer.Option(help="Template name")] = "default"
):
    content = Content(path=input)
    template = Template(content=content, name=template)
    template.to_pdf(output)


if __name__ == "__main__":
    app()
