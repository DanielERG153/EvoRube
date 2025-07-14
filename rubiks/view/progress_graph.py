import multiprocessing as mp
import matplotlib.pyplot as plt

def graph_process(queue):
    plt.ion()  # Interactive mode for live updates
    fig, ax = plt.subplots()
    steps = []
    scores = []
    line, = ax.plot(steps, scores, 'b-')
    ax.set_xlabel('Steps')
    ax.set_ylabel('Score')
    ax.set_title('Progress Graph')
    while True:
        data = queue.get()
        if data is None:  # End signal
            plt.ioff()
            plt.show(block=True)  # Keep open at end
            break
        step, score = data
        steps.append(step)
        scores.append(score)
        line.set_xdata(steps)
        line.set_ydata(scores)
        ax.relim()
        ax.autoscale_view()
        fig.canvas.draw()
        fig.canvas.flush_events()