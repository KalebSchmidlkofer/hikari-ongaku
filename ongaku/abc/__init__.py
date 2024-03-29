"""
Abstract classes.

All of the abstract classes for Ongaku.
"""

from __future__ import annotations

from ongaku.abc.bases import OngakuEvent
from ongaku.abc.error import ExceptionError
from ongaku.abc.error import RestError
from ongaku.abc.events import PlayerBase
from ongaku.abc.events import PlayerUpdateEvent
from ongaku.abc.events import QueueEmptyEvent
from ongaku.abc.events import QueueNextEvent
from ongaku.abc.events import ReadyEvent
from ongaku.abc.events import StatisticsEvent
from ongaku.abc.events import TrackBase
from ongaku.abc.events import TrackEndEvent
from ongaku.abc.events import TrackExceptionEvent
from ongaku.abc.events import TrackStartEvent
from ongaku.abc.events import TrackStuckEvent
from ongaku.abc.events import WebsocketClosedEvent
from ongaku.abc.filters import FilterChannelMix
from ongaku.abc.filters import FilterDistortion
from ongaku.abc.filters import FilterEqualizer
from ongaku.abc.filters import FilterKaraoke
from ongaku.abc.filters import FilterLowPass
from ongaku.abc.filters import FilterRotation
from ongaku.abc.filters import Filters
from ongaku.abc.filters import FilterTimescale
from ongaku.abc.filters import FilterTremolo
from ongaku.abc.filters import FilterVibrato
from ongaku.abc.info import Info
from ongaku.abc.info import InfoGit
from ongaku.abc.info import InfoPlugin
from ongaku.abc.info import InfoVersion
from ongaku.abc.player import Player
from ongaku.abc.player import PlayerState
from ongaku.abc.player import PlayerVoice
from ongaku.abc.playlist import Playlist
from ongaku.abc.playlist import PlaylistInfo
from ongaku.abc.route_planner import FailingAddress
from ongaku.abc.route_planner import IPBlock
from ongaku.abc.route_planner import RoutePlannerDetails
from ongaku.abc.route_planner import RoutePlannerStatus
from ongaku.abc.session import Session
from ongaku.abc.statistics import Statistics
from ongaku.abc.statistics import StatsCpu
from ongaku.abc.statistics import StatsFrameStatistics
from ongaku.abc.statistics import StatsMemory
from ongaku.abc.track import Track
from ongaku.abc.track import TrackInfo

__all__ = (
    # .events
    "OngakuEvent",
    "ReadyEvent",
    "PlayerUpdateEvent",
    "StatisticsEvent",
    "WebsocketClosedEvent",
    "TrackBase",
    "TrackStartEvent",
    "TrackEndEvent",
    "TrackExceptionEvent",
    "TrackStuckEvent",
    "PlayerBase",
    "QueueEmptyEvent",
    "QueueNextEvent",
    # .filters
    "Filters",
    "FilterEqualizer",
    "FilterKaraoke",
    "FilterTimescale",
    "FilterTremolo",
    "FilterVibrato",
    "FilterRotation",
    "FilterDistortion",
    "FilterChannelMix",
    "FilterLowPass",
    # .lavalink
    "InfoVersion",
    "InfoGit",
    "InfoPlugin",
    "Info",
    "RestError",
    "ExceptionError",
    # .player
    "PlayerState",
    "PlayerVoice",
    "Player",
    # .route_planner
    "IPBlock",
    "FailingAddress",
    "RoutePlannerDetails",
    "RoutePlannerStatus",
    # .session
    "Session",
    # .track
    "TrackInfo",
    "Track",
    # .playlist
    "PlaylistInfo",
    "Playlist",
    # .statistics
    "Statistics",
    "StatsMemory",
    "StatsCpu",
    "StatsFrameStatistics",
)


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
