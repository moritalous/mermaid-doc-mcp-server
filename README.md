# Mermaid Doc MCP Server

Mermaid Doc MCP Server is a server for generating Mermaid documents.

## Features

- **List Diagrams**: List all available Mermaid diagram names in the documentation.
- **Retrieve Documentation**: Retrieve the documentation content for a specific Mermaid diagram.


## Prerequisites

### Installation Requirements

1. Install `uv` from [Astral](https://docs.astral.sh/uv/getting-started/installation/) or the [GitHub README](https://github.com/astral-sh/uv#installation)
2. Install Python 3.10 or newer using `uv python install 3.10` (or a more recent version)

## Installation

To add this MCP server to your Amazon Q or Claude, add the following to your MCP config file. With Amazon Q, create (if does not yet exist) a file named `.amazonq/mcp.json` under the same directory that is running `q chat`. Then add the following config:

```json
{
  "mcpServers": {
    "mermaid-doc-mcp-server": {
        "command": "uvx",
        "args": ["mermaid-doc-mcp-server@latest"]
    }
  }
}
```

## Tools

### list_diagrams

List all available Mermaid diagram names in the documentation.

```python
def list_diagrams() -> list:
```

### get_diagram_doc

Retrieve the documentation content for a specific Mermaid diagram.

```python
def get_diagram_doc(diagram_name: str) -> str:
```
