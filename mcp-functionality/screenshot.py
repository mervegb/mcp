from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.utilities.types import Image
from mss import mss
from PIL import Image as PILImage
import io

mcp = FastMCP("screenshot")

@mcp.tool()
def capture_screenshot() -> Image:
    """
    Capture the current screen and return it as an MCP Image.
    """
    with mss() as sct:
        screenshot = sct.grab(sct.monitors[0])
        img = PILImage.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")
        buffer = io.BytesIO()
        img.save(buffer, format="JPEG", quality=70)
        return Image(data=buffer.getvalue(), format="jpeg")

if __name__ == "__main__":
    mcp.run()