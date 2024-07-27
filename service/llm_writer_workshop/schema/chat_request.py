from marshmallow import Schema, ValidationError, fields, validates


class ChatModel(Schema):
    """
    Schema for validating chat model information.
    """
    model = fields.String(required=True)
    role = fields.String(required=True)

    @validates("role")
    def validate_role(self, value: str) -> None:
        """
        Validate the role field.

        Args:
            value (str): The role to validate.

        Raises:
            ValidationError: If the role is not in the allowed list.
        """
        if value not in ["Editor", "Agent", "Publisher", "Writer"]:
            raise ValidationError("Role not allowed")

    @validates("model")
    def validate_model(self, value: str) -> None:
        """
        Validate the model field.

        Args:
            value (str): The model to validate.

        Raises:
            ValidationError: If the model is not in the allowed list.
        """
        if value not in [
            "gpt-4-turbo",
            "GPT-4",
            "gpt-3.5-turbo",
            "mistral-small",
            "mistral-medium",
            "mistral-large-latest",
            "gemini-pro-1.5",
            "gemini-pro",
            "claude-3-haiku-20240307",
            "claude-3-sonnet-20240229",
            "claude-3-opus-20240229",
        ]:
            raise ValidationError("Model not allowed")


class ChatRequest(Schema):
    """
    Schema for validating chat request data.
    """
    text = fields.String(required=True)
    models = fields.List(fields.Nested(ChatModel), required=True)
