# ADK and FastMCP Integration Demo

This repository contains a demonstration project showcasing the integration between the Google Agent Development Kit (ADK) and a FastMCP (Fast Multi-Capability Proxy) server.

The project consists of two main components:
1.  A **FastMCP server** that exposes several tools via an HTTP endpoint.
2.  An **ADK agent** that connects to the MCP server to use its tools to perform a series of tasks based on user interaction.

## Overview

The goal of this demo is to illustrate how an ADK agent can leverage external tools hosted on a FastMCP server.

### The MCP Server

Located in the `mcp_server/` directory, the server is built using the `fastmcp` library. It automatically discovers and registers any tools placed within the `mcp_server/tools/` directory.

The following tools are included:

*   `generate_random_number(max_number: int) -> int`: Returns a random integer between 1 and `max_number`.
*   `is_prime(n: int) -> bool`: Checks if a given integer `n` is a prime number.
*   `calculate_pi_to_digits(digits: int) -> str`: Calculates the value of Pi to a specified number of decimal digits.

### The ADK Agent

Located in `agents/mcp_demo/`, the `Random_Prime_Number_Pi_Calculating_Agent` is an `LlmAgent` configured to use a Gemini model. It has a quirky personality, speaking in 1990's hip-hop slang.

The agent follows this logic:

1.  It asks the user for a positive integer.
2.  It uses the `generate_random_number` tool with the user's number as the maximum value.
3.  **If the random number is 10 or less**, it tells the user the number and playfully suggests they aren't "nerdy enough" if they need a tool to calculate Pi to so few digits. The interaction then waits for a new number from the user.
4.  **If the random number is greater than 10**, it uses the `is_prime` tool to check for primality.
5.  **If the number is not prime**, it informs the user and loops back to generate a new random number.
6.  **If the number is prime**, it uses the `calculate_pi_to_digits` tool to calculate Pi to that many digits. It then presents the prime number and the calculated value of Pi to the user, completing the loop.

## Getting Started

Follow these instructions to set up and run the demo.

### Prerequisites

*   Python 3.8 or higher
*   `pip` (Python package installer)

### Installation

1.  **Clone the repository:**
    ```sh
    git clone <your-repo-url>
    cd adk_mcp_demo
    ```

2.  **Set up a virtual environment (recommended):**
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    # On Windows, use: venv\Scripts\activate
    ```

3.  **Install the required dependencies:**
    This project depends on `google-adk` and `fastmcp` which are in the included requirments.txt.
    ```sh
    pip install -r requirment.txt"
    ```

## How to Run the Demo

The demo requires two separate processes running in two different terminals: the MCP server and the ADK agent.

### Step 1: Start the MCP Server

In your first terminal, run the MCP server from the root of the project directory.

```sh
python mcp_server/main.py
```

You should see output indicating the server has started and has discovered the tools:

```
Discovered and loaded tool package: tools.calc_pi
Discovered and loaded tool package: tools.is_prime
Discovered and loaded tool package: tools.random_num
INFO:     Started server process [XXXXX]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:9000 (Press CTRL+C to quit)
```

You can optionally verify the server is working by running the test script in a separate terminal:
```sh
python mcp_server/test_fastmcp_server.py
```

It should output something like this:

```
[Tool(name='calculate_pi_to_digits', title=None, description='Calculates Pi to a given number of digits.', inputSchema={'properties': {'digits': {'type': 'integer'}}, 'required': ['digits'], 'type': 'object'}, outputSchema={'properties': {'result': {'type': 'string'}}, 'required': ['result'], 'type': 'object', 'x-fastmcp-wrap-result': True}, icons=None, annotations=None, meta={'_fastmcp': {'tags': []}}), Tool(name='is_prime', title=None, description='Checks if a number is prime.', inputSchema={'properties': {'n': {'type': 'integer'}}, 'required': ['n'], 'type': 'object'}, outputSchema={'properties': {'result': {'type': 'boolean'}}, 'required': ['result'], 'type': 'object', 'x-fastmcp-wrap-result': True}, icons=None, annotations=None, meta={'_fastmcp': {'tags': []}}), Tool(name='generate_random_number', title=None, description='Returns a random number between 1 and max_number.', inputSchema={'properties': {'max_number': {'default': 100, 'type': 'integer'}}, 'type': 'object'}, outputSchema={'properties': {'result': {'type': 'integer'}}, 'required': ['result'], 'type': 'object', 'x-fastmcp-wrap-result': True}, icons=None, annotations=None, meta={'_fastmcp': {'tags': []}})]
```

### Step 2: Run the ADK Agent
You'll need to create a `.env` file in the `agents/mcp_demo/` directory consisting of the following information:
```
# For use on Google Cloud Vertex AI
GOOGLE_GENAI_USE_VERTEXAI=1
GOOGLE_CLOUD_PROJECT=<your-gcp-project-id>
GOOGLE_CLOUD_LOCATION=us-central1

# For use with Google AI Studio you need:
GOOGLE_GENAI_USE_VERTEXAI=0
GOOGLE_API_KEY="YOUR_API_KEY"
```

In a second terminal (ensure your virtual environment is active), use the `adk` command-line tool to run the agent.

```sh
cd agents
adk web
```
You should see output indicating the server has started something like this:
```
INFO:     Started server process [XXXXX]
INFO:     Waiting for application startup.

+-----------------------------------------------------------------------------+
| ADK Web Server started                                                      |
|                                                                             |
| For local testing, access at http://127.0.0.1:8000.                         |
+-----------------------------------------------------------------------------+

INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```
### Step 3: Interact with the Agent in the web ui
In your web browser navigate to http://127.0.0.1:8000 and start chatting with the agent using the ADK web ui.
