import os
from enum import Enum
from pathlib import Path

from mcp.server.fastmcp import FastMCP


class DiagramType(Enum):
    ARCHITECTURE = "architecture"
    BLOCK = "block"
    C4 = "c4"
    CLASSDIAGRAM = "classDiagram"
    ENTITYRELATIONSHIPDIAGRAM = "entityRelationshipDiagram"
    EXAMPLES = "examples"
    FLOWCHART = "flowchart"
    GANTT = "gantt"
    GITGRAPH = "gitgraph"
    KANBAN = "kanban"
    MINDMAP = "mindmap"
    PACKET = "packet"
    PIE = "pie"
    QUADRANTCHART = "quadrantChart"
    RADAR = "radar"
    REQUIREMENTDIAGRAM = "requirementDiagram"
    SANKEY = "sankey"
    SEQUENCEDIAGRAM = "sequenceDiagram"
    STATEDIAGRAM = "stateDiagram"
    TIMELINE = "timeline"
    USERJOURNEY = "userJourney"
    XYCHART = "xyChart"
    ZENUML = "zenuml"


# Initialize FastMCP server
mcp = FastMCP("mermaid-doc")

DIAGRAM_DIR = "docs/syntax"

parent = Path(__file__).resolve().parent


@mcp.tool()
def get_diagram_doc(diagram_name: DiagramType) -> str:
    """
    Retrieve the documentation content for a specific Mermaid diagram.

    Args:
        diagram_name (DiagramType): The name of the diagram. Possible values are: 'architecture', 'block', 'c4', 'classDiagram', 'entityRelationshipDiagram', 'examples', 'flowchart', 'gantt', 'gitgraph', 'kanban', 'mindmap', 'packet', 'pie', 'quadrantChart', 'radar', 'requirementDiagram', 'sankey', 'sequenceDiagram', 'stateDiagram', 'timeline', 'userJourney', 'xyChart', 'zenuml'. These are case sensitive strings.

    Returns:
        str: The documentation content as a string, or an empty string if the diagram is not found.
    """

    file_path = os.path.join(parent.joinpath(DIAGRAM_DIR), f"{diagram_name.value}.md")

    with open(file_path, "r") as f:
        return f.read()


def main():
    # Initialize and run the server
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
