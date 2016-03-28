# FavServersEditor
Python module for easily adding, removing, and moving favorite servers in the "Connect to Server" window.

Example Usage:
```
#!/usr/bin/python

from FavServerEditor import FavoriteServers     # Import the module

servers = FavoriteServers()                     # Create a Favorite Servers instance to act on.

servers.removeAll()                             # Remove all favorite servers
servers.add("Shares", "afp://shares")           # Add 'afp://shares' favorite labelled 'Shares'
servers.add("Server", "smb://server", index=0)  # Add 'smb://server' favorite labelled 'Server' at 0th position
servers.move("Shares", 0)                       # Move 'Shares' favorite back to 0th position
servers.swap("Shares", "Server")                # Swap positions of 'Shares' and 'Server' favorites
servers.remove("Shares")                        # Remove 'Shares' favorite

servers.write()                                 # Write changes

```
## Notes

- Changes made to the favorites may require logout / login to appear. Consider using the module in a script meant for [Outset](https://github.com/chilcote/outset) to avoid this issue.
- In 10.11 the introduction of '.sfl' files and 'SFLListItem's means the hip way of editing these favorites would be something like [Mike Lynn's approach](https://gist.github.com/pudquick/b85fcfd4a0479810e6aa).