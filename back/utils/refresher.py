## Used to refresh the game universe. 
# It is designed to update allegiances when a faction disappears, for example.  

## Optimization approach: refresh on view.  
# If a faction/world/element is never seen or mentioned by players, it remains unrefreshed.  

# There is 1 cycle every [X].  
# All guests send their changes to the host machine.  
# The refresher only runs on the host machine.  
# At the end of each cycle, the host machine refreshes the database.  

# NOTE: This was designed for friendly games ONLY or solo play.  
# It is not suitable for large-scale public multiplayer.  
# Treat it like a tabletop game.
