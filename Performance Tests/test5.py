from mpi4py import MPI
import numpy as np
import time
from alive_progress import alive_bar

def matrix_multiply(A, B, C, rows_per_process, progress_bar):
    for i in range(rows_per_process):
        for j in range(B.shape[1]):
            for k in range(B.shape[0]):
                C[i, j] += A[i, k] * B[k, j]
            progress_bar()  # Update the progress bar after each row is processed

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    matrix_size = 500  # Define the size of the matrix
    A = None
    B = None

    if rank == 0:
        A = np.random.rand(matrix_size, matrix_size)
        B = np.random.rand(matrix_size, matrix_size)

    A = comm.bcast(A, root=0)
    B = comm.bcast(B, root=0)

    rows_per_process = matrix_size // size + (rank < matrix_size % size)
    start_row = sum(matrix_size // size + (i < matrix_size % size) for i in range(rank))
    end_row = start_row + rows_per_process

    local_A = A[start_row:end_row, :]
    local_C = np.zeros((rows_per_process, B.shape[1]))

    with alive_bar(rows_per_process * B.shape[1], title=f'Node {rank}') as bar:
        start_time = time.time()
        matrix_multiply(local_A, B, local_C, rows_per_process, bar)
        total_time = time.time() - start_time

    all_C = comm.gather(local_C, root=0)

    if rank == 0:
        C = np.vstack(all_C)
        print("Matrix multiplication completed.")
        print("Time taken: {:.2f} seconds".format(total_time))

if __name__ == "__main__":
    main()
