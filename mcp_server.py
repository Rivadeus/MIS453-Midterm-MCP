from fastmcp import FastMCP
import requests

# Define the MCP Server
mcp = FastMCP("SentimentScope")

# The Backend API URL (Use localhost if testing locally, or HF URL if deployed)
API_URL = "https://riva1205-midterm.hf.space/predict"

@mcp.tool()
def get_sentiment(text: str) -> str:
    """
    Analyzes the sentiment of a given text string. 
    Useful for checking if a review or statement is positive or negative.
    """
    try:
        response = requests.post(API_URL, json={"text": text})
        if response.status_code == 200:
            data = response.json()
            return f"The text is classified as {data['label']} with {data['confidence']} confidence."
        else:
            return f"Error analyzing text. Status: {response.status_code}"
    except Exception as e:
        return f"Failed to connect to SentimentScope API: {str(e)}"

if __name__ == "__main__":
    # Run the MCP server
    mcp.run()