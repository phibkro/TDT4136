from typing import Any
from queue import Queue


class CSP:
    def __init__(
        self,
        variables: list[str],
        domains: dict[str, set],
        edges: list[tuple[str, str]],
    ):
        """Constructs a CSP instance with the given variables, domains and edges.

        Parameters
        ----------
        variables : list[str]
            The variables for the CSP
        domains : dict[str, set]
            The domains of the variables
        edges : list[tuple[str, str]]
            Pairs of variables that must not be assigned the same value
        """
        self.variables = variables
        self.domains = domains

        # Binary constraints as a dictionary mapping variable pairs to a set of value pairs.
        #
        # To check if variable1=value1, variable2=value2 is in violation of a binary constraint:
        # if (
        #     (variable1, variable2) in self.binary_constraints and
        #     (value1, value2) not in self.binary_constraints[(variable1, variable2)]
        # ) or (
        #     (variable2, variable1) in self.binary_constraints and
        #     (value1, value2) not in self.binary_constraints[(variable2, variable1)]
        # ):
        #     Violates a binary constraint
        self.binary_constraints: dict[tuple[str, str], set] = {}
        for variable1, variable2 in edges:
            self.binary_constraints[(variable1, variable2)] = set()
            for value1 in self.domains[variable1]:
                for value2 in self.domains[variable2]:
                    if value1 != value2:
                        self.binary_constraints[(variable1, variable2)].add(
                            (value1, value2)
                        )
                        self.binary_constraints[(variable1, variable2)].add(
                            (value2, value1)
                        )

    def ac_3(self) -> bool:
        """Performs AC-3 on the CSP.
        Meant to be run prior to calling backtracking_search() to reduce the search for some problems.

        Returns
        -------
        bool
            False if a domain becomes empty, otherwise True
        """
        queue = Queue()
        for edge in self.binary_constraints:
            queue.put(edge)

        while not queue.empty():
            edge = queue.get()
            if self.revise(edge):
                if len(self.domains[edge[0]]) <= 0:
                    return False
                for constraint in self.binary_constraints:
                    if constraint == edge:
                        pass
                    elif edge[0] in constraint:
                        Xk = (
                            constraint[0] if constraint[1] == edge[0] else constraint[1]
                        )
                        queue.put((Xk, edge[1]))
        return True

    def revise(self, edge: tuple[str, str]) -> bool:
        revised = False
        if edge in self.binary_constraints:
            for x in self.domains[
                edge[0]
            ].copy():  # copy() to avoid modifying the original set while iterating, which throws an error
                for y in self.domains[edge[1]]:
                    if (x, y) in self.binary_constraints[edge]:
                        break
                else:
                    # Only runs if the loop completes without breaking
                    # If no value in the domain of X satisfies the constraint with a value in the domain of Y
                    self.domains[edge[0]].remove(x)
                    revised = True
        return revised

    def backtracking_search(self) -> None | dict[str, Any]:
        """Performs backtracking search on the CSP.

        Returns
        -------
        None | dict[str, Any]
            A solution if any exists, otherwise None
        """

        def backtrack(assignment: dict[str, Any]):
            # If all variables are assigned, then the assignment is a solution
            if len(assignment) >= len(self.variables):
                return assignment
            # select unassigned variable
            var = self.select_unassigned_variable(assignment)
            # order domain values
            for value in self.domains.get(var):
                assignment[var] = value
                if self.is_consistent(assignment):
                    result = backtrack(assignment)
                    if result:
                        return result
                del assignment[var]
            # no solution exists
            return None

        return backtrack({})

    def is_consistent(self, assignment: dict[str, Any]) -> bool:
        """
        Checks if the current assignment is consistent with the binary constraints.
        Returns True if the assignment is consistent, False otherwise
        """
        # Check edges
        for edge in self.binary_constraints:
            # If an edge is assigned, check if the assignment is consistent
            if edge[0] in assignment and edge[1] in assignment:
                if (
                    assignment[edge[0]],
                    assignment[edge[1]],
                ) not in self.binary_constraints[(edge[0], edge[1])]:
                    return False
        return True

    def select_unassigned_variable(self, assignment: dict[str, Any]):
        """
        Returns an unassigned variable, or None if there is none
        """
        for var in self.variables:
            if var not in assignment:
                return var
        # no unassigned variables
        return None


def alldiff(variables: list[str]) -> list[tuple[str, str]]:
    """Returns a list of edges interconnecting all of the input variables

    Parameters
    ----------
    variables : list[str]
        The variables that all must be different

    Returns
    -------
    list[tuple[str, str]]
        List of edges in the form (a, b)
    """
    return [
        (variables[i], variables[j])
        for i in range(len(variables) - 1)
        for j in range(i + 1, len(variables))
    ]
