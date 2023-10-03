import random
import sys
import pygame as pg



WIDTH, HEIGHT = 1600, 900

delta = {pg.K_UP:(0,-5),pg.K_DOWN:(0,+5),pg.K_LEFT:(-5,0),pg.K_RIGHT:(+5,0)}

def check_bound(obj_rct: pg.Rect):
    """
    引数：こうかとんRectかばくだんRect
    戻り値：タプル（横方向判定結果、縦方向判定結）
    画面内ならTrue
    """
    yoko , tate= True,True
    if obj_rct.left < 0 or WIDTH <obj_rct.right:
        yoko = False
    if obj_rct.top<0 or HEIGHT < obj_rct.bottom:
        tate = False
    return yoko,tate

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_rct = kk_img.get_rect()
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk1_img = kk_img
    kk2_img =pg.transform.flip(kk_img,True,False)
    kk3_img= pg.transform.flip(kk1_img,True,False)
    kk4_img=pg.transform.rotozoom(kk3_img, -90, 1.0)
    kk3_img=pg.transform.rotozoom(kk3_img, 90, 1.0)
    kk5_img=pg.transform.rotozoom(kk_img, 45, 1.0)
    kk_rct.center = (900,400)
    
    clock = pg.time.Clock()
    """ばくだん"""
    bd_img = pg.Surface((20,20))
    bd_img.set_colorkey((0, 0, 0))
    pg.draw.circle(bd_img, (255, 0, 0), (10, 10), 10)
    bd_rct = bd_img.get_rect()
    x,y=random.randint(0,WIDTH),random.randint(0,HEIGHT)
    vx,vy=+5,+5
    bd_rct.center = (x,y)
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        screen.blit(bg_img, [0, 0])
        if kk_rct.colliderect(bd_rct):
            print("ゲームオーバー")
            return
        
        
        """こうかとん"""
        key_list = pg.key.get_pressed()
        sum_mv =[0,0]

        for key,mv in delta.items():
            if key_list[pg.K_RIGHT]:
                kk_img =kk2_img
            if key_list[pg.K_LEFT]:
                kk_img=kk1_img
            if key_list[pg.K_UP]:
                kk_img=kk3_img
            if key_list[pg.K_DOWN]:
                kk_img=kk4_img
            if key_list[key]:
                sum_mv[0] +=mv[0]
                sum_mv[1] +=mv[1]

            
        kk_rct.move_ip(sum_mv[0],sum_mv[1])
        if check_bound(kk_rct) != (True,True):
            kk_rct.move_ip(-sum_mv[0],-sum_mv[1])
        screen.blit(kk_img,kk_rct)
        """爆弾"""
        bd_rct.size=(20,20)
        bd_rct.move_ip(vx,vy)
        yoko,tate= check_bound(bd_rct)
        if not yoko:
            vx *= -1
        if not tate:
            vy *= -1
        screen.blit(bd_img,bd_rct)  
        pg.display.update()
        tmr += 1
        clock.tick(50)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()