import sys
import pygame as pg
#Create a variable to change current button being selected
currentBtn = 1
back = False

pg.joystick.init()
joystickEnter = False

def checkEvents(setting, screen, stats, sb, playBtn, twoPlayBtn, aboutBtn, quitBtn, menuBtn, sel, ship, aliens, bullets, eBullets):
	"""Respond to keypresses and mouse events."""
	global currentBtn
	for event in pg.event.get():
		if event.type == pg.QUIT:
			sys.exit()
		#Check for key down has been pressed
		elif event.type == pg.KEYDOWN:
			#Check if down, up, enter, esc is pressed
			if event.key == pg.K_DOWN :
				if currentBtn < 4:
					currentBtn += 1
					sel.rect.y += 50
			if event.key == pg.K_UP:
				if currentBtn > 1:
					currentBtn -= 1
					sel.rect.y -= 50
			if event.key == pg.K_RETURN:
				if currentBtn == 1:
					stats.mainMenu = False
					stats.mainGame = False
					stats.playMenu = True
					stats.mainAbout = False
					stats.twoPlayer = False
					currentBtn = 1
					sel.centery = playBtn.rect.centery
				elif currentBtn == 2:
					stats.mainMenu = False
					stats.mainAbout = False
					stats.mainGame = False
					stats.twoPlayer = True
					currentBtn = 1
					sel.rect.centery = playBtn.rect.centery
				elif currentBtn == 3:
					stats.mainMenu = False
					stats.mainAbout = True
					stats.mainGame = False
					stats.twoPlayer = False
					currentBtn = 1
					sel.rect.centery = menuBtn.rect.centery
				elif currentBtn == 4:
					sys.exit()
			if event.key == pg.K_ESCAPE:
				sys.exit()
	prepTitle(setting, screen)

def prepTitle(setting, screen):
	#Font settings for scoring information
	global image, rect
	image = pg.image.load('gfx/title_modify.png')
	rect = image.get_rect()


def drawMenu(setting, screen, sb, playBtn, menuBtn, twoPlayBtn, aboutBtn, quitBtn, sel):
	"""Draw the menu and all of its elements"""
	global image, rect
	quitBtn.rect.y = 350
	quitBtn.msgImageRect.y = 350
	menuBtn.rect.y = 450
	menuBtn.msgImageRect.y = 450
	screen.fill(setting.bgColor)
	#screen.blit(setting.bg, (0,0))
	screen.blit(image, rect)
	#screen.fill(setting.bgColor)
	#screen.blit(setting.bg, (0,0))
	playBtn.drawBtn()
	twoPlayBtn.drawBtn()
	aboutBtn.drawBtn()
	quitBtn.drawBtn()
	#sb.showScore()
	#screen.blit(image, rect)
	sel.blitme()
	pg.display.flip()
