import os
import requests

USERNAME = "debjeetxyz"
TOKEN = os.getenv("GH_TOKEN")

# Query to fetch live contribution data from GitHub GraphQL API
query = """
{
  user(login: "%s") {
    contributionsCollection {
      contributionCalendar {
        totalContributions
        weeks {
          contributionDays {
            date
            contributionCount
            color
          }
        }
      }
    }
  }
}
""" % USERNAME

headers = {"Authorization": f"Bearer {TOKEN}"}
response = requests.post("https://api.github.com/graphql", json={"query": query}, headers=headers)
data = response.json()

try:
    weeks = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
except Exception as e:
    print("Error fetching data:", data)
    exit(1)

# Flatten all days and their colors
all_days = []
for week in weeks:
    for day in week["contributionDays"]:
        all_days.append(day["color"] if day["contributionCount"] > 0 else "#161b22")

# Build an Eiffel Tower SVG silhouette mapping live contribution blocks
svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="100%" height="100%">
  <style>
    .bg {{ fill: #0d1117; }}
    .tower-text {{ fill: #58a6ff; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 14px; font-weight: bold; }}
  </style>
  <rect width="800" height="600" rx="10" class="bg"/>
  <text x="400" y="40" text-anchor="middle" class="tower-text">🗼 Debjeet's Live Eiffel Tower Contribution Structure</text>
  <g transform="translate(250, 70)">
'''

# Procedurally map contribution color blocks into the structural tiers of an Eiffel Tower
index = 0
total_days = len(all_days)

# Tip of the tower (Spire & Top platform)
for y in range(0, 50, 10):
    color = all_days[index % total_days]
    svg_content += f'    <rect x="395" y="{y}" width="10" height="8" fill="{color}" rx="2"/>\n'
    index += 1

# Upper section (narrow body tapering down)
for y in range(50, 180, 12):
    width_span = int(10 + (y - 50) * 0.35)
    for x_offset in range(-width_span, width_span + 1, 12):
        color = all_days[index % total_days]
        svg_content += f'    <rect x="{400 + x_offset}" y="{y}" width="10" height="10" fill="{color}" rx="2"/>\n'
        index += 1

# First balcony / middle tier
for y in range(180, 210, 12):
    width_span = 55
    for x_offset in range(-width_span, width_span + 1, 12):
        color = all_days[index % total_days]
        svg_content += f'    <rect x="{400 + x_offset}" y="{y}" width="10" height="10" fill="{color}" rx="2"/>\n'
        index += 1

# Lower main section (wide open legs tapering out to the base)
for y in range(210, 420, 14):
    width_span = int(55 + (y - 210) * 0.55)
    for x_offset in range(-width_span, width_span + 1, 14):
        # Create the iconic open architectural archway in the middle of the legs
        if y > 300 and -25 < x_offset < 25:
            continue
        color = all_days[index % total_days]
        svg_content += f'    <rect x="{400 + x_offset}" y="{y}" width="12" height="12" fill="{color}" rx="2"/>\n'
        index += 1

# Massive foundational base platform
for y in range(420, 450, 12):
    for x_offset in range(-140, 141, 12):
        color = all_days[index % total_days]
        svg_content += f'    <rect x="{400 + x_offset}" y="{y}" width="10" height="10" fill="{color}" rx="2"/>\n'
        index += 1

svg_content += '''  </g>
</svg>'''

with open("metrics.eiffel.svg", "w") as f:
    f.write(svg_content)

print("Eiffel Tower SVG generated successfully using live contribution data!")