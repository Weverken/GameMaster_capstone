from pydantic import BaseModel
from typing import List


class Action(BaseModel):
    name: str
    description: str


class GameRules(BaseModel):
    game_title: str
    player_count: str
    play_time: str
    age_rating: str
    components: List[str]
    setup: List[str]
    objective: str
    round_structure: List[str]
    actions: List[Action]
    end_game: str
    scoring: str
    notes: List[str]
