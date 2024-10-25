import pgzrun 
WIDTH = 1000
HEIGHT = 550
is_game_over = False
#drawing the boxes
question_box = Rect(0,0,770,150)
question_box.move_ip(20,25)
answer_box1 = Rect(0,0,370,150)
answer_box1.move_ip(20,200)
answer_box2 = Rect(0,0,370,150)
answer_box2.move_ip(420,200)
answer_box3 = Rect(0,0,370,150)
answer_box3.move_ip(20,380)
answer_box4 = Rect(0,0,370,150)
answer_box4.move_ip(420,380)
timer_box = Rect(0,0,180,150)
timer_box.move_ip(810,25)
skip_box = Rect(0,0,180,330)
skip_box.move_ip(810,200)

#grouping the answer boxes
answer_boxes = [answer_box1,answer_box2,answer_box3,answer_box4]

#score and time
score = 0
time_left = 10


question_count = 0
question_index = 0

questions = []
#display function
def draw():
    screen.clear()
    screen.fill("black")
    screen.draw.filled_rect(question_box,"yellow")
    screen.draw.filled_rect(answer_box1,"SeaGreen2")
    screen.draw.filled_rect(answer_box2,"SeaGreen2")
    screen.draw.filled_rect(answer_box3,"SeaGreen2")
    screen.draw.filled_rect(answer_box4,"SeaGreen2")
    screen.draw.filled_rect(timer_box,"purple")
    screen.draw.filled_rect(skip_box,"purple")
    screen.draw.textbox(str(time_left),timer_box,color = ("red"))
    screen.draw.textbox(("SKIP"),skip_box,color = ("red"))
    screen.draw.textbox(question[0].strip(),question_box,color = ("black"))   
    index = 1                                                                                           
    for i in answer_boxes: 
        screen.draw.textbox(question[index],i,color = ("yellow"))
        index +=1 
    

def read_questions():
    global question_count, questions
    q_file=open("questions.txt","r")
    for q in q_file:
        print(q)
        questions.append(q)
    print(questions)
def read_next_questions():
    global question_index,questions 
    question_index = question_index+1
    return questions.pop(0).split(",")
def on_mouse_down(pos):
    global questions,question,time_left
    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            if index is int(question[5]):
                correct_answer()
            else:
                game_over()
        index +=1          
    if skip_box.collidepoint(pos):
        skip()

def skip():
    global question,time_left
    if questions and not is_game_over:
        question = read_next_questions()
        time_left = 10
    else:
        game_over()
                 

def correct_answer():
    global question,questions
    if questions:
        question = read_next_questions()
        
def game_over():
    global question,is_game_over
    question = ["game over","-","-","-","-",3]
    is_game_over = True

#timer
def timer():
    global time_left,game_over
    if is_game_over == False:
        time_left = time_left - 1
    if time_left == 0:
        game_over()
clock.schedule_interval(timer,1)
read_questions()
question = read_next_questions() 


pgzrun.go()
