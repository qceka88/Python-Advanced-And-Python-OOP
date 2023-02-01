class Player:

    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        if skill_name not in self.skills:
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"
        return "Skill already added"

    def player_info(self):
        skills = "\n".join(f'==={skill} - {mana}' for skill, mana in self.skills.items())
        message = f'''Name: {self.name}
Guild: {self.guild}
HP: {self.hp}
MP: {self.mp}
{skills}'''
        return message
