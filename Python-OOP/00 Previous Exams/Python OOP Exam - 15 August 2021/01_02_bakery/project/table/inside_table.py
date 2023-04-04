from project.table.table import Table


class InsideTable(Table):

    @staticmethod
    def allowed_numbers():
        return 1, 50
