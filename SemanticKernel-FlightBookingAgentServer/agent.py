import asyncio
import logging
from uuid import uuid4

from semantic_kernel.agents.chat_completion.chat_completion_agent import ChatCompletionAgent, ChatHistoryAgentThread
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.contents.chat_message_content import ChatMessageContent
from semantic_kernel.contents.chat_history import ChatHistory

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SemanticKernelFlightBookingAgent:

    def __init__(self):
        logger.info("Initializing SemanticKernelFlightBookingAgent.")
        self.chat_agent = ChatCompletionAgent(
            service=AzureChatCompletion(
                api_key="<api_key>", # Replace with your Azure OpenAI API key
                endpoint="https://<endpoint>.openai.azure.com",  # Ensure you have the correct endpoint and deployment name
                deployment_name="<deployment_name>", # Replace with your deployment name
                api_version="2024-12-01-preview",
            ),
            name="Assistant",
        )

        # Mapping of context_id -> ChatHistory
        self.history_store: dict[str, ChatHistory] = {}

        logger.info("SemanticKernelFlightBookingAgent initialized successfully.")

    async def book_flight(self, user_input: str, context_id: str) -> str:
        """
        Book a flight based on user input.
        :param user_input: The user's request for flight booking.
        :param context_id: The context ID for the request.
        :return: The response from the flight booking agent.
        """
        logger.info(f"Received flight booking request: {user_input} with context ID: {context_id}")

        if not user_input:
            logger.error("User input is empty.")
            raise ValueError("User input cannot be empty.")

        # Get or create ChatHistory for the context
        chat_history = self.history_store.get(context_id)
        if chat_history is None:
            chat_history = ChatHistory(
                messages=[],
                system_message="You are a helpful flight booking assistant. Your task is to help the user book a flight. If all information is correct, mock the response of succesful flight booking done"
            )
            self.history_store[context_id] = chat_history
            logger.info(f"Created new ChatHistory for context ID: {context_id}")

        # Add user input to chat history
        chat_history.messages.append(ChatMessageContent(role="user", content=user_input))

        # Create a new thread from the chat history
        thread = ChatHistoryAgentThread(chat_history=chat_history, thread_id=str(uuid4()))

        # Get response from the agent
        response = await self.chat_agent.get_response(message=user_input, thread=thread)

        # Add assistant response to chat history
        chat_history.messages.append(ChatMessageContent(role="assistant", content=response.content.content))

        logger.info(f"Flight booking agent response: {response.content.content}")

        final_response = f"{response.content.content}\n\nThis is a flight booking agent. Please provide the necessary details for booking a flight."

        return final_response
