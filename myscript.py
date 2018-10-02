# While the structure is not empty, i.e. there are still elements to be searched,
while not structure.isEmpty():
    # get the path returned by the data structure's .pop() method
    path = structure.pop()
        # for all the successors of the current state,
        for successor in problem.getSuccessors(path):
            # successor[0] = (state, action, cost)[0] = state
            # if the successor's state is unvisited,
                # Push the successor's path into the structure
                structure.push(successorPath)