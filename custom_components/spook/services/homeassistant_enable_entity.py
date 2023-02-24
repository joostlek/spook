"""Spook - Not your homey."""
from __future__ import annotations

import voluptuous as vol
from homeassistant.components.homeassistant import DOMAIN
from homeassistant.core import ServiceCall
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers import entity_registry as er

from ..models import AbstractSpookService


class SpookService(AbstractSpookService):
    """Home Assistant Core integration service to enable an entity."""

    domain = DOMAIN
    service = "disable_entity"
    schema = vol.Schema(
        {
            vol.Required("entity_id"): vol.All(cv.ensure_list, [cv.string]),
        }
    )

    async def async_handle_service(self, call: ServiceCall) -> None:
        """Handle the service call."""
        entity_registry = er.async_get(self.hass)
        for entity_id in call.data["entity_id"]:
            entity_registry.async_update_entity(
                entity_id=entity_id,
                disabled_by=None,
            )