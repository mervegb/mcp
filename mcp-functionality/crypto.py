from mcp.server.fastmcp import FastMCP
import requests

mcp = FastMCP("Crypto")

@mcp.tool()
def get_cryptocurrency_price(crypto: str) -> str:
    """
    Get the current price of a cryptocurrency.
    Args:
        crypto: The symbol of the cryptocurrency. (eg: bitcoin, ethereum)
    """
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price"
        params={"ids": crypto.lower(), "vs_currencies": "usd"}
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        price = data.get(crypto.lower(), {}).get("usd")

        if price is not None:
            return f"The price of {crypto} is ${price} USD."
        else:
            return f"Price not found for {crypto}."
    except Exception as e:
        return f"Error fetching price: {e}"
   
 
if __name__ == "__main__":
    mcp.run()