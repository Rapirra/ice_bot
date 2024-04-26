from __future__ import annotations

from dataclasses import dataclass
from environs import Env


@dataclass
class Config:
    tg_bot: str
    url: str
    local_url: str


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot=env('API_TOKEN'), url=env('GRAPHQL'), local_url=env('LOCAL'))
