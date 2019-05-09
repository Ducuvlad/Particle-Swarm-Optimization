from Controller import run
import matplotlib.pyplot as plt



    
def main():
    f = open("params.in", 'r')
    target_error = float(f.readline().split("=")[1])
    w = float(f.readline().split("=")[1])
    c1 = float(f.readline().split("=")[1])
    c2 = float(f.readline().split("=")[1])
    n_particles = int(f.readline().split("=")[1])
    n_iterations = int(f.readline().split("=")[1])
    f.close()
    gbestpos,iter,fitness=run(target_error, n_particles,c1,c2,w,n_iterations)
    print("The best solution is: ", gbestpos, " in n_iterations: ", iter)

    plt.plot(range(iter), fitness, label='BestFitness vs iteration')

    plt.xlabel('Iteration')
    plt.ylabel('BestFitness')
    plt.title("BestFitness evolution")
    plt.legend()
    plt.show()
if __name__ == "__main__":
    main()