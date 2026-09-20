"""
Pulls your last 50 played tracks from your own Spotify account via the
Web API's /v1/me/player/recently-played endpoint, and saves them to a CSV.

This does NOT require waiting for the Extended Streaming History export --
it works immediately, using your own Spotify login, and is meant as a
real proof-of-access sample while the full historical export is pending.

Setup (one-time):
1. Go to https://developer.spotify.com/dashboard and log in with your
   normal Spotify account.
2. Click "Create app". Any name/description is fine. For the Redirect URI,
   enter: http://127.0.0.1:8080/callback
   (must match REDIRECT_URI below exactly)
3. Once created, open the app's Settings and copy the Client ID and
   Client Secret into the two variables below.
4. Install the one dependency this script needs:
       pip install spotipy
5. Run it:
       python get_recent_tracks.py
   A browser window will open asking you to log in and authorize the app.
   After you approve, it'll save recently_played_sample.csv in this folder.
"""

import csv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "PASTE_YOUR_CLIENT_ID_HERE"
CLIENT_SECRET = "PASTE_YOUR_CLIENT_SECRET_HERE"
REDIRECT_URI = "http://127.0.0.1:8080/callback"
SCOPE = "user-read-recently-played"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE,
))

results = sp.current_user_recently_played(limit=50)

rows = []
for item in results["items"]:
    track = item["track"]
    rows.append([
        item["played_at"],
        track["name"],
        ", ".join(a["name"] for a in track["artists"]),
        track["duration_ms"],
    ])

with open("recently_played_sample.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["played_at_utc", "track_name", "artist_name", "duration_ms"])
    writer.writerows(rows)

print(f"Saved {len(rows)} tracks to recently_played_sample.csv")
