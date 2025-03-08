import csv
import numpy as np
def solve_system(ext_mat, ret=False):
    """Solves a system of three linear equations using Cramer's Rule.
    Args:
        ext_mat (numpy.ndarray): A 3x4 augmented matrix representing the system of equations,
                                where the first three columns are the coefficients and the
                                last column contains the constants.
        ret (bool, optional): If True, returns the solution as a tuple (x, y, z).
                            If False (default), prints the solution.

    Returns:
            tuple or None: Returns (x, y, z) if `ret=True`, otherwise prints the solution.
                    If the system has no unique solution (determinant is 0), a message is printed instead.

    Example:
        ----------
        Given the system: \n
        2x + 3y - z = 5   \n 
        4x - 2y + 6z = 10 \n 
        -3x + y + 2z = -2
        
        The corresponding augmented matrix is:
        ```python
            ext_matrix = np.array([[2, 3, -1, 5], 
                                [4, -2, 6, 10], 
                                [-3, 1, 2, -2]])
        ```
    Calling:
        solve_system(ext_matrix, ret=True)

    Would return:
        (x, y, z) = (1.5, 2.0, 2.5)
    """
    det_mat = round(np.linalg.det(ext_mat[:, :3]), 2)  # Compute determinant of the coefficient matrix
    
    if det_mat != 0:
        # Compute determinants for x, y, and z matrices
        x_mat = np.column_stack((ext_mat[:, 3], ext_mat[:, 1:3]))
        det_x = round(np.linalg.det(x_mat), 2)

        y_mat = np.column_stack((ext_mat[:, 0], ext_mat[:, 3], ext_mat[:, 2]))
        det_y = round(np.linalg.det(y_mat), 2)

        z_mat = np.column_stack((ext_mat[:, 0:2], ext_mat[:, 3]))
        det_z = round(np.linalg.det(z_mat), 2)

        # Compute solutions using Cramer's Rule
        x = det_x / det_mat
        y = det_y / det_mat
        z = det_z / det_mat

        if (ret):
            return((x, y, z))
        else :
            print(f"x: {x}, y: {y}, z: {z}")
    else:
        print("The system of linear equations doesn't have a unique solution.")

def get_system_matrix_from_csv(filepath):
    """Reads a CSV file and converts it into an augmented extended matrix for a linear system.
    Parameters:
        filepath (str): Path to the CSV file containing the system of equations.
                        The file should have a header row and numerical values only.
    Returns:
        numpy.ndarray: A matrix where the first columns are coefficients, and the last column is the constant terms.
    """
    system_matrix = []

    with open(filepath) as csvfile:
        datareader = csv.reader(csvfile)
        next(datareader)
        for row in datareader:
            system_matrix.append(list(map(int, row)))

    return np.array(system_matrix).reshape([3, 4])
