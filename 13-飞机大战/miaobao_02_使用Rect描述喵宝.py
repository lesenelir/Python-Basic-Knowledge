import pygame

hero_rect = pygame.Rect(100, 500, 120, 125)

print("喵宝的原点 %d %d" % (hero_rect.x, hero_rect.y))
print("喵宝的尺寸 %d %d" % (hero_rect.width, hero_rect.height))
print("%d %d" % hero_rect.size )