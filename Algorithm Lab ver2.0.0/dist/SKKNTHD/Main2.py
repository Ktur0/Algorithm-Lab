import pygame
import time
import random
import pyperclip
import numpy as np
import matplotlib.pyplot as plt

from Search.covertstr import *
from Sort.bubblesort import *
from Sort.quicksort import *
from Sort.mergesort import *
from Sort.heapsort import *
from Sort.cocktailsort import *
from Search.show_parameter_search import *
from Sort.insertionsort import *
from Search.interpolation_search import *
from Search.binary_search import *
from Search.sequential_search import *
from Search.jump_search import *
from Search.BFS import *
from Search.DFS import *
from Sort.drawarray import *
from Search.auto_solve_maze import *
from Search.mazeplayer import finding_game_player
from Sort.convertstrtolist import *

pygame.init()

# Set up

icon = pygame.image.load('SKKNTHD/Image/logo - Copy.png')
screen_width,screen_height = 1067,600
screen = pygame.display.set_mode((screen_width,screen_height))
x_mouse,y_mouse = 0,0
mouse_box = pygame.Rect(x_mouse,y_mouse,20,20)
run = True
main_menu = True
setting_menu_on = False
pygame.display.set_icon(icon)
pygame.display.set_caption('CodeSimulate THĐ')

# Text
copy_message_font = pygame.font.Font('SKKNTHD/Font/ClearSans-Bold.ttf',40)
number_message_font = pygame.font.Font('SKKNTHD/Font/ClearSans-Bold.ttf',40)
number_message_font_arr = pygame.font.Font('SKKNTHD/Font/ClearSans-Bold.ttf',25)
number_message_end_font = pygame.font.Font('SKKNTHD/Font/ClearSans-Bold.ttf',100)
font_for_finding_game = pygame.font.Font('SKKNTHD/Font/ClearSans-Bold.ttf',60)

# Image
background = pygame.image.load('SKKNTHD/Image/backgroundmenu.jpg')

sortmenu_background = pygame.image.load('SKKNTHD/Image/sortmenu.jpg')
quicksort_image = pygame.image.load('SKKNTHD/Image/quicksort1.jpg')
heapsort_image = pygame.image.load('SKKNTHD/Image/heapsort1.jpg')
mergesort_image = pygame.image.load('SKKNTHD/Image/mergesort1.jpg')
bubblesort_image = pygame.image.load('SKKNTHD/Image/bubblesort1.jpg')
cocktailsort_image = pygame.image.load('SKKNTHD/Image/cocktailsort1.jpg')
insertionsort_image = pygame.image.load('SKKNTHD/Image/insertionsort1.jpg')

searchmenu_background = pygame.image.load('SKKNTHD/Image/searchmenu.jpg')
binarysearch_image = pygame.image.load('SKKNTHD/Image/binarysearch1.jpg')
sequentialsearch_image = pygame.image.load('SKKNTHD/Image/sequentialsearch1.jpg')
jumpsearch_image = pygame.image.load('SKKNTHD/Image/jumpsearch1.jpg')
interpolationsearch_image = pygame.image.load('SKKNTHD/Image/interpolationsearch1.jpg')
bfs_image = pygame.image.load('SKKNTHD/Image/bfs1.jpg')
dfs_image = pygame.image.load('SKKNTHD/Image/dfs1.jpg')

sortgamemenu = pygame.image.load('SKKNTHD/Image/wining.jpg')
sortgamemainmenu = pygame.image.load('SKKNTHD/Image/sortgamemainmenu.jpg')
sortgameplay = pygame.image.load('SKKNTHD/Image/sortgameplaymenu.jpg')

findinggame_image = pygame.image.load('SKKNTHD/Image/findinggame_select_mode.jpg')
finding_gameplay_bot = pygame.image.load('SKKNTHD/Image/finding_gameplay_bot.jpg')
finding_gameplay_player = pygame.image.load('SKKNTHD/Image/finding_gameplay_player.jpg')

help_image_1 = pygame.image.load('SKKNTHD/Image/help1.jpg')
help_image_2 = pygame.image.load('SKKNTHD/Image/help2.jpg')
help_image_3 = pygame.image.load('SKKNTHD/Image/help3.jpg')
help_image_4 = pygame.image.load('SKKNTHD/Image/help4.jpg')
help_image_5 = pygame.image.load('SKKNTHD/Image/help5.jpg')

# Buttons
sort_button = pygame.Rect(110,340,320,150)
search_button = pygame.Rect(660,340,320,150)
game_button = pygame.Rect(855,28,75,30)
helpbutton = pygame.Rect(940,28,75,30)
homebutton = pygame.Rect(770,28,75,30)
close_button = pygame.Rect(965,110,30,30)

show_parameter = pygame.Rect(1000,520,50,50)
copy_button = pygame.Rect(1000,465,50,50)
tutorial_button = pygame.Rect(1000,410,50,50)
tutorial_button_sorting_game = pygame.Rect(1000,80,50,50)
back_button = pygame.Rect(25,90,100,50)
chest = pygame.Rect(338,150,405,350)
length_button = pygame.Rect(530,514,110,55)
slow_button = pygame.Rect(810,514,130,55)
arr_button = pygame.Rect(35,525,295,40)
graph_button = pygame.Rect(150,514,800,70)

bubblesort_button = pygame.Rect(135, 215 , 370, 88)
insertionsort_button = pygame.Rect(535, 215 , 370, 88)
heapsort_button = pygame.Rect(135, 340 , 370, 88)
cocktailsort_button = pygame.Rect(535, 340 , 370, 88)
quicksort_button = pygame.Rect(135, 465 , 370, 88)
mergesort_button = pygame.Rect(535, 465 , 370, 88)

sequentialsearch_button = pygame.Rect(135, 215 , 370, 88)
interpolationsearch_button = pygame.Rect(535, 215 , 370, 88)
binarysearch_button = pygame.Rect(135, 340 , 370, 88)
jumpsearch_button = pygame.Rect(535, 340 , 370, 88)
bfs_button = pygame.Rect(135, 465 , 370, 88)
dfs_button = pygame.Rect(535, 465 , 370, 88)

search_button_game = pygame.Rect(385,350,300,170)
sort_button_game = pygame.Rect(60,350,300,170)
find_button_game = pygame.Rect(710,350,300,170)

finding_mode_bot = pygame.Rect(670,120,320,180)
finding_mode_player = pygame.Rect(670,330,320,180)
playagain_button = pygame.Rect(670,425,320,80)

# Help menu
help_menu_1 = False
help_menu_2 = False
help_menu_3 = False
help_menu_4 = False
help_menu_5 = False

# Sort menu
sort_menu = False
game_mainmenu = False
graph_write = False
write_length = False
write_slow = False
input_text = input_text2 = ''
size_arr = 10
input_text_print = input_text_print2 = ''
speed = 1
arr_write = False
array = np.random.randint(1,100,size=10)

# Quicksort
quicksort_menu = False


# Bubblesort
bubblesort_menu = False

# Mergesort
mergesort_menu = False

# Heapsort
heapsort_menu = False

# Insertion sort
insertionsort_menu = False

# Cocktail sort
cocktailsort_menu = False

# Game menu
playing = False
findinggame_menu = False
sortgame_menu = False
sortgame_menu_end = False
findinggame_bot = False
findinggame_player = False
text = None
steps,time_played = 0,'0s'
finished_time_of_player,finished_time_of_bot = 0,0
limit = 110
player_choice = bot_choice = ''
list_kind_of_sorting_alogrithm = ["b_sort","q_sort","m_sort","i_sort","h_sort","c_sort"]
sortalogrithm_of_player = sortalogrithm_of_bot = []
sortalgorithm_text = []
button = []
button_used = []
width_array,height_array = 1067,350
score_player, score_bot = 0,0
line = ' '

# Search
search_menu = False
speed = 1
line_print = ''
# Đồ thị dưới dạng danh sách liền kề
graph = {
    0: [1, 2, 3],
    1: [4, 5, 6],
    2: [7, 8, 9],
    3: [10, 11, 12],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: [],
    10:[],
    11:[],
    12:[]
}

# Interpolation Search
interpolationsearch_menu = False

# Binary search
binarysearch_menu = False

# Sequential search
sequentialsearch_menu = False

# Jump search
jumpsearch_menu = False

# BFS 
bfs_menu = False

# DFS
dfs_menu = False

