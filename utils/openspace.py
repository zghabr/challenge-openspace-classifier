import random

from utils.table import Table


class Openspace:
    """
    Class representing an open space containing multiple tables.

    Attributes:
        __tables (list[Table]): List of tables in the open space.
        __number_of_tables (int): Maximum number of tables allowed.
    """

    def __init__(
            self, tables: list[Table] | None = None, number_of_tables: int = 6
    ) -> None:
        """
        Initialize a new Openspace instance.

        :param tables: Optional list of Table objects. If None, tables will be created automatically.
        :param number_of_tables: Maximum number of tables allowed in the open space.
        :return: None
        """
        if tables is None:
            tables = [Table() for _ in range(number_of_tables)]

        self.__tables: list[Table] = tables
        self.__number_of_tables: int = number_of_tables

    def __str__(self) -> str:
        """
        String representation of the Openspace.

        :return: A string describing the open space and its tables.
        """
        return f"Openspace(tables={len(self.__tables)}, max_tables={self.__number_of_tables})"

    def organize(self, names: list[str]) -> None:
        """
        Organize people into tables by assigning them to free seats.

        :param names: List of names to assign to seats.
        :return: None

        Notes:
            If the number of people exceeds the total seating capacity,
            a new table is added (if allowed).
        """
        # Compute total capacity
        total_capacity = self.__number_of_tables * self.__tables[0].get_capacity()

        # Add a new table if needed and allowed
        if len(names) > total_capacity:
            self.__tables.append(Table())

        # Assign names randomly to free seats
        for table in self.__tables:
            if not table.has_free_spot():
                continue

            free_spots = table.left_capacity()

            for _ in range(free_spots):
                if not names:
                    return

                # Pick a random name
                name = names.pop(random.randrange(len(names)))
                table.assign_seat(name)

    def display(self) -> None:
        """
        Display the seating arrangement of the open space.

        :return: None
        """
        table_number = 1
        for table in self.__tables:
            print(f"---- Table {table_number} ----")
            for seat in table.get_seats():
                print(seat.get_name())
            print("----------------------------")
            table_number += 1
