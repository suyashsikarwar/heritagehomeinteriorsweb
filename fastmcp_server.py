from fastmcp import FastMCP

mcp = FastMCP("Math Server")

@mcp.tool()
def add(a: float, b: float) -> str:
    """Add two numbers together."""
    return str(int(a) + int(b))
    #return str(int(a)) + str(int(b))

if __name__ == "__main__":
    mcp.run()