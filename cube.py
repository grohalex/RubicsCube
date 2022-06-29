# Rubic's cube solver
# 0 - white, 1 - yellow, 2 - green, 3 - red, 4 - blue, 5 - orange

class cube:
    def __init__(self,CubeState='random'):
        self.state = [  [[0,0,0],[0,0,0],[0,0,0]],
                        [[1,1,1],[1,1,1],[1,1,1]],
                        [[2,2,2],[2,2,2],[2,2,2]],
                        [[3,3,3],[3,3,3],[3,3,3]],
                        [[4,4,4],[4,4,4],[4,4,4]],
                        [[5,5,5],[5,5,5],[5,5,5]]
                    ]
        if CubeState == 'random':
            pass

    def Print(self):
        W = '\033[107m'  # white
        Y = '\033[103m'#yellow
        R = '\033[101m' # red
        G = '\033[42m' # green
        B = '\033[44m' # blue
        O = '\033[45m' # orange
        N = '\033[0m'  # normal

        sides = range(0,6)
        for side in sides:
            for row in range(0,3):
                print("\n", end='')
                for e in self.state[side][row]:
                    #print(e)
                    if e==0:
                        print(W + str(e) + N, end='')
                    if e==1:
                        print(Y + str(e) + N, end='')
                    if e==2:
                        print(G + str(e) + N, end='')
                    if e==3:
                        print(R + str(e) + N, end='')
                    if e==4:
                        print(B + str(e) + N, end='')
                    if e==5:
                        print(O + str(e) + N, end='')

    def Shuffle(self, moves=50):
        pass



    #  modifies the state of the cube according to the selected move
    #  side: 0 - white, 1 - yellow, 2 - green, 3 - red, 4 - blue, 5 - orange
    #  move:
    #            0^  1^
    #            | | | | -> 2
    #            | | | |
    #            | | | | -> 3

    def Move(self, side, move):
        pass
    '''
        #white side
        if side == 0:
            if move==0:
                #self.state =
            elif move==1:

            elif move==2:

            elif move==3:


        #yellow side
        elif side == 1:


        #green side
        elif side == 2:

        #red side
        elif side == 3:

        #blue side
        elif side == 4:

        #orange site
        elif side == 5:
    '''

a = cube(CubeState='clear')
#print(a.state[0],a.state[1], a.state[2])

a.Print()
