import PySimpleGUI as sg;

sg.Popup("This is my first pop up!");

var1, var2 = 5, 6;

sg.Popup('Variable number of parameters example', var1, var2, "etc");

'''
def Popup(*args,
           button_color=None,
           button_type=MSG_BOX_OK,
           auto_close=False,
           auto_close_duration=None,
           icon=DEFAULT_WINDOW_ICON,
           line_width=MESSAGE_BOX_LINE_WIDTH,
           font=None):
		   '''

sg.Popup('This box has a custom button color', button_color=('black', 'yellow'));

sg.Popup('Popup')
#sg.PopupOk('PopupOk') 失效了
sg.PopupYesNo('PopupYesNo')
sg.PopupCancel('PopupCancel')
#sg.PopupOkCancel('PopupOkCancel') 失效了
sg.PopupError('PopupError')
sg.PopupTimed('PopupTimed')
#sg.PopupAutoClose('PopupAutoClose')
'''
my_text = This call will create a scrolled box 80 characters wide 
             and a height dependent upon the number of lines of text.
             sg.PopupScrolled(my_text, size=(80, None)) Note that the
			 default max number of lines before scrolling happens is 
			 set to 50. At 50 lines the scrolling will begin.

sg.PopupScrolled(my_text)
'''
text = sg.PopupGetText('Title', 'Please input something')
sg.Popup('Results', 'The value returned from PopupGetText', text)

text = sg.PopupGetFile('Please enter a file name')
sg.Popup('Results', 'The value returned from PopupGetFile', text)

for i in range(1,10000):
    sg.OneLineProgressMeter('My Meter', i+1, 10000, 'key','Optional message')
	
for i in range(1000000):
    sg.Print(i)

