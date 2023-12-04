from mpi4py import MPI
import time
import random

def compute_pi(points, start_seed):
    random.seed(start_seed)
    inside_circle = 0
    for _ in range(points):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1.0:
            inside_circle += 1
    return inside_circle

def main():
    # Initialize MPI
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    # Number of points to use for the Pi estimation
    total_points = 1000000000
    points_per_process = total_points // size

    # Seed for random number generation to vary between processes
    seed = rank * (total_points // size)

    # Sync all processes before timing
    comm.Barrier()
    
    # Start the timer
    start_time = time.time() if rank == 0 else None

    # Scatter workload
    local_points = points_per_process
    local_count = compute_pi(local_points, seed)

    # Gather results
    counts = comm.gather(local_count, root=0)

    # Stop the timer and process results on the root
    if rank == 0:
        total_time = time.time() - start_time
        pi_estimate = (4.0 * sum(counts)) / total_points
        print(f"Estimated Pi: {pi_estimate}")
        print(f"Time taken: {total_time} seconds")
        print(f"Accuracy of the result: {abs(pi_estimate - 3.141592653589793)}")
        with open("results", "a") as file:
            file.write("Num processes: {}\nEstimated Pi: {}\n"
            "Time taken: {} seconds\nAccuracy of the result: {}\n"
            "=======================================\n"
            .format(size, pi_estimate, total_time, 
            abs(pi_estimate - 3.141592653589793)))

if __name__ == "__main__":
    main()

