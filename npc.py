class NPC:
    def __init__(self, name, dialogue):
        self.name = name
        self.dialogue = dialogue

class Dialogue:
    def __init__(self, lines):
        self.lines = lines

    def start_dialogue(self):
        for line in self.lines:
            print(line)


from npc import NPC, Dialogue

# Define dialogues
dialogue_1 = Dialogue(["Hello there!", "How can I help you?"])
dialogue_2 = Dialogue(["Welcome, adventurer!", "Would you like to hear a tale?"])

# Define NPCs
npc_1 = NPC("Bob", dialogue_1)
npc_2 = NPC("Elder", dialogue_2)

