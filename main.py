import sys
import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GLUT.fonts import GLUT_BITMAP_HELVETICA_18
import numpy as np


# Inicializando as variáveis globais para os ângulos de cada parte do robô
angle_head = 0
angle_neck = 0
angle_torso = 0
angle_upper_arm_left = -15
angle_forearm_left = 0
angle_hand_left = 0
angle_pincer_left = [0, 0]
angle_upper_arm_right = 15
angle_forearm_right = 0
angle_hand_right = 0
angle_pincer_right = [0, 0]
angle_thigh_left = 0
angle_leg_left = 0
angle_foot_left = 0
angle_thigh_right = 0
angle_leg_right = 0
angle_foot_right = 0

# Função para desenhar um quadrado


def DesenhaQuadrado():
    glBegin(GL_QUADS)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.5, 0.5)
    glVertex2f(-0.5, 0.5)
    glEnd()

# Funções para desenhar cada parte do corpo do robô


def DesenhaCabeca():
    glPushMatrix()
    glScalef(0.4, 0.4, 1.0)
    DesenhaQuadrado()
    glPopMatrix()


def DesenhaPescoco():
    glPushMatrix()
    glScalef(0.2, 0.4, 1.0)
    DesenhaQuadrado()
    glPopMatrix()


def DesenhaTronco():
    glPushMatrix()
    glScalef(0.8, 1.2, 1.0)
    DesenhaQuadrado()
    glPopMatrix()


def DesenhaBraco():
    glPushMatrix()
    glScalef(0.2, 0.6, 1.0)
    DesenhaQuadrado()
    glPopMatrix()


def DesenhaAntebraco():
    glPushMatrix()
    glScalef(0.2, 0.6, 1.0)
    DesenhaQuadrado()
    glPopMatrix()


def DesenhaMao():
    glPushMatrix()
    glScalef(0.2, 0.2, 1.0)
    DesenhaQuadrado()
    glPopMatrix()


def DesenhaPinca():
    glPushMatrix()
    glScalef(0.1, 0.3, 1.0)
    DesenhaQuadrado()
    glPopMatrix()


def DesenhaCoxa():
    glPushMatrix()
    glScalef(0.3, 0.7, 1.0)
    DesenhaQuadrado()
    glPopMatrix()


def DesenhaPerna():
    glPushMatrix()
    glScalef(0.3, 0.7, 1.0)
    DesenhaQuadrado()
    glPopMatrix()


def DesenhaPe():
    glPushMatrix()
    glScalef(0.4, 0.2, 1.0)
    DesenhaQuadrado()
    glPopMatrix()

# Função que desenha o robô inteiro


def DesenhaRobo():
    global angle_head, angle_neck, angle_torso
    global angle_upper_arm_left, angle_forearm_left, angle_hand_left, angle_pincer_left
    global angle_upper_arm_right, angle_forearm_right, angle_hand_right, angle_pincer_right
    global angle_thigh_left, angle_leg_left, angle_foot_left
    global angle_thigh_right, angle_leg_right, angle_foot_right

    # Desenha o tronco
    glPushMatrix()
    glRotatef(angle_torso, 0, 0, 1)
    DesenhaTronco()

    # Desenha o pescoço
    glPushMatrix()
    glTranslatef(0.0, 0.8, 0.0)
    glRotatef(angle_neck, 0, 0, 1)
    DesenhaPescoco()

    # Desenha a cabeça
    glTranslatef(0.0, 0.3, 0.0)
    glRotatef(angle_head, 0, 0, 1)
    DesenhaCabeca()
    glPopMatrix()  # Final do pescoço e cabeça

    # Desenha o braço esquerdo
    glPushMatrix()
    glTranslatef(-0.56, 0.3, 0.0)
    glRotatef(angle_upper_arm_left, 0, 0, 1)
    DesenhaBraco()

    glTranslatef(0.0, -0.6, 0.0)
    glRotatef(angle_forearm_left, 0, 0, 1)
    DesenhaAntebraco()

    glTranslatef(0.0, -0.4, 0.0)
    glRotatef(angle_hand_left, 0, 0, 1)
    DesenhaMao()

    # Desenha os dedos da mão esquerda
    glPushMatrix()
    glTranslatef(-0.1, -0.2, 0.0)
    glRotatef(angle_pincer_left[0], 0, 0, 1)
    DesenhaPinca()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.1, -0.2, 0.0)
    glRotatef(angle_pincer_left[1], 0, 0, 1)
    DesenhaPinca()
    glPopMatrix()

    glPopMatrix()  # Final do braço esquerdo

    # Desenha o braço direito
    glPushMatrix()
    glTranslatef(0.56, 0.3, 0.0)
    glRotatef(angle_upper_arm_right, 0, 0, 1)
    DesenhaBraco()

    glTranslatef(0.0, -0.6, 0.0)
    glRotatef(angle_forearm_right, 0, 0, 1)
    DesenhaAntebraco()

    glTranslatef(0.0, -0.4, 0.0)
    glRotatef(angle_hand_right, 0, 0, 1)
    DesenhaMao()

    # Desenha os dedos da mão direita
    glPushMatrix()
    glTranslatef(-0.1, -0.2, 0.0)
    glRotatef(angle_pincer_right[0], 0, 0, 1)
    DesenhaPinca()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.1, -0.2, 0.0)
    glRotatef(angle_pincer_right[1], 0, 0, 1)
    DesenhaPinca()
    glPopMatrix()

    glPopMatrix()  # Final do braço direito

    # Desenha a perna esquerda
    glPushMatrix()
    glTranslatef(-0.3, -0.6, 0.0)
    glRotatef(angle_thigh_left, 0, 0, 1)
    DesenhaCoxa()

    glTranslatef(0.0, -0.7, 0.0)
    glRotatef(angle_leg_left, 0, 0, 1)
    DesenhaPerna()

    glTranslatef(0.0, -0.4, 0.0)
    glRotatef(angle_foot_left, 0, 0, 1)
    DesenhaPe()

    glPopMatrix()  # Final da perna esquerda

    # Desenha a perna direita
    glPushMatrix()
    glTranslatef(0.3, -0.6, 0.0)
    glRotatef(angle_thigh_right, 0, 0, 1)
    DesenhaCoxa()

    glTranslatef(0.0, -0.7, 0.0)
    glRotatef(angle_leg_right, 0, 0, 1)
    DesenhaPerna()

    glTranslatef(0.0, -0.4, 0.0)
    glRotatef(angle_foot_right, 0, 0, 1)
    DesenhaPe()

    glPopMatrix()  # Final da perna direita

    glPopMatrix()  # Final do tronco


