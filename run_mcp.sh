#!/bin/bash
# Script pour lancer le serveur MCP
source .venv/bin/activate
fastmcp run mcp_server.py:mcp --transport http --path /mcp --port 8000 --host 0.0.0.0
