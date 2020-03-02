This file holds the tests that you create. Remember to import the python file(s)
you wish to test, along with any other modules you may need.
Run your tests with "python3 ok -t --suite SUITE_NAME --case CASE_NAME -v"
--------------------------------------------------------------------------------

Suite 1

	>>> from ants import *

	Case Example
		>>> x = 5
		>>> x
		5

Suite 1

    >>> from ants import *

    Case LongThrowerOutOfRange
        >>> hive, layout = Hive(AssaultPlan()), dry_layout
        >>> dimensions = (1, 9)
        >>> colony = AntColony(None, hive, ant_types(), layout, dimensions)
        >>> # Testing LongThrower miss
        >>> ant = LongThrower()
        >>> out_of_range = Bee(2)
        >>> colony.places["tunnel_0_0"].add_insect(ant)
        >>> colony.places["tunnel_0_4"].add_insect(out_of_range)
        >>> ant.action(colony)


