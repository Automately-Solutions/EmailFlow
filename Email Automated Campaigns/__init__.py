# email_automated_campaign/__init__.py

from .campaign import Campaign
from .email_sender import EmailSender
from .email_list_manager import EmailListManager
from .config import Config

__all__ = ["Campaign", "EmailSender", "EmailListManager", "Config"]
