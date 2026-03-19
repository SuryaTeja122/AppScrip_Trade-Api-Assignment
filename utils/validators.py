def validate_sector(sector: str):
    if not sector.isalpha():
        raise ValueError("Invalid sector")