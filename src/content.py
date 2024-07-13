import yaml
from typing import Dict, List, Any, Optional


class Content:
    """Resume content.

    This class contains data for the resume parsed from a YAML file.
    Additional sections or information is prefixed with additional_.

    Args:
    - path: Path to the YAML file.
    """

    title: str
    email: str
    phone: str

    expericence: List[Dict[str, str]]
    education: List[Dict[str, str]]

    styles: Optional[Dict[str, Dict[str, str]]]
    additional_info: Optional[List[Dict[str, str]]]

    def __init__(
        self,
        path: str,
    ):
        yml: Dict[str, Any] = self.__parse_yml(path)

        # Validate required fields.
        required = ["title", "email", "phone", "experience", "education"]
        for field in required:
            if field not in yml.keys():
                raise Exception(f"Missing required field: {field}")

        self.title = yml["title"]
        self.email = yml["email"]
        self.phone = yml["phone"]
        self.experience = yml["experience"]
        self.education = yml["education"]

        # Additional.
        self.additional_info = yml.get("additional_info")
        self.styles = yml.get("styles")

    @staticmethod
    def __parse_yml(path: str):
        with open(path) as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as e:
                raise Exception(f"Error parsing YML file: {e}")

        return None
