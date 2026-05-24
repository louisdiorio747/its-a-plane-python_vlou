from .fetcher import ESPNFetcher

class TickerEngine:
    def __init__(self):
        self.fetcher = ESPNFetcher()

    def format_game_string(self, game):
        """Formats game data into a clean text string for an LED matrix."""
        if game["state"] == "pre":
            # Scheduled game: "NYM @ PHI (7:05 PM)"
            return f"[{game['league']}] {game['away']} @ {game['home']} ({game['clock']})"
        elif game["state"] == "in":
            # Live game: "NYR 3 - 2 BOS (2nd Period)"
            return f"[{game['league']}] {game['away']} {game['away_score']} - {game['home_score']} {game['home']} ({game['clock']})"
        else:
            # Completed game: "NYG 24 - 17 DAL (Final)"
            return f"[{game['league']}] {game['away']} {game['away_score']} - {game['home_score']} {game['home']} (F)"

    def get_next_display_text(self):
        """
        Determines what to display based on your prioritization rules.
        Returns a string formatted for scrolling.
        """
        priority_live, general = self.fetcher.get_all_scores()

        # Rule 1: Prioritize live NY teams if any exist
        if priority_live:
            display_strings = [self.format_game_string(g) for g in priority_live]
            prefix = "🚨 LIVE NY UPDATE: "
        # Rule 2: Fallback to general league data
        else:
            display_strings = [self.format_game_string(g) for g in general]
            prefix = "ALL SCORES: "

        if not display_strings:
            return "No games scheduled today."

        # Join games together with a clean spacing separator
        return prefix + "  |  ".join(display_strings) + "  |  "