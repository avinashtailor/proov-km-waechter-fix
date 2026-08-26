# fleet_utils.py
# Helper utilities for Vossberg Mobility fleet reporting.
# Written 2013. Dead code removed and bugs fixed 2025.

KM_TO_MILES: float = 0.621371          # 1 km = 0.621371 miles (was 1.609, which is km-per-mile — inverted)


def km_to_miles(km: float) -> float:
    """Convert kilometres to miles."""
    return km * KM_TO_MILES


def format_number(value: float) -> str:
    """Format a float to one decimal place."""
    return f"{value:.1f}"


def format_percent(value: float) -> str:
    """Format a float as a whole-number percentage string."""
    return f"{int(value)}%"
