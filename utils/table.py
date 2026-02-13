class Seat:
    """
    Class representing a seat in a table.

    Attributes:
        __free (bool): Indicates whether the seat is available.
        __occupant (str): Name of the person occupying the seat.
    """

    def __init__(self) -> None:
        """
        Initialize a new Seat instance.

        The seat starts free with no occupant.
        """
        self.__free: bool = True
        self.__occupant: str = "No one"

    def __str__(self) -> str:
        """
        String representation of the Seat.

        :return: A string describing the seat and its occupant.
        """
        status = "free" if self.__free else f"occupied by {self.__occupant}"
        return f"Seat({status})"

    def get_name(self) -> str:
        """
        Get the name of the current occupant.

        :return: The occupant's name as a string.
        """
        return self.__occupant

    def is_free(self) -> bool:
        """
        Check whether the seat is free.

        :return: True if the seat is free, otherwise False.
        """
        return self.__free

    def set_occupant(self, name: str) -> None:
        """
        Assign an occupant to the seat if it is free.

        :param name: Name of the person to assign to the seat.
        :return: None
        """
        if self.__free:
            self.__occupant = name
            self.__free = False
        else:
            print("Seat already occupied")

    def remove_occupant(self) -> None:
        """
        Remove the current occupant from the seat.

        :return: None
        """
        if not self.__free:
            self.__occupant = "No one"
            self.__free = True


class Table:
    """
    Class representing a table containing multiple seats.

    Attributes:
        __capacity (int): Maximum number of seats allowed at the table.
        __seats (list[Seat]): List of Seat objects assigned to the table.
    """

    def __init__(self, capacity: int = 4) -> None:
        """
        Initialize a new Table instance.

        :param capacity: Maximum number of seats the table can hold.
        :return: None
        """
        self.__capacity: int = capacity
        self.__seats: list[Seat] = [Seat() for _ in range(capacity)]

    def __str__(self) -> str:
        """
        String representation of the Table.

        :return: A string describing the table and its seats.
        """
        seat_descriptions = ", ".join(str(seat) for seat in self.__seats)
        return f"Table(capacity={self.__capacity}, seats=[{seat_descriptions}])"

    def get_seats(self) -> list[Seat]:
        """
        Get the list of seats at the table.

        :return: A list of Seat objects.
        """
        return self.__seats

    def get_capacity(self) -> int:
        """
        Get the maximum number of seats available at the table.

        :return: The table's seating capacity as an integer.
        """
        return self.__capacity

    def has_free_spot(self) -> bool:
        """
        Determine whether the table has at least one free seat.

        :return: True if at least one seat is free, otherwise False.
        """
        return any(seat.is_free() for seat in self.__seats)

    def get_first_empty_seat(self) -> Seat | None:
        """
        Get the first available free seat.

        :return: A Seat object if available, otherwise None.
        """
        for seat in self.__seats:
            if seat.is_free():
                return seat
        return None

    def assign_seat(self, name: str) -> None:
        """
        Assign a person to the first available free seat.

        :param name: Name of the person to assign.
        :return: None
        """
        seat = self.get_first_empty_seat()
        if seat is not None:
            seat.set_occupant(name)

    def left_capacity(self) -> int:
        """
        Count how many seats are still free at the table.

        :return: Number of unoccupied seats.
        """
        return sum(1 for seat in self.__seats if seat.is_free())
