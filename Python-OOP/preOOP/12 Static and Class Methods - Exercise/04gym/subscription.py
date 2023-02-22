class Subscription:
    main_id = 0

    def __init__(self, *data):
        [self.date,
         self.customer_id,
         self.trainer_id,
         self.exercise_id
         ] = data
        self.id = self.get_next_id()

    @staticmethod
    def get_next_id():
        Subscription.main_id += 1
        return Subscription.main_id

    def __repr__(self):
        return f"Subscription <{self.id}> on {self.date}"
