import random

from nouns import nouns
from verbs import verbs
from adjectives import adjectives as adj

print("Your phrase is:", " ".join([ adj[random.randrange(0, len(adj))], nouns[random.randrange(0, len(nouns))], verbs[random.randrange(0, len(verbs))]]))