# Main loop
while run:

    if main_menu == True:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.draw.rect(screen,('white'),game_button)
        pygame.draw.rect(screen,('black'),helpbutton)
        pygame.draw.rect(screen,("red"),sort_button) 
        pygame.draw.rect(screen,("red"),search_button)
        screen.blit(background,(0,0))
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse,y_mouse = pygame.mouse.get_pos()
            mouse_box = pygame.Rect(x_mouse,y_mouse,20,20)

            if mouse_box.colliderect(sort_button):

                main_menu = False
                sort_menu = True

            if mouse_box.colliderect(search_button):

                main_menu = False
                search_menu = True
            
            if mouse_box.colliderect(game_button):

                main_menu = False
                game_mainmenu = True
            
            if mouse_box.colliderect(helpbutton):

                help_menu_1 = True

    # Các thuật toán Sort
    if sort_menu == True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                x_mouse,y_mouse = pygame.mouse.get_pos()
                mouse_box = pygame.Rect(x_mouse,y_mouse,20,20)

                if mouse_box.colliderect(quicksort_button):
                    sort_menu = False
                    quicksort_menu = True

                if mouse_box.colliderect(bubblesort_button):
                    sort_menu = False
                    bubblesort_menu = True

                if mouse_box.colliderect(mergesort_button):
                    sort_menu = False
                    mergesort_menu = True
                
                if mouse_box.colliderect(heapsort_button):
                    sort_menu = False
                    heapsort_menu = True

                if mouse_box.colliderect(cocktailsort_button):
                    sort_menu = False
                    cocktailsort_menu = True

                if mouse_box.colliderect(insertionsort_button):
                    sort_menu = False
                    insertionsort_menu = True
                
                if mouse_box.colliderect(homebutton):
                    sort_menu = False
                    main_menu = True
                
                if mouse_box.colliderect(game_button):
                    sort_menu = False
                    game_mainmenu = True

                if mouse_box.colliderect(helpbutton):
                    help_menu_1 = True

        pygame.draw.rect(screen,'white',bubblesort_button)
        pygame.draw.rect(screen,'white',insertionsort_button)
        pygame.draw.rect(screen,'white',heapsort_button)
        pygame.draw.rect(screen,'white',cocktailsort_button)
        pygame.draw.rect(screen,'white',quicksort_button)
        pygame.draw.rect(screen,'white',mergesort_button)
        pygame.draw.rect(screen,('white'),homebutton)
        pygame.draw.rect(screen,('white'),game_button)
        pygame.draw.rect(screen,('black'),helpbutton)
        screen.blit(sortmenu_background,(0,0))

    if quicksort_menu == True:

        # Background
        
        pygame.draw.rect(screen,("white"),homebutton)
        pygame.draw.rect(screen,('white'),length_button)
        pygame.draw.rect(screen,('white'),slow_button)
        pygame.draw.rect(screen,('white'),game_button)
        pygame.draw.rect(screen,('white'),tutorial_button)
        pygame.draw.rect(screen,("white"),copy_button)
        pygame.draw.rect(screen,("white"),show_parameter)
        pygame.draw.rect(screen,('white'),back_button)
        pygame.draw.rect(screen,('black'),arr_button)
        screen.blit(quicksort_image,(0,0))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
            
                if arr_write:
                    
                    if event.key == pygame.K_RETURN:
                        arr_write = False
                        array = convert_str_to_list(line_print)
                        if array == 'Error':
                            line_print = 'Error'
                            array = np.random.randint(1,100,size=size_arr)
                    elif event.key == pygame.K_BACKSPACE:
                        line_print = line_print[:-1]
                    elif len(line_print) < 23:
                        line_print += event.unicode
                
                if write_length:
                    
                    if event.key == pygame.K_RETURN:  # Nhấn Enter để kết thúc
                        if len(input_text) == 0:
                            size_arr = 10
                        else:
                            size_arr = int(input_text)
                        input_text = ""  # Đặt lại văn bản
                        array = np.random.randint(1,100,size=size_arr)
                        write_length = False
                    elif event.key == pygame.K_BACKSPACE:  # Xóa ký tự cuối
                        input_text = input_text[:-1]
                    elif len(input_text) <= 3:  # Thêm ký tự mới
                        input_text += event.unicode

                    if input_text != '':
                        input_text_print = input_text
                
                if write_slow:
                    
                    if event.key == pygame.K_RETURN:  # Nhấn Enter để kết thúc
                        write_slow = False
                        if len(input_text2) == 0:
                            speed = 1
                        else:
                            speed = int(input_text2)
                        input_text2 = ""  # Đặt lại văn bản
                    elif event.key == pygame.K_BACKSPACE:  # Xóa ký tự cuối
                        input_text2 = input_text2[:-1]
                    elif len(input_text2) <= 3:  # Thêm ký tự mới
                        input_text2 += event.unicode

                    if input_text2 != '':
                        input_text_print2 = input_text2

            if event.type == pygame.MOUSEBUTTONDOWN:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                mouse_box = pygame.Rect(x_mouse,y_mouse,20,20)

                
                # Khi nhấn vào nút show cách hoạt động sẽ hiển thị lên màn hình
                if mouse_box.colliderect(show_parameter):

                    write_slow = False
                    write_length = False
                    arr_write = False

                    if line_print != '':
                        array = convert_str_to_list(line_print)
                    elif len(input_text) == 0:
                        size_arr = 10
                        array = np.random.randint(1,100,size=size_arr)
                    else:
                        size_arr = int(input_text)
                        array = np.random.randint(1,100,size=size_arr)
                    
                    if len(input_text2) == 0:
                        speed = 1
                    else:
                        speed = int(input_text2)

                    plt.ion()
                    quick_sort(array, 0, len(array) - 1,speed)
                    plt.title("Mảng đã được sắp xếp")
                    plt.bar(range(len(array)),array,color = "lime")
                    array = []
                    plt.ioff()
                    plt.show()

                elif mouse_box.colliderect(homebutton):
                    quicksort_menu = False
                    main_menu = True

                elif mouse_box.colliderect(game_button):
                    quicksort_menu = False
                    game_mainmenu = True

                elif mouse_box.colliderect(back_button):
                    quicksort_menu = False
                    sort_menu = True

                elif mouse_box.colliderect(arr_button):

                    arr_write = True
                    write_length = False
                    write_slow = False
                    line_print = ''

                elif mouse_box.colliderect(tutorial_button):

                    help_menu_4 = True

                elif mouse_box.colliderect(copy_button):
                    
                    # Đọc nội dung tệp
                    with open('SKKNTHD/Text/Sort/quicksort.txt', 'r', encoding='utf-8') as file:
                        content = file.read()

                    # Sao chép vào clipboard
                    pyperclip.copy(content)
                    copy_message = copy_message_font.render("Copied!",True,('green'))
                    screen.blit(copy_message,(400,260))

                elif mouse_box.colliderect(length_button):
                    write_length = True
                    write_slow = False
                    arr_write = False
                    input_text = ''
                    input_text_print = ''

                elif mouse_box.colliderect(slow_button):
                    write_slow = True
                    write_length = False
                    arr_write = False
                    input_text2 = ''
                    input_text_print2 = ''
                
                else:
                    if line_print != '':
                        array = convert_str_to_list(line_print)
                    elif len(input_text) == 0:
                        size_arr = 10
                        array = np.random.randint(1,100,size=size_arr)
                    else:
                        size_arr = int(input_text)
                        array = np.random.randint(1,100,size=size_arr)
                    
                    if len(input_text2) == 0:
                        speed = 1
                    else:
                        speed = int(input_text2)
            
                        
        text = number_message_font.render(input_text_print,True,('black'))
        screen.blit(text,(535,512))
        text2 = number_message_font.render(input_text_print2,True,('black'))
        screen.blit(text2,(800,512))
        text3 = number_message_font_arr.render(line_print,True,('black'))
        screen.blit(text3,(45,525))

        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            quicksort_image = pygame.image.load('SKKNTHD/Image/quicksort2.jpg')
        elif key[pygame.K_LEFT]:
            quicksort_image = pygame.image.load('SKKNTHD/Image/quicksort1.jpg')
    
    if bubblesort_menu == True:
        
        pygame.draw.rect(screen,("white"),show_parameter)
        pygame.draw.rect(screen,("white"),homebutton)
        pygame.draw.rect(screen,("white"),copy_button)
        pygame.draw.rect(screen,('white'),length_button)
        pygame.draw.rect(screen,('white'),slow_button)
        pygame.draw.rect(screen,('white'),back_button)
        screen.blit(pygame.transform.scale(bubblesort_image,(1067,600)),(0,0))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
            
                if arr_write:
                    
                    if event.key == pygame.K_RETURN:
                        arr_write = False
                        array = convert_str_to_list(line_print)
                        if array == 'Error':
                            line_print = 'Error'
                            array = np.random.randint(1,100,size=size_arr)
                    elif event.key == pygame.K_BACKSPACE:
                        line_print = line_print[:-1]
                    elif len(line_print) < 23:
                        line_print += event.unicode
                
                if write_length:
                    
                    if event.key == pygame.K_RETURN:  # Nhấn Enter để kết thúc
                        if len(input_text) == 0:
                            size_arr = 10
                        else:
                            size_arr = int(input_text)
                        input_text = ""  # Đặt lại văn bản
                        array = np.random.randint(1,100,size=size_arr)
                        write_length = False
                    elif event.key == pygame.K_BACKSPACE:  # Xóa ký tự cuối
                        input_text = input_text[:-1]
                    elif len(input_text) <= 3:  # Thêm ký tự mới
                        input_text += event.unicode

                    if input_text != '':
                        input_text_print = input_text
                
                if write_slow:
                    
                    if event.key == pygame.K_RETURN:  # Nhấn Enter để kết thúc
                        write_slow = False
                        if len(input_text2) == 0:
                            speed = 1
                        else:
                            speed = int(input_text2)
                        input_text2 = ""  # Đặt lại văn bản
                    elif event.key == pygame.K_BACKSPACE:  # Xóa ký tự cuối
                        input_text2 = input_text2[:-1]
                    elif len(input_text2) <= 3:  # Thêm ký tự mới
                        input_text2 += event.unicode

                    if input_text2 != '':
                        input_text_print2 = input_text2

            if event.type == pygame.MOUSEBUTTONDOWN:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                mouse_box = pygame.Rect(x_mouse,y_mouse,20,20)

                
                # Khi nhấn vào nút show cách hoạt động sẽ hiển thị lên màn hình
                if mouse_box.colliderect(show_parameter):

                    write_slow = False
                    write_length = False
                    arr_write = False

                    if line_print != '':
                        array = convert_str_to_list(line_print)
                    elif len(input_text) == 0:
                        size_arr = 10
                        array = np.random.randint(1,100,size=size_arr)
                    else:
                        size_arr = int(input_text)
                        array = np.random.randint(1,100,size=size_arr)
                    
                    if len(input_text2) == 0:
                        speed = 1
                    else:
                        speed = int(input_text2)

                    plt.ion()
                    sorted_arr = bubble_sort(array,speed)
                    plt.title("Mảng đã được sắp xếp")
                    plt.bar(range(len(sorted_arr)),sorted_arr,color = "lime")
                    array = []
                    plt.ioff()
                    plt.show()

                elif mouse_box.colliderect(homebutton):
                    bubblesort_menu = False
                    main_menu = True

                elif mouse_box.colliderect(game_button):
                    bubblesort_menu = False
                    game_mainmenu = True

                elif mouse_box.colliderect(back_button):
                    bubblesort_menu = False
                    sort_menu = True

                elif mouse_box.colliderect(arr_button):

                    arr_write = True
                    write_length = False
                    write_slow = False
                    line_print = ''

                elif mouse_box.colliderect(tutorial_button):

                    help_menu_4 = True

                elif mouse_box.colliderect(copy_button):
                    
                    # Đọc nội dung tệp
                    with open('SKKNTHD/Text/Sort/bubblesort.txt', 'r', encoding='utf-8') as file:
                        content = file.read()

                    # Sao chép vào clipboard
                    pyperclip.copy(content)
                    copy_message = copy_message_font.render("Copied!",True,('green'))
                    screen.blit(copy_message,(400,260))

                elif mouse_box.colliderect(length_button):
                    write_length = True
                    write_slow = False
                    arr_write = False
                    input_text = ''
                    input_text_print = ''

                elif mouse_box.colliderect(slow_button):
                    write_slow = True
                    write_length = False
                    arr_write = False
                    input_text2 = ''
                    input_text_print2 = ''
                
                else:
                    if line_print != '':
                        array = convert_str_to_list(line_print)
                    elif len(input_text) == 0:
                        size_arr = 10
                        array = np.random.randint(1,100,size=size_arr)
                    else:
                        size_arr = int(input_text)
                        array = np.random.randint(1,100,size=size_arr)
                    
                    if len(input_text2) == 0:
                        speed = 1
                    else:
                        speed = int(input_text2)
            
                        
        text = number_message_font.render(input_text_print,True,('black'))
        screen.blit(text,(535,512))
        text2 = number_message_font.render(input_text_print2,True,('black'))
        screen.blit(text2,(800,512))
        text3 = number_message_font_arr.render(line_print,True,('black'))
        screen.blit(text3,(45,525))

        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            bubblesort_image = pygame.image.load('SKKNTHD/Image/bubblesort2.jpg')
        elif key[pygame.K_LEFT]:
            bubblesort_image = pygame.image.load('SKKNTHD/Image/bubblesort1.jpg')
        
    if mergesort_menu == True:

        pygame.draw.rect(screen,("white"),show_parameter)
        pygame.draw.rect(screen,("white"),homebutton)
        pygame.draw.rect(screen,("white"),copy_button)
        pygame.draw.rect(screen,('white'),length_button)
        pygame.draw.rect(screen,('white'),slow_button)
        pygame.draw.rect(screen,('white'),back_button)
        screen.blit(pygame.transform.scale(mergesort_image,(1067,600)),(0,0))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
            
                if arr_write:
                    
                    if event.key == pygame.K_RETURN:
                        arr_write = False
                        array = convert_str_to_list(line_print)
                        if array == 'Error':
                            line_print = 'Error'
                            array = np.random.randint(1,100,size=size_arr)
                    elif event.key == pygame.K_BACKSPACE:
                        line_print = line_print[:-1]
                    elif len(line_print) < 23:
                        line_print += event.unicode
                
                if write_length:
                    
                    if event.key == pygame.K_RETURN:  # Nhấn Enter để kết thúc
                        if len(input_text) == 0:
                            size_arr = 10
                        else:
                            size_arr = int(input_text)
                        input_text = ""  # Đặt lại văn bản
                        array = np.random.randint(1,100,size=size_arr)
                        write_length = False
                    elif event.key == pygame.K_BACKSPACE:  # Xóa ký tự cuối
                        input_text = input_text[:-1]
                    elif len(input_text) <= 3:  # Thêm ký tự mới
                        input_text += event.unicode

                    if input_text != '':
                        input_text_print = input_text
                
                if write_slow:
                    
                    if event.key == pygame.K_RETURN:  # Nhấn Enter để kết thúc
                        write_slow = False
                        if len(input_text2) == 0:
                            speed = 1
                        else:
                            speed = int(input_text2)
                        input_text2 = ""  # Đặt lại văn bản
                    elif event.key == pygame.K_BACKSPACE:  # Xóa ký tự cuối
                        input_text2 = input_text2[:-1]
                    elif len(input_text2) <= 3:  # Thêm ký tự mới
                        input_text2 += event.unicode

                    if input_text2 != '':
                        input_text_print2 = input_text2

            if event.type == pygame.MOUSEBUTTONDOWN:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                mouse_box = pygame.Rect(x_mouse,y_mouse,20,20)

                
                # Khi nhấn vào nút show cách hoạt động sẽ hiển thị lên màn hình
                if mouse_box.colliderect(show_parameter):

                    write_slow = False
                    write_length = False
                    arr_write = False

                    if line_print != '':
                        array = convert_str_to_list(line_print)
                    elif len(input_text) == 0:
                        size_arr = 10
                        array = np.random.randint(1,100,size=size_arr)
                    else:
                        size_arr = int(input_text)
                        array = np.random.randint(1,100,size=size_arr)
                    
                    if len(input_text2) == 0:
                        speed = 1
                    else:
                        speed = int(input_text2)

                    plt.ion()
                    sorted_arr = merge_sort(array,speed)
                    plt.title("Mảng đã được sắp xếp")
                    plt.bar(range(len(sorted_arr)),sorted_arr,color = "lime")
                    array = []
                    plt.ioff()
                    plt.show()

                elif mouse_box.colliderect(homebutton):
                    mergesort_menu = False
                    main_menu = True

                elif mouse_box.colliderect(game_button):
                    mergesort_menu = False
                    game_mainmenu = True

                elif mouse_box.colliderect(back_button):
                    mergesort_menu = False
                    sort_menu = True

                elif mouse_box.colliderect(arr_button):

                    arr_write = True
                    write_length = False
                    write_slow = False
                    line_print = ''

                elif mouse_box.colliderect(tutorial_button):

                    help_menu_4 = True

                elif mouse_box.colliderect(copy_button):
                    
                    # Đọc nội dung tệp
                    with open('SKKNTHD/Text/Sort/mergesort.txt', 'r', encoding='utf-8') as file:
                        content = file.read()

                    # Sao chép vào clipboard
                    pyperclip.copy(content)
                    copy_message = copy_message_font.render("Copied!",True,('green'))
                    screen.blit(copy_message,(400,260))

                elif mouse_box.colliderect(length_button):
                    write_length = True
                    write_slow = False
                    arr_write = False
                    input_text = ''
                    input_text_print = ''

                elif mouse_box.colliderect(slow_button):
                    write_slow = True
                    write_length = False
                    arr_write = False
                    input_text2 = ''
                    input_text_print2 = ''
                
                else:
                    if line_print != '':
                        array = convert_str_to_list(line_print)
                    elif len(input_text) == 0:
                        size_arr = 10
                        array = np.random.randint(1,100,size=size_arr)
                    else:
                        size_arr = int(input_text)
                        array = np.random.randint(1,100,size=size_arr)
                    
                    if len(input_text2) == 0:
                        speed = 1
                    else:
                        speed = int(input_text2)
            
                        
        text = number_message_font.render(input_text_print,True,('black'))
        screen.blit(text,(535,512))
        text2 = number_message_font.render(input_text_print2,True,('black'))
        screen.blit(text2,(800,512))
        text3 = number_message_font_arr.render(line_print,True,('black'))
        screen.blit(text3,(45,525))

        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            mergesort_image = pygame.image.load('SKKNTHD/Image/mergesort2.jpg')
        elif key[pygame.K_LEFT]:
            mergesort_image = pygame.image.load('SKKNTHD/Image/mergesort1.jpg')

    if heapsort_menu == True:

        pygame.draw.rect(screen,("white"),show_parameter)
        pygame.draw.rect(screen,("white"),homebutton)
        pygame.draw.rect(screen,("white"),copy_button)
        pygame.draw.rect(screen,('white'),length_button)
        pygame.draw.rect(screen,('white'),slow_button)
        pygame.draw.rect(screen,('white'),back_button)
        screen.blit(heapsort_image,(0,0))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
            
                if arr_write:
                    
                    if event.key == pygame.K_RETURN:
                        arr_write = False
                        array = convert_str_to_list(line_print)
                        if array == 'Error':
                            line_print = 'Error'
                            array = np.random.randint(1,100,size=size_arr)
                    elif event.key == pygame.K_BACKSPACE:
                        line_print = line_print[:-1]
                    elif len(line_print) < 23:
                        line_print += event.unicode
                
                if write_length:
                    
                    if event.key == pygame.K_RETURN:  # Nhấn Enter để kết thúc
                        if len(input_text) == 0:
                            size_arr = 10
                        else:
                            size_arr = int(input_text)
                        input_text = ""  # Đặt lại văn bản
                        array = np.random.randint(1,100,size=size_arr)
                        write_length = False
                    elif event.key == pygame.K_BACKSPACE:  # Xóa ký tự cuối
                        input_text = input_text[:-1]
                    elif len(input_text) <= 3:  # Thêm ký tự mới
                        input_text += event.unicode

                    if input_text != '':
                        input_text_print = input_text
                
                if write_slow:
                    
                    if event.key == pygame.K_RETURN:  # Nhấn Enter để kết thúc
                        write_slow = False
                        if len(input_text2) == 0:
                            speed = 1
                        else:
                            speed = int(input_text2)
                        input_text2 = ""  # Đặt lại văn bản
                    elif event.key == pygame.K_BACKSPACE:  # Xóa ký tự cuối
                        input_text2 = input_text2[:-1]
                    elif len(input_text2) <= 3:  # Thêm ký tự mới
                        input_text2 += event.unicode

                    if input_text2 != '':
                        input_text_print2 = input_text2

            if event.type == pygame.MOUSEBUTTONDOWN:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                mouse_box = pygame.Rect(x_mouse,y_mouse,20,20)

                
                # Khi nhấn vào nút show cách hoạt động sẽ hiển thị lên màn hình
                if mouse_box.colliderect(show_parameter):

                    write_slow = False
                    write_length = False
                    arr_write = False

                    if line_print != '':
                        array = convert_str_to_list(line_print)
                    elif len(input_text) == 0:
                        size_arr = 10
                        array = np.random.randint(1,100,size=size_arr)
                    else:
                        size_arr = int(input_text)
                        array = np.random.randint(1,100,size=size_arr)
                    
                    if len(input_text2) == 0:
                        speed = 1
                    else:
                        speed = int(input_text2)

                    plt.ion()
                    heap_sort(array,speed)
                    plt.title("Mảng đã được sắp xếp")
                    plt.bar(range(len(array)),array,color = "lime")
                    array = []
                    plt.ioff()
                    plt.show()

                elif mouse_box.colliderect(homebutton):
                    heapsort_menu = False
                    main_menu = True

                elif mouse_box.colliderect(game_button):
                    heapsort_menu = False
                    game_mainmenu = True

                elif mouse_box.colliderect(back_button):
                    heapsort_menu = False
                    sort_menu = True

                elif mouse_box.colliderect(arr_button):

                    arr_write = True
                    write_length = False
                    write_slow = False
                    line_print = ''

                elif mouse_box.colliderect(tutorial_button):

                    help_menu_4 = True

                elif mouse_box.colliderect(copy_button):
                    
                    # Đọc nội dung tệp
                    with open('SKKNTHD/Text/Sort/heapsort.txt', 'r', encoding='utf-8') as file:
                        content = file.read()

                    # Sao chép vào clipboard
                    pyperclip.copy(content)
                    copy_message = copy_message_font.render("Copied!",True,('green'))
                    screen.blit(copy_message,(400,260))

                elif mouse_box.colliderect(length_button):
                    write_length = True
                    write_slow = False
                    arr_write = False
                    input_text = ''
                    input_text_print = ''

                elif mouse_box.colliderect(slow_button):
                    write_slow = True
                    write_length = False
                    arr_write = False
                    input_text2 = ''
                    input_text_print2 = ''
                
                else:
                    if line_print != '':
                        array = convert_str_to_list(line_print)
                    elif len(input_text) == 0:
                        size_arr = 10
                        array = np.random.randint(1,100,size=size_arr)
                    else:
                        size_arr = int(input_text)
                        array = np.random.randint(1,100,size=size_arr)
                    
                    if len(input_text2) == 0:
                        speed = 1
                    else:
                        speed = int(input_text2)
            
                        
        text = number_message_font.render(input_text_print,True,('black'))
        screen.blit(text,(535,512))
        text2 = number_message_font.render(input_text_print2,True,('black'))
        screen.blit(text2,(800,512))
        text3 = number_message_font_arr.render(line_print,True,('black'))
        screen.blit(text3,(45,525))

        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            heapsort_image = pygame.image.load('SKKNTHD/Image/heapsort2.jpg')
        elif key[pygame.K_LEFT]:
            heapsort_image = pygame.image.load('SKKNTHD/Image/heapsort1.jpg')
                
    if insertionsort_menu == True:

        pygame.draw.rect(screen,("white"),show_parameter)
        pygame.draw.rect(screen,("white"),homebutton)
        pygame.draw.rect(screen,("white"),copy_button)
        pygame.draw.rect(screen,('white'),length_button)
        pygame.draw.rect(screen,('white'),slow_button)
        pygame.draw.rect(screen,('white'),back_button)
        screen.blit(insertionsort_image,(0,0))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
            
                if arr_write:
                    
                    if event.key == pygame.K_RETURN:
                        arr_write = False
                        array = convert_str_to_list(line_print)
                        if array == 'Error':
                            line_print = 'Error'
                            array = np.random.randint(1,100,size=size_arr)
                    elif event.key == pygame.K_BACKSPACE:
                        line_print = line_print[:-1]
                    elif len(line_print) < 23:
                        line_print += event.unicode
                
                if write_length:
                    
                    if event.key == pygame.K_RETURN:  # Nhấn Enter để kết thúc
                        if len(input_text) == 0:
                            size_arr = 10
                        else:
                            size_arr = int(input_text)
                        input_text = ""  # Đặt lại văn bản
                        array = np.random.randint(1,100,size=size_arr)
                        write_length = False
                    elif event.key == pygame.K_BACKSPACE:  # Xóa ký tự cuối
                        input_text = input_text[:-1]
                    elif len(input_text) <= 3:  # Thêm ký tự mới
                        input_text += event.unicode

                    if input_text != '':
                        input_text_print = input_text
                
                if write_slow:
                    
                    if event.key == pygame.K_RETURN:  # Nhấn Enter để kết thúc
                        write_slow = False
                        if len(input_text2) == 0:
                            speed = 1
                        else:
                            speed = int(input_text2)
                        input_text2 = ""  # Đặt lại văn bản
                    elif event.key == pygame.K_BACKSPACE:  # Xóa ký tự cuối
                        input_text2 = input_text2[:-1]
                    elif len(input_text2) <= 3:  # Thêm ký tự mới
                        input_text2 += event.unicode

                    if input_text2 != '':
                        input_text_print2 = input_text2

            if event.type == pygame.MOUSEBUTTONDOWN:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                mouse_box = pygame.Rect(x_mouse,y_mouse,20,20)

                
                # Khi nhấn vào nút show cách hoạt động sẽ hiển thị lên màn hình
                if mouse_box.colliderect(show_parameter):

                    write_slow = False
                    write_length = False
                    arr_write = False

                    if line_print != '':
                        array = convert_str_to_list(line_print)
                    elif len(input_text) == 0:
                        size_arr = 10
                        array = np.random.randint(1,100,size=size_arr)
                    else:
                        size_arr = int(input_text)
                        array = np.random.randint(1,100,size=size_arr)
                    
                    if len(input_text2) == 0:
                        speed = 1
                    else:
                        speed = int(input_text2)

                    plt.ion()
                    sorted_arr = insertion_sort(array,speed)
                    plt.clf()
                    plt.title("Mảng đã được sắp xếp")
                    plt.bar(range(len(sorted_arr)),sorted_arr,color = "lime")
                    array = []
                    plt.ioff()
                    plt.show()

                elif mouse_box.colliderect(homebutton):
                    insertionsort_menu = False
                    main_menu = True

                elif mouse_box.colliderect(game_button):
                    insertionsort_menu = False
                    game_mainmenu = True

                elif mouse_box.colliderect(back_button):
                    insertionsort_menu = False
                    sort_menu = True

                elif mouse_box.colliderect(arr_button):

                    arr_write = True
                    write_length = False
                    write_slow = False
                    line_print = ''

                elif mouse_box.colliderect(tutorial_button):

                    help_menu_4 = True

                elif mouse_box.colliderect(copy_button):
                    
                    # Đọc nội dung tệp
                    with open('SKKNTHD/Text/Sort/insertionsort.txt', 'r', encoding='utf-8') as file:
                        content = file.read()

                    # Sao chép vào clipboard
                    pyperclip.copy(content)
                    copy_message = copy_message_font.render("Copied!",True,('green'))
                    screen.blit(copy_message,(400,260))

                elif mouse_box.colliderect(length_button):
                    write_length = True
                    write_slow = False
                    arr_write = False
                    input_text = ''
                    input_text_print = ''

                elif mouse_box.colliderect(slow_button):
                    write_slow = True
                    write_length = False
                    arr_write = False
                    input_text2 = ''
                    input_text_print2 = ''
                
                else:
                    if line_print != '':
                        array = convert_str_to_list(line_print)
                    elif len(input_text) == 0:
                        size_arr = 10
                        array = np.random.randint(1,100,size=size_arr)
                    else:
                        size_arr = int(input_text)
                        array = np.random.randint(1,100,size=size_arr)
                    
                    if len(input_text2) == 0:
                        speed = 1
                    else:
                        speed = int(input_text2)
            
                        
        text = number_message_font.render(input_text_print,True,('black'))
        screen.blit(text,(535,512))
        text2 = number_message_font.render(input_text_print2,True,('black'))
        screen.blit(text2,(800,512))
        text3 = number_message_font_arr.render(line_print,True,('black'))
        screen.blit(text3,(45,525))

        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            insertionsort_image = pygame.image.load('SKKNTHD/Image/insertionsort2.jpg')
        elif key[pygame.K_LEFT]:
            insertionsort_image = pygame.image.load('SKKNTHD/Image/insertionsort1.jpg')
    
    if cocktailsort_menu == True:

        pygame.draw.rect(screen,("white"),show_parameter)
        pygame.draw.rect(screen,("white"),homebutton)
        pygame.draw.rect(screen,("white"),copy_button)
        pygame.draw.rect(screen,('white'),length_button)
        pygame.draw.rect(screen,('white'),slow_button)
        pygame.draw.rect(screen,('white'),back_button)
        screen.blit(cocktailsort_image,(0,0))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
            
                if arr_write:
                    
                    if event.key == pygame.K_RETURN:
                        arr_write = False
                        array = convert_str_to_list(line_print)
                        if array == 'Error':
                            line_print = 'Error'
                            array = np.random.randint(1,100,size=size_arr)
                    elif event.key == pygame.K_BACKSPACE:
                        line_print = line_print[:-1]
                    elif len(line_print) < 23:
                        line_print += event.unicode
                
                if write_length:
                    
                    if event.key == pygame.K_RETURN:  # Nhấn Enter để kết thúc
                        if len(input_text) == 0:
                            size_arr = 10
                        else:
                            size_arr = int(input_text)
                        input_text = ""  # Đặt lại văn bản
                        array = np.random.randint(1,100,size=size_arr)
                        write_length = False
                    elif event.key == pygame.K_BACKSPACE:  # Xóa ký tự cuối
                        input_text = input_text[:-1]
                    elif len(input_text) <= 3:  # Thêm ký tự mới
                        input_text += event.unicode

                    if input_text != '':
                        input_text_print = input_text
                
                if write_slow:
                    
                    if event.key == pygame.K_RETURN:  # Nhấn Enter để kết thúc
                        write_slow = False
                        if len(input_text2) == 0:
                            speed = 1
                        else:
                            speed = int(input_text2)
                        input_text2 = ""  # Đặt lại văn bản
                    elif event.key == pygame.K_BACKSPACE:  # Xóa ký tự cuối
                        input_text2 = input_text2[:-1]
                    elif len(input_text2) <= 3:  # Thêm ký tự mới
                        input_text2 += event.unicode

                    if input_text2 != '':
                        input_text_print2 = input_text2

            if event.type == pygame.MOUSEBUTTONDOWN:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                mouse_box = pygame.Rect(x_mouse,y_mouse,20,20)

                
                # Khi nhấn vào nút show cách hoạt động sẽ hiển thị lên màn hình
                if mouse_box.colliderect(show_parameter):

                    write_slow = False
                    write_length = False
                    arr_write = False

                    if line_print != '':
                        array = convert_str_to_list(line_print)
                    elif len(input_text) == 0:
                        size_arr = 10
                        array = np.random.randint(1,100,size=size_arr)
                    else:
                        size_arr = int(input_text)
                        array = np.random.randint(1,100,size=size_arr)
                    
                    if len(input_text2) == 0:
                        speed = 1
                    else:
                        speed = int(input_text2)

                    plt.ion()
                    sorted_arr = cocktail_sort(array,speed)
                    plt.title("Mảng đã được sắp xếp")
                    plt.bar(range(len(sorted_arr)),sorted_arr,color = "lime")
                    array = []
                    plt.ioff()
                    plt.show()

                elif mouse_box.colliderect(homebutton):
                    cocktailsort_menu = False
                    main_menu = True

                elif mouse_box.colliderect(game_button):
                    cocktailsort_menu = False
                    game_mainmenu = True

                elif mouse_box.colliderect(back_button):
                    cocktailsort_menu = False
                    sort_menu = True

                elif mouse_box.colliderect(arr_button):

                    arr_write = True
                    write_length = False
                    write_slow = False
                    line_print = ''

                elif mouse_box.colliderect(tutorial_button):

                    help_menu_4 = True

                elif mouse_box.colliderect(copy_button):
                    
                    # Đọc nội dung tệp
                    with open('SKKNTHD/Text/Sort/cocktailsort.txt', 'r', encoding='utf-8') as file:
                        content = file.read()

                    # Sao chép vào clipboard
                    pyperclip.copy(content)
                    copy_message = copy_message_font.render("Copied!",True,('green'))
                    screen.blit(copy_message,(400,260))

                elif mouse_box.colliderect(length_button):
                    write_length = True
                    write_slow = False
                    arr_write = False
                    input_text = ''
                    input_text_print = ''

                elif mouse_box.colliderect(slow_button):
                    write_slow = True
                    write_length = False
                    arr_write = False
                    input_text2 = ''
                    input_text_print2 = ''
                
                else:
                    if line_print != '':
                        array = convert_str_to_list(line_print)
                    elif len(input_text) == 0:
                        size_arr = 10
                        array = np.random.randint(1,100,size=size_arr)
                    else:
                        size_arr = int(input_text)
                        array = np.random.randint(1,100,size=size_arr)
                    
                    if len(input_text2) == 0:
                        speed = 1
                    else:
                        speed = int(input_text2)
            
                        
        text = number_message_font.render(input_text_print,True,('black'))
        screen.blit(text,(535,512))
        text2 = number_message_font.render(input_text_print2,True,('black'))
        screen.blit(text2,(800,512))
        text3 = number_message_font_arr.render(line_print,True,('black'))
        screen.blit(text3,(45,525))

        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            cocktailsort_image = pygame.image.load('SKKNTHD/Image/cocktailsort2.jpg')
        elif key[pygame.K_LEFT]:
            cocktailsort_image = pygame.image.load('SKKNTHD/Image/cocktailsort1.jpg')

    # Game menu
    if game_mainmenu ==  True:
       
        
        pygame.draw.rect(screen,("white"),search_button)
        pygame.draw.rect(screen,("white"),sort_button)
        pygame.draw.rect(screen,('white'),homebutton)
        pygame.draw.rect(screen,('black'),helpbutton)
        screen.blit(sortgamemainmenu,(0,0))
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                mouse_box = pygame.Rect(x_mouse,y_mouse,20,20)

                if mouse_box.colliderect(sort_button):

                    game_mainmenu = False
                    sortgame_menu = True

                    score_player = 0
                    score_bot = 0
                    finished_time_of_player = 0
                    finished_time_of_bot = 0

                    array = np.random.randint(1,180,size=random.randint(20,30))
                    array_of_player = array.copy()
                    array_of_bot = array.copy()

                    for i in range(3):

                        sortalogrithm_of_player.append(random.choice(list_kind_of_sorting_alogrithm))
                        if sortalogrithm_of_player[i] == 'q_sort':
                            text_algorithm = copy_message_font.render("Quick Sort",True,('black'))
                        if sortalogrithm_of_player[i] == 'b_sort':
                            text_algorithm = copy_message_font.render("Bubble Sort",True,('black'))
                        if sortalogrithm_of_player[i] == 'i_sort':
                            text_algorithm = copy_message_font.render("Insertion Sort",True,('black'))
                        if sortalogrithm_of_player[i] == 'm_sort':
                            text_algorithm = copy_message_font.render("Merge Sort",True,('black'))
                        if sortalogrithm_of_player[i] == 'c_sort':
                            text_algorithm = copy_message_font.render("Cocktail Sort",True,('black'))
                        if sortalogrithm_of_player[i] == 'h_sort':
                            text_algorithm = copy_message_font.render("Heap Sort",True,('black'))
                        sortalgorithm_text.append(text_algorithm)
                        sortalogrithm_of_bot.append(random.choice(list_kind_of_sorting_alogrithm))
                        button.append(pygame.Rect(35+324*i+10*i,409,324,131))

                if mouse_box.colliderect(search_button):

                    game_mainmenu = False
                    findinggame_menu = True
                    playing = True
                
                if mouse_box.colliderect(homebutton):

                    main_menu = True
                    game_mainmenu = False
                
                if mouse_box.colliderect(helpbutton):

                    help_menu_1 = True
    # Sort game
    if sortgame_menu == True:

        if len(button_used) == 3:
            sortgame_menu = False
            sortgame_menu_end = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                mouse_box = pygame.Rect(x_mouse,y_mouse,20,20)

                if mouse_box.colliderect(homebutton):
                    sortgame_menu = False
                    main_menu = True
                    score_player = 0
                    score_bot = 0
                    finished_time_of_player = 0
                    finished_time_of_bot = 0
                    button_used = []
                    sortalogrithm_of_player = sortalogrithm_of_bot = []
                    sortalgorithm_text = []
                    button = []

                
                if mouse_box.colliderect(game_button):
                    sortgame_menu = False
                    game_mainmenu = True
                    score_player = 0
                    score_bot = 0
                    finished_time_of_player = 0
                    finished_time_of_bot = 0
                    button_used = []
                    sortalogrithm_of_player = sortalogrithm_of_bot = []
                    sortalgorithm_text = []
                    button = []


                if mouse_box.colliderect(tutorial_button_sorting_game):
                    help_menu_2 = True
        
                for i in range(len(button)):
                    if mouse_box.colliderect(button[i]) and i not in button_used:

                        player_choice = sortalogrithm_of_player[i]
                        bot_choice = random.choice(sortalogrithm_of_bot)
                        button_used.append(i)
                        plt.clf()
                        plt.clf()

                        plt.ion()

                        if player_choice == 'b_sort':
                            moc = time.time()
                            sorted_arr = bubble_sort_game(array_of_player,player="Player's",time=moc)
                            finished_time_of_player = int(time.time() - moc)
                            plt.title("Player's Time: " + str(int(time.time()-moc))+'s')
                            plt.bar(range(len(sorted_arr)),sorted_arr,color = 'lime')  

                        if player_choice == 'q_sort':
                            moc = time.time()
                            quick_sort_game(array_of_player,0,len(array_of_player)-1,player="Player's",time=moc)
                            finished_time_of_player = int(time.time() - moc)
                            plt.title("Player's Time: " + str(int(time.time()-moc))+'s')
                            plt.bar(range(len(array_of_player)),array_of_player,color = 'lime')  

                        if player_choice == 'h_sort':
                            moc = time.time()
                            heap_sort_game(array_of_player,player="Player's",time=moc)
                            finished_time_of_player = int(time.time() - moc)
                            plt.title("Player's Time: " + str(int(time.time()-moc))+'s')
                            plt.bar(range(len(array_of_player)),array_of_player,color = 'lime') 

                        if player_choice == 'i_sort':
                            moc = time.time()
                            insertion_sort_game(array_of_player,player="Player's",time=moc)
                            finished_time_of_player = int(time.time() - moc)
                            plt.clf()
                            plt.title("Player's Time: " + str(int(time.time()-moc))+'s')
                            plt.bar(range(len(array_of_player)),array_of_player,color = 'lime') 

                        if player_choice == 'm_sort':
                            moc = time.time()
                            sorted_arr=merge_sort_game(array_of_player,player="Player's",time=moc)
                            finished_time_of_player = int(time.time() - moc)
                            plt.clf()
                            plt.title("Player's Time: " + str(int(time.time()-moc))+'s')
                            plt.bar(range(len(sorted_arr)),sorted_arr,color = 'lime') 

                        if player_choice == 'c_sort':
                            moc = time.time()
                            sorted_arr=cocktail_sort_game(array_of_player,player="Player's",time=moc)
                            finished_time_of_player = int(time.time() - moc)
                            plt.clf()
                            plt.title("Player's Time: " + str(int(time.time()-moc))+'s')
                            plt.bar(range(len(sorted_arr)),sorted_arr,color = 'lime') 

                        if bot_choice == 'b_sort':
                            moc = time.time()
                            sorted_arr = bubble_sort_game(array_of_bot,player="Bot's",time=moc)
                            finished_time_of_bot = int(time.time() - moc)
                            plt.title("Bot's time: " + str(int(time.time()-moc))+'s')
                            plt.bar(range(len(sorted_arr)),sorted_arr,color = 'lime')

                        if bot_choice == 'q_sort':
                            moc = time.time()
                            quick_sort_game(array_of_bot,0,len(array_of_bot)-1,player="Bot's",time=moc)
                            finished_time_of_bot = int(time.time() - moc)
                            plt.title("Bot's Time: " + str(int(time.time()-moc))+'s')
                            plt.bar(range(len(array_of_bot)),array_of_bot,color = 'lime') 

                        if bot_choice == 'h_sort':
                            moc = time.time()
                            heap_sort_game(array_of_bot,player="Bot's",time=moc)
                            finished_time_of_bot = int(time.time() - moc)
                            plt.title("Bot's Time: " + str(int(time.time()-moc))+'s')
                            plt.bar(range(len(array_of_bot)),array_of_bot,color = 'lime') 

                        if bot_choice == 'i_sort':
                            moc = time.time()
                            insertion_sort_game(array_of_bot,player="Bot's",time=moc)
                            finished_time_of_bot = int(time.time() - moc)
                            plt.clf()
                            plt.title("Bot's Time: " + str(int(time.time()-moc))+'s')
                            plt.bar(range(len(array_of_bot)),array_of_bot,color = 'lime') 

                        if bot_choice == 'm_sort':
                            moc = time.time()
                            sorted_arr=merge_sort_game(array_of_bot,player="Bot's",time=moc)
                            finished_time_of_bot = int(time.time() - moc)
                            plt.clf()
                            plt.title("Bot's Time: " + str(int(time.time()-moc))+'s')
                            plt.bar(range(len(sorted_arr)),sorted_arr,color = 'lime') 

                        if bot_choice == 'c_sort':
                            moc = time.time()
                            sorted_arr=cocktail_sort_game(array_of_bot,player="Bot's",time=moc)
                            finished_time_of_bot = int(time.time() - moc)
                            plt.clf()
                            plt.title("Bot's Time: " + str(int(time.time()-moc))+'s')
                            plt.bar(range(len(sorted_arr)),sorted_arr,color = 'lime') 

                        plt.ioff()
                        plt.show()

                        array = np.random.randint(1,100,size=random.randint(20,30))
                        array_of_player = array.copy()
                        array_of_bot = array.copy()
                
                if finished_time_of_player < finished_time_of_bot and finished_time_of_bot != 0 and finished_time_of_player !=0:
                    score_player += 1
                    finished_time_of_player = 0
                    finished_time_of_bot = 0
                elif finished_time_of_player > finished_time_of_bot and finished_time_of_bot != 0 and finished_time_of_player !=0:
                    score_bot += 1
                    finished_time_of_player = 0
                    finished_time_of_bot = 0
                elif finished_time_of_player == finished_time_of_bot and finished_time_of_bot != 0 and finished_time_of_player !=0:
                    score_player += 1
                    score_bot += 1
                    finished_time_of_player = 0
                    finished_time_of_bot = 0

        result_score = number_message_font.render(str(score_player)+'-'+ str(score_bot),True,('black'))

        if help_menu_2 == False:
            for i in range(len(button)):
                if i not in button_used:
                    pygame.draw.rect(screen,('black'),button[i])
                else:
                    pygame.draw.rect(screen,('grey'),button[i])

            pygame.draw.rect(screen,('white'),homebutton)
            pygame.draw.rect(screen,('white'),game_button)
            pygame.draw.rect(screen,('black'),helpbutton)
            pygame.draw.rect(screen,('black'),tutorial_button_sorting_game)

            screen.blit(sortgameplay,(0,0))
            screen.blit(result_score,(100,100))
            for i in range (len(sortalgorithm_text)):
                screen.blit(sortalgorithm_text[i],(20+330*i+60,440))
            draw_array(array,limit,width_array,height_array,screen)    

    if sortgame_menu_end == True:
        
        pygame.draw.rect(screen,('white'),homebutton)
        pygame.draw.rect(screen,('white'),game_button)
        pygame.draw.rect(screen,('black'),helpbutton)
        if int(score_player) >= int(score_bot):
            ending_screen = pygame.image.load('SKKNTHD/Image/wining.jpg')
        else:
            ending_screen = pygame.image.load('SKKNTHD/Image/losing.jpg')
        screen.blit(ending_screen,(0,0))

        result_score = number_message_end_font.render(str(score_player)+'-'+ str(score_bot),True,('black'))
        screen.blit(result_score,(450,300))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:

                x_mouse,y_mouse = pygame.mouse.get_pos()
                mouse_box = pygame.Rect(x_mouse,y_mouse,20,20)

                if mouse_box.colliderect(homebutton):
                    sortgame_menu_end = False
                    main_menu = True
                    score_player = 0
                    score_bot = 0
                    finished_time_of_player = 0
                    finished_time_of_bot = 0
                    button_used = []
                    sortalogrithm_of_player = sortalogrithm_of_bot = []
                    sortalgorithm_text = []
                    button = []

                
                if mouse_box.colliderect(game_button):
                    sortgame_menu_end = False
                    game_mainmenu = True
                    score_player = 0
                    score_bot = 0
                    finished_time_of_player = 0
                    finished_time_of_bot = 0    
                    button_used = []
                    sortalgorithm_text = []
                    button = []
    
    # Finding game
    if findinggame_menu == True:

        pygame.draw.rect(screen,('black'), finding_mode_bot)
        pygame.draw.rect(screen,('black'),finding_mode_player)
        pygame.draw.rect(screen,('black'),homebutton)
        pygame.draw.rect(screen,('black'),game_button) 
        screen.blit(findinggame_image,(0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                x_mouse,y_mouse = pygame.mouse.get_pos()
                mouse_box = pygame.Rect(x_mouse,y_mouse,20,20)

                if mouse_box.colliderect(helpbutton):
                    help_menu_1 = True

                if mouse_box.colliderect(finding_mode_bot):
                    findinggame_bot = True
                    findinggame_menu = False

                if mouse_box.colliderect(finding_mode_player):
                    findinggame_player = True
                    findinggame_menu = False

                if mouse_box.colliderect(homebutton):

                    findinggame_menu = False
                    findinggame_bot = False
                    main_menu = True

                if mouse_box.colliderect(game_button):

                    findinggame_menu = False
                    findinggame_bot = False
                    game_mainmenu = True

    if findinggame_bot == True:

        pygame.draw.rect(screen,('black'),homebutton)
        pygame.draw.rect(screen,('black'),game_button) 
        pygame.draw.rect(screen,('black'),playagain_button)
        screen.blit(finding_gameplay_bot,(0,0))

        # Start/End
        start = (0, 0)

        start_text = number_message_font.render(str(start),True,('green'))

        screen.blit(start_text,(815,155))
        
        
        if text != None:
            screen.blit(text,(820,325))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                x_mouse,y_mouse = pygame.mouse.get_pos()
                mouse_box = pygame.Rect(x_mouse,y_mouse,20,20)

                if mouse_box.colliderect(homebutton):

                    findinggame_menu = False
                    findinggame_bot = False
                    main_menu = True

                if mouse_box.colliderect(helpbutton):
                    
                    help_menu_1 = True

                if mouse_box.colliderect(game_button):

                    findinggame_menu = False
                    findinggame_bot = False
                    game_mainmenu = True

                if mouse_box.colliderect(playagain_button):

                    maze = generate_maze(rows, cols)
                    end = random_end(maze)
                    moc = time.time()
                    end_text = number_message_font.render(str(end),True,('red'))
                    screen.blit(end_text,(815,235))
                    findinggame(maze,start,end)    
                    pygame.time.delay(1000)
                    text = number_message_font.render(str(int(time.time()-moc)) + 's',True,('yellow'))
                    
        end_text = number_message_font.render(str(end),True,('red'))
        screen.blit(end_text,(815,235))  

    if findinggame_player == True:

        pygame.draw.rect(screen,('black'),homebutton)
        pygame.draw.rect(screen,('black'),game_button)
        pygame.draw.rect(screen,('black'),playagain_button)
        screen.blit(finding_gameplay_player,(0,0))

        # Text
        text_steps = font_for_finding_game.render(str(steps), True, GREEN)
        text_time = font_for_finding_game.render(time_played, True, RED)

        screen.blit(text_steps, (820, 150))
        screen.blit(text_time, (820, 260))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                x_mouse,y_mouse = pygame.mouse.get_pos()
                mouse_box = pygame.Rect(x_mouse,y_mouse,20,20)

                if mouse_box.colliderect(homebutton):

                    findinggame_menu = False
                    findinggame_player = False
                    main_menu = True
                
                if mouse_box.colliderect(game_button):

                    findinggame_menu = False
                    findinggame_player = False
                    game_mainmenu = True
                
                if mouse_box.colliderect(helpbutton):
                    help_menu_1 = True
                
                if mouse_box.colliderect(playagain_button):
                    steps,time_played = finding_game_player()

    # Các thuật toán Search 
    if search_menu == True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                x_mouse,y_mouse = pygame.mouse.get_pos()
                mouse_box = pygame.Rect(x_mouse,y_mouse,20,20)

                if mouse_box.colliderect(binarysearch_button):
                    search_menu = False
                    binarysearch_menu = True

                if mouse_box.colliderect(sequentialsearch_button):
                    search_menu = False
                    sequentialsearch_menu = True

                if mouse_box.colliderect(interpolationsearch_button):
                    search_menu = False
                    interpolationsearch_menu = True

                if mouse_box.colliderect(jumpsearch_button):
                    search_menu = False
                    jumpsearch_menu = True

                if mouse_box.colliderect(homebutton):
                    search_menu = False
                    main_menu = True
                
                if mouse_box.colliderect(game_button):
                    search_menu = False
                    game_mainmenu = True

                if mouse_box.colliderect(bfs_button):
                    search_menu = False
                    bfs_menu = True
                
                if mouse_box.colliderect(dfs_button):
                    search_menu = False
                    dfs_menu = True
                
                if mouse_box.colliderect(helpbutton):
                    help_menu_1 = True

        pygame.draw.rect(screen,'white',sequentialsearch_button)
        pygame.draw.rect(screen,'white',interpolationsearch_button)
        pygame.draw.rect(screen,'white',binarysearch_button)
        pygame.draw.rect(screen,'white',jumpsearch_button)
        pygame.draw.rect(screen,'white',bfs_button)
        pygame.draw.rect(screen,'white',dfs_button)
        pygame.draw.rect(screen,('white'),homebutton)
        pygame.draw.rect(screen,('white'),game_button)
        pygame.draw.rect(screen,('black'),helpbutton)
        screen.blit(searchmenu_background,(0,0))

    if interpolationsearch_menu == True:

        # Background
        pygame.draw.rect(screen,("white"),show_parameter)
        pygame.draw.rect(screen,("white"),homebutton)
        pygame.draw.rect(screen,('white'),game_button)
        pygame.draw.rect(screen,("white"),copy_button)
        pygame.draw.rect(screen,('white'),length_button)
        pygame.draw.rect(screen,('white'),slow_button)
        pygame.draw.rect(screen,('white'),back_button)
        screen.blit(interpolationsearch_image,(0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
            
                if arr_write:
                    
                    if event.key == pygame.K_RETURN:
                        arr_write = False
                        array = convert_str_to_list(line_print)
                        if array == 'Error':
                            line_print = 'Error'
                            array = np.random.randint(1,100,size=size_arr)
                    elif event.key == pygame.K_BACKSPACE:
                        line_print = line_print[:-1]
                    elif len(line_print) < 23:
                        line_print += event.unicode
                
                if write_length:
                    
                    if event.key == pygame.K_RETURN:  # Nhấn Enter để kết thúc
                        if len(input_text) == 0:
                            size_arr = 10
                        else:
                            size_arr = int(input_text)
                        input_text = ""  # Đặt lại văn bản
                        array = np.random.randint(1,100,size=size_arr)
                        write_length = False
                    elif event.key == pygame.K_BACKSPACE:  # Xóa ký tự cuối
                        input_text = input_text[:-1]
                    elif len(input_text) <= 3:  # Thêm ký tự mới
                        input_text += event.unicode

                    if input_text != '':
                        input_text_print = input_text
                
                if write_slow:
                    
                    if event.key == pygame.K_RETURN:  # Nhấn Enter để kết thúc
                        write_slow = False
                        if len(input_text2) == 0:
                            speed = 1
                        else:
                            speed = int(input_text2)
                        input_text2 = ""  # Đặt lại văn bản
                    elif event.key == pygame.K_BACKSPACE:  # Xóa ký tự cuối
                        input_text2 = input_text2[:-1]
                    elif len(input_text2) <= 3:  # Thêm ký tự mới
                        input_text2 += event.unicode

                    if input_text2 != '':
                        input_text_print2 = input_text2

            if event.type == pygame.MOUSEBUTTONDOWN:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                mouse_box = pygame.Rect(x_mouse,y_mouse,20,20)

                
                # Khi nhấn vào nút show cách hoạt động sẽ hiển thị lên màn hình
                if mouse_box.colliderect(show_parameter):

                    write_slow = False
                    write_length = False
                    arr_write = False

                    if line_print != '':
                        array = convert_str_to_list(line_print)
                    elif len(input_text) == 0:
                        size_arr = 10
                        array = np.random.randint(1,100,size=size_arr)
                    else:
                        size_arr = int(input_text)
                        array = np.random.randint(1,100,size=size_arr)
                    
                    if len(input_text2) == 0:
                        speed = 1
                    else:
                        speed = int(input_text2)

                    target = random.choice(array)
                    array.sort()
                    plt.ion()
                    result = interpolation_search(arr=array,target=target,speed=speed)
                    if result != -1:
                        show_parameter_search(arr=array,highlight=[result],highlight_color=['lime'],target=target,speed=speed)

                    plt.ioff()
                    plt.show()

                elif mouse_box.colliderect(homebutton):
                    interpolationsearch_menu = False
                    main_menu = True

                elif mouse_box.colliderect(game_button):
                    interpolationsearch_menu = False
                    game_mainmenu = True

                elif mouse_box.colliderect(back_button):
                    interpolationsearch_menu = False
                    search_menu = True

                elif mouse_box.colliderect(arr_button):

                    arr_write = True
                    write_length = False
                    write_slow = False
                    line_print = ''

                elif mouse_box.colliderect(tutorial_button):

                    help_menu_4 = True

                elif mouse_box.colliderect(copy_button):
                    
                    # Đọc nội dung tệp
                    with open('SKKNTHD/Text/Search/interpolationsearch.txt', 'r', encoding='utf-8') as file:
                        content = file.read()

                    # Sao chép vào clipboard
                    pyperclip.copy(content)
                    copy_message = copy_message_font.render("Copied!",True,('green'))
                    screen.blit(copy_message,(400,260))

                elif mouse_box.colliderect(length_button):
                    write_length = True
                    write_slow = False
                    arr_write = False
                    input_text = ''
                    input_text_print = ''

                elif mouse_box.colliderect(slow_button):
                    write_slow = True
                    write_length = False
                    arr_write = False
                    input_text2 = ''
                    input_text_print2 = ''
                
                else:
                    if line_print != '':
                        array = convert_str_to_list(line_print)
                    elif len(input_text) == 0:
                        size_arr = 10
                        array = np.random.randint(1,100,size=size_arr)
                    else:
                        size_arr = int(input_text)
                        array = np.random.randint(1,100,size=size_arr)
                    
                    if len(input_text2) == 0:
                        speed = 1
                    else:
                        speed = int(input_text2)
            
                        
        text = number_message_font.render(input_text_print,True,('black'))
        screen.blit(text,(535,512))
        text2 = number_message_font.render(input_text_print2,True,('black'))
        screen.blit(text2,(800,512))
        text3 = number_message_font_arr.render(line_print,True,('black'))
        screen.blit(text3,(45,525))

        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            interpolationsearch_image = pygame.image.load('SKKNTHD/Image/interpolationsearch2.jpg')
        elif key[pygame.K_LEFT]:
            interpolationsearch_image = pygame.image.load('SKKNTHD/Image/interpolationsearch1.jpg')
    
    if binarysearch_menu == True:

        # Background
        pygame.draw.rect(screen,("white"),show_parameter)
        pygame.draw.rect(screen,("white"),homebutton)
        pygame.draw.rect(screen,('white'),game_button)
        pygame.draw.rect(screen,("white"),copy_button)
        pygame.draw.rect(screen,('white'),length_button)
        pygame.draw.rect(screen,('white'),slow_button)
        pygame.draw.rect(screen,('white'),back_button)
        screen.blit(binarysearch_image,(0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
            
                if arr_write:
                    
                    if event.key == pygame.K_RETURN:
                        arr_write = False
                        array = convert_str_to_list(line_print)
                        if array == 'Error':
                            line_print = 'Error'
                            array = np.random.randint(1,50,size=size_arr)
                    elif event.key == pygame.K_BACKSPACE:
                        line_print = line_print[:-1]
                    elif len(line_print) < 23:
                        line_print += event.unicode
                
                if write_length:
                    
                    if event.key == pygame.K_RETURN:  # Nhấn Enter để kết thúc
                        if len(input_text) == 0:
                            size_arr = 10
                        else:
                            size_arr = int(input_text)
                        input_text = ""  # Đặt lại văn bản
                        array = np.random.randint(1,50,size=size_arr)
                        write_length = False
                    elif event.key == pygame.K_BACKSPACE:  # Xóa ký tự cuối
                        input_text = input_text[:-1]
                    elif len(input_text) <= 3:  # Thêm ký tự mới
                        input_text += event.unicode

                    if input_text != '':
                        input_text_print = input_text
                
                if write_slow:
                    
                    if event.key == pygame.K_RETURN:  # Nhấn Enter để kết thúc
                        write_slow = False
                        if len(input_text2) == 0:
                            speed = 1
                        else:
                            speed = int(input_text2)
                        input_text2 = ""  # Đặt lại văn bản
                    elif event.key == pygame.K_BACKSPACE:  # Xóa ký tự cuối
                        input_text2 = input_text2[:-1]
                    elif len(input_text2) <= 3:  # Thêm ký tự mới
                        input_text2 += event.unicode

                    if input_text2 != '':
                        input_text_print2 = input_text2

            if event.type == pygame.MOUSEBUTTONDOWN:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                mouse_box = pygame.Rect(x_mouse,y_mouse,20,20)

                
                # Khi nhấn vào nút show cách hoạt động sẽ hiển thị lên màn hình
                if mouse_box.colliderect(show_parameter):

                    write_slow = False
                    write_length = False
                    arr_write = False

                    if line_print != '':
                        array = convert_str_to_list(line_print)
                    elif len(input_text) == 0:
                        size_arr = 10
                        array = np.random.randint(1,50,size=size_arr)
                    else:
                        size_arr = int(input_text)
                        array = np.random.randint(1,50,size=size_arr)
                    
                    if len(input_text2) == 0:
                        speed = 1
                    else:
                        speed = int(input_text2)

                    target = random.choice(array)
                    array.sort()
                    plt.ion()
                    result = binary_search(arr=array,target=target,speed=speed)
                    if result != -1:
                        show_parameter_search(arr=array,highlight=[result],highlight_color=['lime'],target=target,speed=speed)

                    plt.ioff()
                    plt.show()

                elif mouse_box.colliderect(homebutton):
                    binarysearch_menu = False
                    main_menu = True

                elif mouse_box.colliderect(game_button):
                    binarysearch_menu = False
                    game_mainmenu = True

                elif mouse_box.colliderect(back_button):
                    binarysearch_menu = False
                    search_menu = True

                elif mouse_box.colliderect(arr_button):

                    arr_write = True
                    write_length = False
                    write_slow = False
                    line_print = ''

                elif mouse_box.colliderect(tutorial_button):

                    help_menu_4 = True

                elif mouse_box.colliderect(copy_button):
                    
                    # Đọc nội dung tệp
                    with open('SKKNTHD/Text/Search/binarysearch.txt', 'r', encoding='utf-8') as file:
                        content = file.read()

                    # Sao chép vào clipboard
                    pyperclip.copy(content)
                    copy_message = copy_message_font.render("Copied!",True,('green'))
                    screen.blit(copy_message,(400,260))

                elif mouse_box.colliderect(length_button):
                    write_length = True
                    write_slow = False
                    arr_write = False
                    input_text = ''
                    input_text_print = ''

                elif mouse_box.colliderect(slow_button):
                    write_slow = True
                    write_length = False
                    arr_write = False
                    input_text2 = ''
                    input_text_print2 = ''
                
                else:
                    if line_print != '':
                        array = convert_str_to_list(line_print)
                    elif len(input_text) == 0:
                        size_arr = 10
                        array = np.random.randint(1,100,size=size_arr)
                    else:
                        size_arr = int(input_text)
                        array = np.random.randint(1,100,size=size_arr)
                    
                    if len(input_text2) == 0:
                        speed = 1
                    else:
                        speed = int(input_text2)
            
                        
        text = number_message_font.render(input_text_print,True,('black'))
        screen.blit(text,(535,512))
        text2 = number_message_font.render(input_text_print2,True,('black'))
        screen.blit(text2,(800,512))
        text3 = number_message_font_arr.render(line_print,True,('black'))
        screen.blit(text3,(45,525))

        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            binarysearch_image = pygame.image.load('SKKNTHD/Image/binarysearch2.jpg')
        elif key[pygame.K_LEFT]:
            binarysearch_image = pygame.image.load('SKKNTHD/Image/binarysearch1.jpg')
        
    if sequentialsearch_menu == True:

        # Background
        pygame.draw.rect(screen,("white"),show_parameter)
        pygame.draw.rect(screen,("white"),homebutton)
        pygame.draw.rect(screen,('white'),game_button)
        pygame.draw.rect(screen,("white"),copy_button)
        pygame.draw.rect(screen,('white'),length_button)
        pygame.draw.rect(screen,('white'),slow_button)
        pygame.draw.rect(screen,('white'),back_button)
        screen.blit(sequentialsearch_image,(0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
            
                if arr_write:
                    
                    if event.key == pygame.K_RETURN:
                        arr_write = False
                        array = convert_str_to_list(line_print)
                        if array == 'Error':
                            line_print = 'Error'
                            array = np.random.randint(1,50,size=size_arr)
                    elif event.key == pygame.K_BACKSPACE:
                        line_print = line_print[:-1]
                    elif len(line_print) < 23:
                        line_print += event.unicode
                
                if write_length:
                    
                    if event.key == pygame.K_RETURN:  # Nhấn Enter để kết thúc
                        if len(input_text) == 0:
                            size_arr = 10
                        else:
                            size_arr = int(input_text)
                        input_text = ""  # Đặt lại văn bản
                        array = np.random.randint(1,50,size=size_arr)
                        write_length = False
                    elif event.key == pygame.K_BACKSPACE:  # Xóa ký tự cuối
                        input_text = input_text[:-1]
                    elif len(input_text) <= 3:  # Thêm ký tự mới
                        input_text += event.unicode

                    if input_text != '':
                        input_text_print = input_text
                
                if write_slow:
                    
                    if event.key == pygame.K_RETURN:  # Nhấn Enter để kết thúc
                        write_slow = False
                        if len(input_text2) == 0:
                            speed = 1
                        else:
                            speed = int(input_text2)
                        input_text2 = ""  # Đặt lại văn bản
                    elif event.key == pygame.K_BACKSPACE:  # Xóa ký tự cuối
                        input_text2 = input_text2[:-1]
                    elif len(input_text2) <= 3:  # Thêm ký tự mới
                        input_text2 += event.unicode

                    if input_text2 != '':
                        input_text_print2 = input_text2

            if event.type == pygame.MOUSEBUTTONDOWN:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                mouse_box = pygame.Rect(x_mouse,y_mouse,20,20)

                
                # Khi nhấn vào nút show cách hoạt động sẽ hiển thị lên màn hình
                if mouse_box.colliderect(show_parameter):

                    write_slow = False
                    write_length = False
                    arr_write = False

                    if line_print != '':
                        array = convert_str_to_list(line_print)
                    elif len(input_text) == 0:
                        size_arr = 10
                        array = np.random.randint(1,50,size=size_arr)
                    else:
                        size_arr = int(input_text)
                        array = np.random.randint(1,50,size=size_arr)
                    
                    if len(input_text2) == 0:
                        speed = 1
                    else:
                        speed = int(input_text2)

                    target = random.choice(array)
                    array.sort()
                    plt.ion()
                    result = sequential_search(arr=array,target=target,speed=speed)
                    if result != -1:
                        show_parameter_search(arr=array,highlight=[result],highlight_color=['lime'],target=target,speed=speed)

                    plt.ioff()
                    plt.show()

                elif mouse_box.colliderect(homebutton):
                    sequentialsearch_menu = False
                    main_menu = True

                elif mouse_box.colliderect(game_button):
                    sequentialsearch_menu = False
                    game_mainmenu = True

                elif mouse_box.colliderect(back_button):
                    sequentialsearch_menu = False
                    search_menu = True

                elif mouse_box.colliderect(arr_button):

                    arr_write = True
                    write_length = False
                    write_slow = False
                    line_print = ''

                elif mouse_box.colliderect(tutorial_button):

                    help_menu_4 = True

                elif mouse_box.colliderect(copy_button):
                    
                    # Đọc nội dung tệp
                    with open('SKKNTHD/Text/Search/sequentialsearch.txt', 'r', encoding='utf-8') as file:
                        content = file.read()

                    # Sao chép vào clipboard
                    pyperclip.copy(content)
                    copy_message = copy_message_font.render("Copied!",True,('green'))
                    screen.blit(copy_message,(400,260))

                elif mouse_box.colliderect(length_button):
                    write_length = True
                    write_slow = False
                    arr_write = False
                    input_text = ''
                    input_text_print = ''

                elif mouse_box.colliderect(slow_button):
                    write_slow = True
                    write_length = False
                    arr_write = False
                    input_text2 = ''
                    input_text_print2 = ''
                
                else:
                    if line_print != '':
                        array = convert_str_to_list(line_print)
                    elif len(input_text) == 0:
                        size_arr = 10
                        array = np.random.randint(1,100,size=size_arr)
                    else:
                        size_arr = int(input_text)
                        array = np.random.randint(1,100,size=size_arr)
                    
                    if len(input_text2) == 0:
                        speed = 1
                    else:
                        speed = int(input_text2)
            
                        
        text = number_message_font.render(input_text_print,True,('black'))
        screen.blit(text,(535,512))
        text2 = number_message_font.render(input_text_print2,True,('black'))
        screen.blit(text2,(800,512))
        text3 = number_message_font_arr.render(line_print,True,('black'))
        screen.blit(text3,(45,525))

        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            sequentialsearch_image = pygame.image.load('SKKNTHD/Image/sequentialsearch2.jpg')
        elif key[pygame.K_LEFT]:
            sequentialsearch_image = pygame.image.load('SKKNTHD/Image/sequentialsearch1.jpg')

    if jumpsearch_menu == True:

        # Background
        pygame.draw.rect(screen,("white"),show_parameter)
        pygame.draw.rect(screen,("white"),homebutton)
        pygame.draw.rect(screen,('white'),game_button)
        pygame.draw.rect(screen,("white"),copy_button)
        pygame.draw.rect(screen,('white'),length_button)
        pygame.draw.rect(screen,('white'),slow_button)
        pygame.draw.rect(screen,('white'),back_button)
        screen.blit(jumpsearch_image,(0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
            
                if arr_write:
                    
                    if event.key == pygame.K_RETURN:
                        arr_write = False
                        array = convert_str_to_list(line_print)
                        if array == 'Error':
                            line_print = 'Error'
                            array = np.random.randint(1,50,size=size_arr)
                    elif event.key == pygame.K_BACKSPACE:
                        line_print = line_print[:-1]
                    elif len(line_print) < 23:
                        line_print += event.unicode
                
                if write_length:
                    
                    if event.key == pygame.K_RETURN:  # Nhấn Enter để kết thúc
                        if len(input_text) == 0:
                            size_arr = 10
                        else:
                            size_arr = int(input_text)
                        input_text = ""  # Đặt lại văn bản
                        array = np.random.randint(1,50,size=size_arr)
                        write_length = False
                    elif event.key == pygame.K_BACKSPACE:  # Xóa ký tự cuối
                        input_text = input_text[:-1]
                    elif len(input_text) <= 3:  # Thêm ký tự mới
                        input_text += event.unicode

                    if input_text != '':
                        input_text_print = input_text
                
                if write_slow:
                    
                    if event.key == pygame.K_RETURN:  # Nhấn Enter để kết thúc
                        write_slow = False
                        if len(input_text2) == 0:
                            speed = 1
                        else:
                            speed = int(input_text2)
                        input_text2 = ""  # Đặt lại văn bản
                    elif event.key == pygame.K_BACKSPACE:  # Xóa ký tự cuối
                        input_text2 = input_text2[:-1]
                    elif len(input_text2) <= 3:  # Thêm ký tự mới
                        input_text2 += event.unicode

                    if input_text2 != '':
                        input_text_print2 = input_text2

            if event.type == pygame.MOUSEBUTTONDOWN:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                mouse_box = pygame.Rect(x_mouse,y_mouse,20,20)

                
                # Khi nhấn vào nút show cách hoạt động sẽ hiển thị lên màn hình
                if mouse_box.colliderect(show_parameter):

                    write_slow = False
                    write_length = False
                    arr_write = False

                    if line_print != '':
                        array = convert_str_to_list(line_print)
                    elif len(input_text) == 0:
                        size_arr = 10
                        array = np.random.randint(1,50,size=size_arr)
                    else:
                        size_arr = int(input_text)
                        array = np.random.randint(1,50,size=size_arr)
                    
                    if len(input_text2) == 0:
                        speed = 1
                    else:
                        speed = int(input_text2)

                    target = random.choice(array)
                    array.sort()
                    plt.ion()
                    result = jump_search(arr=array,target=target,speed=speed)
                    if result != -1:
                        show_parameter_search(arr=array,highlight=[result],highlight_color=['lime'],target=target,speed=speed)

                    plt.ioff()
                    plt.show()

                elif mouse_box.colliderect(homebutton):
                    jumpsearch_menu = False
                    main_menu = True

                elif mouse_box.colliderect(game_button):
                    jumpsearch_menu = False
                    game_mainmenu = True

                elif mouse_box.colliderect(back_button):
                    jumpsearch_menu = False
                    search_menu = True

                elif mouse_box.colliderect(arr_button):

                    arr_write = True
                    write_length = False
                    write_slow = False
                    line_print = ''

                elif mouse_box.colliderect(tutorial_button):

                    help_menu_4 = True

                elif mouse_box.colliderect(copy_button):
                    
                    # Đọc nội dung tệp
                    with open('SKKNTHD/Text/Search/jumpsearch.txt', 'r', encoding='utf-8') as file:
                        content = file.read()

                    # Sao chép vào clipboard
                    pyperclip.copy(content)
                    copy_message = copy_message_font.render("Copied!",True,('green'))
                    screen.blit(copy_message,(400,260))

                elif mouse_box.colliderect(length_button):
                    write_length = True
                    write_slow = False
                    arr_write = False
                    input_text = ''
                    input_text_print = ''

                elif mouse_box.colliderect(slow_button):
                    write_slow = True
                    write_length = False
                    arr_write = False
                    input_text2 = ''
                    input_text_print2 = ''
                
                else:
                    if line_print != '':
                        array = convert_str_to_list(line_print)
                    elif len(input_text) == 0:
                        size_arr = 10
                        array = np.random.randint(1,100,size=size_arr)
                    else:
                        size_arr = int(input_text)
                        array = np.random.randint(1,100,size=size_arr)
                    
                    if len(input_text2) == 0:
                        speed = 1
                    else:
                        speed = int(input_text2)
            
                        
        text = number_message_font.render(input_text_print,True,('black'))
        screen.blit(text,(535,512))
        text2 = number_message_font.render(input_text_print2,True,('black'))
        screen.blit(text2,(800,512))
        text3 = number_message_font_arr.render(line_print,True,('black'))
        screen.blit(text3,(45,525))

        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            jumpsearch_image = pygame.image.load('SKKNTHD/Image/jumpsearch2.jpg')
        elif key[pygame.K_LEFT]:
            jumpsearch_image = pygame.image.load('SKKNTHD/Image/jumpsearch1.jpg')

    if bfs_menu == True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if graph_write == True:

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        graph_write = False
                        graph = convert_str_to_graph(line)
                        
                        if graph == 'Error':
                            line = 'Error'
                            graph = {
                                        0: [1, 2, 3],
                                        1: [4, 5, 6],
                                        2: [7, 8, 9],
                                        3: [10, 11, 12],
                                        4: [],
                                        5: [],
                                        6: [],
                                        7: [],
                                        8: [],
                                        9: [],
                                        10:[],
                                        11:[],
                                        12:[]
                                    }
            
                    elif event.key == pygame.K_BACKSPACE:
                        line = line[:-1]
                    elif len(line) <= 40:
                        line += event.unicode

                line_print = line

            if event.type == pygame.MOUSEBUTTONDOWN:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                mouse_box = pygame.Rect(x_mouse,y_mouse,20,20)

                # Khi nhấn vào nút show cách hoạt động sẽ hiển thị lên màn hình
                if mouse_box.colliderect(show_parameter):

                    graph = convert_str_to_graph(line)
                    
                    if graph == 'Error':
                        line = 'Error'
                        graph = {
                                    0: [1, 2, 3],
                                    1: [4, 5, 6],
                                    2: [7, 8, 9],
                                    3: [10, 11, 12],
                                    4: [],
                                    5: [],
                                    6: [],
                                    7: [],
                                    8: [],
                                    9: [],
                                    10:[],
                                    11:[],
                                    12:[]
                                }

                    

                    # Chạy BFS với chuyển động dạng cây
                    bfs_with_animation_tree(graph, start=0, speed=0.5)
                
                if mouse_box.colliderect(back_button):

                    bfs_menu = False
                    search_menu = True

                if mouse_box.colliderect(tutorial_button):
                    help_menu_5 = True
                
                if mouse_box.colliderect(homebutton):

                    bfs_menu = False
                    main_menu = True
                
                if mouse_box.colliderect(copy_button):

                    with open('SKKNTHD/Text/Search/bfs.txt', 'r', encoding='utf-8') as file:
                        content = file.read()

                    # Sao chép vào clipboard
                    pyperclip.copy(content)
                    copy_message = copy_message_font.render("Copied!",True,('green'))
                    screen.blit(copy_message,(400,260))
                
                if mouse_box.colliderect(game_button):
                    
                    bfs_menu = False
                    game_mainmenu = True
                
                if mouse_box.colliderect(graph_button):

                    graph_write = True
                    line = ' '
                
                else:
                    graph_write = False
                    line_print = line

        pygame.draw.rect(screen,('black'),copy_button)
        pygame.draw.rect(screen,('black'),homebutton)
        pygame.draw.rect(screen,('black'),game_button)
        pygame.draw.rect(screen,('black'),graph_button)
        pygame.draw.rect(screen,('black'),show_parameter)
        pygame.draw.rect(screen,("black"),back_button)

        screen.blit(bfs_image,(0,0))
        
        if line_print == 'Error':
            text = number_message_font.render(line_print,True,('red'))
        else:
            text = number_message_font.render(line_print,True,('black'))
        screen.blit(text,(graph_button))

        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            bfs_image = pygame.image.load('SKKNTHD/Image/bfs2.jpg')
        elif key[pygame.K_LEFT]:
            bfs_image = pygame.image.load('SKKNTHD/Image/bfs1.jpg')

    if dfs_menu == True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if graph_write == True:

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        graph_write = False
                        graph = convert_str_to_graph(line)
                        
                        if graph == 'Error':
                            line = 'Error'
                            graph = {
                                        0: [1, 2, 3],
                                        1: [4, 5, 6],
                                        2: [7, 8, 9],
                                        3: [10, 11, 12],
                                        4: [],
                                        5: [],
                                        6: [],
                                        7: [],
                                        8: [],
                                        9: [],
                                        10:[],
                                        11:[],
                                        12:[]
                                    }
            
                    elif event.key == pygame.K_BACKSPACE:
                        line = line[:-1]
                    elif len(line) <= 40:
                        line += event.unicode

                line_print = line

            if event.type == pygame.MOUSEBUTTONDOWN:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                mouse_box = pygame.Rect(x_mouse,y_mouse,20,20)

                # Khi nhấn vào nút show cách hoạt động sẽ hiển thị lên màn hình
                if mouse_box.colliderect(show_parameter):

                    graph = convert_str_to_graph(line)
                    
                    if graph == 'Error':
                        line = 'Error'
                        graph = {
                                    0: [1, 2, 3],
                                    1: [4, 5, 6],
                                    2: [7, 8, 9],
                                    3: [10, 11, 12],
                                    4: [],
                                    5: [],
                                    6: [],
                                    7: [],
                                    8: [],
                                    9: [],
                                    10:[],
                                    11:[],
                                    12:[]
                                }

                    

                    # Chạy DFS với chuyển động dạng cây
                    dfs_with_animation_tree(graph, start=0, speed=0.5)
                
                if mouse_box.colliderect(back_button):

                    dfs_menu = False
                    search_menu = True

                if mouse_box.colliderect(tutorial_button):
                    help_menu_5 = True
                
                if mouse_box.colliderect(homebutton):

                    dfs_menu = False
                    main_menu = True
                
                if mouse_box.colliderect(copy_button):

                    with open('SKKNTHD/Text/Search/dfs.txt', 'r', encoding='utf-8') as file:
                        content = file.read()

                    # Sao chép vào clipboard
                    pyperclip.copy(content)
                    copy_message = copy_message_font.render("Copied!",True,('green'))
                    screen.blit(copy_message,(400,260))
                
                if mouse_box.colliderect(game_button):
                    
                    dfs_menu = False
                    game_mainmenu = True
                
                if mouse_box.colliderect(graph_button):

                    graph_write = True
                    line = ' '
                
                else:
                    graph_write = False
                    line_print = line

        pygame.draw.rect(screen,('black'),copy_button)
        pygame.draw.rect(screen,('black'),homebutton)
        pygame.draw.rect(screen,('black'),game_button)
        pygame.draw.rect(screen,('black'),graph_button)
        pygame.draw.rect(screen,('black'),show_parameter)
        pygame.draw.rect(screen,("black"),back_button)

        screen.blit(dfs_image,(0,0))
        
        if line_print == 'Error':
            text = number_message_font.render(line_print,True,('red'))
        else:
            text = number_message_font.render(line_print,True,('black'))
        screen.blit(text,(graph_button))

        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            dfs_image = pygame.image.load('SKKNTHD/Image/dfs2.jpg')
        elif key[pygame.K_LEFT]:
            dfs_image = pygame.image.load('SKKNTHD/Image/dfs1.jpg')

    if help_menu_5 == True:

        pygame.draw.rect(screen,('red'),close_button)
        screen.blit(help_image_5,(0,0))

        if event.type == pygame.MOUSEBUTTONDOWN:

            x_mouse,y_mouse = pygame.mouse.get_pos()
            mouse_box = pygame.Rect(x_mouse,y_mouse,20,20)

            if mouse_box.colliderect(close_button):
                help_menu_5 = False
                
    if help_menu_4 == True:

        pygame.draw.rect(screen,('red'),close_button)
        screen.blit(help_image_4,(0,0))

        if mouse_box.colliderect(close_button):
            help_menu_4 = False

    if help_menu_1 == True:

        pygame.draw.rect(screen,('red'),close_button)
        screen.blit(help_image_1,(0,0))

        if event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse,y_mouse = pygame.mouse.get_pos()
            mouse_box = pygame.Rect(x_mouse,y_mouse,20,20)

            if mouse_box.colliderect(close_button):
                help_menu_1 = False

    if help_menu_2 == True:

        pygame.draw.rect(screen,('red'),close_button)
        screen.blit(help_image_2,(0,0))

        if event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse,y_mouse = pygame.mouse.get_pos()
            mouse_box = pygame.Rect(x_mouse,y_mouse,20,20)

            if mouse_box.colliderect(close_button):
                help_menu_2 = False           


    pygame.display.update()

pygame.quit()
