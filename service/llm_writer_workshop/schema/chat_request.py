from marshmallow import Schema, ValidationError, fields, validates


class ChatModel(Schema):
    model = fields.String(required=True)
    role = fields.String(required=True)

    @validates("role")
    def validate_role(self, value):
        if value not in ["Editor", "Agent", "Publisher", "Writer"]:
            raise ValidationError("Role not allowed")

    @validates("model")
    def validate_model(self, value):
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
    text = fields.String(required=True)
    models = fields.List(fields.Nested(ChatModel), required=True)
