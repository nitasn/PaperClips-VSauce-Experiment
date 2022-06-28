# PaperClips vs Zipf
Modeling a PaperClip experiment to demonstrate Zipf's Law.

The idea was [presented by Michael Stevens on VSauce](https://www.youtube.com/watch?v=fCn8zs912OE&t=827s) and was beautifully explained and performed by hand.

The procedure goes as follows:

    0. Start with a pile of unconnected paper clips.
    
    1. Pick any two paper clips at random.
    
    2. Link them together and throw them back in the pile. 
    
       If any of them is already part of a chain - lengthen the chain by connecting to its end.
    
    3. Repeat.


The final chains' lengths should have a pretty Zipf'ian distribution, i.e.
if laid down side by side, longest to shortest, they should like the graph of the function `f(x) = 1/x`.

Example Output:
![Example Output](https://raw.githubusercontent.com/nitasn/PaperClips_vs_Zipf/main/output-screenshot.png "Example Output")

The code uses the *Disjoint-Set* data structure (a.k.a *Union-Find*), <br />
hence each **pick-and-join operation takes O(1)** amortized time (well... almost ¹).

*¹ Actually it's `O(log* n)` (the "iterated logarithm" of n). But this function grows slower than extremely slow; <br />
If `n < 2⁶⁵˒⁵³⁶` (a number with 19,729 digits) then `log*(n) < 5`*.
