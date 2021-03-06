# Stopwatch: The Game
# Author - Noel Pereira
# Submission link - http://www.codeskulptor.org/#user47_aQapkfOnEQRd8E6.py

#############################################################################################





# template for "Stopwatch: The Game"
import simplegui
# define global variables
count = 0
message = "0:00.0"
x = 0
y = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    ABC = t / 10
    D = t % 10
    BC = ABC % 60
    A = ABC / 60
    if len(str(BC)) == 0:
        return str(A) +':00'+ str(BC) +'.' + str(D)
    elif len(str(BC)) == 1:
        return str(A) +':0' +str(BC) + '.'+ str(D)
    elif len(str(BC)) == 2:
        return str(A)+ ':' + str(BC) + '.' +str(D)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_button():
    timer.start()
    
def stop_button():
    if timer.is_running():
        timer.stop()
        global x,y
        y = y + 1
        if count % 10 == 0:
            x = x + 1
    
def reset_button():
    timer.stop()
    global count
    global message
    global x
    global y
    count = 0
    message = "0:00.0"
    x = 0
    y = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global count
    global message
    count = count + 1
    message = format(count)  
        
# define draw handler
def draw(canvas):
    canvas.draw_text(message, [100,100], 36, "White")
    canvas.draw_text(str(x)+'/'+str(y), [123,190], 36, "White")
    
# create frame
frame = simplegui.create_frame('Stopwatch', 300, 300)


# register event handlers
timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw)
frame.add_button("Start", start_button, 100)
frame.add_button("Stop", stop_button, 100)
frame.add_button("Reset", reset_button, 100)


# start frame
frame.start()