"""
Contains utility function to generate random passcodes.

Classes:
--------
    None

Functions:
----------
    generate_passcode():
        a utility function to generate random passcodes

Misc Variables:
--------------
    None
"""

import random


class Randomize:
    """
    Randomize class to generate random passcodes

    ...........
    """
    @classmethod
    async def generate_passcode(cls) -> int:
        """
        A utility function to generate random passcodes

        Parameters:
        ----------
            None

        Returns:
        -------
            passcode: int
                A 6-digit random passcode.
        """
        randomlist = []
        for i in range(0, 3):
            n = random.randint(10, 100)
            randomlist.append(str(n))

        return int("".join(randomlist))
