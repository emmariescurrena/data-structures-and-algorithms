# pylint: disable=bare-except
# pylint: disable=invalid-name
# pyright: reportMissingModuleSource=false

"""Modules..."""
import sys
import pandas as pd

sys.setrecursionlimit(4000)

def solution_hanoi():
    """Get solution to Towers of Hanoi"""

    num =  int(input("Insert number of disks: "))

    def move_tower(n,source,objective,auxiliar,data):
        """Auto-move a disk"""
        
        if n == 1:
            data.append([n,source,objective])
            return data

        else:
            move_tower(n-1,source,auxiliar,objective,data)
            data.append([n,source,objective])
            move_tower(n-1,auxiliar,objective,source,data)
            return data

    data = move_tower(num, "A", "C", "B",[])

    df = pd.DataFrame(data, columns=['Disk', 'From', 'To'])
    df.to_csv('towers_solution.csv', index=False)

solution_hanoi()
