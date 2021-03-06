from model_bakery.recipe import Recipe, foreign_key

from common.enums import NotificationWebhookTypes, StateFieldFormats
from election import models

new_state = Recipe(models.State, code="XX")


markdown_field_type = Recipe(
    models.StateInformationFieldType,
    slug="example_markdown_field",
    long_name="An Example Markdown Field",
    field_format=StateFieldFormats.MARKDOWN,
)


markdown_information = Recipe(
    models.StateInformation,
    field_type=foreign_key(markdown_field_type),
    state=foreign_key(new_state),
    text="# Great Information",
    notes="Just a headline",
)


netlify_webhook = Recipe(
    models.UpdateNotificationWebhook,
    type=NotificationWebhookTypes.NETLIFY,
    name="Test Trigger Endpoint",
    trigger_url="http://test.local/trigger_endpoint",
    active=True,
)
