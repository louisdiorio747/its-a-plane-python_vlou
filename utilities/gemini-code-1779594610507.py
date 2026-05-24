import requests

LEAGUES = {
    "nfl": ("football", "nfl"),
    "mlb": ("baseball", "mlb"),
    "nhl": ("hockey", "nhl"),
    "nba": ("basketball", "nba")
}

# The priority teams you requested
PRIORITY_TEAMS = {"NYG", "NYM", "NYR", "NYK"}

class ESPNFetcher:
    def __init__(self):
        self.base_url = "https://site.api.espn.com/apis/site/v2/sports/{sport}/{league}/scoreboard"

    def fetch_league_scores(self, sport, league):
        """Fetches live scoreboard data for a specific league."""
        url = self.base_url.format(sport=sport, league=league)
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                return response.json()
        except requests.RequestException:
            pass
        return None

    def get_all_scores(self):
        """Aggregates scores across all leagues and identifies live priority games."""
        priority_live_games = []
        general_games = []

        for league_name, (sport, league) in LEAGUES.items():
            data = self.fetch_league_scores(sport, league)
            if not data or "events" not in data:
                continue

            for event in data["events"]:
                competition = event["competitions"][0]
                status = event["status"]["type"]["name"] # STATUS_IN_PROGRESS, STATUS_FINAL, STATUS_SCHEDULED
                state = event["status"]["type"]["state"]   # "in", "pre", "post"
                
                # Extract teams and scores
                home_node = competition["competitors"][0]
                away_node = competition["competitors"][1]
                
                home_team = home_node["team"]["abbreviation"]
                away_team = away_node["team"]["abbreviation"]
                
                home_score = home_node.get("score", "0")
                away_score = away_node.get("score", "0")
                
                # Get game clock / period details
                display_clock = event["status"]["type"]["detail"]

                game_summary = {
                    "league": league_name.upper(),
                    "home": home_team,
                    "away": away_team,
                    "home_score": home_score,
                    "away_score": away_score,
                    "status": status,
                    "state": state,
                    "clock": display_clock
                }

                # Check if a priority team is playing and the game is LIVE
                is_priority = home_team in PRIORITY_TEAMS or away_team in PRIORITY_TEAMS
                is_live = state == "in"

                if is_priority and is_live:
                    priority_live_games.append(game_summary)
                else:
                    general_games.append(game_summary)

        return priority_live_games, general_games