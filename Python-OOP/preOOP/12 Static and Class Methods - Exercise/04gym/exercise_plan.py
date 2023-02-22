class ExercisePlan:
    main_id = 0

    def __init__(self, *input_data):
        [self.trainer_id,
         self.equipment_id,
         self.duration  # is in minutes
         ] = input_data
        self.id = self.get_next_id()

    @classmethod
    def from_hours(cls, trainer_id, equipment_id, hours):
        durations = hours * 60 # in minutes
        return cls(trainer_id, equipment_id, durations)

    @staticmethod
    def get_next_id():
        ExercisePlan.main_id += 1
        return ExercisePlan.main_id

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"
