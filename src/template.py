import os
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
from src.content import Content
from typing import Optional

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
TEMPLATES_DIR = os.path.join(ROOT_DIR, "templates")


class Template:
    content: Content
    path: str

    def __init__(self, content: Content, name: Optional[str] = "default"):
        self.content = content
        self.path = os.path.join(name, "template.jinja")

        full_path = os.path.join(TEMPLATES_DIR, self.path)
        assert os.path.exists(full_path), f"Template not found: {name}"

    def to_html(self) -> str:
        env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
        template = env.get_template(self.path)

        content = self.content
        return template.render(
            title=content.title,
            email=content.email,
            phone=content.phone,
        )

    def to_pdf(self, output: str):
        html = self.to_html()
        output_file = os.path.join(output, "Resume.pdf")
        HTML(string=html).write_pdf(output_file)