def key_callback(window, key, scancode, action, mods):
    global angle_head, angle_neck, angle_torso
    global angle_upper_arm_left, angle_forearm_left, angle_hand_left, angle_pincer_left
    global angle_upper_arm_right, angle_forearm_right, angle_hand_right, angle_pincer_right
    global angle_thigh_left, angle_leg_left, angle_foot_left
    global angle_thigh_right, angle_leg_right, angle_foot_right

    if action == glfw.PRESS or action == glfw.REPEAT:
        # Cabeça
        if key == glfw.KEY_1:
            angle_head += 5
        elif key == glfw.KEY_2:
            angle_head -= 5

        # Tronco
        elif key == glfw.KEY_3:
            angle_torso += 5
        elif key == glfw.KEY_4:
            angle_torso -= 5

        # Braço Direito
        elif key == glfw.KEY_Q:
            angle_upper_arm_right += 5
        elif key == glfw.KEY_W:
            angle_upper_arm_right -= 5
        elif key == glfw.KEY_E:
            angle_forearm_right += 5
        elif key == glfw.KEY_R:
            angle_forearm_right -= 5
        elif key == glfw.KEY_T:
            angle_hand_right += 5
        elif key == glfw.KEY_Y:
            angle_hand_right -= 5
        elif key == glfw.KEY_U:
            angle_pincer_right[0] += 5
        elif key == glfw.KEY_I:
            angle_pincer_right[0] -= 5

        # Braço Esquerdo
        elif key == glfw.KEY_A:
            angle_upper_arm_left += 5
        elif key == glfw.KEY_S:
            angle_upper_arm_left -= 5
        elif key == glfw.KEY_D:
            angle_forearm_left += 5
        elif key == glfw.KEY_F:
            angle_forearm_left -= 5
        elif key == glfw.KEY_G:
            angle_hand_left += 5
        elif key == glfw.KEY_H:
            angle_hand_left -= 5
        elif key == glfw.KEY_J:
            angle_pincer_left[0] += 5
        elif key == glfw.KEY_K:
            angle_pincer_left[0] -= 5

        # Perna Direita
        elif key == glfw.KEY_Z:
            angle_thigh_right += 5
        elif key == glfw.KEY_X:
            angle_thigh_right -= 5
        elif key == glfw.KEY_C:
            angle_leg_right += 5
        elif key == glfw.KEY_V:
            angle_leg_right -= 5
        elif key == glfw.KEY_B:
            angle_foot_right += 5
        elif key == glfw.KEY_N:
            angle_foot_right -= 5

        # Perna Esquerda
        elif key == glfw.KEY_M:
            angle_thigh_left += 5
        elif key == glfw.KEY_COMMA:
            angle_thigh_left -= 5
        elif key == glfw.KEY_PERIOD:
            angle_leg_left += 5
        elif key == glfw.KEY_SLASH:
            angle_leg_left -= 5
        elif key == glfw.KEY_SEMICOLON:
            angle_foot_left += 5
        elif key == glfw.KEY_LEFT_BRACKET:
            angle_foot_left -= 5

# Função para desenhar texto na tela


def draw_text(position, text, font=GLUT_BITMAP_HELVETICA_18):
    glRasterPos2f(*position)
    for character in text:
        glutBitmapCharacter(font, ord(character))

# Função para desenhar as instruções


def draw_instructions():
    instructions = [
        "Cabeça: 1/2",
        "Tronco: 3/4",
        "Braço Dir: Q/W (Superior), E/R (Antebraço), T/Y (Mão), U/I (Pinças)",
        "Braço Esq: A/S (Superior), D/F (Antebraço), G/H (Mão), J/K (Pinças)",
        "Perna Dir: Z/X (Coxa), C/V (Perna), B/N (Pé)",
        "Perna Esq: M/, (Coxa), ./? (Perna), ;/[ (Pé)"
    ]

    glColor3f(1, 1, 1)
    y_offset = 2.7  # Posição inicial no eixo Y
    for instruction in instructions:
        draw_text((-3, y_offset), instruction)
        y_offset -= 0.2

# Função principal


def main():
    if not glfw.init():
        return
    window = glfw.create_window(800, 600, "Robô Interativo", None, None)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)

    # Inicializando o GLUT
    glutInit(sys.argv)

    glClearColor(0.5, 0.5, 0.5, 1.0)

    # Configurando a projeção ortográfica
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-3, 3, -3, 3, -2, 2)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)

        glPushMatrix()
        glTranslatef(0.0, -1.2, 0.0)  # Posição inicial do robô
        DesenhaRobo()
        glPopMatrix()

        # Desenhar instruções
        glPushMatrix()
        glLoadIdentity()
        draw_instructions()
        glPopMatrix()

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    main()
