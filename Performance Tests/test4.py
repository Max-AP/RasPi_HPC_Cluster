from mpi4py import MPI
import numpy as np
import time

def matrix_multiply(A, B):
    return np.dot(A, B)

def main():
    # Initialize MPI
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    # Matrix dimensions (example)
    N = 2250

    # Generate matrices on the master node
    if rank == 0:
        A = np.random.rand(N, N).astype(np.float64)
        B = np.random.rand(N, N).astype(np.float64)
    else:
        A = None
        B = np.empty([N, N], dtype=np.float64)  # Ensure B has the same shape and type on all nodes

    # Broadcast matrix B to all nodes
    comm.Bcast(B, root=0)

    # Calculate the number of rows each process will handle
    rows_per_node = N // size
    remainder = N % size
    sendcounts = [(rows_per_node + (1 if i < remainder else 0)) * N for i in range(size)]
    displacements = [sum(sendcounts[:i]) for i in range(size)]

    # Prepare a buffer for receiving rows of A
    A_section = np.empty((sendcounts[rank] // N, N), dtype=np.float64)

    # Scatter rows of matrix A to all nodes
    if rank == 0:
        A = A.flatten()  # Flatten the matrix for scattering
    comm.Scatterv([A, sendcounts, displacements, MPI.DOUBLE], A_section, root=0)

    # Start timer
    start_time = time.time()

    # Perform matrix multiplication
    C_section = matrix_multiply(A_section, B)

    # Prepare buffer for gathering results
    C_gathered = None
    if rank == 0:
        C_gathered = np.empty([N, N], dtype=np.float64)

    # Gather the results back
    comm.Gatherv(C_section, [C_gathered, sendcounts, displacements, MPI.DOUBLE], root=0)

    # Finalize MPI
    MPI.Finalize()
    
    # End timer and print time taken if master node
    if rank == 0:
        print(f"Time taken: {time.time() - start_time} seconds")


if __name__ == "__main__":
    main()
