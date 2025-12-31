# MIS453-Midterm-MCP



This is the Model Context Protocol (MCP) interface for the SentimentScope application. It serves as a bridge between the SentimentScope API and AI agents like **Claude Desktop**, allowing the AI to directly perform sentiment analysis on user text.

## Prerequisites

* **Python 3.9+** installed.
* **Claude Desktop App** installed.
* A running instance of the SentimentScope Backend (hosted on Hugging Face).

## Installation & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/Rivadeus/sentimentscope-mcp.git](https://github.com/Rivadeus/sentimentscope-mcp.git)
cd sentimentscope-mcp

2. Install Dependencies
''''bash

pip install -r requirements.txt

3. Configure Claude Desktop
To enable Claude to use this tool, you must register it in the Claude Desktop configuration file.

Step 1: Locate the configuration file:

Windows: %APPDATA%\Claude\claude_desktop_config.json

macOS: ~/Library/Application Support/Claude/claude_desktop_config.json

Step 2: Open the file (create it if it doesn't exist) and add the following JSON. Note: Ensure the path points to the actual location of mcp_server.py on your machine.
{
  "mcpServers": {
    "sentimentscope": {
      "command": "python",
      "args": [
        "C:\\Users\\Riva\\Desktop\\sentimentscope-mcp\\mcp_server.py"
      ]
    }
  }
}
4. Restart Claude
Fully close and restart the Claude Desktop application.

Look for the socket icon (🔌) in the Claude interface, indicating the tool is connected.
