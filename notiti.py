import time,pygame
import webbrowser
from win10toast_click import ToastNotifier

page_url = 'https://forms.gle/MBFJDqNV95RxPZ4S7'

def open_url():
    try:
        webbrowser.open_new(page_url)
        print('Opening URL...') 
    except:
        print('Failed to open URL. Unsupported variable type.')
   
toaster = ToastNotifier()

pygame.init()
clock = pygame.time.Clock()
while True:
        clock.tick(1)
        theTime=time.strftime("%H:%M:%S", time.localtime())
        print (theTime)
   
        if theTime == "08:30:00":
            toaster.show_toast("Start the first period at 08:30, are you studying now?",
                       "Click here to check in",
                       icon_path = '',
                       duration = 10,
                       threaded = True,
                       callback_on_click = open_url)
        if theTime == "08:35:00":
            toaster.show_toast("Start the first period at 08:30, have you checked in?",
                       "If you haven't, click here to check in",
                       icon_path = '',
                       duration = 10,
                       threaded = True,
                       callback_on_click = open_url)

        if theTime == "09:20:00":
            toaster.show_toast("Start the second period at 09:20, are you studying now?",
                       "Click here to check in",
                       icon_path = '',
                       duration = 10,
                       threaded = True,
                       callback_on_click = open_url)
        if theTime == "09:25:00":
            toaster.show_toast("Start the second period at 09:20, have you checked in?",
                       "If you haven't, click here to check in",
                       icon_path = '',
                       duration = 10,
                       threaded = True,
                       callback_on_click = open_url)
           
        if theTime == "10:20:00":
            toaster.show_toast("Start the third period at 10:20, are you studying now?",
                       "Click here to check in",
                       icon_path = '',
                       duration = 10,
                       threaded = True,
                       callback_on_click = open_url)
        if theTime == "10:25:00":
            toaster.show_toast("Start the third period at 10:20, have you checked in?",
                       "If you haven't, click here to check in",
                       icon_path = '',
                       duration = 10,
                       threaded = True,
                       callback_on_click = open_url)
           
        if theTime == "12:00:00":
            toaster.show_toast("Start the fifth period at 12:00, are you studying now?",
                       "Click here to check in",
                       icon_path = '',
                       duration = 10,
                       threaded = True,
                       callback_on_click = open_url)
        if theTime == "12:05:00":
            toaster.show_toast("Start the fifth period at 12:00, have you checked in?",
                       "If you haven't, click here to check in",
                       icon_path = '',
                       duration = 10,
                       threaded = True,
                       callback_on_click = open_url)
           
        if theTime == "12:50:00":
            toaster.show_toast("Start the sixth period at 12:50, are you studying now?",
                       "Click here to check in",
                       icon_path = '',
                       duration = 10,
                       threaded = True,
                       callback_on_click = open_url)
        if theTime == "12:55:00":
            toaster.show_toast("Start the sixth period at 12:50, have you checked in?",
                       "If you haven't, click here to check in",
                       icon_path = '',
                       duration = 10,
                       threaded = True,
                       callback_on_click = open_url)
           
        if theTime == "13:50:00":
            toaster.show_toast("Start the seventh period at 13:50, are you studying now?",
                       "Click here to check in",
                       icon_path = '',
                       duration = 10,
                       threaded = True,
                       callback_on_click = open_url)
        if theTime == "13:55:00":
            toaster.show_toast("Start the seventh period at 13:50, have you checked in?",
                       "If you haven't, click here to check in",
                       icon_path = '',
                       duration = 10,
                       threaded = True,
                       callback_on_click = open_url)
           
        if theTime == "14:40:00":
            toaster.show_toast("Start the eighth period at 14:40, are you studying now?",
                       "Click here to check in",
                       icon_path = '',
                       duration = 10,
                       threaded = True,
                       callback_on_click = open_url)
        if theTime == "14:45:00":
            toaster.show_toast("Start the eighth period at 14:40, have you checked in?",
                       "If you haven't, click here to check in",
                       icon_path = '',
                       duration = 10,
                       threaded = True,
                       callback_on_click = open_url)
