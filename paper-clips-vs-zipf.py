"""
this is a model of the paper clips pile mathematical experiment, probing zipf's law,
as presented by Vsauce here: https://www.youtube.com/watch?time_continue=86&v=fCn8zs912OE

the procedure goes as follows:

    0. start with a pile of paper clips.

    1. pick two paper clips randomly.

    2. link them together (if a paperclip already belongs to a chain, make the chain longer).

    3. drop the new (or prolonged) chain back to the pile.

    4. repeat. a couple of times. about half the number of paper clips (? how many times, really?)


the final chains' lengths should have a pretty zipf'ly distribution, i.e.
if laid down side by side, longest to shortest, it should like the graph of the function f(x) = 1/x * constant
"""

P = 5_000_000  # num of paper clips
N = 2_500_000  # num of pick-up-&-link operations to perform

CHAINS_TO_PLOT = 90  # only draw this number of the first longest chains

"""
TL;DR
every pick-up-&-link operation is O(1) (amortized).

a pile is modeled using an upside down tree:
the root's address (__id__) is the name of the pile;
a paperclip is a node; it points to its parent, which points to its parent, ..., which points to the root.

also, every time a node is queried for its root, 
we set its parent to be the root itself, to make the next query quicker.

linking piles is done by telling one the two involved roots that it is a son of the other root.

total time it takes to perform n links = O(n log*n), which is practically O(n), 
because if n < 2^65,536 (a number with 19,729 digits) then log*(n) < 5.
"""


class PaperClip:
    """
    a node in the up-pointing tree.
    """

    def __init__(self):
        self.parent = self
        self.rank = 0  # normal rank, i.e. 1 + height of highest son.

    def get_root(self):
        """
        gets the root, and while so, makes every node in the way point to the root directly, to quicken future look ups.
        """
        nodes_visited = []
        node = self

        while node.parent != node:
            nodes_visited.append(node)
            node = node.parent

        root = node

        for node_visited in nodes_visited:
            node_visited.parent = root

        return root

    def link(self, paper_clip):
        """
        merge two chains given a representative from each chain.
        """
        self_root, their_root = self.get_root(), paper_clip.get_root()

        if self_root != their_root:

            if self_root.rank > their_root.rank:
                their_root.parent = self_root

            elif their_root.rank > self_root.rank:
                self_root.parent = their_root

            else:  # if self_root.rank == their_root.rank:
                their_root.parent = self_root
                self_root.rank += 1


def merge_some_chains():
    """
    creates P paperclips, then N times links two random ones.
    :return: a list of paper_clips, inter-connected via shared parents and roots.
    """
    from random import randrange

    paper_clips = [PaperClip() for _ in range(P)]

    for _ in range(N):

        i, j = randrange(P), randrange(P - 1)

        if j == i:  # picking up two different paper clips
            j = P - 1

        paper_clips[i].link(paper_clips[j])

    return paper_clips


def measure_chains(paper_clips):
    """
    asks each paper clip for their root and sums up answers.
    :param paper_clips: result of the function merge_some_chains.
    :return: list of lengths of chains, sorted largest to smallest.
    """
    from collections import defaultdict
    lengths_dict = defaultdict(int)

    for paper_clip in paper_clips:
        root = paper_clip.get_root()
        lengths_dict[id(root)] += 1

    return sorted(lengths_dict.values(), reverse=True)


def show_statistics(chains):
    """
    plot a nice graph of the final chains' lengths.
    :param chains: measure_chains's result: numbers, sorted highest to lowest
    """
    import matplotlib.pyplot as plt
    import numpy as np

    def prettify(num: int) -> str:
        """ turn 200000 into '200,000' """
        return "{:,}".format(num)

    column_width = np.sqrt(30 / CHAINS_TO_PLOT)

    plt.axis([column_width, CHAINS_TO_PLOT + column_width, 0, 1])

    plt.gcf().canvas.manager.set_window_title('Paper-Clip Chains vs. Zipf\'s Law')

    plt.xlabel('rank of the chain\'s length')
    plt.ylabel('length of the chain / length of longest chain')

    plt.title(
        'the final chains, from longest to shortest,' + '\n' +
        'vs. the curve y=1/x for comparison.'
    )

    plt.gcf().text(0.5, 0.6,
                   'num paper clips: ' + prettify(P) + '\n' +
                   'num links: ' + prettify(N) + '\n' +
                   'length of longest chain: ' + prettify(chains[0]))

    xs = np.arange(1, CHAINS_TO_PLOT, step=0.01)
    ys = 1 / xs
    plt.plot(xs, ys, lw=2, color='black')

    for x, chain in enumerate(chains[:CHAINS_TO_PLOT]):  # iterate only over the longest chains
        y = chain / chains[0]
        # plot each chain's length compared to the longest chain's length, which gets the value 1.
        plt.bar(x + 1, y, width=column_width)

    plt.show()


def main():
    print('performing paper-clips experiment (should take ~10 seconds)...')
    paper_clips = merge_some_chains()
    print('measuring chains\'s lengths...')
    clips_lengths = measure_chains(paper_clips)
    print('plotting the results...')
    show_statistics(clips_lengths)


if __name__ == '__main__':
    main()
