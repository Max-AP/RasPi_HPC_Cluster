from mpi4py import MPI
import numpy as np
import time

def matrix_multiply(a, b, comm):
    rank = comm.Get_rank()
    size = comm.Get_size()

    # Calculate the number of rows for each process
    send_counts = [a.shape[0] // size + (i < a.shape[0] % size) for i in range(size)]
    send_displacements = [sum(send_counts[:i]) for i in range(size)]

    # Calculate the number of elements for each process
    send_elements = [send_counts[i] * b.shape[1] for i in range(size)]
    displacements = [send_displacements[i] * b.shape[1] for i in range(size)]

    # Split the matrix rows among nodes
    rows = send_counts[rank]
    a_split = np.array_split(a, size, axis=0)[rank]

    # Perform local matrix multiplication
    local_result = np.dot(a_split, b)

    # Gather the results from all nodes
    gather_result = None
    if rank == 0:
        gather_result = np.zeros((a.shape[0], b.shape[1]))

    comm.Gatherv(sendbuf=local_result, recvbuf=(gather_result, (send_elements, displacements)), root=0)

    return gather_result

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    matrix_size = 6000

    # Initialize matrices
    if rank == 0:
        a = np.random.rand(matrix_size, matrix_size)
        b = np.random.rand(matrix_size, matrix_size)
    else:
        a = np.empty((matrix_size, matrix_size))
        b = np.empty((matrix_size, matrix_size))

    # Broadcast matrix b to all nodes
    comm.Bcast(b, root=0)

    # Start timing
    start_time = time.time()

    # Perform matrix multiplication
    result = matrix_multiply(a, b, comm)

    # Measure time and print result
    if rank == 0:
        print(f"Time taken: {time.time() - start_time} seconds")
        print(f"Result matrix shape: {result.shape}")
        
        with open("results2", "a") as file:
            file.write("Num processes: {} seconds\nTime taken: {}\n"
            "Result matrix shape: {}\n"
            "=======================================\n"
            .format(size, time.time() - start_time, result.shape))

if __name__ == "__main__":
    main()
