from mcp.server.fastmcp import FastMCP
from starlette.applications import Starlette
from starlette.applications import Starlette
from starlette.routing import Mount

mcp = FastMCP("My App")

@mcp.tool()
async def hello() -> str:
    """Return string 'Hello World!'"""
    return f"Hello World!"

app = Starlette(
    routes=[
        Mount('/', app=mcp.sse_app()),
    ]
)
