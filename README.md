# Multi-Agent System with Semantic Kernel and Google A2A

This repository contains the code reference for building a multi-agent system that demonstrates seamless collaboration between agents built with **Microsoft Semantic Kernel** and communicating via **Google Agent-to-Agent (A2A) protocol**.

The project showcases a practical example: a **Trip Management System** where a `Travel Planner Agent` orchestrates a `Flight Booking Agent` to assist users with their travel needs.

-----

## 🌟 Features

  * **Multi-Agent Collaboration:** See how independent agents can work together using a common communication protocol.
  * **Microsoft Semantic Kernel Integration:** Agents are built leveraging Semantic Kernel's powerful capabilities for AI orchestration and tool use.
  * **Google A2A Protocol:** Demonstrates how to set up A2A servers and clients for robust agent-to-agent communication.
  * **Modular Design:** Each agent is independent, with its own toolset and runtime, promoting scalability and maintainability.
  * **Stateful Interactions:** Agents maintain context for multi-turn conversations using `context_id`.

-----

## 🚀 Project Structure

This project is divided into two main parts:

1.  **A2A Agent Server (`flight-booking-agent`):** Hosts the `Flight Booking Agent`.
2.  **A2A Client (`travel-planner-agent`):** Hosts the `Travel Planner Agent` which acts as the orchestrator and consumes the `Flight Booking Agent` as a tool.

The core components and their roles are detailed in the [accompanying blog post](https://www.google.com/search?q=YOUR_BLOG_POST_LINK_HERE).

```
.
├── flight_booking_agent_server/
│   ├── __main__.py          # A2A Server implementation for Flight Booking Agent
│   └── flight_booking_agent.py # Defines the SemanticKernelFlightBookingAgent
├── travel_planner_agent_client/
│   ├── travel_agent.py      # A2A Client implementation for Travel Planner Agent
│   └── flight_booking_tool.py # Semantic Kernel tool to interact with Flight Booking Agent
├── requirements.txt         # Project dependencies
└── README.md                # You are here!
```

-----

## 🛠️ Setup and Installation

### Prerequisites

Before you begin, ensure you have the following:

  * Python 3.9+
  * An Azure OpenAI Service deployment with a chat completion model (e.g., `gpt-35-turbo`, `gpt-4`). You'll need the API key, endpoint, and deployment name.
  * `uvicorn` (for running the A2A server).

### Installation Steps

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
    cd YOUR_REPO_NAME
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate # On Windows, use `venv\Scripts\activate`
    # OR, with uv (https://github.com/astral-sh/uv):
    uv venv venv
    source venv/bin/activate # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    # OR, with uv:
    uv pip install -r requirements.txt
    ```

4.  **Configure API Keys:**

    * Copy the provided `.env.example` file to `.env` and fill in your Azure OpenAI credentials:

      ```bash
      cp .env.example .env  # On Windows, use: copy .env.example .env
      ```

      Then open `.env` and set the following values:

      ```env
      A2A_SERVER_URL=http://<your-A2A-server-host>:<port>/
      AZURE_OPENAI_API_KEY=<your-api-key>
      AZURE_OPENAI_ENDPOINT=https://<your-endpoint>.openai.azure.com
      AZURE_OPENAI_DEPLOYMENT_NAME=<your-deployment-name>
      AZURE_OPENAI_API_VERSION=<your-deployment-api-version>
      ```

      Your server and agent code will read these values automatically.

       * **Note:** For production environments, consider using environment variables to manage sensitive API keys securely.

-----

## 🏃 How to Run

To see the multi-agent system in action, you'll need to run the A2A server and client in separate terminals.

1.  **Start the Flight Booking Agent (A2A Server):**
    Open your first terminal, navigate to the project root, and run:

    ```bash
    cd flight_booking_agent_server
    python __main__.py
    ```

    You should see output indicating the server is starting on `http://0.0.0.0:9999`.

2.  **Start the Travel Planner Agent (A2A Client):**
    Open a *second* terminal, navigate to the project root, and run:

    ```bash
    cd travel_planner_agent_client
    python travel_agent.py
    ```

    This will start the `Travel Planner Agent`, which will then be ready to communicate. You can interact with it via its chat interface.

-----

## 📬 Example: Chat with the Travel Planner Agent via curl or UI

You can interact with the Travel Planner Agent using the UI at `http://localhost:8000/` or with a simple `curl` command:

```bash
curl -X POST http://localhost:8000/chat \
  -F "user_input=I want to book a flight from Paris to New York on July 10th." \
  -F "context_id=default"
```

The response will be a JSON object containing the assistant's reply:

```json
{"response": "Your assistant's response will appear here."}
```

-----

## 💡 How it Works

When you interact with the `Travel Planner Agent` (the A2A client), it will intelligently determine if a user query requires flight booking assistance. If it does, it will:

1.  Invoke its internal `FlightBookingTool`.
2.  The `FlightBookingTool` will act as an A2A client, fetching the `AgentCard` from the `Flight Booking Agent` (A2A server).
3.  It will then send a `SendMessageRequest` to the `Flight Booking Agent` with the user's flight booking request.
4.  The `Flight Booking Agent` processes the request and sends back a response, which the `Travel Planner Agent` then relays back to the user.

Both agents maintain their own conversational context based on a `context_id`, demonstrating stateful interactions within this multi-agent setup.

-----

## 📚 Learn More

  * **Microsoft Semantic Kernel Documentation:** [https://learn.microsoft.com/en-us/semantic-kernel/](https://learn.microsoft.com/en-us/semantic-kernel/)
  * **Google Agent-to-Agent (A2A) Documentation:** [https://developers.google.com/agents/docs/a2a](https://www.google.com/search?q=https://developers.google.com/agents/docs/a2a)
  * **My Blog Post:** [https://ai.gopubby.com/step-by-step-guide-to-create-a-multi-agent-system-with-microsoft-semantic-kernel-and-google-a2a-1347d5ac8f4b] (Highly recommended for a detailed explanation of the steps\!)

-----

## 🙏 Contributing

Contributions are welcome\! If you have suggestions or improvements, please open an issue or submit a pull request.

-----
