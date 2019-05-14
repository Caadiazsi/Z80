import pygame as py


def main():
    #Buses
    AddressBus = [16]
    DataBus = [8]
    #System Control
    m1,mreq,iorq,rd,wr,rfsh = 1,1,1,1,1,1
    #CPU Control
    halt,wait,int,nmi,reset = 0,0,0,0,0
    #CPU Bus Control
    busrq,busack = 0,0
    #Clock (?)
    clk = 0
    ##Colors
    BLACK,LIGHTGREY,RED,GREEN,BLUE = (0,0,0),(100,100,100),(255,0,0),(0,255,0),(0,127,255)
    WHITE,PURPLE,LIGHTBLUE,LIGHTYELLOW = (255,255,255),(255,127,0),(153,255,255),(248,252,158)
    py.init()
    WIN_WIDTH,WIN_HEIGHT,FPS = 600,600,30
    WIN = py.display.set_mode((WIN_WIDTH+100,WIN_HEIGHT))
    py.display.set_caption("Z80 Simulator")
    CLOCK = py.time.Clock()
    loop = True
    while(loop):
        CLOCK.tick(FPS)
        WIN.fill(BLACK)
        for event in py.event.get():
            if event.type == py.QUIT:
                loop = False
        py.display.flip()
        py.display.update
    py.quit()
if __name__ == '__main__':
    main()
