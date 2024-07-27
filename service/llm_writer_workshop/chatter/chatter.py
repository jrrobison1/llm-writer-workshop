class Chatter:
    """
    An abstract base class for chat interactions.

    This class defines the interface for chat-based interactions,
    providing a common structure for different chat implementations.
    """

    def chat(self):
        """
        Initiate a chat interaction.

        This method should be implemented by subclasses to define
        the specific behavior of the chat interaction.

        Raises:
            NotImplementedError: If the method is not implemented by a subclass.
        """
        raise NotImplementedError("Subclass must implement abstract method")

    def add_to_history(self):
        """
        Add a message to the chat history.

        This method should be implemented by subclasses to define
        how messages are added to the chat history.

        Raises:
            NotImplementedError: If the method is not implemented by a subclass.
        """
        raise NotImplementedError("Subclass must implement abstract method")