from project.band_members.musician import Musician


class Guitarist(Musician):

    @property
    def valid_skills(self):
        return [
            "play metal",
            "play rock",
            "play jazz",
        ]
