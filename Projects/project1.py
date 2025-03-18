###############################################
### SETUP ###
import codesters

from codesters import StageClass
stage = StageClass()
###############################################
stage.set_background("summer")
q1 = codesters.Square (100, 100, 200, 'dodger blue')
q2 = codesters.Square (-100, 100, 200, 'cornflower blue')
q3 = codesters.Square (-100, -100, 200, 'light sky blue')
q4 = codesters.Square (100, -100, 200, 'deep sky blue')

s1 = codesters.Sprite ("softball2", 100,100)
s1.set_size(0.2)
s2 = codesters.Sprite ("Mountains", -100,100)
s2.set_size(0.2)
s3 = codesters.Sprite ("music", 100,-100)
s3.set_size(0.1)
s4 = codesters.Sprite ("cardinal", -100, -100)

message1 = codesters.Text ("Maggie Parks", 0,220, "black")
message2 = codesters.Text ("This is my message", 0, -200, "black")