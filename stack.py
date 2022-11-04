

class StackString():
    def __init__(self) -> None:
        self.__stack = []

    def push(self, var) -> None:
        """
        Add element to end of the stack
        :param var: Variable to push in the end of the stack
        :return: Returns nothing
        """
        self.__stack.append(var)

    def pop(self) -> str:
        """
        Get last element from the top of the stack. Then deletes it from the stack.
        :return: Last variable from the stack
        """
        return self.__stack.pop()

    @property
    def last_element(self) -> str:
        """
        Get last element from the stack without deleting it.
        :return: Last variable from the stack
        """

        return self.__stack[-1]

    @property
    def length(self) -> int:
        """
        Current length of the stack
        """
        return len(self.__stack)

    def __to_str(self) -> str:
        return "[" + ",".join(map(str, self.__stack)) + "]"

    def __str__(self) -> str:
        return self.__to_str()

    def __repr__(self) -> str:
        return self.__to_str()