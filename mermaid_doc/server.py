import glob
import os
from pathlib import Path

from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("mermaid-doc")

DIAGRAM_DIR = "docs/syntax"

parent = Path(__file__).resolve().parent


@mcp.tool()
def list_diagrams() -> list:
    """
    List all available Mermaid diagram names in the documentation.

    Returns:
        list: A list of diagram names.
    """

    md_files = glob.glob(os.path.join(parent.joinpath(DIAGRAM_DIR), "*.md"))
    diagram_names = [os.path.splitext(os.path.basename(f))[0] for f in md_files]

    return diagram_names


@mcp.tool()
def get_diagram_doc(diagram_name: str) -> str:
    """
    Retrieve the documentation content for a specific Mermaid diagram.

    Args:
        diagram_name (str): The name of the diagram.

    Returns:
        str: The documentation content as a string, or an empty string if the diagram is not found.
    """
    file_path = os.path.join(parent.joinpath(DIAGRAM_DIR), f"{diagram_name}.md")

    if not os.path.exists(file_path):
        return "ERROR"

    with open(file_path, "r") as f:
        return f.read()


def main():
    # Initialize and run the server
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
