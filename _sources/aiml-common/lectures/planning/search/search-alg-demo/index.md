#  Interactive Demo 

This [demo](https://qiao.github.io/PathFinding.js/visual/) is instructive of the various search algorithms we will cover here. You can introduce using your mouse obstacles in the canvas and see how the various search methods behave. 


![astar-demo](images/astar-demo.png)

*$A^*$ algorithm demo . If the demo is not shown below, click on the link above. Define the gray wall and run all the search algorithms.*


We can clearly see the substantial difference in search speed and the beamforming-effect as soon as the wave (frontier) evaluates nodes where the heuristic (the Manhattan distance from the goal node) becomes dominant. Notice the difference between A* and the UCS / Dijkstra's algorithm in the number of nodes that needed to be evaluated. 


<iframe src="https://qiao.github.io/PathFinding.js/visual/" width="900" height="1200"></iframe>


