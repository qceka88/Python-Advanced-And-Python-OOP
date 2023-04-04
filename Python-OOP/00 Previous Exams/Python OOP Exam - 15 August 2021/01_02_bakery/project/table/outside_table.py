from project.table.table import Table


class OutsideTable(Table):

    @staticmethod
    def allowed_numbers():
        return 51, 100
