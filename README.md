# PaperClips vs Zipf
Modeling a PaperClip experiment to demonstrate Zipf's Law.

The idea was [presented by Michael Stevens on VSauce](https://www.youtube.com/watch?time_continue=86&v=fCn8zs912OE) and was beautifully explained and performed by hand.

The procedure goes as follows:

    0. Start with a pile of unconnected paper clips.
    
    1. Pick two paper clips at random.
    
    2. Link them together and throw them back in the pile. 
    
       If each of them is already part of its own chain, connect the two chains into a one long chain.
    
    3. Repeat.


The final chains' lengths should have a pretty Zipf'ian distribution, i.e.
if laid down side by side, longest to shortest, they should like the graph of the function `f(x) = 1/x`.

Example Output:
![Example Output](https://raw.githubusercontent.com/nitasn/PaperClips_vs_Zipf/main/output-screenshot.png "Example Output")

Also,
The code uses the *Disjoint-Set* data structure (a.k.a *Union-Find*), 
hence each **pick-and-join operation takes O(1)** amortized time¹.

*¹ Actually it's `O(log* n)`. But `log*` grows slower than extremely slow;
if `n < 2^65,536` (a number with 19,729 digits) then `log*(n) < 5`*
