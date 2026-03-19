def generate_markdown(sector, analysis):
    return f"""
# {sector.capitalize()} Sector Analysis

## AI Generated Insights
{analysis['raw']}
"""