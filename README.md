# FavServersEditor
Python module for easily adding, removing, and moving positions of Favorite Servers entries in the context of the currently logged in user.

Example Usage:
```
#!/usr/bin/python

from FavServersEditor import FavoriteServers       # Import the module

fav_servers = FavoriteServers()                    # Create a Favorite Servers instance to act on.
   
fav_servers.removeAll()                            # Remove all current Favorite Servers
fav_servers.add("Shares", "afp://shares")          # Add Favorite for "afp://shares" labelled "Shares"
fav_servers.add("Server", "smb://server", index=0) # Add Favorite for "smb://server" labelled "Server" at 0th position
fav_servers.move("Shares", 0)                      # Move "Shares" Favorite back to 0th position
fav_servers.remove("Server")                       # Remove the "Servers" Favorite

fav_servers.write()                                # Write changes to preferences

```

## Notes

- Currently requires logout -> login for changes to show up in Favorite Servers window. I believe this is due to these Favorites being cached on login then read from said cache when the "Connect to Servers" window is opened. Looking for a fix for this but for now this is the way it is.
