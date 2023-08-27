# Air Hockey

<p align="center">
  <img src="images\air_hockey.jpg" width="700">
</p>





Air hockey is a Pong-like tabletop sport where two opposing players try to score goals against each other on a low-friction table using two hand-held discs ("mallets") and a lightweight plastic puck.

I was thinking it would be fun to implement the game with Python,
therefore I was thrilled and started coding.

I have implemented few functions, an explanation of each function is written here below:

| Function                  | Short explanation                                                                                                               |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| is_disc_hit_the_wall      | I would like to check if the disc has hit the wall, if so the disc direction will get changed in both axis (x,y).               |
| is_disc_reached_gate      | I would like to check if the disc reached one of the gates, the disc's value of x and y should be checked with the constraints. |
| is_racket_protecting_gate | The purpose of the racket to protect the gate, therefore we check if racket is positioned in the area of the gate.              |
| init_stage                | After each phase the disc is positioned in the center of the stage and the players start again playing.                         |
| show_score_board          | Shows the score for each player during the game with large font                                                                 |

<p align="center">
  <img src="images\Flowchart.png" width="700">
</p>


The result of coding the game: 

<p align="center">
  <img src="images\ice_hockey.gif" width="700">
</p>