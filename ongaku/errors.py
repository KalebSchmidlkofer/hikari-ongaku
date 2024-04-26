"""
Errors.

All of the ongaku errors.
"""

from __future__ import annotations

import attrs
from aiohttp import WSCloseCode
from hikari import Snowflake

from ongaku.enums import WebsocketEvent
from ongaku.enums import WebsocketOPCode

__all__ = (
    "OngakuException",
    "WebsocketException",
    "WebsocketClosureException",
    "WebsocketTypeException",
    "SessionException",
    "SessionConnectionException",
    "PlayerException",
    "PlayerConnectException",
    "PlayerQueueException",
    "PlayerMissingException",
    "BuildException",
    "SessionHandlerException",
)


class OngakuException(Exception):
    """The base ongaku exception."""


# Client related:


class ClientException(OngakuException):
    """The base exception for the client."""


class ClientAliveException(ClientException):
    """Raised when the client is not alive."""

    reason: str = "Client has not been initialized."
    """Reason for client not being alive."""


# Websocket related:


class WebsocketException(OngakuException):
    """Base websocket exception."""


@attrs.define
class WebsocketClosureException(WebsocketException):
    """When a websocket has closed."""

    code: WSCloseCode
    """The disconnection code."""
    reason: str | None
    """The reason for the disconnection."""


@attrs.define
class WebsocketTypeException(WebsocketException):
    """When a event has an issue decoding."""

    op: WebsocketOPCode | WebsocketEvent | None
    """The op code or event type that this event error is attached too. If unknown, this will be none."""
    reason: str
    """The reason for the events error."""


# Session related:


@attrs.define
class SessionException(OngakuException):
    """Base session exception."""

    session_id: str | None
    """The session ID that this exception is related to."""


@attrs.define
class SessionAvailabilityException(SessionException):
    """Raised when there is no available sessions."""


@attrs.define
class SessionConnectionException(SessionException):
    """Raised when the session has either failed to connect, or is not connected."""

    reason: str = "Session is missing."
    """The reason for the connection exception."""


# Player related:


@attrs.define
class PlayerException(OngakuException):
    """Base player exception."""

    guild_id: Snowflake
    """The guild id that this player is attached to."""


@attrs.define
class PlayerConnectException(PlayerException):
    """raised when the player fails to connect to a channel."""

    reason: str
    """The reason for the failed connection."""


@attrs.define
class PlayerQueueException(PlayerException):
    """Raised when an issue occurs within the queue of a player."""

    reason: str
    """The reason for the failed queuing."""


class PlayerMissingException(PlayerException):
    """Raised when the player was unable to be found."""


# Other:


@attrs.define
class BuildException(OngakuException):
    """Raised when something fails to be built."""

    reason: str
    """The reason for the failed build."""


class LavalinkException(OngakuException):
    """Raised when an issue occurs with lavalink or rest actions."""


@attrs.define
class SessionHandlerException(OngakuException):
    """Raised when an issue occurs within a session handler."""

    reason: str
    """The reason for the session handler exception."""


# MIT License

# Copyright (c) 2023 MPlatypus

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
