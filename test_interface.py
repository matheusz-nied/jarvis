#!/usr/bin/env python3
"""
Teste da interface gráfica do Jarvis
Este script permite testar a interface visual do Jarvis independentemente do sistema principal.
Mostra dois olhos e uma boca que se movimenta quando "conversa".
"""

import pygame
import time
import math
import sys
import random

class JarvisInterface:
    def __init__(self):
        """Inicializa a interface gráfica do Jarvis."""
        pygame.init()
        # Configurações da janela
        self.width, self.height = 600, 400
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Jarvis Interface Test")
        
        # Cores
        self.background_color = (0, 0, 0)  # Fundo preto
        self.accent_color = (0, 191, 255)  # Azul brilhante (cyan)
        
        # Estados
        self.running = True
        self.talking = False
        self.blinking = False
        self.emotion = "neutral"  # neutral, happy, thinking, listening
        
        # Animações e timers
        self.last_blink = pygame.time.get_ticks()
        self.blink_interval = random.randint(2000, 5000)  # tempo em ms entre piscadas
        self.pulse_start = pygame.time.get_ticks()
        
        # Fonte para texto
        self.font = pygame.font.SysFont(None, 24)
        self.status_text = ""
    
    def draw_eyes(self):
        """Desenha os olhos com animações baseadas no estado."""
        eye_color = self.accent_color
        eye_width = 80
        eye_height = 40
        
        # Posições base dos olhos
        left_eye_pos = (self.width//2 - 100, self.height//2 - 50)
        right_eye_pos = (self.width//2 + 20, self.height//2 - 50)
        
        # Animação de piscada
        if self.blinking:
            # Durante uma piscada, reduz a altura dos olhos
            eye_height = 5
            
        # Animação de fala
        elif self.talking:
            # Pulso suave quando falando
            pulse = (math.sin(pygame.time.get_ticks() / 200) + 1) / 10
            eye_width = int(eye_width * (1 + pulse))
            eye_height = int(eye_height * (1 + pulse))
        
        # Desenho dos olhos
        pygame.draw.ellipse(self.screen, eye_color, 
                           (left_eye_pos[0], left_eye_pos[1], eye_width, eye_height))
        pygame.draw.ellipse(self.screen, eye_color, 
                           (right_eye_pos[0], right_eye_pos[1], eye_width, eye_height))
        
        # Pupilas (apenas visíveis quando não está piscando)
        if not self.blinking:
            pupil_size = 15
            # Posicionamento das pupilas baseado na emoção
            if self.emotion == "thinking":
                # Olhando para cima quando pensando
                pupil_offset_y = -8
                pupil_offset_x = 0
            elif self.emotion == "listening":
                # Olhando para o lado quando ouvindo
                pupil_offset_y = 0
                # Movimento suave das pupilas
                pupil_offset_x = int(math.sin(pygame.time.get_ticks() / 500) * 10)
            else:
                pupil_offset_y = 0
                pupil_offset_x = 0
                
            # Desenho das pupilas
            pygame.draw.circle(self.screen, self.background_color, 
                              (left_eye_pos[0] + eye_width//2 + pupil_offset_x, 
                               left_eye_pos[1] + eye_height//2 + pupil_offset_y), 
                              pupil_size)
            pygame.draw.circle(self.screen, self.background_color, 
                              (right_eye_pos[0] + eye_width//2 + pupil_offset_x, 
                               right_eye_pos[1] + eye_height//2 + pupil_offset_y), 
                              pupil_size)
    
    def draw_mouth(self):
        """Desenha a boca com animações baseadas no estado."""
        mouth_color = self.accent_color
        mouth_width = 180
        mouth_height = 60
        mouth_pos = (self.width//2 - mouth_width//2, self.height//2 + 40)
        
        if self.talking:
            # Boca animada quando falando - forma de onda
            points = []
            amplitude = 10 + abs(math.sin(pygame.time.get_ticks() / 150)) * 10
            center_y = mouth_pos[1] + 20
            
            for i in range(mouth_width):
                x = mouth_pos[0] + i
                # Onda senoidal para simular fala
                y = center_y + int(amplitude * math.sin(i/20 + pygame.time.get_ticks()/100))
                points.append((x, y))
                
            if len(points) > 1:
                pygame.draw.lines(self.screen, mouth_color, False, points, 4)
        
        elif self.emotion == "happy":
            # Sorriso quando feliz
            rect = pygame.Rect(mouth_pos[0], mouth_pos[1], mouth_width, mouth_height)
            pygame.draw.arc(self.screen, mouth_color, rect, 0, math.pi, 4)
        
        elif self.emotion == "listening":
            # Linha reta pulsante quando ouvindo
            pulse = (math.sin(pygame.time.get_ticks() / 300) + 1) / 4
            line_width = int(mouth_width * (0.8 + pulse/2))
            start_x = self.width//2 - line_width//2
            pygame.draw.line(self.screen, mouth_color, 
                            (start_x, mouth_pos[1] + 20), 
                            (start_x + line_width, mouth_pos[1] + 20), 4)
        
        else:  # neutral ou outros estados
            # Boca levemente curvada
            rect = pygame.Rect(mouth_pos[0], mouth_pos[1], mouth_width, mouth_height)
            pygame.draw.arc(self.screen, mouth_color, rect, math.pi/10, math.pi - math.pi/10, 4)
    
    def draw_status(self):
        """Desenha o texto de status, se houver."""
        if self.status_text:
            text_surface = self.font.render(self.status_text, True, self.accent_color)
            text_rect = text_surface.get_rect(center=(self.width//2, self.height - 30))
            self.screen.blit(text_surface, text_rect)
    
    def handle_blink(self):
        """Gerencia a animação de piscada."""
        current_time = pygame.time.get_ticks()
        
        # Verifica se é hora de piscar
        if current_time - self.last_blink > self.blink_interval:
            self.blinking = True
            self.last_blink = current_time
            # Varia o intervalo entre piscadas para parecer mais natural
            self.blink_interval = random.randint(2000, 5000)
        
        # Termina a piscada após 150ms
        if self.blinking and current_time - self.last_blink > 150:
            self.blinking = False
    
    def set_emotion(self, emotion):
        """Define a emoção atual da interface."""
        valid_emotions = ["neutral", "happy", "thinking", "listening"]
        if emotion in valid_emotions:
            self.emotion = emotion
    
    def set_status_text(self, text):
        """Define o texto de status."""
        self.status_text = text
    
    def start_talking(self):
        """Inicia o modo de fala."""
        self.talking = True
        self.emotion = "neutral"
        self.set_status_text("Falando...")
    
    def stop_talking(self):
        """Interrompe o modo de fala."""
        self.talking = False
        self.emotion = "neutral"
        self.set_status_text("")
    
    def start_listening(self):
        """Inicia o modo de escuta."""
        self.talking = False
        self.emotion = "listening"
        self.set_status_text("Ouvindo...")
    
    def stop_listening(self):
        """Interrompe o modo de escuta."""
        self.emotion = "neutral"
        self.set_status_text("")
    
    def start_thinking(self):
        """Inicia o modo de pensamento."""
        self.talking = False
        self.emotion = "thinking"
        self.set_status_text("Pensando...")
    
    def be_happy(self, duration=2000):
        """Mostra emoção feliz por um tempo específico (ms)."""
        self.emotion = "happy"
        self.set_status_text("Feliz!")
        
        # Após a duração, volta ao estado neutro
        pygame.time.set_timer(pygame.USEREVENT, duration)
    
    def run(self):
        """Loop principal da interface gráfica."""
        clock = pygame.time.Clock()
        
        # Instruções na tela
        instructions = [
            "Pressione as teclas para testar diferentes estados:",
            "F - Falar (talking)",
            "L - Ouvir (listening)",
            "T - Pensar (thinking)",
            "H - Feliz (happy)",
            "N - Neutro (neutral)",
            "ESC - Sair"
        ]
        
        while self.running:
            # Tratamento de eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                # Eventos de teclado para testar diferentes estados
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    elif event.key == pygame.K_f:  # Falar
                        self.start_talking()
                    elif event.key == pygame.K_l:  # Ouvir
                        self.start_listening()
                    elif event.key == pygame.K_t:  # Pensar
                        self.start_thinking()
                    elif event.key == pygame.K_h:  # Feliz
                        self.be_happy()
                    elif event.key == pygame.K_n:  # Neutro
                        self.stop_talking()
                        self.stop_listening()
                        self.emotion = "neutral"
                        self.set_status_text("")
                
                # Timer para voltar ao estado neutro após ser feliz
                elif event.type == pygame.USEREVENT:
                    self.emotion = "neutral"
                    self.set_status_text("")
                    pygame.time.set_timer(pygame.USEREVENT, 0)  # Desativa o timer
            
            # Limpa a tela
            self.screen.fill(self.background_color)
            
            # Gerencia a piscada
            self.handle_blink()
            
            # Desenha os elementos
            self.draw_eyes()
            self.draw_mouth()
            self.draw_status()
            
            # Desenha as instruções
            for i, text in enumerate(instructions):
                text_surface = self.font.render(text, True, (200, 200, 200))
                self.screen.blit(text_surface, (10, 10 + i * 25))
            
            # Atualiza a tela
            pygame.display.flip()
            clock.tick(30)  # 30 FPS
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    interface = JarvisInterface()
    interface.run()
