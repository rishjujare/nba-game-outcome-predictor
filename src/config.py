"""Project settings and dataset attribution."""
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
LEAGUE = 'NBA'
DATA_URL = 'https://raw.githubusercontent.com/junior-ta/NBA-Data-Analytics-Web-App/main/database/games.csv'
RAW_CSV = ROOT / 'data' / 'nba_games.csv'
RESULTS = ROOT / 'results'
RANDOM_STATE = 42
