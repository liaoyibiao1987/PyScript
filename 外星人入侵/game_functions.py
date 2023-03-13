import sys
from bullet import Bullet
import pygame

def check_keydown_events(event,ai_settings,screen,ship,bullets) :
    if event.key == pygame.K_RIGHT :
        ship.moving_right = True
    elif event.key == pygame.K_LEFT :
        ship.moving_left = True
    elif event.key == pygame.K_SPACE :
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)
 
def check_keyup_events(event,ship) :
    if event.key == pygame.K_RIGHT:
         ship.moving_right = False
    elif event.key == pygame.K_LEFT :
         ship.moving_left = False
 
def check_events(ai_settings, screen, stats,play_button,ship,aliens, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN :
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,play_button,ship,aliens,bullets,mouse_x,mouse_y)
 
def check_play_button(ai_settings,screen,stats,play_button,ship,aliens,bullets,mouse_x,mouse_y) :
    #在玩家点击play按钮时开始游戏
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if  button_clicked and not stats.game_active :
        #隐藏光标
        pygame.mouse.set_visible(False)
        #重置游戏信息
        stats.reset_stats()
        stats.game_active = True
 
        #清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()
 
        #创建一群新的外星人，并让飞船居中
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
 
def update_screen(ai_settings, screen,stats, ship, aliens, bullets,play_button):
    """Update images on the screen, and flip to the new screen."""
    # Redraw the screen, each pass through the loop.
    screen.fill(ai_settings.bg_color)
     
    # Redraw all bullets, behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    if not stats.game_active :
        play_button.draw_button()
     
    # Make the most recently drawn screen visible.
    pygame.display.flip()

def create_fleet(settings,screen,ship,aliens):
    pass
def update_bullets(ai_settings, screen, ship, aliens, bullets):
    pass
def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    pass