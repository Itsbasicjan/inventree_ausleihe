"""A short description of the project"""

from django.urls import path, include
from plugin import InvenTreePlugin
from . import models, api, admin

from plugin.mixins import EventMixin, LocateMixin, ScheduleMixin, SettingsMixin, UserInterfaceMixin

from . import PLUGIN_VERSION


class Ausleihfunktion(EventMixin, LocateMixin, ScheduleMixin, SettingsMixin, UserInterfaceMixin, InvenTreePlugin):

    """Ausleihfunktion - custom InvenTree plugin."""

    # Plugin metadata
    TITLE = "Stock Loan Manager"
    NAME = "StockLoanPlugin"
    SLUG = "stock-loan"
    DESCRIPTION = "Enables tracking and management of stock item loans"
    VERSION = "1.0.0"
    MIN_VERSION = '0.18.0'
    AUTHOR = "Jan Schüler"
    LICENSE = "MIT"
    
    # URL routing
    URLPATHS = [
        path('loan/', include(('ausleihfunktion.api.urls', 'ausleihfunktion'), namespace='stock-loans')),
    ]
    VERSION = PLUGIN_VERSION

    # Additional project information
    AUTHOR = "Jan Schüler"
    
    LICENSE = "MIT"

    # Optionally specify supported InvenTree versions
    # MIN_VERSION = '0.18.0'
    # MAX_VERSION = '2.0.0'
    
    # Scheduled tasks (from ScheduleMixin)
    # Ref: https://docs.inventree.org/en/stable/extend/plugins/schedule/
    SCHEDULED_TASKS = {
        # Define your scheduled tasks here...
    }
    
    # Plugin settings (from SettingsMixin)
    # Ref: https://docs.inventree.org/en/stable/extend/plugins/settings/
    SETTINGS = {
        # Define your plugin settings here...
        'CUSTOM_VALUE': {
            'name': 'Custom Value',
            'description': 'A custom value',
            'validator': int,
            'default': 42,
        }
    }
    
    # Respond to InvenTree events (from EventMixin)
    # Ref: https://docs.inventree.org/en/stable/extend/plugins/event/
    def wants_process_event(self, event: str) -> bool:
        """Return True if the plugin wants to process the given event."""
        # Example: only process the 'part.create' event
        return event == 'part.create'
    
    def process_event(self, event: str, *args, **kwargs) -> None:
        """Process the provided event."""
        print("Processing custom event:", event)
        print("Arguments:", args)
        print("Keyword arguments:", kwargs)
    
    # Perform custom locate operations (from LocateMixin)
    # Ref: https://docs.inventree.org/en/stable/extend/plugins/locate/
    def locate_stock_item(self, item_id: int):
        """Attempt to locate a particular StockItem."""
        ...

    def locate_stock_location(self, location_id: int):
        """Attempt to locate a particular StockLocation."""
        ...
    

    # User interface elements (from UserInterfaceMixin)
    # Ref: https://docs.inventree.org/en/stable/extend/plugins/ui/
    
    # Custom UI panels
    def get_ui_panels(self, request, context: dict, **kwargs):
        """Return a list of custom panels to be rendered in the InvenTree user interface."""

        panels = []

        # Only display this panel for the 'part' target
        if context.get('target_model') == 'part':
            panels.append({
                'key': 'ausleihfunktion-panel',
                'title': 'Ausleihfunktion',
                'description': 'Custom panel description',
                'icon': 'ti:mood-smile:outline',
                'source': self.plugin_static_file('Panel.js:renderAusleihfunktionPanel'),
                'context': {
                    # Provide additional context data to the panel
                    'settings': self.get_settings_dict(),
                    'foo': 'bar'
                }
            })
        
        return panels
    
    # Custom dashboard items
    def get_ui_dashboard_items(self, request, context: dict, **kwargs):
        """Return a list of custom dashboard items to be rendered in the InvenTree user interface."""

        # Example: only display for 'staff' users
        if not request.user or not request.user.is_staff:
            return []
        
        items = []

        items.append({
            'key': 'ausleihfunktion-dashboard',
            'title': 'Ausleihfunktion Dashboard Item',
            'description': 'Custom dashboard item',
            'icon': 'ti:dashboard:outline',
            'source': self.plugin_static_file('Dashboard.js:renderAusleihfunktionDashboardItem'),
            'context': {
                # Provide additional context data to the dashboard item
                'settings': self.get_settings_dict(),
                'bar': 'foo'
            }
        })

        return items
