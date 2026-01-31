import json
from fastmcp import FastMCP
from typing import List, Optional

# Initialize FastMCP
mcp = FastMCP("City Scoring Server")

DATA_FILE = "city_data.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def _find_city_score(city_name: str) -> str:
    data = load_data()
    city_name_lower = city_name.lower()
    
    for city in data:
        if city["city"].lower() == city_name_lower:
            return json.dumps(city, indent=2)
            
    return f"City '{city_name}' not found in the database."

@mcp.tool()
def find_city_score(city_name: str) -> str:
    """
    Find the score and details for a specific city.
    
    Args:
        city_name: The name of the city to look up (case-insensitive).
        
    Returns:
        A formatted string with the city's score and details, or a message if not found.
    """
    return _find_city_score(city_name)

def _list_cities(limit: int = 10) -> str:
    data = load_data()
    # Sort by score descending
    sorted_data = sorted(data, key=lambda x: x.get("score", 0), reverse=True)
    return json.dumps(sorted_data[:limit], indent=2)

@mcp.tool()
def list_cities(limit: int = 10) -> str:
    """
    List top cities with their scores.
    
    Args:
        limit: The maximum number of cities to return (default: 10).
        
    Returns:
        A JSON string containing the list of cities and their scores.
    """
    return _list_cities(limit)

if __name__ == "__main__":
    mcp.run()
