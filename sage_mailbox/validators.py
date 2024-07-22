import re

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class FolderNameValidator:
    """
    Validator for folder names.

    Rules:
    - Length must be between 1 and 255 characters.
    - No special characters except underscore and hyphen.
    - No spaces allowed.
    - Must be unique (this will be handled by the unique constraint on the field).
    """

    length_error_message = "Folder name must be between 1 and 255 characters long."
    character_error_message = "Folder name contains invalid characters. Allowed characters are letters, numbers, underscore, and hyphen. Spaces are not allowed."
    code = "invalid"
    regex = re.compile(r"^[\w-]+$")

    def __call__(self, value):
        if not (1 <= len(value) <= 255):
            raise ValidationError(self.length_error_message, code=self.code)

        if not self.regex.match(value):
            raise ValidationError(self.character_error_message, code=self.code)

    def __eq__(self, other):
        return (
            isinstance(other, FolderNameValidator)
            and self.length_error_message == other.length_error_message
            and self.character_error_message == other.character_error_message
            and self.code == other.code
            and self.regex.pattern == other.regex.pattern
        )


validate_folder_name = FolderNameValidator()
