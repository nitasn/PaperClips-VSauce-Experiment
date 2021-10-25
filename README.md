# PaperClips vs Zipf
Modeling a PaperClip experiment to demonstrate Zipf's Law, as suggested by Michal Stevens from VSause.

The idea was [presented by Michael Stevens on VSauce](https://www.youtube.com/watch?time_continue=86&v=fCn8zs912OE), and parts from this description are transcribed from the video's narration.


    The procedure goes as follows:

    0. Start with a pile of unconnected paper clips.
    
    1. Pick two paper clips at random.
    
    2. Link them together and throw them back in the pile. 
       If you grab paper clips that are already part of a chain, link ‘em anyway.
    
    4. Repeat.


The final chains' lengths should have a pretty zipf'ian distribution, i.e.
if laid down side by side, longest to shortest, they should like the graph of the function f(x) = 1/x.
