from tkinter import *#tkinter is a UI/UX capable python libray to create interactive and dynamic user iterfaces
from tkinter import ttk #we have to separately import 'ttk' for making frames within main tkinter window
from tkinter.ttk import *
from tkinter import font
import webbrowser
from tkinter import filedialog
import tkinter.messagebox
from textblob import TextBlob
import re
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.patches

#this a comment to test the successful commit 

def open_file(event=""): #create a function to take a file input with shortcut key enabled.

    open_return = filedialog.askopenfile(initialdir="/",title="Select File",filetypes=(("*.txt files",".txt"),("*.htm files",".htm"),("*.rtf files",".rtf"))) #enable permissions for some file extensions.
    for line in open_return:
        user_input_box.insert(END,line)

    open_return.close()


def save_report_eng(event=""):
    save_eng = filedialog.asksaveasfile(mode="wb", defaultextension=".html")
    if save_eng is None:
        return
    save_input = user_input_box.get("1.0",END)
    save_total_words = output_box_total.get("1.0", END)
    save_positive_words = output_box_positive.get("1.0", END)
    save_negative_words = output_box_negative.get("1.0", END)
    save_neutral_words = output_box_neutral.get("1.0", END)
    save_stop_words = output_box_stop.get("1.0", END)

    save_positive_percent = output_box_positive.get("1.0", END)
    save_negative_percent = output_box_negative.get("1.0", END)
    save_neutral_percent = output_box_neutral.get("1.0", END)
    save_stop_percent = output_box_stop.get("1.0", END)

    save_eng.write(("<h1 align='center'>ANALYSIS REPORT</h1>" + "<br>\n"+ "<hr>" + "<h2>Your Input: </h2>" + "<br>\n").encode('utf-8'))
    save_eng.write((str(save_input)+"<br>\n"+"<br>\n").encode('utf-8'))
    save_eng.write(("<hr>").encode('utf-8'))
    save_eng.write(("<h2 align='center'>RESULTS</h2>"+"<br>\n").encode('utf-8'))
    save_eng.write(("<h2 align='left'>Statistical Figures:</h2>"+"<br>\n").encode('utf-8'))
    save_eng.write(("Total Number of Words: "+str(save_total_words)+"<br>\n").encode('utf-8'))
    save_eng.write(("Number of Positive Words: "+str(save_positive_words)+"<br>\n").encode('utf-8'))
    save_eng.write(("Number of Negative Words: "+str(save_negative_words)+"<br>\n").encode('utf-8'))
    save_eng.write(("Number of Neutral Words: "+str(save_neutral_words)+"<br>\n").encode('utf-8'))
    save_eng.write(("Number of Stop Words: "+str(save_stop_words)+"<br>\n"+"<br>\n").encode('utf-8'))

    save_eng.write(("<h2 align='left'>Percentage Distribution:</h2>" + "<br>\n").encode('utf-8'))
    save_eng.write(("Positive: " + str(save_positive_percent)+" %" + "<br>\n").encode('utf-8'))
    save_eng.write(("Negative: " + str(save_negative_percent) +" %" + "<br>\n").encode('utf-8'))
    save_eng.write(("Neutral: " + str(save_neutral_percent) + " %" + "<br>\n").encode('utf-8'))
    save_eng.write(("Stop Words: " + str(save_stop_percent) + " %"+ "<br>\n" + "<br>\n").encode('utf-8'))

    save_eng.write(("<h2 align='left'>Classification of Words</h2>" + "<br>\n").encode('utf-8'))
    save_eng.write(("<b>List of Neutral Words: </b>" + str(neutral_list) + "<br>\n" + "<br>\n").encode('utf-8'))
    save_eng.write(("<b>List of Positive Words: </b>" + str(positive_list) + "<br>\n" + "<br>\n").encode('utf-8'))
    save_eng.write(("<b>List of Negative Words: </b>" + str(negative_list) + "<br>\n"+"<br>\n").encode('utf-8'))

    save_eng.write(("<h2 align='left'>Overall Emotion</h2>"+"<br>\n").encode('utf-8'))
    save_eng.write(("The Polarity Score is: "+ blob_value2 + "<br>\n").encode('utf-8'))
    if (blob_value > 0) and (blob_value <= 0.05):
        save_eng.write(("The Input is <b>'Neutral to Positive'</b>." + "<br>\n").encode('utf-8'))
    elif (blob_value > 0.05) and (blob_value <= 0.1):
        save_eng.write(("The Input is <b>'Fairly Positive'</b>." + "<br>\n").encode('utf-8'))
    elif (blob_value > 0.1):
        save_eng.write(("The Input is <b>'Extremely Positive'</b>." + "<br>\n").encode('utf-8'))
    elif (blob_value >= -0.05) and (blob_value < 0):
        save_eng.write(("The Input is <b>'Neutral to Negative'</b>." + "<br>\n").encode('utf-8'))
    elif (blob_value >= -0.1) and (blob_value < -0.05):
        save_eng.write(("The Input is <b>'Fairly Negative'</b>." + "<br>\n").encode('utf-8'))
    elif (blob_value < -0.1):
        save_eng.write(("The Input is <b>'Extremely Negative'</b>." + "<br>\n").encode('utf-8'))
    elif (blob_value == 0):
        save_eng.write(("The Input is <b>'Neutral'</b>." + "<br>\n").encode('utf-8'))

    save_eng.write(("<hr>").encode('utf-8'))
    save_eng.close()

def save_report_nep(event=""):
    save_nep = filedialog.asksaveasfile(mode='wb', defaultextension=".html")
    if save_nep is None:
        return
    save_input = user_input_box.get("1.0",END)
    save_total_words = output_box_total.get("1.0", END)
    save_positive_words = output_box_positive.get("1.0", END)
    save_negative_words = output_box_negative.get("1.0", END)
    save_neutral_words = output_box_neutral.get("1.0", END)
    save_stop_words = output_box_stop.get("1.0", END)

    save_positive_percent = output_box_positive.get("1.0", END)
    save_negative_percent = output_box_negative.get("1.0", END)
    save_neutral_percent = output_box_neutral.get("1.0", END)
    save_stop_percent = output_box_stop.get("1.0", END)

    save_nep.write(("<h1 align='center'>विश्लेषण रिपोर्ट</h1>" + "<br>\n"+ "<hr>" + "<h2>तपाइको पाठ्य : </h2>" + "<br>\n").encode('utf-8'))
    save_nep.write((str(save_input)+"<br>\n"+"<br>\n").encode('utf-8'))
    save_nep.write(("<hr>").encode('utf-8'))
    save_nep.write(("<h2 align='center'>परिणामहरू</h2>"+"<br>\n").encode('utf-8'))
    save_nep.write(("<h2 align='left'>सांख्यिकीय मूल्यांकन:</h2>"+"<br>\n").encode('utf-8'))
    save_nep.write(("कुल शब्दहरु: "+str(save_total_words)+"<br>\n").encode('utf-8'))
    save_nep.write(("सकारात्मक शब्दहरु को संख्या: "+str(save_positive_words)+"<br>\n").encode('utf-8'))
    save_nep.write(("नकारात्मक शब्दहरु को संख्या: "+str(save_negative_words)+"<br>\n").encode('utf-8'))
    save_nep.write(("निष्पक्ष शब्दहरु को संख्या: "+str(save_neutral_words)+"<br>\n").encode('utf-8'))
    save_nep.write(("अर्थहीन शब्दहरु को संख्या: "+str(save_stop_words)+"<br>\n"+"<br>\n").encode('utf-8'))

    save_nep.write(("<h2 align='left'>प्रतिशत अनुपात:</h2>"+"<br>\n").encode('utf-8'))
    save_nep.write(("सकारात्मक: " + str(save_positive_percent)+ " %"+"<br>\n").encode('utf-8'))
    save_nep.write(("नकारात्मक: " + str(save_negative_percent) + " %"+ "<br>\n").encode('utf-8'))
    save_nep.write(("निष्पक्ष: " + str(save_neutral_percent) + " %" + "<br>\n").encode('utf-8'))
    save_nep.write(("अर्थहीन: " + str(save_stop_percent) + " %" + "<br>\n" + "<br>\n").encode('utf-8'))

    save_nep.write(("<h2 align='left'>शब्दहरु को वर्गीकरण</h2>" + "<br>\n").encode('utf-8'))
    save_nep.write(("<b>पाठ्य मा निष्पक्ष शब्दहरु: </b>" + str(neutral_list) + "<br>\n" + "<br>\n").encode('utf-8'))
    save_nep.write(("<b>पाठ्य मा सकारात्मक शब्दहरु: </b>" + str(positive_list) + "<br>\n" + "<br>\n").encode('utf-8'))
    save_nep.write(("<b>पाठ्य मा नकारात्मक शब्दहरु:: </b>" + str(negative_list) + "<br>\n"+"<br>\n").encode('utf-8'))

    save_nep.write(("<h2 align='left'>पूर्णरुपी भावना</h2>"+"<br>\n").encode('utf-8'))
    save_nep.write(("पाठ्यको को भावनात्मक अंक हो: "+ blob_value2 + "<br>\n").encode('utf-8'))
    if (blob_value > 0) and (blob_value <= 0.05):
        save_nep.write(("तपाईको पाठ्य निष्पक्ष-सकारात्मक को बिचमा छ।" + "<br>\n").encode('utf-8'))
    elif (blob_value > 0.05) and (blob_value <= 0.1):
        save_nep.write(("तपाईको पाठ्य ठिक-ठिकै सकारात्मक  छ।" + "<br>\n").encode('utf-8'))
    elif (blob_value > 0.1):
        save_nep.write(("तपाईको पाठ्य धेरै सकारात्मक  छ।" + "<br>\n").encode('utf-8'))
    elif (blob_value >= -0.05) and (blob_value < 0):
        save_nep.write(("तपाईको पाठ्य निष्पक्ष-नकारात्मक को बिचमा छ।" + "<br>\n").encode('utf-8'))
    elif (blob_value >= -0.1) and (blob_value < -0.05):
        save_nep.write(("तपाईको पाठ्य ठिक-ठिकै नकारात्मक छ।" + "<br>\n").encode('utf-8'))
    elif (blob_value < -0.1):
        save_nep.write(("तपाईको पाठ्य धेरै नकारात्मक छ।" + "<br>\n").encode('utf-8'))
    elif (blob_value == 0):
        save_nep.write(("तपाईको पाठ्य निष्पक्ष छ।" + "<br>\n").encode('utf-8'))

    save_nep.write(("<hr>").encode('utf-8'))
    save_nep.close()

def clear_input_text(event=""): #create a clear/remove input function to remove input text with shortcut key enabled.
    user_input_box.delete("1.0",END)

def clear_outputs(event=""): #create a clear/remove function to clear field in output sections with shortcut key enabled.
    output_box_overall.delete("1.0",END)
    output_box_all_words_list.delete("1.0",END)
    output_box_positive.delete("1.0",END)
    output_box_negative.delete("1.0",END)
    output_box_neutral.delete("1.0",END)
    output_box_stop.delete("1.0",END)
    output_box_total.delete("1.0",END)
    output_box_positive_percent.delete("1.0",END)
    output_box_negative_percent.delete("1.0",END)
    output_box_neutral_percent.delete("1.0",END)
    output_box_stop_percent.delete("1.0",END)

#functions for helpmenu:
#english section
def precautions_eng():
    data1 = "1. Ensure you have entered some valid text in the input canvas and not left it empty. "+"\n" + "\n" + "2. Make sure that your input is in either English or Nepali language. Emogen, however, also works fine for any other input if it is in the Devanagari Script, especially Hindi. " + "\n" + "\n" + "3. Please don't use inappropriate language and use our services for ethical, professional and educational purposes. " + "\n" + "\n" + "4. Before performing another computation, clear all the previous data for better efficiency and save all necessary files like reports, reviews and graphs in your system. " + "\n" + "\n" + "5. For more information, go to the Technical Support section. "+"\n"
    tkinter.messagebox.showinfo('Before you start with EMOGEN:',data1)

def upload_eng():
    data2 = "1. While uploading a file, make sure that it is a .txt file. If not, then convert it to .txt and then upload." + "\n" + "\n" + "2. Since, configurations vary from system to sytem, .txt has been set as the standard format for uploading files in Emogen due to its effectiveness, simplicity and wider compatability.  " + "\n" + "\n" + "3. If you are not able to upload a file due to some complications in the system, you can simply enter text or copy-paste some text directly inside the input canvas. The algorithm will not be affected and will process it anyway."
    tkinter.messagebox.showinfo('Uploading Files to Input Canvas',data2)

def results_eng():
    data3 = "1. You can save a detailed report of the results in both English and Nepali as per your requirements. " + "\n" + "\n" + "2. Following are the available formats for storing results: " + "\n" + "a) .html (Recommended- for better visuals and portability) " + "\n" + "b) .txt" + "\n" + "c) .rtf" + "\n" + "\n" + "3. After filling the feedback, save the form in your PC and send it to <gltech@gmail.com>. This is for our records so that we can look into your reviews and suggesstions, and hence improvize on our services and technologies. "
    tkinter.messagebox.showinfo('Saving and Storing Results',data3)

def graphs_eng():
    data4 = '1. All controls are present in the Navigation Bar, which is generated everytime along with the graphs. You can scale, space, zoom and perform other operations on the subgraphs through the controls in the navigation bar. ' + '\n' + '\n' + "2. The combined graphical analysis is saved in the .png format for better sharing and storing capabilities. " + "\n" + "\n" + "3. Do clear the graphs before performing another computation. While, you can view previous and subsequent graphs using the navigation bar, it would be feasible to clear it for another computation. "
    tkinter.messagebox.showinfo('Managing Graphical Visualizations',data4)

def shortcut_eng():
    data5 = "Open/Upload a new file:  Ctrl+O " + "\n" + "\n" + "Save English Report:  Ctrl+E " + "\n" + "\n" + "Save Nepali Report:  Ctrl+N" + "\n" + "\n" + "Clear Input Canvas:  Ctrl+R" + "\n" + "\n" + "Clear Output Canvas:  Ctrl+D" + "\n" + "\n" + "Clear Graphs Canvas:  Ctrl+G" + "\n" + "\n" + "Undo:  Ctrl+Z" + "\n" + "\n" + "Redo: Ctrl+Y"
    tkinter.messagebox.showinfo(' Complete list of Shortcut Keys',data5)

def version_eng():
    data6 = 'EMOGEN VERSION 1.0' + '\n' + '\n' + ' © 2019, GL Technologies Pvt.Ltd- All rights reserved.'
    tkinter.messagebox.showinfo('Version Details',data6)

def precautions_nep():
    tkinter.messagebox.showinfo('इमोजेन सुरु गर्न भन्दा अगाडी:',("१. पाठ्यक्रम हाल्ने ठाउँ मा केही न केही पाठ्य त हाल्नु नै होला । " + "\n" + "\n" + "२. हालेको पाठ्य अंग्रेजी अथवा नेपाली मा हुनु पर्यो ।  तर इमोजेनले नेपाली बाहेक, देवनागरी मा लेखेको अन्य पाठ्यहरुलाई पनि संचालित गर्न सक्छ, खास गरी संस्कृत र हिन्दी। " +  "\n" + "\n" + "३. कृपया अपमानजनक भाषा को प्रयोग नगर्नुहोला । " + "\n" + "\n" + "४. अर्को विश्लेषण गर्न भन्दा अगाडी, पछिलो पाठ्य र परिणामहरुलाई  हटाईदिनु होला र सबै आवश्यक कुराहरुलाई  राम्रो संग आफ्नो कम्प्युटर मा  सेव गरि हाल्नु होला ।" +  "\n" + "\n" + "५. अरु जानकारी को लागि टेक्निकल सहयोग विभाग मा जानुहोस । "))

def upload_nep():
    tkinter.messagebox.showinfo('पाठ्य अपलोड को बारेमा जानकारी :',("१. इमोजेन मा पाठ्य अपलोड गर्दा खेरि, यो पक्का गरि हाल्नु होला की तपाई को पाठ्य .txt फोरमेट मा छ । " + "\n" + "\n" +  "२ अलग अलग कम्प्युटर को कन्फिग्रेसनहरु बेग्लै हुन्छन ।  त्यसले गर्दा, हामीले txt फोरमेट लाई मुख्य अपलोड फोरमेट राखेका छौ |" + "\n" + "\n" + "३ यदि अपलोड गर्नमा तपाईलाई अफ्ठ्यारो भईराको छ भने, पाठ्यलाई कोपी-पेस्ट पनि गर्न सक्न हुन्छ ।  एस्तो गर्दा केही फरक पर्दैन, इमोजेन मज्जा ले काम गर्छ। |"))

def results_nep():
    tkinter.messagebox.showinfo('परिणामहरु सेव गर्नको लागि जानकारी :',("१. तपाईले आफ्नो आवश्यकता अनुसार नेपाली अथवा अंग्रेजी, जुन्सुके भाषामा सेव गर्न सक्नु हुन्छ ।  " + "\n" + "\n" + "२. सेव गर्नको लागि यी फोरमेटहरु उपलब्ध छन्: "+ "\n" + "i) .html (सब भन्दा राम्रो फोरमेट)" + "\n" + "ii) .txt" + "\n" + "iii) .rtf" + "\n" + "\n" + "३. मुल्यांकन फारम भरेपछि, फारम लाई आफ्नो कम्प्युटर मा गर्नुहोस र <gltech@gmail com > मा पठाउनुहोस । यो हाम्रो रेकोर्ड को लागि हो । "))

def graphs_nep():
    tkinter.messagebox.showinfo('गरफहरु मा समस्या:',( "१. गरफहरु संग आफै एउटा नेविगेशन बार पनि आई हालचा। यो नेविगेशन बारले, तपाई गरफहरु लाई आफ्नो आवश्यकता अनुसार मिलाउन सक्नु हुन्छ। "+ "\n" + "\n" + "२. सबै ग्राफ्हरु .png  फोरमेट मा सेव हुन्छन। यो सब भन्दा राम्रो फोरमेट हो चित्रहरु सेव र शेयर गर्नको लागि ।" + "\n" + "\n" + "३. पछिलो ग्राफहरुलाई  हटाऊन नबिर्सिनु होला।  नया विशेलषण गर्नमा सजिलो हुन्छ। "))

def shortcut_nep():
    tkinter.messagebox.showinfo('शर्टकट बटनहरु:',("नया पाठ्य खोल्नको लागि:  Ctrl+O " + "\n" + "\n" + "अंग्रेजी रिपोर्ट सेव गर्नको लागि:  Ctrl+E " + "\n" + "\n" + "नेपाली रिपोर्ट सेव गर्नको लागि:  Ctrl+N" + "\n" + "\n" + "हालेको पाठ्य हटाऊनको लागि:  Ctrl+R" + "\n" + "\n" + "रिणामपहरु हटाऊनको लागि:  Ctrl+D" + "\n" + "\n" + "ग्राफ्हरु हटाऊनको लागि:  Ctrl+G" + "\n" + "\n" + "अंडू:  Ctrl+Z" + "\n" + "\n" + "रिडू: Ctrl+Y"))

def version_nep():
    tkinter.messagebox.showinfo('इमोजेन वर्जन को बारेमा:',('इमोजेन वर्जन १.०' + '\n' + '\n' + ' © २०७५, जी.एल.टेक्नोलोजीस.प्रा.लि'))
#create a GUI window and point it to tkinter.
window = Tk() #always pass the window variable as a parameter in its component objects.
window.title("EMOGEN v1.0 - ईमोजेन भावनात्मक विश्लेषक वर्जन १.० ") #set the title.
window.config(bg='white') #set a background color.
window.geometry('1280x700') #set the the window size.
window.iconbitmap(r'D:\pycharm\projects\Emogen1.0\emoicon.ico')

#call save report functions here only. Because we are calling it in the menubar
#create a menubar for file handling and formatting facilities.
menubar = Menu(window) #point it to the window and create objects as required.
filemenu = Menu(menubar)
menubar.add_cascade(label='File - फाईल',menu=filemenu)
filemenu.add_command(label='Open - खोल्नुहोस',command=open_file,accelerator="Ctrl+O")
window.bind('<Control-o>',open_file)
savemenu = Menu(filemenu)
filemenu.add_cascade(label='Save - सेव गर्नुहोस',menu=savemenu)
savemenu.add_command(label='English Report',accelerator="Ctrl+E",command=save_report_eng)
window.bind('<Control-e>',save_report_eng)
savemenu.add_command(label='नेपाली रिपोर्ट',accelerator="Ctrl+N",command=save_report_nep)
window.bind('<Control-n>',save_report_nep)
filemenu.add_separator()
filemenu.add_command(label='Exit - बन्द गर्नुहोस्', command=window.destroy)

#create edit menu.
editmenu=Menu(menubar)
menubar.add_cascade(label="Edit - इडिट",menu=editmenu)
clearmenu = Menu(editmenu)
editmenu.add_cascade(label='Clear - हटाउनुहोस',menu=clearmenu)
clearmenu.add_command(label="Input Canvas - पाठ्यक्रम",command=clear_input_text,accelerator="Ctrl+R")
window.bind("<Control-r>",clear_input_text)
clearmenu.add_command(label="Output Canvas -परिणामहरू ",command=clear_outputs,accelerator="Ctrl+D")
window.bind("<Control-d>",clear_outputs)
editmenu.add_command(label="Undo - अंडू",accelerator="Ctrl+Z")
editmenu.add_command(label="Redo - रिडू",accelerator="Ctrl+Y")

#create a help menu.
helpmenu = Menu(menubar)
menubar.add_cascade(label='Help-सहयोग',menu=helpmenu)
engmenu = Menu(helpmenu)
helpmenu.add_cascade(label="English",menu=engmenu)
engmenu.add_command(label="Precautions",command=precautions_eng)
techmenu = Menu(helpmenu)
engmenu.add_cascade(label="Technical Support",menu=techmenu)
techmenu.add_command(label='Uploading File(s)',command=upload_eng)
techmenu.add_command(label='Saving Results',command=results_eng)
techmenu.add_command(label='Managing Graphs',command=graphs_eng)
techmenu.add_command(label='Shortcut Keys',command=shortcut_eng)
engmenu.add_command(label="Version Details",command=version_eng)
nepmenu = Menu(helpmenu)
helpmenu.add_cascade(label="नेपाली",menu=nepmenu)
nepmenu.add_command(label='पूर्व जानकारी',command=precautions_nep)
techmenu2 = Menu(helpmenu)
nepmenu.add_cascade(label=' टेक्निकल सहयोग',menu=techmenu2)
techmenu2.add_command(label='फाईल अपलोड',command=upload_nep)
techmenu2.add_command(label='परिणामहरु सेव गर्नमा',command=results_nep)
techmenu2.add_command(label=' ग्राफ्हरु मा समस्या',command=graphs_nep)
techmenu2.add_command(label='शर्टकट बटनहरु',command=shortcut_nep)
nepmenu.add_command(label='इमोजेन वर्जन को बारेमा',command=version_nep)

window.config(menu=menubar)
#set rows and columns for the frame within. Here it is being done w.r.t row major.
rows = 0
while rows<50:
    window.rowconfigure(rows,weight=1)
    window.columnconfigure(rows, weight=1)
    rows +=1

#create tab style.
tabstyle = ttk.Style()
set_font = font.Font(family='tahoma', size=8) #set a certain font
tabstyle.theme_create( "mystyle", parent="alt", settings={
        "TNotebook": {"configure": {"tabmargins": [0,0,0,0] },"background":"black" },
        "TNotebook.Tab": {
            "configure": {"padding": [64, 4], "focuscolor":"#4D4D4D","background": "#E9830E","foreground":"#000000", "font":set_font },
            "map":       {"background": [("selected", "#4D4D4D")],"foreground": [("selected", "#ffffff")],
                          "expand": [("selected", [0, 0, 0, 0])] } } } )
tabstyle.configure("TNotebook", background="black", borderwidth=0)
tabstyle.theme_use("mystyle")

#now create the frame
mainframe = ttk.Notebook(window,width=50, height=200) #Notebook function of ttk method is used to define the orientation of the frame
mainframe.grid(row=0,column=0,columnspan=50,rowspan=43,sticky='NESW')

#create frame style
frame_style=ttk.Style()
frame_style.configure('TFrame',background='#4D4D4D')
frame_style.configure('Frame1.TFrame',background='#4D4D4D')

#create tabs within the frame. Now pass mainframe variable as a parameter since tabs are its component objects
#---------------------------------------------------------------------------------------------------------------#
#tab1 begins.
tab1 = ttk.Frame(mainframe, style='Frame1.TFrame') #use the style set for frame1
mainframe.add(tab1, text="GET STARTED-परिचय") #name of the tab

 #Following are the english texts
label1_eng_tab1 = Label(tab1, text="WELCOME TO EMOGEN v1.0", font=("tahoma", 17), foreground="#ffffff",background="#4D4D4D",padding=13).place(x=480, y=10)
label2_eng_tab1 = Label(tab1, text='"A SIMPLISTIC AND INTERACTIVE EMOTION AI BASED GRAPHICAL USER INTERFACE"', font=("tahoma", 11), foreground="#ffffff",background="#4D4D4D").place(x=350, y=55)
label3_eng_tab1 = Label(tab1, text='WHAT IS EMOGEN?', font=("tahoma", 10), foreground="#ffffff",background="#4D4D4D").place(x=10, y=120)
label4_eng_tab1 = Label(tab1, text='Emotion-Generator “Emogen” is an interactive and easy-to-use ', font=("tahoma", 10), foreground="#ffffff",background="#4D4D4D").place(x=10, y=140)
label5_eng_tab1 = Label(tab1, text='Emotion AI-based Graphical User Interface that scans a user input', font=("tahoma", 10), foreground="#ffffff",background="#4D4D4D").place(x=10, y=160)
label6_eng_tab1 = Label(tab1, text='and computes it’s associated emotional statistical parameters', font=("tahoma", 10), foreground="#ffffff",background="#4D4D4D").place(x=10, y=180)
label8_eng_tab1 = Label(tab1, text='such as positive, negative and neutral. ', font=("tahoma", 10), foreground="#ffffff",background="#4D4D4D").place(x=10, y=200)
label9_eng_tab1 = Label(tab1, text='It also determines the overall emotional polarity and', font=("tahoma", 10), foreground="#ffffff",background="#4D4D4D").place(x=10, y=200)
label10_eng_tab1 = Label(tab1, text='classifies the user input with respect to its emotion leanings. ', font=("tahoma", 10), foreground="#ffffff",background="#4D4D4D").place(x=10, y=220)

label11_eng_tab1 = Label(tab1, text='FEATURES OF EMOGEN :', font=("tahoma", 10), foreground="#ffffff",background="#4D4D4D").place(x=10, y=280)
label12_eng_tab1 = Label(tab1, text=' Emogen takes user input in English and Nepali languages.  ', font=("tahoma", 10), foreground="#ffffff",background="#4D4D4D").place(x=10, y=300)
label13_eng_tab1 = Label(tab1, text=' It works efficiently for any language written in a congruent script ', font=("tahoma", 10), foreground="#ffffff",background="#4D4D4D").place(x=10, y=320)
label14_eng_tab1 = Label(tab1, text='to English and Devanagari.', font=("tahoma", 10), foreground="#ffffff",background="#4D4D4D").place(x=25, y=340)
label15_eng_tab1 = Label(tab1, text=' It is a multifaceted GUI that performs statistical operations', font=("tahoma", 10), foreground="#ffffff",background="#4D4D4D").place(x=10, y=360)
label16_eng_tab1 = Label(tab1, text='and classifies inputs with respect to emotional polarities at real time. ', font=("tahoma", 10), foreground="#ffffff",background="#4D4D4D").place(x=25, y=380)
label17_eng_tab1 = Label(tab1, text=' You can visualize results with a variety of graphical representations.', font=("tahoma", 10), foreground="#ffffff",background="#4D4D4D").place(x=10, y=400)
label18_eng_tab1 = Label(tab1, text=' You can save and store your results as Emogen is enabled with ', font=("tahoma", 10), foreground="#ffffff",background="#4D4D4D").place(x=10, y=420)
label19_eng_tab1 = Label(tab1, text='file system properties.', font=("tahoma", 10), foreground="#ffffff",background="#4D4D4D").place(x=25, y=440)
label20_eng_tab1 = Label(tab1, text=' It is very ease to use, set-up, portable and compatible with ', font=("tahoma", 10), foreground="#ffffff",background="#4D4D4D").place(x=10, y=460)
label21_eng_tab1 = Label(tab1, text='with Windows, Linux and macOS.', font=("tahoma", 10), foreground="#ffffff",background="#4D4D4D").place(x=25, y=480)

#Following are the Nepali texts
label1_nep_tab1 = Label(tab1, text="ईमोजेन वर्जन १.० मा स्वागत छ!", font=("tahoma", 17), foreground="#ffffff",background="#4D4D4D").place(x=500, y=95)
label2_nep_tab1 = Label(tab1, text='"भावनात्मक विश्लेषणको लागि एउटा सरल र रचनात्मक सफ्टवेयर"', font=("tahoma", 12), foreground="#ffffff",background="#4D4D4D").place(x=450, y=126)
label3_nep_tab1 = Label(tab1, text='ईमोजेनको बारेमा:', font=("tahoma", 11), foreground="#ffffff",background="#4D4D4D").place(x=1000, y=128)
label4_nep_tab1 = Label(tab1, text='ईमोजेन एउटा सरल र रचनात्मक  प्राविधिक सफ्टवेयर प्लेटफार्म छ', font=("tahoma", 10), foreground="#ffffff",background="#4D4D4D").place(x=870, y=152)
label5_nep_tab1 = Label(tab1, text='जसले प्रयोगकर्ताबाट पाठ्य इन्पुटमा लिन्छ र पाठ्यसंग सम्बन्धित', font=("tahoma", 10), foreground="#ffffff",background="#4D4D4D").place(x=870, y=172)
label6_nep_tab1 = Label(tab1, text='भावनात्मक सांख्यिकीय मूल्यहरु- सकारात्मक, नकारात्मक र निष्पक्ष', font=("tahoma", 10), foreground="#ffffff",background="#4D4D4D").place(x=870, y=192)
label7_nep_tab1 = Label(tab1, text=' को गणन गरी, पाठ्यको पूर्णरुपी भावना बताउँछ|', font=("tahoma", 10), foreground="#ffffff",background="#4D4D4D").place(x=870, y=212)

label8_nep_tab1 = Label(tab1, text=' उपलब्ध विशेषताहरु:', font=("tahoma", 11), foreground="#ffffff",background="#4D4D4D").place(x=1000, y=262)
label9_nep_tab1 = Label(tab1, text=' ईमोजेनले प्रयोगकर्ताबाट पाठ्यक्रम,  नेपाली अथवा अंग्रेजी', font=("tahoma", 10), foreground="#ffffff",background="#4D4D4D").place(x=870, y=286)
label10_nep_tab1 = Label(tab1, text='भाषामा लिन सक्छ।', font=("tahoma", 10), foreground="#ffffff",background="#4D4D4D").place(x=880, y=306)
label11_nep_tab1 = Label(tab1, text=' कुनै पनि भाषा जो अंग्रेजी अथवा देवनागरी सम्बन्धित पाठ्यमा ', font=("tahoma", 10), foreground="#ffffff",background="#4D4D4D").place(x=870, y=326)
label12_nep_tab1 = Label(tab1, text='लेखेको छ,इमोगेनले उसको विश्लेषण गर्छ|', font=("tahoma", 10), foreground="#ffffff",background="#4D4D4D").place(x=880, y=346)
label13_nep_tab1 = Label(tab1, text=' भावनात्मक विश्लेषण बाहेक, यसले सांख्यिकीय मुल्यांकन ', font=("tahoma", 10), foreground="#ffffff",background="#4D4D4D").place(x=870, y=366)
label14_nep_tab1 = Label(tab1, text='र भावना को आधारमा वर्गीकरण पनि गर्छ|', font=("tahoma", 10), foreground="#ffffff",background="#4D4D4D").place(x=880, y=386)
label15_nep_tab1 = Label(tab1, text=' यसले विभिन्न प्रकारका ग्राफहरू पनि निकाल्न सकिन्छ|', font=("tahoma", 10), foreground="#ffffff",background="#4D4D4D").place(x=870, y=406)
label16_nep_tab1 = Label(tab1, text=' परिणामहरू लाई सजिलो तरिकाले  कम्प्युटरमा सेव गर्ने ', font=("tahoma", 10), foreground="#ffffff",background="#4D4D4D").place(x=870, y=426)
label17_nep_tab1 = Label(tab1, text='प्रावधान पनि उपलब्ध छ|', font=("tahoma", 10), foreground="#ffffff",background="#4D4D4D").place(x=880, y=446)
label18_nep_tab1 = Label(tab1, text=' सेट-अप गर्न, चलाउन र शेयर गर्नमा एकदमै सजिलो |', font=("tahoma", 10), foreground="#ffffff",background="#4D4D4D").place(x=870, y=466)
label19_nep_tab1 = Label(tab1, text='विन्दोस, लिनक्स र मैक ओएस, सबैमा चलाउन सकिन्छ |', font=("tahoma", 10), foreground="#ffffff",background="#4D4D4D").place(x=880, y=486)

emogen_banner = PhotoImage(file='emogen-banner.png')
label_tab1_image = Label (tab1, image=emogen_banner,background='#4D4D4D').place(x=445, y=150)
#tab1_canvas = Canvas(tab1,width=200, height = 600, bg="#C8F9C4", highlightthickness=2, highlightbackground="#111")
#tab1_canvas.place(x=500,y=120)
emotion_banner = PhotoImage(file='emotions.png')
label_tab1_image2 = Label (tab1, image=emotion_banner, background='#4D4D4D').place(x=30,y=10)

calc_banner = PhotoImage(file='charts.png')
label_tab1_image3 = Label (tab1, image=calc_banner, background='#4D4D4D').place(x=1000,y=10)

#tab1 ends
#---------------------------------------------------------------------------------------------------------------#
#tab2 begins
frame_style.configure('Frame2.TFrame',background='#4D4D4D')
tab2 = ttk.Frame(mainframe, style='Frame2.TFrame')
mainframe.add(tab2, text="WORKING-काम गर्ने तरिका ")

flowchart = PhotoImage(file="Flowchart2.png") #an image of the flowchart that shows the process of the GUI.
label_tab2_flowchart = Label(tab2, image=flowchart, border=0) #put the image in a label.
label_tab2_flowchart.place(x=10,y=10)

tree = PhotoImage(file="Tree.png") #an image of the flowchart that shows the process of the GUI.
label_tab2_tree = Label(tab2, image=tree, border=0) #put the image in a label.
label_tab2_tree.place(x=800,y=10)

#tab 2 ends

#---------------------------------------------------------------------------------------------------------------#

#tab 3 begins
tab3 = ttk.Frame(mainframe)
mainframe.add(tab3, text="CALCULATE-विश्लेषण गर्नुहोस्")#add some neccessary labels.
label_tab3_entry_eng = Label(tab3,text="(Upload Text: Go to File -> Open or Press Ctrl+O) OR (Enter Text Manually) ",font=('tahoma',8),background="#4D4D4D",foreground="white").place(x=2,y=18)
label_tab3_entry_nep = Label(tab3,text=" फाइल अपलोड गर्नुहोस अथवा आफै लेख्नुहोस | ",font=('tahoma',9),background="#4D4D4D",foreground="white").place(x=390,y=18)

#add a input box to take an input from the user. File uploading is also available. Function declared on top of the program.
user_input_box = Text(tab3, width=100, height=39, bg="white", font=("tahoma", 8))
user_input_box.place(x=7, y=40)
scrollbar_user_input = Scrollbar(tab3, orient=VERTICAL, command=user_input_box.yview)#add a scroll bar too.
user_input_box['yscroll'] = scrollbar_user_input.set
scrollbar_user_input.place(in_=user_input_box, relx=1.0, relheight=1.0, bordermode="outside")
#create multiple output boxes for the different kinds of outputs. Place them in a canvas for better organization.
label_tab3_getoutput_eng = Label(tab3,text="(Get your Results Here) ",font=('tahoma',8),background="#4D4D4D",foreground="white").place(x=670,y=18)
label_tab3_getoutput_nep = Label(tab3,text=" - तपाईंको परिणामहरू|",font=('tahoma',9),background="#4D4D4D",foreground="white").place(x=790,y=18)
label_tab3_next_page_eng = Label(tab3,text=" Graphs in Next Tab ",font=('tahoma',8),background="#4D4D4D",foreground="white").place(x=1030,y=18)
label_tab3_next_page_nep = Label(tab3,text=" - अगाडि ग्राफहरु छन् --> ",font=('tahoma',9),background="#4D4D4D",foreground="white").place(x=1130,y=18)

tab3_canvas = Canvas(tab3,width=600,height=510,bg="#D3D3D3", highlightthickness=0, highlightbackground="black")
tab3_canvas.place(x=670,y=40)
stats_image = PhotoImage(file='stats-img.png')
tab3_canvas_stats = Label(tab3_canvas,image=stats_image,background='#D3D3D3').place(x=420,y=10)
stats_icon = PhotoImage(file='stats_icon.png')
tab3_canvas_heading_icon = Label(tab3_canvas,image=stats_icon,background='#D3D3D3').place(x=70,y=10)
tab3_canvas_heading1 = Label(tab3_canvas,text="STATISTICAL FIGURES - शब्दहरुको सांख्यिकीय मूल्यांकन|",font=('tahoma',9,'bold'),background="#D3D3D3",foreground="black").place(x=100,y=10)
tab3_canvas_total = Label(tab3_canvas,text="Total Number of Words - कुल शब्दहरू :",font=('tahoma',8),background="#D3D3D3",foreground="black").place(x=30,y=40)
output_box_total = Text(tab3_canvas, width=12, height=1, bg="white", font=("tahoma", 9))
output_box_total.place(x=310, y=40)
tab3_canvas_positive = Label(tab3_canvas,text="Number of Positive Words - सकारात्मक शब्दहरूको संख्या:",font=('tahoma',8),background="#D3D3D3",foreground="black").place(x=30,y=60)
output_box_positive = Text(tab3_canvas, width=12, height=1, bg="white", font=("tahoma", 9))
output_box_positive.place(x=310, y=60)
tab3_canvas_negative = Label(tab3_canvas,text="Number of Negative Words - नकारात्मक शब्दहरूको संख्या:",font=('tahoma',8),background="#D3D3D3",foreground="black").place(x=30,y=80)
output_box_negative = Text(tab3_canvas, width=12, height=1, bg="white", font=("tahoma", 9))
output_box_negative.place(x=310, y=80)
tab3_canvas_neutral = Label(tab3_canvas,text="Number of Neutral Words - निष्पक्ष शब्दहरूको संख्या:",font=('tahoma',8),background="#D3D3D3",foreground="black").place(x=30,y=100)
output_box_neutral = Text(tab3_canvas, width=12, height=1, bg="white", font=("tahoma", 9))
output_box_neutral.place(x=310, y=100)
tab3_canvas_stop = Label(tab3_canvas,text="Number of Stop Words - अर्थहीन शब्दहरूको संख्या:",font=('tahoma',8),background="#D3D3D3",foreground="black").place(x=30,y=120)
output_box_stop = Text(tab3_canvas, width=12, height=1, bg="white", font=("tahoma", 9))
output_box_stop.place(x=310, y=120)

percent_icon = PhotoImage(file='percent.png')
tab3_canvas_percent_icon = Label(tab3_canvas,image=percent_icon,background='#D3D3D3').place(x=70,y=175)
tab3_canvas_heading2 = Label(tab3_canvas,text="PERECNTAGE COMPOSITION - प्रतिशत अनुपात|",font=('tahoma',9,'bold'),background="#D3D3D3",foreground="black").place(x=100,y=180)
tab3_positive_percent = Label(tab3_canvas,text="Postive - सकारात्मक  :",font=('tahoma',8),background="#D3D3D3",foreground="black").place(x=30,y=210)
output_box_positive_percent = Text(tab3_canvas, width=8, height=1, bg="white", font=("tahoma", 9))
output_box_positive_percent.place(x=160, y=210)
tab3_negative_percent = Label(tab3_canvas,text="Negative - नकारात्मक  :",font=('tahoma',8),background="#D3D3D3",foreground="black").place(x=248,y=210)
output_box_negative_percent = Text(tab3_canvas, width=8, height=1, bg="white", font=("tahoma", 9))
output_box_negative_percent.place(x=380, y=210)
tab3_neutral_percent = Label(tab3_canvas,text="Neutral - निष्पक्ष :",font=('tahoma',8),background="#D3D3D3",foreground="black").place(x=30,y=230)
output_box_neutral_percent = Text(tab3_canvas, width=8, height=1, bg="white", font=("tahoma", 9))
output_box_neutral_percent.place(x=160, y=230)
tab3_stop_percent = Label(tab3_canvas,text="Stop Words - अर्थहीन :",font=('tahoma',8),background="#D3D3D3",foreground="black").place(x=250,y=230)
output_box_stop_percent = Text(tab3_canvas, width=8, height=1, bg="white", font=("tahoma", 9))
output_box_stop_percent.place(x=380, y=230)

classify_icon = PhotoImage(file='classify.png')
tab3_canvas_classify_icon = Label(tab3_canvas,image=classify_icon,background='#D3D3D3').place(x=65,y=265)
tab3_canvas_heading3 = Label(tab3_canvas,text="CLASSIFICATION OF WORDS- शब्दहरु को वर्गीकरण|",font=('tahoma',9,'bold'),background="#D3D3D3",foreground="black").place(x=100,y=270)
tab3_all_words_list = Label(tab3_canvas,text="Positive, Negative, Neutral and Bipolar Words :",font=('tahoma',8),background="#D3D3D3",foreground="black").place(x=30,y=300)
tab3_all_words_list2 = Label(tab3_canvas,text="सकारात्मक,नकारात्मक,निष्पक्ष र द्विध्रुवीय शब्दहरु :",font=('tahoma',8),background="#D3D3D3",foreground="black").place(x=30,y=320)
output_box_all_words_list = Text(tab3_canvas, width=31, height=8, bg="white", font=("tahoma", 9))
output_box_all_words_list.place(x=30, y=340)

sentscale_icon = PhotoImage(file='sentscale.png')
tab3_canvas_sentscale_icon = Label(tab3_canvas,image=sentscale_icon,background='#D3D3D3').place(x=400,y=270)
tab3_canvas_overall = Label(tab3_canvas,text="OVERALL EMOTION- पाठ्यको पूर्णरुपी भावना|",font=('tahoma',8,'bold'),background="#D3D3D3",foreground="black").place(x=325,y=320)
output_box_overall = Text(tab3_canvas, width=39, height=6, bg="white", font=("tahoma", 9))
output_box_overall.place(x=300, y=340)

save_icon = PhotoImage(file='save-icon.png')
tab3_canvas_save_icon = Label(tab3_canvas,image=save_icon,background="#D3D3D3",foreground="black").place(x=380,y=437)
tab3_canvas_save = Label(tab3_canvas,text="Save Report - रिपोर्ट सेव गर्नुहोस|",font=('tahoma',9,'bold'),background="#D3D3D3",foreground="black").place(x=400,y=440)

btnsavestyle=ttk.Style()
btnsavestyle.configure("bsave.TButton", padding=0,font=('tahoma',9,'underline'), relief="flat",background="#D3D3D3",foreground="black",cursor='hand1',width=17) #set a certain style for the button.
btn_eng_save = ttk.Button(tab3_canvas,text="- English",style="bsave.TButton",command=save_report_eng)
btn_eng_save.place(x=405,y=468)
save_eng = PhotoImage(file='english-icon.png')
btn_eng_save.configure(image=save_eng,compound=RIGHT)
save_nep = PhotoImage(file='nepali-icon.png')
btn_nep_save = ttk.Button(tab3_canvas,text="- नेपाली",style="bsave.TButton",command=save_report_nep)
btn_nep_save.place(x=495,y=465)
btn_nep_save.configure(image=save_nep,compound=RIGHT)

def sentiment_analyzer(): #create a function for the button.

 user_input = user_input_box.get("1.0",END)

 positive_words = ['a+','appropriate','abound','abounds','abundance','abundant','accessable','accessible','acclaim','acclaimed','acclamation','accolade','accolades','accommodative','accomplish','accomplished','accomplishment','accomplishments','accurate','accurately','achievable','achievement','achievements','achievable','acumen','adaptable','adaptive','adequate','adjustable','admirable','admirably','admiration','admire','admirer','admiring','admiringly','adorable','adore','adored','adorer','adoring','adoringly','adroit','adroitly','adulate','adulation', 'adulatory','advanced','advantage','advantageous','advantageously','advantages','adventuresome','adventurous','advocate','advocated','advocates','affability','affable','affably','affectation','affection','affectionate','affinity','affirm','affirmation','affirmative','affluence','affluent','afford','affordable','affordably','agile','agilely','agility','agreeable','agreeableness','agreeably','all-around','alluring','alluringly','altruistic','altruistically',
'amaze','amazed','amazement','amazes','amazing','amazingly','ambitious','ambitiously','ameliorate','amenable','amenity','amiability','amiabily','amiable','air','amicability','amicable','amicably','amity','ample','amply','amuse','amusing','amusingly','angel','angelic','apotheosis','appeal','appealing','applaud','appreciable','appreciate','appreciated','appreciates','appreciative','appreciatively','appropriate','approval','approve','ardent','ardently','ardor','articulate','aspiration','aspirations','aspire','assurance','assurances','assure','assuredly','assuring','astonish','astonished','astonishing','astonishingly','astonishment','astound','astounded','astounding','astoundingly','astutely','attentive','attraction','attractive','attractively','attune','audible','audibly','auspicious','authentic','authoritative','autonomous','available','aver','avid','avidly','award','awarded','awards','awe','awed','awesome','awesomely','awesomeness','awestruck','backbone','balanced','bargain','beauteous','beautiful','beautifully','beautify','beauty','beckon','beckoned','beckoning','beckons','believable','beloved','benefactor','beneficent','beneficial','beneficially','beneficiary','benefit','benefits','benevolence','benevolent','benifits','best','best-known','best-performing','best-selling','better','better-known','better-than-expected','beutifully','blameless','bless','blessing','bliss','blissful','blissfully','blithe','blockbuster','bloom','blossom','bolster','bonny','bonus','bonuses','boom','booming','boost','boundless','bountiful','brainiest','brainy','brand-new','brave','bravery','bravo','breakthrough','breakthroughs','breathlessness','breathtaking','breathtakingly','breeze','bright','brighten','brighter','brightest','brilliance','brilliances','brilliant','brilliantly','brisk','brotherly','bullish','buoyant','cajole','calm','calming','carp','calmness','capability','capable','capably','captivate','captivating','carefree','cashback','cashbacks','catchy','celebrate','celebrated','celebration','celebratory','champ','champion','charisma','charismatic','charitable','charm','charming','charmingly','chaste','cheaper','cheapest','cheer','cheerful','cheery','cherish','cherished','cherub','chic','chivalrous','chivalry','civility','civilize','clarity','classic','classy','clean','cleaner','cleanest','cleanliness','cleanly','clear','clear-cut','cleared','clearer','clearly','clears','clever','cleverly','cohere','coherence','coherent','cohesive','colorful','comely','comfort','comfortable','cordial','comfortably','comforting','comfy','commend','commendable','commendably','commitment','commodious','compact','compactly','compassion','compassionate','compatible','competitive','complement','complementary','complemented','complements','compliant','compliment','complimentary','comprehensive','conciliate','conciliatory','concise','confidence','confident','congenial',
'congratulate','congratulations','congratulatory','conscientious','considerate','consistent','consistently','constructive','consummate','contentment','continuity','contrasty','contribution','convenience','convenient','conveniently','convience','convienient','convient','convincing','convincingly','cool','coolest','cooperative','cooperatively','cornerstone','correct','correctly','cost-effective','cost-saving','counter-attack','counter-attacks','courage','courageous','courageously','courageousness','courteous','courtly','covenant','cozy','creative','credence','credible','crisp','crisper','cure','cushy','cute','cuteness','danke','danken','daring','daringly','darling','dashing','dauntless','dawn','dazzle','dazzled','dazzling','dead-cheap','dead-on','decency','decent','decisive','decisiveness','dedicated','defeat','defeated','defeating','defeats','defender','deference','deft','deginified','delectable','delicacy','delicate','delicious','delight','delighted','delightful','delightfully','delightfulness',
'dependable','dependably','deservedly','deserving','desirable','desiring','desirous','destiny','detachable','devout','dexterous','dexterously','dextrous','dignified','dignify','dignity','diligence','diligent','diligently','diplomatic','dirt-cheap','distinction','distinctive','distinguished','diversified', 'divine','divinely','dominate','dominated','dominates','dote','dotingly','doubtless','dreamland','dumbfounded','dumbfounding','dummy-proof','durable','dynamic','eager','eagerly','eagerness','earnest','earnestly','earnestness','ease','eased','eases','easier','easiest','easiness','easing','easy','easy-to-use','easygoing','ebullience','ebullient','ebulliently', 'ecenomical','economical','ecstasies','ecstasy','ecstatic','ecstatically','edify','educated','effective','effectively','effectiveness','effectual','efficacious','efficient','efficiency','efficiently','effortless','effortlessly','effusion','effusive','effusively','effusiveness','elan','elate','elated','elatedly','elation',
'electrify','elegance','elegant','elegantly','elevate','elite','eloquence','eloquent','eloquently','embolden','eminence','eminent','empathize','empathy','empower','empowerment','enchant','enchanted','enchanting','enchantingly','encourage','encouragement','encouraging','encouragingly','endear','endearing','endorse','endorsed','endorsement','endorses','endorsing','energetic','energize','energy-efficient','energy-saving','engaging','engrossing','enhance','enhanced','enhancement','enhances','enjoy','enjoyable','enjoyably','enjoyed','enjoying','enjoyment','enjoys','enlighten','enlightened','enlightenment','enliven','ennoble','enough','enrapt','enrapture','enraptured','enrich','enrichment','enterprising','entertain','entertaining','entertains','enthrall','enthralled','enthuse','enthusiasm','enthusiast','enthusiastic','enthusiastically','entice','formidable','enticed','enticing','enticingly','entranced','entrancing','entrust','enviable','enviably','equitable','ergonomical','err-free','erudite','ethical','eulogize','euphoria','euphoric','euphorically','evaluative','evenly','eventful','everlasting','evocative','exalt','exaltation','exalted','exaltedly','exalting','exaltingly','examplar','examplary','excellent','excel','exceled','excellence','excellency','excellently','excels','exceptional','exceptionally','excite','excited','excitedly','excitedness','excitement','excites','exciting','excitingly','exhilarate','exhilarating','exhilaratingly','exhilaration','exonerate','expeditiously','expertly','exquisite','exquisitely','extol','extraordinarily','extraordinary','exuberance','exuberant','exuberantly','exult','exultant','exultation','exultingly','eye-catch','eye-catching','eyecatch','eyecatching','fabulous','fabulously','facilitate','fair','fairly','fairness','faithful','faithfully','faithfulness',
'fame','famed','famous','famously','fancier','fancinating','fancy','fanfare','fans','fantastic','fantastically','fascinate','fascinating','fascinatingly','fascination','fashionable','fashionably','fast','fast-growing','fast-paced','faster','fastest','fastest-growing','faultless','favorable','favorite','fearless','fearlessly','feasible','feasibly','feat','fecilitous','feisty','felicitate','felicitous','felicity','fertile','fervent','fervently','fervid','fervidly','fervor','festive','fidelity','fiery','fine','fine-looking','finely','finer','finest','firmer','first-class','first-in-class','first-rate','flashy','flatter','flattering','flatteringly','flawless','flawlessly','flexibility','flexible','flourish','flourishing','fluent','flutter','fond','fondly','fondness','foolproof','foremost','foresight','formidable','fortitude','fortuitous','fortuitously','fortunate','fortunately','fortune','fragrant','freedom','fresh','fresher','freshest','friendliness','friendly','friend','frolic','frugal','fruitful','fulfillment','futuristic','gaiety','gaily','gain','gained','gainful',
'gainfully','gaining','gains','gallant','gallantly','galore','geekier','geeky','gem','gems','generosity','generous','generously','genial','genius','gentle','gentlest','genuine','gifted','glad','gross','gladden','gladly','gladness','glamorous','glee','gleeful','gleefully','glimmer','glimmering','glisten','glistening','glitter','glitz','glorify','glorious','gloriously','glory','glow','glowing','glowingly','godlike','godsend','gold','golden','good','goodly','goodness','goodwill','gorgeous','gorgeously','grace','graceful','gracefully','gracious','graciously','graciousness','grand','grandeur','grateful','gratefully','gratification','gratified','gratifies','gratify','gratifying','gratifyingly','gratitude','great','greatest','greatness','grin','groundbreaking','guarantee','guidance','guiltless','gumption','gush','gusto','gutsy',
'hail','halcyon','hale','hallmark','hallmarks','hallowed','handier','handily','hands-down','handsome','handsomely','handy','happier','happily','happiness','happy','hard-working','hardier','hardy','harmless','harmonious','harmoniously','harmonize','harmony','headway','heal','healthful','healthy','hearten','heartening','heartfelt','heartily','heartwarming','heaven','heavenly','helped','helpful','helping','hero','harbor','heroic','heroically','heroize','heros','high-quality','high-spirited',
'hilarious','holy','homage','honest','honesty','honor','honorable','honored','honoring','hooray','hopeful','hospitable','hug','humane','humble','humility','humor','humorous','humorously','humour','humourous','ideal','idealize','ideally','idol','idolize','idolized','idyllic','illuminate','illuminating','illumine','illustrious','ilu','imaginative','immaculate','immaculately','immense','impartial','impartiality','impartially','impassioned','impeccable','impeccably','important','impress','impressed','impresses','impressive','impressively','impressiveness','improve','improved','improvement','improvements','improves','improving','incredible','incredibly','indebted','individualized','indulgence','indulgent','industrious','inestimable','inestimably','inexpensive','infallibility','infallible','infallibly','influential','ingenious','ingeniously','ingenuity','ingenuous','ingenuously','innocuous','innovation','innovative','insightful',
'insightfully','inspiration','inspirational','inspire','inspiring','instantly','instructive','instrumental','integral','integrated','intelligence','intelligent','intelligible','interesting','interests','intimacy','intimate','intricate','intrigue','intriguing','intriguingly','intuitive','invaluable','invaluablely','inventive','invigorate','invigorating','invincibility','invincible','inviolable','inviolate','invulnerable','irreplaceable','irreproachable','irresistible','irresistibly','issue-free','jaw-droping','jollify','jolly','jovial','joy',
'joyful','joyfully','joyous','joyously','jubilant','jubilantly','jubilate','jubilation','jubiliant','judicious','justly','keen','keenly','keenness','kid-friendly','kindliness','kindly','kindness','knowledgeable','kudos','large-capacity','laud','laudable','laudably','lavish','lavishly','law-abiding','lawful','lawfully','lead','leading','leads','lean','led','legendary','leverage','levity','liberate','liberation','liberty','lifesaver','light-hearted','lighter','likable','like','liked','likes','liking','lionhearted','lively','logical','long-lasting','lovable','lovably','love','loved','loveliness',
'lovely','lover','loves','loving','low-cost','low-price','low-priced','low-risk','lower-priced','loyal','loyalty','lucid','lucidly','luck','luckier','luckiest','luckiness','lucky','lucrative','luminous','lush','luster','lustrous','luxuriant','luxuriate','luxurious','luxuriously','luxury','lyrical','magic','magical','magnanimous','magnanimously','magnificence','magnificent','magnificently','majestic','majesty','manageable','maneuverable','marvel','marveled','marvelled','marvellous','marvelous','marvelously','marvelousness','marvels','master','masterful','masterfully','masterpiece','masterpieces','masters','mastery','matchless','mature','maturely','maturity','meaningful','memorable','merciful','mercifully','mercy',
'merit','meritorious','merrily','merriment','merriness','merry','mesmerize','mesmerized','mesmerizes','mesmerizing','mesmerizingly','meticulous','meticulously','mightily','mighty','mind-blowing','miracle','miracles','miraculous','miraculously','miraculousness','modern','modest','modesty','momentous','monumental','monumentally','morality','motivated','multi-purpose','navigable','neat','neatest','neatly','nice','nicely','nicer','nicest','nifty','nimble','noble','nobly','noiseless','non-violence','non-violent','notably','noteworthy','nourish','nourishing',
'nourishment','novelty','novel','nurturing','oasis','obsession','obsessions','obtainable','openly','openness','optimal','optimism','optimistic','opulent','orderly','originality','outdo','outdone','outperform','outperformed','outperforming','outperforms','outshine','outshone','outsmart','outstanding','outstandingly','outstrip','outwit','ovation','overjoyed','overtake','overtaken','overtakes','overtaking','overtook','overture','pain-free','painless','painlessly','palatial','pamper','pampered','pamperedly','pamperedness','pampers','panoramic','paradise','paramount','pardon',
'passion','passionate','passionately','patience','patient','patiently','patriot','patriotic','peace','peaceable','peaceful','peacefully','peacekeepers','peach','peerless','pep','pepped','pepping','peppy','peps','perfect','perfection','perfectly','permissible','perseverance','persevere','personages','personalized','phenomenal','phenomenally','picturesque','piety','pinnacle','playful','playfully','pleasant','pleasantly','pleased','pleases','pleasing','pleasingly','pleasurable','pleasurably','pleasure','plentiful','pluses','plush','plusses','poetic',
'poeticize','poignant','poise','poised','polished','polite','politeness','popular','portable','posh','positive','positively','positives','powerful','powerfully','positivity','praise','praiseworthy','praising','pre-eminent','precious','precise','precisely','preeminent','prefer','preferable','preferably','preferred','preferring','prefers','premier','prestige','prestigious','prettily','pretty','priceless','pride','principled','privilege','privileged','prize','proactive','problem-free','problem-solver','prodigious','prodigiously','prodigy','productive','productively',
'proficient','proficiently','profound','profoundly','profuse','profusion','progress','progressive','prolific','prominence','prominent','promising','promoter','prompt','promptly','proper','properly','propitious','propitiously','pros','prosper','prosperity','prosperous','protect','protection','protective','proud','proven','providence','proving','prowess','prudence','prudent','prudently','punctual','pure','purify','purposeful','quaint','qualified','qualify','quicker','quiet','quieter',
'radiance','radiant','rapid','rapport','rapt','rapture','raptureous','raptureously','rapturous','rapturously','rational','razor-sharp','reachable','readable','readily','ready','reaffirm','reaffirmation','realistic','realizable','reasonable','reasonably','reasoned','reassurance','reassure','receptive','reclaim','recomend','recommend','recommendation','recommendations','recommended','reconcile','reconciliation','record-setting','recover','recovery','rectification','rectify','rectifying','redeem','redeeming','redemption','refine','refined','refinement','reform','reformed','reforming','reforms','refresh','refreshed','refreshing','refund','refunded','regal','regally','regard','rejoice','rejoicing','rejoicingly','rejuvenate','rejuvenated',
'rejuvenating','relaxed','relent','reliable','reliably','relief','relish','remarkable','remarkably','remedy','remission','remunerate','renaissance','renewed','renown','renowned','replaceable','reputable','reputation','resilient','resolute','resound','resounding','resourceful','resourcefulness','respect','respectable','respectful','respectfully','respite','resplendent','responsibly','responsive','restful','restored','restructure','restructured','restructuring','retractable','revel','revere','reverence','reverent','reverently','revitalize','revival','revive','revives','revolutionary','revolutionize','revolutionized','revolutionizes','reward','rewarding','rewardingly','rich','richer','richly','richness','right',
'righten','righteous','righteously','righteousness','rightful','rightfully','rightly','rightness','risk-free','robust','rockstar','rockstars','romantic','romantically','romanticize','roomier','roomy','rosy','safe','safely','sagacity','sagely','saint','saintliness','saintly','salutary','salute','sane','satisfactorily','satisfactory','satisfied','satisfies','satisfy','satisfying','satisified','saver','savings','savior','savvy','scenic','seamless','seasoned','secure','securely','scientific','selective','self-determination','self-respect','self-satisfaction','self-sufficiency','self-sufficient','sensation','sensational','sensationally','sensations','sensible','sensibly','sensitive','serene',
'serenity','sexy','sharp','sharper','sharpest','shimmering','shimmeringly','shine','shiny','significant','silent','simpler','simplest','simplified','simplifies','simplify','simplifying','sincere','sincerely','sincerity','skill','skilled','skillful','skillfully','slick','smart','smarter','smartest','smartly','smile','smiles','smiling','smilingly','smitten','smooth','smoother','smoothes','smoothest','smoothly','snappy','snazzy','sociable','soft','softer','solace','solicitous','solicitously','solid','solidarity','soothe','soothingly','sophisticated','soulful','soundly','soundness','spacious','sparkle','sparkling','spectacular','spectacularly','speedily','speedy','spellbind','spellbinding','spellbindingly','spellbound','spirited','spiritual','splendid','splendidly',
'splendor','spontaneous','sporty','spotless','sprightly','stability','stabilize','stable','stainless','standout','state-of-the-art','stately','statuesque','staunch','staunchly','staunchness','steadfast','steadfastly','steadfastness','steadiest','steadiness','steady','stellar','stellarly','stimulate','stimulates','stimulating','stimulative','stirringly','straighten','straightforward','streamlined','striking','strikingly','striving','strong','stronger','strongest','stunned','stunning','stunningly','stupendous','stupendously','sturdier','sturdy','stylish','stylishly','stylized','suave','suavely','sublime','subsidize','subsidized','subsidizes','subsidizing','substantive','succeed','succeeded','succeeding','succeeds','success','successes',
'successful','successfully','suffice','sufficed','suffices','sufficient','sufficiently','suitable','sumptuous','sumptuously','sumptuousness','super','superb','superbly','superior','superiority','supple','support','supported','supporter','supporting','supportive','supports','supremacy','supreme','supremely','surmount','surpass','surreal','survival','survivor','sustainability','sustainable','swank','swankier','swankiest','swanky','sweeping','sweet','sweeten','sweetheart','sweetly','sweetness','swift','swiftness','talent','talented', 'talents','tantalize','tantalizing','tantalizingly','tempt',
'tempting','temptingly','tenacious','tenaciously','tenacity','tender','tenderly','terrific','terrifically','thank','thankful','thoughtful','thoughtfully','thoughtfulness','thrift','thrifty','thrill','thrilled','thrilling','thrillingly','thrills','thrive','thriving','thumb-up','thumbs-up','tickle','tidy','time-honored','timely','titillate','titillating','titillatingly','togetherness','tolerable','tolerant','toll-free','top','top-notch','top-quality','topnotch','tops','tough','tougher','toughest','traction','tranquil','tranquility','transparent','treasure','tremendously','trendy','triumph','triumphal','triumphant','triumphantly','trivially','trophy','trouble-free','trump',
'trumpet','trust','trusted','trusting','trustingly','trustworthiness','trustworthy','trusty','truthful','truthfully','truthfulness','twinkly','ultra-crisp','unabashed','unabashedly','unaffected','unassailable','unbeatable','unbiased','unbound','uncomplicated','unconditional','undamaged','undaunted','understandable','undisputable','undisputably','undisputed','unencumbered','unequivocal','unequivocally','unfazed','unfettered','unforgettable','unity','unlimited','unmatched','unparalleled','unquestionable','unquestionably','unreal','unrestricted','unrivaled','unselfish','unwavering','upbeat','upgradable','upgradeable','upgraded','upheld','uphold','uplift','uplifting','upliftingly','upliftment','upscale','usable','useable','useful','user-friendly','user-replaceable',
'valiant','valiantly','valor','valuable','variety','venerate','verifiable','veritable','versatile','versatility','vibrant','vibrantly','victorious','victory','viewable','vigilance','vigilant','virtue','virtuous','virtuously','visionary','vivacious','vivid','vouch','vouchsafe','warm','warmer','warmhearted','warmly','warmth','wealthy','welcome','well','well-backlit','well-balanced','well-behaved','well-being','well-bred','well-connected','well-educated','well-established','well-informed','well-intentioned','well-known','well-made','well-managed','well-mannered','well-positioned','well-received','well-regarded','well-rounded','well-run','well-wishers','wellbeing','wholeheartedly','wholesome','wieldy','willing','willingly','willingness','win','windfall','winnable','winner',
'winners','winning','wins','wisdom','wise','wisely','witty','won','wonder','wonderful','wonderfully','wonderous','wonderously','wonders','wondrous','woo','work','workable','worked','works','world-famous','worth','worth-while','worthiness','worthwhile','worthy','wow','wowed','wowing','wows','yay','youthful','zeal','zenith','zest','zippy',
'प्रशस्त', 'बहुतायत', 'प्रचुर','पहुँचयोग्य','पहुँच योग्य','प्रशंसा','प्रशंसा गरिएको', 'उपलब्ध', 'उपलब्धि', 'सही', 'प्राप्त गर्न', 'उपलब्धिहरू', 'अनुकूल योग्य', 'अनुकूली','पर्याप्त','समायोज्य','प्रशंसनीय', 'मनमोहक', 'साहसिक', 'अधिवक्ता', 'अधिवक्ताहरू', 'प्रभावकारी', 'सम्भव', 'प्रभाव', 'स्नेह', 'स्नेहेट', 'पुष्टि', 'सकारात्मक', 'सम्भावना', 'सम्भोग', 'किफायती', 'सस्ती', 'सस्तो', 'स्वीकार्य', 'अद्भुत', 'महत्वाकांक्षी', 'योग्य', 'मनोरञ्जन', 'स्वर्गदूत', 'स्वर्गिक', 'प्रशस्त', 'सराहनीय', 'सराहना', 'उपयुक्त','अनुमोदन', 'आशिष्', 'योग्यता', 'धर्म', 'धर्मार्थ', 'धार्मिक', 'आशानिर्देश', 'आश्वासन', 'अचम्म', 'अचम्मलाग्दो','आश्चर्यचकित', 'आकर्षण', 'आकर्षक', 'आकर्षित', 'शुभ', 'प्रामाणिक', 'प्राधिकृत', 'आधिकारिक', 'स्वायत्त', 'सुन्दर','खूबसूरत','सुन्दरता', 'विश्वास', 'प्रेमी', 'प्रेमिका', 'अनमोल', 'फायदेमंद', 'लाभ', 'फायदा', 'लाभकारी', 'फायदेक्टर',
'फायदेमेट', 'फायदेमरी', 'लाभार्थी', 'फाइदाहरू', 'उत्तम-प्रदर्शन', 'उत्तम बिक्रि', 'राम्रो', 'उत्त', 'अपेक्षित', 'निर्दोष', 'दिमागी', 'दिग्गज', 'बहादुर', 'शानदार', 'भ्रातृत्व', 'भाईचारा', 'सफलता', 'सफल', 'शान्त', 'क्षमता', 'सक्षम', 'जश्न', 'जश्न मनाई', 'सजिलो', 'स्वच्छता', 'सभ्यता', 'सभ्य', 'स्वच्छ' , 'स्पष्टता', 'सफा', 'सफाई', 'सहज','रंगीन', 'सहजता', 'सान्त्वना','सहिष्णु', 'आराम', 'प्रतिबद्ध', 'प्रतिबद्धता', 'अनुपालन', 'दयालु', 'अनुकूल', 'मानार्थ', 'व्यापक','संगोष्ठी', 'बधाई', 'सावधानी', 'निरंतर', 'निरन्तर', 'रचनात्मक', 'भत्ता', 'संतोष', 'योगदान','सुविधा','सुविधाजनक', 'ठिक', 'सबभन्दा राम्रो', 'सहि', 'सहकारी','सहकार्य', 'साहसी', 'कर्तव्य', 'विश्वसनीय' ,'उपचार', 'प्यारा', 'स्वादिष्ट', 'प्रसन्न', 'प्रसन्नता',
'भरोसेमंद', 'वांछनीय', 'इच्छाकारी', 'वांछित', 'भाग्य', 'सम्मानित', 'परिश्रम', 'मेहनत', 'आधुनिक', 'वैज्ञानिक', 'प्राविधिक', 'विशिष्ट','प्रतिष्ठित','विविध','दिव्य', 'प्रभुत्व', 'टिकाऊ', 'गतिशील', 'प्रमाणित', 'उत्सुक','उत्सुकतापूर्वक','ईमानदारी',
'सजिलो', 'उत्सुकता', 'उत्सव', 'ईमानदार', 'किफायती', 'शिक्षित', 'प्रभावकारी', 'प्रभावकारिता', 'प्रभावमुक्त', 'कुशल', 'दक्षता', 'कुशलतापूर्वक', 'विद्युतीय', 'सुन्दरता', 'सुरुचिपूर्ण', 'उच्च','कुलीन', 'भव्यता', 'भव्य', 'विद्युत', 'सहानुभूति', 'सशक्तिकरण',
'जादुगर', 'कृतज्ञता', 'प्रोत्साहन', 'उत्साहजनक', 'ऊर्जा', 'संलग्न',  'ऊर्जावान', 'वृद्धि', 'बढावा', 'रमाइलो', 'मजेदार', 'सुखद', 'मजा प्राप्त', 'मजा गर्दै', 'मस्ती', 'प्रबुद्ध', 'मोज','समृद्ध','संवर्धन', 'मनोरञ्जन', 'उत्साह', 'उत्साही',
'उत्तेजित', 'रोमाञ्चक','उपलब्ध','प्रभावशाली', 'उत्साहजनक', 'उत्साहित', 'खुसीसाथ', 'अभिनय', 'स्पष्ट रूपमा','विशेषज्ञता','अति उत्तम', 'उत्तम',
'विशेष', 'असाधारण', 'आश्चर्यचकित', 'शानदार', 'निष्पक्ष', 'विश्वासी', 'विश्वासयोग्य', 'वफादारी','प्रसिद्धि', 'विश्वास', 'प्रशंसक', 'उत्कृष्ट', 'छिटो बढ्दै', 'गलतीहीन', 'अनुकूल', 'मनपर्ने', 'निष्ठा', 'निष्ठावान', 'ठीक', 'सर्वोत्तम', 'धाराप्रवाह',
'सौदाजनक', 'सौभाग्य', 'सुगन्धित','आजादी', 'ताजा', 'मित्रता', 'मित्र', 'फलदायी', 'पूर्ति', 'दैनिक', 'लाभदायक','लाभप्रद', 'उदारता', 'सज्जन', 'वास्तविक', 'खुसी', 'चमक', 'महिमा', 'महिनावारी', 'ईश्वर', 'देवदर', 'सुन', 'भलाइ', 'अनुग्रह', 'कृतज्ञ', 'दयावान', 'भव्यता', 'कृतज्ञता', 'महान', 'महानता', 'सुख', 'सुखी', 'खुशी', 'समानुपातिक', 'समानता', 'स्वस्थ', 'हृदय',
'हार्दिक', 'हृदयवाचक', 'स्वर्ग','स्वर्गीय', 'मद्दत', 'नायक', 'नायिका', 'उच्च गुणस्तर', 'गुण', 'गुणहरु', 'सम्मान', 'सम्माननीय', 'सम्मानित', 'आशाजनक', 'अतिथि', 'नम्र', 'नम्रता','हास्य', 'हतोत्साहित', 'शगुन', 'उपहार', 'अनुहार', 'पुरस्कार', 'आदर्श','अनुकूलित', 'अनुकुल', 'बेजोड', 'नैतिक', 'नैतिकता', 'निष्पक्षता', 'प्रभावित', 'प्रभावशाली', 'प्रभावशीलता',
'सुधार', 'सुधारिएको', 'ईमानदारीपूर्वक', 'निर्मल', 'अभिनव', 'व्यावहारिक','प्रेरणा', 'प्रेरणात्मक', 'प्रेरणादायक', 'अभिन्न', 'बुद्धिमान', 'सुव्यवस्थित', 'रोचक','अंतरंग', 'जटिल', 'सावधानी', 'अमूल्य','अतुल्यनीय', 'आविष्कारक', 'तीव्रता', 'तीव्र',
'अतुल्य', 'उचित', 'आनन्द','आनन्दित', 'आनन्दमय', 'ज्ञानयोग्य', 'ज्ञान', 'ज्ञानी', 'बुद्धिजीवी', 'बौद्धिक', 'कानुनी व्यवस्था', 'कानुनी', 'वैधानिक', 'कानूनी रूपमा', 'नेतृत्व', 'अग्रणी', 'पौष्टिक', 'मुक्ति', 'स्वतन्त्र', 'स्वन्तन्त्रता', 'मनपर्दो', 'मनपर्यो','प्यार', 'मनपराउने', 'सिंहदर', 'जीवंत', 'तार्किक', 'प्यारी', 'मायालु', 'माया', 'वफादार' 'वफादारी', 'चमकदार', 'जादुई',
'अद्भुत', 'अद्भुतता', 'मानवता', 'अतुल्य','परिपक्व', 'परिपक्वता','सार्थक', 'यादगार', 'जटिल', 'सावधानीपूर्वक', 'शक्तिशाली',
'शक्ति', 'चमत्कार', 'चमत्कारहरू', 'चमत्कारपूर्ण', 'स्मारक', 'प्रेरित’, ‘उद्देश्य', 'विशेष रूपमा', 'विशेषता','उल्लेखनीय','पोषण',
'नवीनता', 'उपन्यास', 'नवीन', 'खुलापन', 'इष्टतम','आशावाद', 'आशावादी', 'मौलिकता', 'धेरै खुसी', 'जुनून', 'भावुक', 'धैर्य', 'धैर्यपूर्वक', 'देशभक्त', 'शान्ति', 'शान्त', 'शान्तिपूर्वक', 'शान्तिकालमा', 'आचरण', 'पूर्णतया', 'अनुमति', 'दृढता', 'सुखद', 'भरपूर', 'लोकप्रिय', 'सकारात्मकता', 'नकारात्मकता', 'पूर्व प्रतिष्ठित', 'कीमती', 'पूर्वनिर्धारित', 'रुचि', 'प्राथमिकता',
'अधिमानतः', 'पसंदीदा', 'रुचाउने', 'प्रतिष्ठा', 'प्रतिष्ठित', 'सुंदरता', 'सुन्दर', 'सौन्दर्य', 'सौन्दर्यता', 'निर्मल', 'शीतल', 'गर्व',
'विशेषाधिकार','सक्रिय', 'अदभूत', 'उत्पादक','कुशल', 'प्रगति', 'प्रगतिशील', 'प्रवर्द्धन', 'प्रमुख', 'प्रतिज्ञा', 'तुरुन्त',
'समुचित', 'शुभकामना', 'शुभचिन्तक', 'शुभ कार्य', 'शुभकार्य', 'समृद्धि', 'सुरक्षा', 'सुरक्षित','रक्षा', 'संरक्षण', 'सिद्ध',
'प्रताप','प्रबुद्ध', 'गर्भपात', 'शुद्ध', 'उद्देश्यपूर्ण','योग्य', 'योग्यता', 'शुद्धता', 'बास्नादार', 'स्वादिलो', 'पोषिलो', 'चाहने', 'चाहिने', 'नचाहने', 'नचाहिने', 'उज्ज्वल', 'चाँडो', 'उज्ज्वालित', 'प्रज्ज्वल', 'प्रज्वल', 'प्रज्ज्वलित', 'प्रज्वलित', 'तर्कसंगत', 'पहुँचयोग्य', 'पढ्न योग्य','पढाई', 'तैयार', 'पुनः पुष्टि', 'पुनः पुष्टि', 'यथार्थवादी', 'स्वीकार्य', 'पुनःप्राप्त', 'सुलभ', 'छुटकारा', 'परिष्कृत', 'राहत', 'प्रसिद्ध', 'ज्ञात','प्रतिस्थापन योग्य', 'समाधान', 'प्रत्याशित', 'उत्तरदायी', 'क्रांतिकारी', 'क्रांति', 'इनाम', 'पुरस्कृत', 'अमीर', 'धनी', 'आदर' , 'आदरणीय', 'शिक्षक', 'शिक्षा', 'धर्मी', 'धार्मिकता', 'मजबूत', 'निडर', 'पराक्रम', 'पराक्रमी', 'वीर' ,'वीरता', 'शुर वीर' , 'शौर्य', 'प्रेम', 'मोहित', 'मोहक', 'मन्मोहित', 'सुगम', 'सुगमता', 'मीठो', 'सुगन्धित', 'संतोषजनक', 'संतुष्ट', 'सन्तुष्ट', 'संतोष', 'मुक्तिदाता', 'स्व-निर्धारण', 'निर्धारण', 'आत्म-सम्मान', 'आत्म-सन्तुष्टि', 'आत्म-क्षमता',
'आत्म-पर्याप्त', 'संवेदन', 'समझदार', 'संवेदनशीलता', 'संवेदनशील', 'महत्वपूर्ण', 'महत्व', 'सरल', 'सरलीकृत', 'सरलता', 'कौशल','कुशल', 'कुशलतापूर्वक', 'कुशलता', 'मुस्कान', 'मुस्कुराउँदै', 'मुस्कुराउँदा', 'नरम', 'एकता', 'आध्यात्मिक', 'अखण्ड', 'अखण्डता', 'स्थिरता', 'स्थिर', 'मृत्युन्जय', 'दृढतापूर्वक', 'प्रयासरत', 'मजबूत', 'बलियो', 'सफलता','सफल', 'सफलतापूर्वक', 'पर्याप्त', 'उपयुक्त', 'योगी', 'श्रेष्ठता', 'समर्थन', 'समर्थित', 'समर्थक', 'श्रेष्ठ', 'सर्वश्रेस्था', 'महाज्ञानी', 'शक्तिमान', 'सर्वशक्तिमान', 'अटल',  'प्रकाश', 'प्रकाशित', 'सहायक', 'सहायता', 'सर्वोच्चता',
'सर्वोच्च', 'मीठा', 'मीठापन', 'न्याय', 'पालक', 'सत्य', 'आस्था', 'प्रतिभा','प्रतिभाशाली', 'प्रलोभन', 'धन्यबाद',
'विचारशील', 'धन्य', 'मिलन','सहिष्णु', 'पारदर्शी', 'खजाना','अत्यन्तै', 'विजय', 'भरोसा', 'भरोसेमंदता', 'विश्वासयोग्य', 'भरोसेमंद', 'सत्यम','सच्चाई', 'मुल्यवान', 'उपलब्ध','उपलब्धि', 'उपलब्धिहरु', 'प्रावधान', 'प्रावधानहरु', 'सहमति', 'सहमत', 'असीमित', 'आवश्यक', 'आवश्यकता', 'प्रयोगयोग्य', 'उपयोगी', 'उपयोग', 'सदुपयोग', 'मूल्यवान', 'विविधता', 'बहुमुखी',
'सतर्कता','राम्रै','चतुराई','बढ्दो','साकार','निष्ठापुर्वक','चतुर','सतर्क','धन्यवाद', 'कुशल', 'कौशल','विजय', 'अजय','परोपकार','निष्ठा','सकुशल','नियमित', 'सद्गुण', 'दर्शन', 'स्वागत', 'सत्कार', 'सन्तुलित', 'सन्तुलन', 'आत्मसंतुलन', 'आत्मसम्मान', 'आत्मसन्तुष्टि', 'आत्मक्षमता','आत्मपर्याप्त', 'आत्मा रक्षा', 'आत्मरक्षा', 'राम्रो व्यवहार', 'राम्रो तरिकाले’, ‘व्यवस्थित', 'राम्रो स्थितिमा', 'राम्रो प्राप्त','राम्रो-मानिएको', 'स्वस्थ', 'इच्छुक', 'इच्छुकता', 'जीत', 'बिजुली', 'विनायक', 'विजेता', 'बुद्धि', 'बुद्धिमानी', 'आश्चर्य', 'आश्चर्यजनक', 'कार्ययोग्य', 'विश्व प्रसिद्ध', 'लायक', 'चाहना', 'सुध्रिढ', 'विकास']


 negative_words = ['two-faced','two-faces','abnormal','abolish','abominable','abominably','abominate','abomination','abort','aborted','aborts','abrade','abrasive','abrupt','abruptly','abscond','absence','absent-minded','absentee','absurd','absurdity','absurdly','absurdness', 'abuse','abused','abuses','abusive','abysmal','abysmally','abyss','accidental','accost','accursed','accusation','accusations','accuse','accuses','accusing','accusingly','acerbate','acerbic','acerbically','ache','ached','aches','achey','aching','acrid','acridly','acridness','acrimonious','acrimoniously','acrimony','adamant','adamantly','addict','addicted','addicting','addicts','admonish','admonisher','admonishingly','admonishment','admonition','adulterate',
'adulterated','adulteration','adulterier','adversarial','adversary','adverse','adversity','afflict','affliction','afflictive','affront','afraid','aggravate','aggravating','aggravation','aggression','aggressive','aggressiveness','aggressor','aggrieve','aggrieved','aggrivation','aghast','agonies','agonize','agonizing','agonizingly','agony','aground','ail','air','ailing','ailment','aimless','alarm','alarmed','alarming','alarmingly','alienate','alienated','alienation','allegation','allegations','allege','allergic','allergies','allergy','aloof','altercation','ambiguity','ambiguous','ambivalence','ambivalent','ambush','amiss','amputate','anarchism','anarchist','anarchistic','anarchy','anemic','anger','angrily','angriness','angry','anguish','animosity','annihilate','annihilation','annoy','annoyance','annoyances','annoyed','annoying','annoyingly','annoys','anomalous','anomaly','antagonism','antagonist','antagonistic',
'antagonize','anti-','anti-occupation','anti-proliferation','anti-semites','anti-social','anti-us','antipathy','antiquated','antithetical','anxieties','anxiety','anxious','anxiously','anxiousness','apathetic','apathetically','apathy','apocalypse','apocalyptic','apologist','apologists','appal','appall','appalled','appalling','appallingly','apprehension','apprehensions','apprehensive','apprehensively','arbitrary','arcane','archaic','arduous','arduously','argumentative','arrogance','arrogant','arrogantly','ashamed','asinine','asininely','asinininity','askance','asperse','aspersion','aspersions','assail','assassin','assassinate','assault','astray','asunder','atrocious','atrocities','atrocity','atrophy','attack','attacks','audacious','audaciously','audaciousness','audacity','audiciously','austere','authoritarian','autocrat','autocratic','avalanche','avarice','avaricious','avariciously','avenge','averse','aversion','aweful','awful','awfully','awfulness','awkward','awkwardness','ax','babble','back-logged','back-wood','back-woods','backache','backaches','backaching','backbite','backbiting','backward','backwardness',
'backwood','backwoods','bankruptcy','bad','badly','baffle','baffled','bafflement','baffling','bait','balk','banal','banalize','bane','banish','banishment','bankrupt','barbarian','barbaric','barbarically','barbarity','barbarous','barbarously','barren','baseless','bash','bashed','bashful','bashing','bastard','bastards','battered','battering','batty','bearish','beastly','bedlam','bedlamite','befoul','beg','beggar','beggarly','begging','beguile','belabor','belated','beleaguer','belie','belittle','belittled','belittling','bellicose','belligerence','belligerent','belligerently','bemoan','bemoaning','bemused','bent','berate','bereave','bereavement','bereft','berserk','beseech','beset','beef','besiege','besmirch','besmirched','bestial','betray','betrayal','betrayals','betrayer','betraying','betrays',
'bewail','beware','bewilder','bewildered','bewildering','bewilderingly','bewilderment','bewitch','bias','biased','biases','bicker','bickering','bid-rigging','bigotries','bigotry','bitch','bitchy','biting','bitingly','bitter','bitterly','bitterness','bizarre','blab','blabber','blackmail','blah','blame','blameworthy','bland','blandish','blaspheme','blasphemous','blasphemy','blasted','blatant','blatantly','blather','bleak','bleakly','bleakness','blemish','blind','blinding','blindingly','blindside','blister','blistering','bloated','blockage','blockhead','bloodshed','bloodthirsty','bloody','blotchy','blow','blunder','blundering','blunders','blunt','blur','bluring','blurred','blurring','blurry','blurs','blurt','boastful','boggle','bogus','boil','boiling','boisterous','bomb','bombard',
'bombardment','bombastic','bondage','bonkers','bore','bored','boredom','bores','boring','botch','botched','botched-up','bother','bothered','bothering','bothers','bothersome','bowdlerize','boycott','braggart','bragger','brainless','brainwash','brash','brashly','brashness','brat','bravado','brazen','brazenly','brazenness','breach','break','break-up','break-ups','breakdown','breaking','breaks','breakup','breakups','bribery','brimstone','bristle','brittle','broke','broken','broken-hearted','brood','browbeat','bruise','bruised','bruises','bruising','brusque','brutal','brutalising','brutalities','brutality','brutalize','brutalizing','brutally','brute','brutish','bs','buckle','bug','bugging','buggy','bugs','bulkyness','bullies','bullshit','bully','bullying','bullyingly','bum','bump','bumped','bumping','bumpping','bumps','bumpy','bungle','bungler','bungling','bunk','burden','burdensome','burdensomely','burn','burned','burning','burns','bust','busts','busybody','butcher','butchery','buzzing','byzantine',
'cackle','calamities','calamitous','conspiracy','conspirator','conspirators','calamitously','calamity','callous','calumniate','calumniation','calumnies','calumnious','calumniously','calumny','cancer','cancerous','cannibal','cannibalize','capitulate','capricious','capriciously','capriciousness','capsize','careless','carelessness','caricature','carnage','carp','cartoonish','cash-strapped','carp','castigate','castrated','casualty','cataclysm','cataclysmal','cataclysmic','cataclysmically','catastrophe','catastrophes','catastrophic','catastrophically','catastrophies','caustic','caustically','censure','chafe','chaff','chagrin','challenging','chaos','chaotic','chasten','chastise','chastisement','chatter','chatterbox','cheap','cheapen','cheaply','cheat','cheated','cheater','cheating','cheats','checkered','cheerless','cheesy','chide','childish','chill','chilly','chintzy','choke','choleric','choppy','chore','chronic','chunky','clamor','clamorous','clash','cliche','cliched','clique','clog','clogged','clogs','cloud','clouding','cloudy','clueless','clumsy','clunky','coarse','cocky','coerce','coercion','coercive','cold','coldly','collapse','collude','collusion','combative',
'commonplace','commotion','commotions','complacent','complain','complained','complaining','complains','complaint','complaints','complex','complicated','complication','complicit','compulsion','compulsive','concede','conceded','conceit','conceited','condemn','condemnable','condemnation','condemned','condemns','condescend','condescending','condescendingly','condescension','confined','conflict','conflicted','conflicting','conflicts','confound','confounded','confounding','confront','confrontation','confrontational','confuse','confused','confuses','confusing','confusion','confusions','congested','congestion','cons','conservative','conspicuous','conspicuously','conspiracies','conspiracy','conspirator','conspiratorial','conspire','consternation','contagious','contaminate','contaminated','contaminates','contaminating','contamination','contempt','contemptible','contemptuous','contemptuously','contend','contention','contentious','contort','contortions','contradict','contradiction','contradictory','contrariness','contravene','contrive','contrived','controversial','controversy','convoluted','corrode','corrosion','corrosions','corrosive','corrupt','corrupted','corrupting','corruption','corrupts','corruptted','costlier','costly','counter-productive','counterproductive','coupists','covetous','coward','cowardly','crabby','crack','cracked','cracks','craftily','craftly',
'crafty','cramp','cramped','cramping','cranky','crap','crappy','craps','crash','crashed','crashes','crashing','crass','craven','cravenly','craze','crazily','craziness','crazy','creak','creaking','creaks','credulous','creep','creeping','creeps','creepy','crept','crime','criminal','cringe','cringed','cringes','cripple','crippled','cripples','crippling','crisis','critic','critical','criticism','criticisms','criticize','criticized','criticizing','critics','cronyism','crook','crooked','crooks','crowded','crowdedness','crude','cruel','crueler','cruelest','cruelly','cruelness','cruelties','cruelty','crumble','crumbling','crummy','crumple','crumpled','crumples','crush','crushed','crushing','cry','culpable','culprit','cumbersome','cunt','cunts','cuplrit','curse','cursed','curses','curt','cuss','cussed','cutthroat','cynical','cynicism','d*mn','damage','damaged','damages','damaging','damn','damnable','damnably','damnation','damned','damning','damper','danger','dangerous','dangerousness','dark','darken','darkened','darker','darkness','dastard','dastardly','daunt','daunting','dauntingly','dawdle','daze','dazed','dead','deadbeat','deadlock','deadly','deadweight','deaf','dearth','death','debacle','debase','debasement','debaser','debatable','debauch','debaucher','debauchery','debilitate','debilitating','debility','debt','debts','decadence','decadent','decay','decayed','deceit','deceitful','deceitfully','deceitfulness','deceive','deceiver','deceivers','deceiving','deception','deceptive','deceptively','declaim','decline','declines','declining','decrement','declined','decrepit','decrepitude','decry','defamation','defamations','defamatory','defame','defect','defective','defects','defensive','defiance','defiant','defiantly','deficiencies','deficiency','deficient','defile','defiler','deform','deformed','defrauding','defunct','defy',
'degenerate','degenerately','degeneration','degradation','degrade','degrading','degradingly','dehumanization','dehumanize','deign','deject','dejected','dejectedly','dejection','delay','delayed','delaying','delays','delinquency','delinquent','delirious','delirium','delude','deluded','deluge','delusion','delusional','delusions','demean','demeaning','demise','demolish','demolisher','demon','demonic','demonize','demonized','demonizes','demonizing','demoralize','demoralizing','demoralizingly','denial','denied','denies','denigrate','denounce','dense','dent','dented','dents','denunciate','denunciation','denunciations','deny','denying','deplete','deplorable','deplorably','deplore','deploring','deploringly','deprave','depraved','depravedly','deprecate','depress','depressed','depressing','depressingly','depression','depressions','deprive','deprived','deride','derision','derisive','derisively','derisiveness','derogatory','desecrate','deserted','desertion','desiccate','desiccated','desititute','desolate','desolately','desolation','despair','despairing','despairingly','desperate','desperately','desperation','despicable','despicably','despise','despised','despoil','despoiler','despondence','despondency','despondent','despondently','despot','despotic','despotism','destabilisation','destains','destitute','destitution','destroy','destroyer','destruction','destructive','desultory','deter','deteriorate','deteriorating','deterioration','deterrent','detest','detestable','detestably','detested','detesting','detests','detract','detracted','detracting','detraction','detracts','detriment','detrimental','devastate','devastated','devastates','devastating','devastatingly','devastation','deviate','deviation','devil','devilish','devilishly','devilment','devilry','devious','deviously','deviousness','devoid','diabolic','diabolical','diabolically','diametrically','diappointed','diatribe','diatribes','dick','dictator','dictatorial','die','die-hard','died','dies','difficult','difficulties','difficulty','diffidence','dilapidated','dilemma','dilly-dally','dim','dimmer','din','ding','dings','dinky','dire','direly','direness','dirt','dirtbag','dirtbags','dirts','dirty','disable','disabled','disaccord','disadvantage','disadvantaged','disadvantageous','disadvantages','disaffect','disaffected','disaffirm','disagree','disagreeable','disagreeably','disagreed','disagreeing','disagreement','disagrees','disallow','disapointed','disapointing','disapointment','disappoint','disappointed','disappointing','disappointingly','disappointment','disappointments','disappoints','disapprobation','disapproval','disapprove','disapproving','disarm','disarray','disaster','disasterous','disastrous','disastrously','disavow','disavowal','disbelief','disbelieve','disbeliever','disclaim','discombobulate','discomfit','discomfititure','discomfort','discompose','disconcert','disconcerted','disconcerting','disconcertingly',
'disconsolate','disconsolately','disconsolation','discontent','discontented','discontentedly','discontinued','discontinuity','discontinuous','discord','discordance','discordant','discountenance','discourage','discouragement','discouraging','discouragingly','discourteous','discourteously','discoutinous','discredit','discrepant','discriminate','discrimination','discriminatory','disdain','disdained','disdainful','disdainfully','disfavor','disgrace','disgraced','disgraceful','disgracefully','disgruntle','disgruntled','disgust','disgusted','disgustedly','disgustful','disgustfully','disgusting','disgustingly','dishearten','disheartening','dishearteningly','dishonest','dishonestly','dishonesty','dishonor','dishonorable','dishonorablely','disillusion','disillusioned','disillusionment','disillusions','disinclination','disinclined','disingenuous','disingenuously','disintegrate','disintegrated','disintegrates','disintegration','disinterest','disinterested','dislike','disliked','dislikes','disliking','dislocated','disloyal','disloyalty','dismal','dismally','dismalness','dismay','dismayed','dismaying','dismayingly','dismissive','dismissively','disobedience','disobedient','disobey','disoobedient','disorder','disordered','disorderly','disorganized','disorient','disoriented','disown','disparage','disparaging','disparagingly','dispensable','dispirit','dispirited','dispiritedly','dispiriting','displace','displaced','displease','displeased','displeasing','displeasure','disproportionate','disprove','disputable','dispute','disputed','disquiet','disquieting','disquietingly','disquietude','disregard','disregardful','disreputable','disrepute','disrespect','disrespectable','disrespectablity','disrespectful','disrespectfully','disrespectfulness','disrespecting','disrupt','disruption','disruptive','diss','dissapointed','dissappointed',
'dissappointing','dissatisfaction','dissatisfactory','dissatisfied','dissatisfies','dissatisfy','dissatisfying','dissed','dissemble','dissembler','dissension','dissent','dissenter','dissention','disservice','disses','dissidence','dissident','dissidents','dissing','dissocial','dissolute','dissolution','dissonance','dissonant','dissonantly','dissuade','dissuasive','distains','distaste','distasteful','distastefully','distort','distorted','distortion','distorts','distract','distracting','distraction','distraught','distraughtly','distraughtness','distress','distressed','distressing','distressingly','distrust','distrustful','distrusting','disturb','disturbance','disturbed','disturbing','disturbingly','disunity','disvalue','divergent','divisive','divisively','divisiveness','dizzing','dizzingly','dizzy','doddering','dodgey','dogged','doggedly','dogmatic','doldrums','domineer','domineering','donside','doom','doomed','doomsday','dope','doubt','doubtful','doubtfully','doubts','douchbag','douchebag','douchebags','downbeat','downcast','downer','downfall','downfallen','downgrade','downhearted','downheartedly','downhill','downside','downsides','downturn','downturns','drab','draconian','draconic','drag','dragged','dragging','drags','drain','drained','draining','drains','drastic','drastically','drawback','drawbacks','dread','dreadful','dreadfully','dreadfulness','dreary','dripped','dripping','drippy','drips','drones','droop','droops','drop-out','drop-outs','dropout','dropouts','drought','drowning','drunk','drunkard','drunken','dubious','dubiously','dubitable','dud','dull','dullard','dumb','dumbfound','dump','dumped','dumping','dumps','dunce','dupe','dust','dusty','dwindling','dying','earsplitting','eccentric',
'eccentricity','effigy','effrontery','egocentric','egomania','egotism','egotistical','egotistically','egregious','egregiously','election-rigger','elimination','emaciated','emasculate','embarrass','embarrassing','embarrassingly','embarrassment','embattled','embroil','embroiled','embroilment','emergency','emphatic','emphatically','emptiness','encroach','encroachment','endanger','enemies','enemy','enervate','enfeeble','enflame','engulf','enjoin','enmity','enrage','enraged','enraging','enslave','entangle','entanglement','entrap','entrapment','envious','enviously','enviousness','epidemic','equivocal','erase','erode','erodes','erosion','err','errant','erratic','erratically','erroneous','erroneously','error','errors','eruptions','escapade','eschew','estranged','evade','evasion','evasive','evil','evildoer','evils','eviscerate','exacerbate','exagerate','exagerated','exagerates','exaggerate','exaggeration','exasperate','exasperated','exasperating','exasperatingly','exasperation','excessive','excessively','exclusion','excoriate','excruciating','excruciatingly','excuse','excuses','execrate','exhaust','exhausted','exhaustion','exhausts','exhorbitant','exhort','exile','exorbitant','exorbitantance','exorbitantly','expel','expensive','expire','expired','explode','exploit','exploitation','explosive','expropriate','expropriation','expulse','expunge','exterminate','extermination','extinguish','extort','extortion','extraneous','extravagance','extravagant','extravagantly','extremism','extremist','extremists','eyesore','fabricate','fabrication','facetious','facetiously','fail','failed','failing','fails','failure','failures','faint','fainthearted','faithless','fake','fall','fallacies','fallacious','fallaciously','fallaciousness','fallacy','fallen','falling','fallout','falls','false','falsehood','falsely','falsify','falter','faltered','famine','famished','fanatic','fanatical','fanatically','fanaticism','fanatics','fanciful','far-fetched','farce','farcical','farcical-yet-provocative','farcically','farfetched','fascism','fascist','fastidious','fastidiously','fastuous','fat','fatal','fatalistic',
'fatalistically','fatally','fatcat','fatcats','fateful','fatefully','fathomless','fatigue','fatigued','fatique','fatty','fatuity','fatuous','fatuously','fault','faults','faulty','fawningly','faze','fear','fearful','fearfully','fears','fearsome','feckless','feeble','feeblely','feebleminded','feign','feint','fell','felon','felonious','ferociously','ferocity','fetid','fever','feverish','fevers','fiasco','fib','fibber','fickle','fiction','fictional','fictitious','fidget','fidgety','fiend','fiendish','filth','filthy','finagle','finicky','fissures','flabbergast','flabbergasted','flagging','flagrant','flagrantly','flair','flairs','flak','flake','flakey','flakieness','flaking','flaky','flare','flares','flareup','flareups','flat-out','flaunt','flaw','flawed','flaws','flee','fleed','fleeing','fleer','flees','fleeting','flicering','flicker','flickering','flickers','flighty','flimflam','flimsy','flirt','flirty','floored','flounder','floundering','flout','fluster','foe','fool','fooled','foolhardy','foolish','foolishly','foolishness','forbid','forbidden','forbidding','forceful','foreboding','forebodingly','forfeit','forged','forgetful','forgetfully','forgetfulness','forlorn','forlornly','forsake','forsaken','forswear','foul','foully','foulness','fractious','fractiously','fracture','fragile','fragmented','frail','frantic','frantically','fraud','fraudulent','fraught','frazzle','frazzled','freak','freaking','freakish','freakishly','freaks','freeze','freezes','freezing','frenetic','frenetically','frenzied','frenzy','fret','fretful','frets','friggin','frigging','fright','frighten','frightening','frighteningly','frightful','frightfully','frigid','frost','frown','froze','frozen','fruitless','fruitlessly','frustrate','frustrated','frustrates','frustrating','frustratingly','frustration','frustrations','fudge','fugitive','full-blown','fulminate','fumble','fume','fumes','fundamentalism','funky','funnily','funny','furious','furiously','furor','fury','fuss','fussy',
'fustigate','fusty','futile','futilely''futility','fuzzy','gabble','gaff','gaffe','gainsay','gainsayer','gall','galling','gallingly','galls','gangster','gape','garbage','garish','gasp','gauche','gaudy','gawk','gawky','geezer','genocide','get-rich','ghastly','ghetto','ghosting','gibber','gibberish','gibe','giddy','gimmick','gimmicked','gimmicking','gimmicks','gimmicky','glare','glaringly','glib','glibly','glitch','glitches','gloatingly','gloom','gloomy','glower','glum','glut','gnawing','goad','goading','god-awful','goof','goofy','goon','gossip','graceless','gracelessly','graft','grainy','grapple','grate','grating','gravely','greasy','greed','greedy','grief','grievance','grievances','grieve','grieving','grievous','grievously','grim','grimace','grind','gripe','gripes','grisly','gritty','gross','grossly','grotesque','grouch','grouchy','groundless','grouse','growl','grudge','grudges','grudging','grudgingly','gruesome','gross','gruesomely','gruff','grumble','grumpier','grumpiest','grumpily','grumpish','grumpy','guile','guilt','guiltily','guilty','gullible','gutless','gutter','hack','hacks','haggard','haggle','hairloss','halfhearted','halfheartedly','hallucinate','hallucination','hamper','hampered','handicapped','hang','hangs','haphazard','hapless','harangue','harass','harassed','harasses','harassment','harboring','harbors','hard','hard-hit','hard-line','hard-liner','hardball','harden','hardened','hardheaded','hardhearted', 'hardliner','hardliners','hardship','hardships','harm','harmed','harmful','harms','harpy','harridan','harried','harrow','harsh','harshly','hasseling','hassle','hassled','hassles','haste','hastily','hasty','hate','hated','hateful','hatefully','hatefulness','hater','haters','hates','hating','hatred','haughtily','haughty','haunt','haunting','havoc','hawkish','haywire','hazard','hazardous','haze','hazy','head-aches','headache','headaches','heartbreaker','heartbreaking','heartbreakingly','heartless','heathen','heavy-handed','heavyhearted','heck','heckle','heckled','heckles','hectic','hedge','hedonistic','heedless','hefty','hegemonism','hegemonistic','hegemony','heinous','hell','hell-bent','hellion','hells','helpless','helplessly','helplessness','heresy','heretic','heretical','hesitant','hestitant','hideous','hideously','hideousness','high-priced','hiliarious','hinder','hindrance','hiss','hissed','hissing','hoard','hoax','hobble','hogs','hollow','hoodium','hoodwink','hooligan','hopeless','hopelessly','hopelessness','horde','horrendous','horrendously','horrible','horrid','horrific','horrified','horrifies','horrify','horrifying','horrifys','hostage','hostile',
'hostilities','hostility','hotbeds','hothead','hotheaded','hothouse','hubris','huckster','hum','humid','humiliate','humiliating','humiliation','humming','hung','hurt','hurted','hurtful','hurting','hurts','hustler','hype','hypocrisy','hypocrite','hypocrites','hypocritical','hypocritically','harbor','hysteria','hysteric','hysterical','hysterically','hysterics','idiocies','idiocy','idiot','idiotic','idiotically','idiots','idle','ignoble','ignominious','ignominiously','ignominy','ignorance','ignorant','ignore','ill-advised','ill-conceived','ill-defined','ill-designed','ill-fated','ill-favored','ill-formed','ill-mannered','ill-natured','ill-sorted','ill-tempered','ill-treated','ill-treatment','ill-usage','ill-used','illegal','illegally','illegitimate','illicit','illiterate','illness','illogic','illogical','illogically','illusory','imaginary','imbalance','imbecile','imbroglio','immaterial','immature','imminence','imminently','immobilized','immoderate','immoderately','immodest','immoral','immorality','immorally','immovable','impair','impaired','impasse','impatience','impatient','impatiently','impeach','impedance','impede','impediment','impending','impenitent','imperfect','imperfection','imperfections','imperfectly','imperialist','imperil','imperious','imperiously','impermissible','impersonal','impertinent','impetuous','impetuously','impiety','impinge','impious','implacable','implausible','implausibly','implicate','implication','implode','impolite','impolitely','impolitic','importunate','importune','impose','imposers','imposing','imposition','impossible', 'impossiblity','impossibly','impotent','impoverish','impoverished','impractical','imprecate','imprecise','imprecisely','imprecision','imprison','imprisonment','improbability','improbable','improbably','improper','improperly','impropriety','imprudence','imprudent','impudence','impudent','impudently','impugn','impulsive','impulsively','impunity','impure','impurity','inability','inaccuracies','inaccuracy','inaccurate','inaccurately','inaction','inactive','inadequacy','inadequate','inadequately','inadverent','inadverently','inadvisable','inadvisably','inane','inanely','inappropriate','inappropriately','inapt','inaptitude','inarticulate','inattentive','inaudible','incapable','incapably','incautious','incendiary','incense','incessant','incessantly','incite','incitement','incivility','inclement','incognizant','incoherence','incoherent','incoherently','incommensurate','incomparable','incomparably','incompatability','incompatibility','incompatible','incompetence', 'incompetent','incompetently','incomplete','incompliant','incomprehensible','incomprehension','inconceivable','inconceivably','incongruous','incongruously','inconsequent','inconsequential','inconsequentially','inconsequently','inconsiderate','inconsiderately','inconsistence','inconsistencies','inconsistency','inconsistent','inconsolable','inconsolably','inconstant','inconvenience','inconveniently','incorrect','incorrectly','incorrigible','incorrigibly','incredulous','incredulously','inculcate','indecency','indecent','indecently','indecision','indecisive','indecisively','indecorum','indefensible','indelicate','indeterminable','indeterminably','indeterminate','indifference','indifferent','indigent','indignant','indignantly','indignation','indignity','indiscernible','indiscreet','indiscreetly','indiscretion','indiscriminate','indiscriminately','indiscriminating','indistinguishable','indoctrinate','indoctrination',
'indolent','indulge','ineffective','ineffectively','ineffectiveness','ineffectual','ineffectually','ineffectualness','inefficacious','inefficacy','inefficiency','inefficient','inefficiently','inelegance','inelegant','ineligible','ineloquent','ineloquently','inept','ineptitude','ineptly','inequalities','inequality','inequitable','inequitably','inequities','inescapable','inescapably','inessential','inevitable','inevitably','inexcusable','inexcusably','inexorable','inexorably','inexperience','inexperienced','inexpert','inexpertly','inexpiable','inexplainable','inextricable','inextricably','infamous','infamously','infamy','infected','infection','infections','inferior','inferiority','infernal','infest','infested','infidel','infidels','infiltrator','infiltrators','infirm','inflame','inflammation','inflammatory','inflammed','inflated','inflationary','inflexible','inflict','infraction','infringe','infringement','infringements','infuriate','infuriated','infuriating','infuriatingly','inglorious','ingrate','ingratitude','inhibit','inhibition','inhospitable','inhospitality','inhuman','inhumane','inhumanity','inimical','inimically','iniquitous','iniquity','injudicious','injure', 'injurious','injury','injustice','injustices','innuendo','inoperable','inopportune','inordinate','inordinately','insane','insanely','insanity','insatiable','insecure','insecurity','insensible','insensitive','insensitively','insensitivity','insidious','insidiously','insignificance','insignificant','insignificantly','insincere','insincerely','insincerity','insinuate','insinuating','insinuation','insociable','insolence','insolent','insolently','insolvent','insouciance','instability','instable','instigate','instigator','instigators','insubordinate','insubstantial','insubstantially','insufferable','insufferably','insufficiency','insufficient','insufficiently','insular','insult','insulted','insulting','insultingly','insults','insupportable','insupportably','insurmountable','insurmountably','insurrection','intefere','inteferes','intense','interfere','interference','interferes','intermittent','interrupt','interruption','interruptions','intimidate','intimidating','intimidatingly','intimidation','intolerable','intolerablely','intolerance','intoxicate','intractable','intransigence','intransigent','intrude','intrusion','intrusive','inundate','inundated','invader','invalid','invalidate','invalidity','invasive','invective','inveigle','invidious','invidiously','invidiousness','invisible','involuntarily','involuntary','irascible','irate','irately','ire','irk','irked',
'irking','irks','irksome','irksomely','irksomeness','irksomenesses','ironic','ironical','ironically','ironies','irony','irragularity','irrational','irrationalities','irrationality','irrationally','irrationals','irreconcilable','irrecoverable','irrecoverableness','irrecoverablenesses','irrecoverably','irredeemable', 'irredeemably','irreformable','irregular','irregularity','irrelevance','irrelevant','irreparable','irreplacible','irrepressible','irresolute','irresolvable','irresponsible','irresponsibly','irretating','irretrievable','irreversible','irritable','irritably','irritant','irritate','irritated','irritating','irritation','irritations','isolate','isolated','isolation','itch','itching','itchy','jabber','jaded','jagged','jam','jarring','jaundiced','jealous','jealously','jealousness','jealousy','jeer','jeering','jeeringly','jeers','jeopardize','jeopardy','jerk','jerky','jitter','jitters','jittery','job-killing','jobless','joke','joker', 'jolt','judder','juddering','judders','jumpy','junk','junky','junkyard','jutter','jutters','kaput','kill','killed','killer','killing','killjoy','kills','knave','knife','knock','knotted','kook','kooky','lack','lackadaisical','lacked','lackey','lackeys','lacking','lackluster','lacks','laconic','lag','lagged','lagging','laggy','lags','laid-off','lambast','lambaste','lame','lame-duck','lament','lamentable','lamentably','languid','languish','languor','languorous','languorously','lanky','lapse','lapsed','lapses','lascivious','last-ditch','latency','laughable','laughably','laughingstock','lawbreaker','lawbreaking','lawless','lawlessness','layoff','layoff-happy','lazy','leak','leakage','leakages','leaking','leaks','leaky','lech','lecher','lecherous','lechery','leech','leer','leery','left-leaning','lemon','lengthy','less-developed','lesser-known','letch','lethal','lethargic','lethargy','lewd','lewdly','lewdness','liability','liable','liar','liars','licentious','licentiously','licentiousness','lie','lied','lier','lies','life-threatening','lifeless','limit','limitation','limitations','limited','limits','limp','listless','litigious','little-known','livid','lividly','loath','loathe','loathing','loathly','loathsome','loathsomely','lone','loneliness','lonely','loner','lonesome','long-time','long-winded','longing','longingly','loophole','loopholes','loose','loot','lorn','lose','loser','losers','loses','losing','loss','losses','lost','loud','louder','lousy','loveless','lovelorn','low-rated','lowly','ludicrous','ludicrously','lugubrious','lukewarm','lull','lumpy','lunatic','lunaticism','lurch','lure','lurid','lurk','lurking','lying','macabre','mad','madden','maddening','maddeningly',
'madder','madly','madman','madness','maladjusted','maladjustment','malady','malaise','malcontent','malcontented','maledict','malevolence','malevolent','malevolently','malice','malicious','maliciously','maliciousness','malign','malignant','malodorous','maltreatment','mangle','mangled','mangles','mangling','mania','maniac','maniacal','manic','manipulate','manipulation','manipulative','manipulators','mar','marginal','marginally','mashed','massacre','massacres','matte','mawkish','mawkishly','mawkishness','meager','meaningless','meanness','measly','meddle','meddlesome','mediocre','mediocrity','melancholy','melodramatic','melodramatically','meltdown','menace','menacing','menacingly','mendacious','mendacity','menial','merciless','mercilessly','mess','messed','messes','messing','messy','midget','miff','militancy','mindless','mindlessly','mirage','mire','misalign','misaligned','misaligns','misapprehend','misbecome','misbecoming','misbegotten','misbehave','misbehavior','miscalculate','miscalculation','miscellaneous','mischief','mischievous','mischievously','misconception','misconceptions','miscreant','miscreants','misdirection','miser','miserable','miserableness','miserably','miseries','miserly','misery','misfit','misfortune','misgiving','misgivings','misguidance','misguide','misguided','mishandle','mishap','misinform','misinformed','misinterpret','misjudge','misjudgment','mislead','misleading','misleadingly','mislike','mismanage','mispronounce','mispronounced','mispronounces','misread','misreading','misrepresent','misrepresentation','miss','missed','misses','misstatement','mist','mistake','mistaken','mistakenly','mistakes','mistified','mistress','mistrust','mistrustful','mistrustfully','mists','misunderstand','misunderstanding','misunderstandings','misunderstood','misuse','moan','mobster','mock','mocked','mockeries','mockery','mocking','mockingly','mocks','molest','molestation','monotonous','monotony','monster','monstrosities',
'monstrosity','monstrous','monstrously','moody','moot','mope','morbid','morbidly','mordant','mordantly','moribund','moron','moronic','morons','mortification','mortified','mortify','mortifying','motionless','motley','mourn','mourner','mournful','mournfully','muddle','muddy','mudslinger','mudslinging','mulish','multi-polarization','mundane','murder','murderer','murderous','murderously','murky','mushy','musty','mystify','myth','nag','nagging','naive','naively','narrower','nastily','nastiness','nasty','naughty','nauseate','nauseates','nauseating','nauseatingly','naive','nebulous','nebulously','needless','needlessly','needy','nefarious','nefariously','negate','negation','negative','negatives','negativity','neglect','neglected','negligence','negligent','nemesis','nepotism','nervous','nervously','nervousness','nettle','nettlesome','neurotic','neurotically','niggle','niggles','nightmare','nightmarish','nightmarishly','novel','nitpick','nitpicking','noise','noises','noisier','noisy','non-confidence','nonexistent','nonresponsive','nonsense','nosey','notoriety','notorious','notoriously','noxious','nuisance','numb','obese','object','objection','objectionable','objections','oblique','obliterate','obliterated','oblivious','obnoxious','obnoxiously','obscene','obscenely','obscenity','obscure','obscured','obscures','obscurity','obsess','obsessive','obsessively','obsessiveness','obsolete','obstacle','obstinate','obstinately','obstruct','obstructed','obstructing','obstruction','obstructs','obtrusive','obtuse','occlude','occluded','occludes','occluding','odd','odder','oddest','oddities','oddity','oddly','odor','offence','offend','offender','offending','offenses','offensive','offensively','offensiveness','officious','ominous','ominously','omission','omit','one-sided','onerous','onerously','onslaught','opinionated','opponent','opportunistic','oppose','opposition','oppositions','oppress','oppression','oppressive','oppressively','oppressiveness','oppressors','ordeal','orphan','ostracize','outbreak','outburst','outbursts','outcast','outcry','outlaw','outmoded','outrage','outraged','outrageous', 'outrageously','outrageousness','outrages','outsider','over-acted','over-awe','over-balanced','over-hyped','over-priced','over-valuation','overact','overacted','overawe','overbalance','overbalanced','overbearing','overbearingly','overblown','overdo','overdone','overdue','overemphasize','overheat','overkill','overloaded','overlook','overpaid','overpayed','overplay','overpower','overpriced','overrated','overreach','overrun','overshadow','oversight','oversights','oversimplification','oversimplified','oversimplify','oversize','oversized','overstate','overstated','overstatement','overstatements','overstates','overtaxed','overthrow','overthrows','overturn','overweight','overwhelm','overwhelmed','overwhelming','overwhelmingly','overwhelms','overzealous','overzealously','overzelous','pain','painful',
'painfull','painfully','pains','pale','pales','paltry','pan','pandemonium','pander','pandering','panders','panic','panick','panicked','panicking','panicky','paradoxical','paradoxically','paralyze','paralyzed','paranoia','paranoid','parasite','pariah','parody','partiality','partisan','partisans','passe','passive','passiveness','pathetic','pathetically','patronize','paucity','pauper','paupers','peculiar','peculiarly','pedantic','peeled','peeve','peeved','peevish','peevishly','penalize','penalty','perfidious','perfidity','perfunctory','peril','perilous','perilously','perish','pernicious','perplex','perplexed','perplexing','perplexity','persecute','persecution','pertinacious','pertinaciously','pertinacity','perturb','perturbed','pervasive','perverse','perversely','perversion','perversity','pervert','perverted','perverts','pessimism','pessimistic','pessimistically','pest','pestilent','petrified','petrify','pettifog','petty','phobia','phobic','phony','picket','picketed','picketing','pickets','picky','pig','pigs','pillage', 'pillory','pimple','pinch','pique','pitiable','pitiful','pitifully','pitiless','pitilessly','pittance','pity','plagiarize','plague','plasticky','plaything','plea','pleas','plebeian','plight','plot','plotters','ploy','plunder','plunderer','pointless','pointlessly','poison','poisonous','poisonously','pokey','poky','polarisation','polemize','polemic','pollute','polluter','polarization','polluters','polution','pompous','poor','poorer','poorest','poorly','posturing','pout','poverty','powerless','prate','pratfall','predatory','predicament','prejudge','prejudice','prejudices','prejudicial','premeditated','preoccupy','preposterous','preposterously','presumptuous','presumptuously','pretence','pretend','pretense','pretentious','pretentiously','prevaricate','pricey','pricier','prick','prickle','prickles','prideful','prik','primitive','prison','prisoner','problem','problematic','problems','procrastinate','procrastinates','procrastination','profane','profanity','prohibit','prohibitive','prohibitively','propaganda','propagandize','proprietary','prosecute','protest','protested','protesting','protests','protracted','provocation','provocative','provoke','pry','pugnacious','pugnaciously','pugnacity','punch','punish','punishable','punitive','punk','puny','puppet','puppets','puzzled','puzzlement','puzzling','quack','qualm','qualms','quandary','quarrel','quarrellous','quarrellously','quarrels','quarrelsome','quash','queer','questionable','quibble','quibbles','quitter','rabid','racism','racist','racists','racy','radical','radicalization','radically','radicals','rage','ragged','raging','rail','raked','rampage','rampant','ramshackle','rancor','randomly','rankle','rant','ranted','ranting','rantingly','rants','rape','raped','raping','rascal','rascals','rash','rattle','rattled','rattles','ravage','raving','reactionary','rebellious','rebuff','rebuke','recalcitrant','recant','recession','recessionary','reckless','recklessly','recklessness','recoil','recourses','redundancy','redundant','refusal','refuse','refused','refuses','refusing','refutation','refute','refuted','refutes','refuting','regress','regression','regressive','regret','regreted','regretful','regretfully','regrets','regrettable','regrettably','regretted','reject','rejected','rejecting','rejection','rejects','relapse','relentless','relentlessly','relentlessness','reluctance','reluctant','reluctantly','remorse','remorseful','remorsefully','remorseless','remorselessly','remorselessness','renounce','renunciation','repel','repetitive','reprehensible','reprehensibly','reprehension','reprehensive','repress','repression','repressive','reprimand','reproach','reproachful','reprove','reprovingly','repudiate','repudiation','repugn','repugnance','repugnant','repugnantly','repulse','repulsed','repulsing','repulsive','repulsively','repulsiveness','resent','resentful','resentment','resignation','resigned','resistance','restless','restlessness','restrict','restrictive','retaliate','retaliatory','retard','retarded','retardedness','retards','reticent','retract','retreat','retreated','revenge','revengeful','revengefully','revert','revile','reviled','revoke','revolt','revolting','revoltingly','revulsion','revulsive','rhapsodize','rhetoric','rhetorical','ricer','ridicule','ridicules','ridiculous','ridiculously','rift','rifts','rigid','rigidity','rigidness',
'rile','riled','rip','rip-off','ripoff','ripped','risk','risks','risky','rival','rivalry','roadblocks','rocky','rogue','rollercoaster','rot','rotten','rough','irremediable','rubbish','rude','rue','ruffian','ruffle','ruin','ruined','ruining','ruinous','ruins','rumbling','rumor','rumors','rumours','rumple','run-down','runaway','rupture','rust','rusts','rusty','rut','ruthless','ruthlessly','ruthlessness','ruts','sabotage','sack','sacrificed','sad','sadden','sadly','sadness','sag','sagged','sagging','saggy','sags','salacious','sanctimonious','sap','sarcasm','sarcastic','sarcastically','sardonic','sardonically','sass','satirical','satirize','savage','savaged','savagery','savages','scaly','scam','scams','scandal','scandalize','scandalized','scandalous','scandalously','scandals','scandel','scandels','scant','scapegoat','scar','scarce','scarcely','scarcity','scare','scared','scarier','scariest','scarily','scarred','scars','scary','scathing','scathingly','sceptical','scoff','scoffingly','scold','scolded','scolding','scoldingly','scorching','scorchingly','scorn','scornful','scornfully','scoundrel','scourge','scowl','scramble','scrambled','scrambles','scrambling','scrap','scratch','scratched','scratches','scratchy','scream','screech','screw-up','screwed','screwed-up','screwy','scuff','scuffs','scum','scummy','second-class','second-tier','secretive','sedentary','seedy','seethe','seething','self-coup','self-criticism','self-defeating','self-destructive','self-humiliation','self-interest','self-interested','self-serving','selfinterested','selfish','selfishly','selfishness','semi-retarded','senile','sensationalize','senseless','senselessly','seriousness','sermonize','servitude','set-up','setback','setbacks','sever','severe','severity','shabby','shadowy','shady','shake','shaky','shallow','sham','shambles','shame','shameful','shamefully','shamefulness','shameless','shamelessly','shamelessness','shark','sharply','shatter','shimmer','shimmy','shipwreck','shirk','shirker','shiver','shock','shocked','shocking','shockingly','shoddy','short-lived','shoddily','shortage','shortchange','shortcoming','shortcomings','shortness','shortsighted','shortsightedness','showdown','shrew','shriek','shrill','shrilly','shrivel','shroud','shrouded','shrug','shun','shunned','sick','sicken','sickening','sickeningly','sickly','sickness','sidetrack','sidetracked','siege','sillily','silly','sin','sinful','sinfully','sinister','sinisterly','sink','sinking','skeletons','skeptic','skeptical','skeptically','skepticism','sketchy','skimpy','skinny','skittish','skittishly','skulk','slack','slander','slanderer','slanderous','slanderously','slanders','slap','slashing','slaughter','slaughtered','slave','slaves','sleazy','slime','slog','slogged','slogging','slogs','sloppily','sloppy','sloth','slothful','slow','slow-moving','slowed','slower','slowest','slowly','slows','slug','sluggish','slump','slumping','slumpping','slur','sly','smack','smallish','smash','smear','smell','smelled','smelling','smells','smelly','smelt','smoke','smokescreen','smolder','smoldering','smother','smoulder','smouldering','smudge','smudged','smudges','smudging','smug','smugly','smut','smuttier','smuttiest','smutty','snag','snagged','snagging','snags','snappish','snappishly','snare','snarky','snarl','sneak','sneakily','sneaky','sneer','sneering','sneeringly','snob','snobbish','snobby','snobish','snobs','snub','so-called','soapy','sob','sober','sobering','solemn','solicitude','somber','sore','sorely','soreness','sorrow','sorrowful','sorrowfully','sorry','sour','sourly','spade','spank','spendy','spew','spewed','spewing','spews','spilling','spinster','spiritless','spite','spiteful','spitefully','spitefulness','splatter','split','splitting','spoil','spoilage','spoilages','spoiled','spoilled','spoils','spook','spookier','spookiest','spookily','spooky','spoon-fed','spoon-feed','spoonfed','sporadic','spotty','spurious','spurn','sputter','squabble','squabbling','squander','squash','squeak','squeaks','squeaky','squeal','squealing','squeals','squirm','stab','stagnant','stagnate','stagnation','staid','stain','stains','stale','stalemate','stall','stalls','stammer','stampede','standstill','stark','starkly','startle','startling','startlingly','starvation','starve','static','steal','stealing','steals','steep','steeply','stench',
'stereotype','stereotypical','stereotypically','stern','stew','sticky','stiff','stiffness','stifle','stifling','stiflingly','stigma','stigmatize','sting','stinging','stingingly','stingy','stink','stinks','stodgy','stole','stolen','stooge','stooges','stormy','straggle','straggler','strain','strained','straining','strange','strangely','stranger','strangest','strangle','streaky','strenuous','stress','stresses','stressful','stressfully','stricken','strict','strictly','strident','stridently','strife','strike','stringent','stringently','struck','struggle','struggled','struggles','struggling','strut','stubborn','stubbornly','stubbornness','stuck','stuffy','stumble','stumbled','stumbles','stump','stumped','stumps','stun','stunt','stunted','stupid','stupidest','stupidity','stupidly','stupified','stupify','stupor','stutter','stuttered','stuttering','stutters','sty','stymied','sub-par','subdued','subjected','subjection','subjugate','subjugation','submissive','subordinate','subpoena','subpoenas','subservience','subservient','substandard','subtract','subversion','subversive','subversively','subvert','succumb','sue','sued','sueing','sues','suffer','suffered','sufferer','sufferers','suffering','suffers','suffocate','sugar-coat','sugar-coated','sugarcoated','suicidal','suicide','sulk','sullen','sully','sunder','sunk','sunken','superficial','superficiality','superficially','superfluous','superstition','superstitious','suppress','suppression','surrender','susceptible','suspicion','suspicions','suspicious','suspiciously','swagger','swamped','sweaty','swelled','swelling','swindle','swipe','swollen','symptom','symptoms','syndrome','taboo','tacky','taint','tainted','tamper','tangle','tangled','tangles','tank','tanked','tanks','tantrum','tardy','tarnish','tarnished','tarnishes','tarnishing','tattered','taunt','taunting','tauntingly','taunts','taut','tawdry','taxing','tease','teasingly','tedious','tediously','temerity','temper','tempest','temptation','tenderness','tense','tension','tentative','tentatively','tenuous','tenuously','tepid','terrible','terribleness','terribly','terror','terror-genic','terrorism','terrorize','terrorist','terrorists','testily',
'testy','tetchily','tetchy','thankless','thicker','thirst','thorny','thoughtless','thoughtlessly','thoughtlessness','thrash','threat','threaten','threatening','threats','threesome','throb','throbbed','throbbing','throbs','throttle','thug','thumb-down','thumbs-down','thwart','time-consuming','timid','timidity','timidly','timidness','tin-y','tingled','tingling','tired','tiresome','tiring','tiringly','toil','toll','top-heavy','topple','torment','tormented','torrent','tortuous','torture','tortured','tortures','torturing','torturous','torturously','totalitarian','touchy','toughness','tout','touted','touts','toxic','traduce','tragedy','tragic','tragically','traitor','traitorous','traitorously','tramp','trample','transgress','transgression','trap','traped','trapped','trash','trashed','trashy','trauma','traumatic','traumatically','traumatize','traumatized','travesties','travesty','treacherous','treacherously','treachery','treason','treasonous','trick','tricked','trickery','tricky','trivial','trivialize','trouble','troubled','troublemaker','troubles','troublesome','troublesomely','troubling','troublingly','truant','tumble','tumbled','tumbles','tumultuous','turbulent','turmoil','twist','twisted','twists','tyrannical','tyrannically','tyranny','tyrant','ugh','uglier','ugliest','ugliness','ugly','ulterior','ultimatum','ultimatums','ultra-hardline','un-viewable','unable','unacceptable','unacceptablely','unacceptably','unaccessible','unaccustomed','unachievable','unaffordable','unappealing','unattractive','unauthentic','unavailable','unavoidably','unbearable','unbearablely','unbelievable','unbelievably','uncaring','uncertain','uncivil','uncivilized','unclean','unclear','uncollectible','uncomfortable','uncomfortably','uncomfy','uncompetitive','uncompromising','uncompromisingly','unconfirmed','unconstitutional','uncontrolled','unconvincing','unconvincingly','uncooperative','uncouth','uncreative','undecided','undefined','undependability','undependable','undercut','undercuts','undercutting','underdog','underestimate','underlings','undermine','undermined','undermines','undermining','underpaid','underpowered','undersized','undesirable','undetermined','undid','undignified','undissolved','undocumented','undone','undue','unease','uneasily','uneasiness','uneasy','uneconomical','unemployed','unequal','unethical','uneven','uneventful','unexpected','unexpectedly','unexplained','unfairly','unfaithful','unfaithfully','unfamiliar','unfavorable','unfeeling','unfinished','unfit','unforeseen','unforgiving','unfortunate','unfortunately','unfounded','unfriendly','unfulfilled','unfunded','ungovernable','ungrateful','unhappily','unhappiness','unhappy','unhealthy','unhelpful','unilateralism','unimaginable','unimaginably','unimportant','uninsured','unintelligible','unintelligile','unjust','unjustifiable','unjustifiably','unjustified','unjustly','unkind','unkindly','unknown','unlamentable','unlamentably','unlawful','unlawfully','unlawfulness','unleash','unlicensed','unlikely','unlucky','unmoved','unnatural','unnaturally','unnecessary','unneeded','unnerve','unnerved','unnerving','unnervingly','unnoticed','unobserved','unorthodox','unorthodoxy','unpleasant','unpleasantries','unpopular','unpredictable','unprepared','unproductive','unprofitable','unprove','unproved','unproven','unproves','unproving','unqualified','unravel','unraveled','unreachable','unreadable','unrealistic','unreasonable','unreasonably','unrelenting','unrelentingly','unreliability','unreliable','unresolved','unresponsive','unrest','unruly','unsafe','unsatisfactory','unsavory','unscrupulous','unscrupulously','unsecure','unseemly','unsettle','unsettled','unsettling','unsettlingly','unskilled','unsophisticated','unsound','unspeakable','unspeakablely','unspecified','unstable','unsteadily','unsteadiness','unsteady','unsuccessful','unsuccessfully','unsupported','unsupportive','unsure','unsuspecting','unsustainable','untenable','untested','unthinkable','unthinkably','untimely','untouched','untrue','untrustworthy','untruthful','unusable','unusably',
'unuseable','unuseably','unusual','unusually','unviewable','unwanted','unwarranted','unwatchable','unwelcome','unwell','unwieldy','unwilling','unwillingly','unwillingness','unwise','unwisely','unworkable','unworthy','unyielding','upbraid','upheaval','uprising','uproar','uproarious','uproariously','uproarous','uproarously','uproot','upset','upseting','upsets','upsetting','upsettingly','useless','usurp','usurper','utterly','vagrant','vague','vagueness','vain','vainly','vanity','vehement','vehemently','vengeance','vengeful','vengefully','vengefulness','venom','venomous','venomously','vent','vestiges','vex','vexation','vexing','vexingly','vibrate','vibrated','vibrates','vibrating','vibration','vice','vicious','viciously','viciousness','victimize','vile','vileness','vilify','villainous','villainously','villains','villian','villianous','villianously','villify','vindictive','vindictively','vindictiveness','violate','violation','violator','violators','violent','violently','viper','virulence','virulent','virulently','virus','vociferous','vociferously','volatile','volatility','vomit','vomited','vomiting','vomits','vulgar','vulnerable','wack','wail','wallow','wane','waning','wanton','war-like','warily','wariness','warlike','warned','warning','warp','warped','wary','washed-out','waste','wasted','wasteful','wastefulness','wasting','water-down','watered-down','wayward','weak','weaken','weakening','weaker','weakness','weaknesses','weariness','wearisome','weary','wedge','weed','weep','weird','weirdly','wheedle','whimper','whine','whining','whiny','whips','wicked','wickedly','wickedness','wild','wildly','wiles','wilt','wily','wimpy','wince','wobble','wobbled','wobbles','woe','woebegone','woeful','woefully','womanizer','womanizing','worn','worried',
'worriedly','worrier','worries','worrisome','worry','worrying','worryingly','worse','worsen','worsening','worst','worthless','worthlessly','worthlessness','wound','wounds','wrangle','wrath','wreak','wreaked','wreaks','wreck','wrest','wrestle','wretch','wretched','wretchedly','wretchedness','wrinkle','wrinkled','wrinkles','wrip','wripped','wripping','writhe','wrong','wrongful','wrongly','wrought','yawn','zap','zapped','zaps','zealot','zealous','zealously','zombie',
'असामान्य', 'समाप्त', 'हानिकारक', 'सामूहिक रूपमा', 'रद्द गरियो','घृणित', 'अव्यवस्था', 'अवरोध', 'घर्षण', 'अचानक', 'अचानक', 'भत्काइयो', 'अनुपस्थिति', 'अनुपस्थित दिमाग' 'अनगिन्ती', 'बेवकूफ', 'दुरुपयोग', 'दुर्व्यवहार', 'अस्लिम', 'आकस्मिक', 'एक्स्टोस्ट', 'अकस्मात', 'आरोप', 'आरोप लगाउने' ,'अशक्त' , 'अचम्म', 'अकस्मिक', 'अचम्म','व्यभिचारी','व्यभिचार', 'प्रतिकृयात्मक', 'विपक्षी', 'प्रतिकृत', 'विपत्ति', 'दुखाइ',' दु: ख ','कष्टप्रद','आक्रामक', 'पीडा', 'खतरनाक', 'अलगाव', 'अलगाईएको', 'अलगाव', 'आरोप', 'एलर्जी', 'अतिक्रमण', 'अस्पष्टता', 'अज्ञात', 'अराजकतावाद', 'अराजकतावादी', 'अराजकवादी', 'अराजकता','क्रोध', 'गुस्सा', 'विनाश', 'अनौपचारिक', 'विरोधाभास', 'प्रतिवादी','विरोधी', 'विरोधी-अभियान', 'विरोधी-प्रसार', 'विरोधी-सामाजिक', 'पुरातन', 'चिन्तित', 'चिंता', 'चिन्ताजनक','चिंतित','बेपत्ता','अप्ठ्यारो', 'आशंका', 'अत्याचार', 'अहंकार', 'अहंकारवादी','हत्यारा', 'आक्रमण', 'गल्ती', 'अहंकारी', 'घमण्डी', 'अराजकता', 'क्रूरता', 'क्रुद्धता', 'क्रूर','हिमविश्वास', 'भयानक', 'अजीब', 'अल्पविराम', 'खराब', 'बिफलता', 'धोखाधड़ी', 'धोखा', 'सावधान', 'बिग्रिएको', 'बिग्रियो', 'बिग्रिन्छ', 'पक्षपात', 'पूर्वाग्रह', 'पक्षपाती', 'दोष', 'बेवास्ता', 'बलात्कार','निन्दा', 'अवधारणा', 'निन्दा','विस्फोट', 'अन्धो', 'अन्धा', 'खूनी', 'झटका', 'बम',' बमबारी', 'परेशान', 'रिश्वत', 'दुष्प्रभाव', 'दुष्टाचार', 'दुखीता', 'दुखी' , 'क्यान्सर', 'लापरवाही', 'विनाशकारी', 'अराजकता','अराजक', 'चोर','चोरी', 'चरित्रहीन','मोटे', 'मोटो', 'ढिलो', 'भ्रम', 'उजुरी', 'शिकायत', 'जटिल', 'जटिलता', 'बाध्यकारी', 'निन्दा','मदिरा', 'घृणा', 'सतावट', 'संवेदना', 'संवेदनाजनक', 'संवेदनासाथ', 'सीमित', 'संघर्ष', 'विवादास्पद', 'संघर्ष' , 'भ्रामक', 'अकस्मात', 'टकराव', 'भ्रष्ट', 'भ्रमित', 'भ्रम', 'षड्यंत्र', 'साजिश', 'साजिशकारी', 'छल', 'संक्रामक' ,'सम्वन्ध', 'प्रदूषण', 'संदूषण', 'अव्यवस्थित', 'विरोधाभास', 'विरोधाभासी', 'विवादित', 'विवाद', 'कष्ट', 'संक्षारण', 'भ्रष्टाचार', 'महँगो', 'दुर्घटनाग्रस्त', 'दुर्घटना' ,'पागलपन','पागल', 'अपराध', 'अपराधी', 'आपराधिक', 'अपराधजनक','संकट', 'आलोचक', 'आलोचना','आलोचनात्मक', 'अभिशाप', 'शाप भएको', 'श्राप', 'शापित', 'अभिशापित', 'क्षति', 'लान्न', 'नमिल्ने', 'नराम्रो', 'खतरा', 'गाढा','गहिरो','अन्धकार', 'मृत्यु', 'कर्ज', 'धोका', 'अस्वीकार', 'गिरावट’, खारेज', 'गिरावट', 'घटाइ', 'घटाइयो', 'दोष' , 'दोषी', 'कमजोरी', 'कमी', 'निराशाजनक', 'अपमान', 'उदास', 'ढिलाइ', 'राक्षस बनाइ', 'राक्षस', 'राक्षसित','निराशा', 'निराशावादी', 'इन्कार','व्युत्पन्न', 'उजाड', 'नितान्त', 'निराशा', 'निराश', 'नष्ट', 'जंगी जहाज', 'घीन', 'हटना','विचलन', 'शैतानको', 'धूर्त', 'खस्कँदो', 'कठिनाइ', 'कठिन', 'गन्दा','अक्षम', 'असक्षम', 'असक्षमता', 'नुकसान' , 'असह्य', 'असहमत', 'असहमति', 'निराव', 'आपदा', 'आपत्तिजनक', 'विच्छेद', 'असुविधा', 'विच्छेदन', 'असंतोष', 'असमानता', 'छुटकारा','भेदभाव', 'बेईमानी' , 'अपमान', 'अवज्ञात', 'अवज्ञादेव', 'अवज्ञा', 'अपमानजनक', 'विकार', 'असन्तुष्ट', 'अप्ठ्यारो', 'असंगत',
'असहमतियोग्य', 'अबरोध','अवरोध', 'विघटनकारी', 'भंग', 'असंतोषजनक', 'असभ्य', 'विकृत','विक्रय', 'बिगबिगी', 'बिचरा','विचलित', 'भेदभाव', 'अविश्वासपूर्ण', 'अविश्वसनीय', 'अविश्वासजनक', 'अशांति', 'विभाजन', 'चकजी', 'संदेह','शंकास्पद', 'शङ्काहरू', 'टाढा भयो', 'धूल', 'उदासीन', 'उदास', 'शर्मिला', 'शर्मिलापन', 'गर्भपात', 'आपातकालीन', 'खाली', 'दुश्मनी', 'दुश्मन', 'अज्ञात','गलत', 'त्रुटि', 'खराब', 'दुष्ट', 'विरूद्ध', 'पूर्वनिर्धारित', 'अनुयायी', 'निर्बाध', 'अत्यधिक', 'बहिष्कार', 'बहाना', 'अधीर', 'निर्वासन', 'म्याद समाप्त भयो', 'शोषण', 'विरूपण', 'अतिवाद', 'उग्रवादी', 'उग्रवाद', 'असफल', 'बनावट', 'विफलता','विश्वासहीन', 'नकली', 'झूटो', 'झूठे', 'अकाल', 'दैलो', 'घातक', 'थकान', 'कमजोर', 'बुखार', 'गन्दा', 'मूर्ख', 'मूर्खता', 'फेल', 'डरलाग्दो', 'डर', 'अफसोस', 'नरसंहार', 'लोभ', 'उत्पीडन', 'कठोर', 'भयानक', 'शत्रु', 'बिरामी', 'अवैध', 'बेमानी', 'बेमान', 'असंतुलन', 'अनैतिक', 'अपरिपक्व', 'अनैतिकता', 'अनोपचारिक', 'अनावश्यक', 'प्रतिबाधा', 'बाधा','अभाव', 'असुरक्षित', 'असिद्धता', 'असम्भव', 'अशक्त', 'व्युत्पन्न', 'अप्रत्यक्ष', 'असहज', 'अत्यावश्यक', 'अत्याचार', 'कैद', 'अनुचित', 'अशुद्ध','अशुद्धता','निष्क्रियता','निष्क्रिय','अपर्याप्त', 'असुविधाजनक', 'अयोग्य', 'असफलता', 'असफल', 'अपूर्णता', 'अपरिचित', 'निस्क्रिय', 'निस्क्रियता', 'संक्रामक', 'संक्रमित', 'संक्रमण', 'उल्लङ्घन','अधर्म', 'चोट','अन्याय', 'निष्क्रिय', 'पागल', 'अनिश्चितता', 'अपर्याप्तता', 'अपर्याप्त', 'हस्तक्षेप', 'अवरोध', 'अवास्तविक',  ' बेरोजगार', 'नर्क', 'लोभ', 'लोभल', 'लोभलाग्दो', 'लोभी', 'अनियमितता', 'अनियमित', 'अपरिवर्तनीय', 'अपरिवर्तनीयता', 'अनैतिकोल', 'अप्रत्याशित', 'जलन', 'पृथक', 'अलगाव', 'ईर्ष्या', 'कमी', 'लंगडा', 'ढिला', 'लापता', 'विलम्बता', 'हानी', 'लापरवाही', 'आलसी', 'झूठ', 'झुटो', 'झुटा', 'ढीलो', 'लुट', 'पागलपन', 'दुर्भावनापूर्ण', 'अर्थहीन','दुर्भाग्य', 'बहु-ध्रुवीकरण', 'ध्रुवीकरण', 'हत्या', 'हत्यारे'
'नौसिख', 'संकीर्ण', 'सङ्कीर्ण','पराजय','अहंकारी', 'ध्रुविकरण','लोभ', 'लोभी','अनिष्ठ', 'अनिष्ठापुर्वक', 'शरारती', 'शोर', 'कुख्यात', 'अप्रचलित', 'अफसोस', 'विरोध','विपक्षी', 'विरोधी', 'अनाथ', 'दर्दनाक', 'दर्द', 'चिच्याइएको', 'आंशिकता', 'विभाजन', 'निष्क्रिय', 'दण्डित', 'दैत्य', 'इष्टिदिभ', 'सताउन', 'सतावट', 'प्रदूषक','गरीब', 'पूर्वनिर्मित', 'प्रलोभन', 'कैदी', 'समस्या', 'समस्याग्रस्त', 'समस्याहरू', 'विलम्ब', 'अभियोग', 'झगडा', 'नस्लवाद', 'नस्लवादी', 'साम्प्रदायिक', 'साम्प्रदायिकता', 'विद्रोह', 'विद्रोही', 'देशद्रोही', 'इन्कार गर्न', 'इन्कार', 'अनिच्छा', 'इस्तीफा','प्रतिरोध', 'बदला', 'प्रतिशोद', 'जोखिम', 'प्रतिद्वंद्व', 'प्रतिद्वन्द्वी', 'बाधाहरू', 'बर्बाद', 'अफवाह', 'बोका', 'घोटाला', 'शिकारी', 'शेक', 'शङ्का', 'संदेह', 'शंका', 'घेराबन्दी', 'पाप','पापी', 'शंकास्पद', 'गन्ध', 'विचित्र', 'तनाव','तनावपूर्ण', 'सख्त', 'ठोकर', 'पीडा', 'लक्षण', 'आतंकवाद', 'आतंक', 'आतंक-जेनिक', 'आतंकवादी','धम्की', 'शीर्ष-भारी', 'तानाशाह', 'तानाशाही', 'मुसीबन्दी', 'झूटा', 'झुठो', 'मुसीबत', 'परेशानी', 'युद्ध', 'अगेड','बदसूरत', 'अस्वीकार्य', 'अनुपलब्ध', 'अचयनयोग्य', 'अनउठ्य', 'अनिश्चित', 'अनियन्त्रित', 'बेपरिवार', 'अवफादार', 'अधूरो', 'दुर्भाग्यवश', 'गैरकानूनी', 'अप्रिय', 'नपढ्ने', 'असमर्थित', 'असमर्थ', 'अक्षम', 'विभेद', 'व्यर्थ', 'हिंसक', 'हिंसा', 'विपरित', 'अस्थिरता', 'अस्थिर', 'उल्टो', 'बेकार', 'क्रोध', 'घात', 'अवगुण','अपशगुन','निष्कासित', 'साजिश', 'जबरदस्ती', 'अज्ञान', 'अज्ञानी', 'लापरवाही', 'लापरवाह', 'रोगी', 'अशान्ति', 'फोर','दुषित', 'प्रदुषण','प्रदुषित', 'समस्या' , 'सुस्त', 'तिरस्कार', 'तिरस्कृत','अनादर', 'असहाय', 'निर्लज्ज', 'निर्लज', 'निर्दय', 'भयानक', 'निर्विष्ट', 'धिक्कार' ,'हार','नकारात्मक']

 stop_words_eng = ["a","about","above","after","again","against","all","am","an","and","any","are","aren't","as","at","be","because","been","before","being","below","between","both","but","by","can't","cannot","could","couldn't","did","didn't","do","does","doesn't","doing","don't","down","during","each","few","for","from","further","had","hadn't","has","hasn't","have","haven't","having","he","he'd","he'll","he's","her","here","here's","hers","herself","him","himself","his","how","how's","i","i'd","i'll","i'm","i've","if","in","into","is","isn't","it","it's","its","itself","let's","me","more","most","mustn't","my","myself","no","nor","not","of","off","on","once","only","or","other","ought","our","ours","ourselves","out","over","own","same","shan't","she","she'd","she'll","she's","should","shouldn't","so","some","such","than","that","that's","the","their","theirs","them","themselves","then","there","there's","these","they","they'd","they'll","they're","they've","this","those","through","to","too","under","until","up","very","was","wasn't","we","we'd","we'll","we're","we've","were","weren't","what","what's","when","when's","where","where's","which","while","who","who's","whom","why","why's","with","won't","would","wouldn't","you","you'd","you'll","you're","you've","your","yours","yourself","yourselves"]
 stop_words_nep = ['अक्सर','अगाडि','अगाडी','अघि','अझै','अठार','अथवा','अनि','अनुसार','अन्तर्गत','अन्य','अन्यत्र','अन्यथा','अब','अरु','अरुलाई','अरू','अर्को','अर्थात','अर्थात्','अलग','अलि','अवस्था','अहिले','आए','आएका','आएको','आज','आजको','आठ','आत्म','आदि','आदिलाई','आफनो','आफू','आफूलाई','आफै','आफैँ','आफ्नै','आफ्नो','आयो','उ','उक्त','उदाहरण','उनको','उनलाई','उनले','उनि','उनी','उनीहरुको','उन्नाइस','उप','उसको','उसलाई','उसले','उहालाई','ऊ','एउटा','एउटै','एक','एकदम','एघार','ओठ','औ','औं','कता','कति','कतै','कम','कमसेकम','कसरि','कसरी','कसै','कसैको','कसैलाई','कसैले','कसैसँग','कस्तो','कहाँबाट','कहिलेकाहीं','का','काम','कारण','कि','किन','किनभने','कुन','कुनै','कुन्नी','कुरा','कृपया','के','केहि','केही','को','कोहि','कोहिपनि','कोही','कोहीपनि','गए','गएको','गएर','गयौ','गरि','गरी','गरे','गरेका','गरेको','गरेर','गरौं','गर्छ','गर्छन्','गर्छु','गर्दा','गर्दै','गर्न','गर्नु','गर्नुपर्छ','गर्ने','गैर','घर','चार','चाले','चाहनुहुन्छ','चाहन्छु','चाहिं','चाहिए','चाहिंले','चाहीं','चाहेको','चाहेर','चोटी','चौथो','चौध','छ','छन','छन्','छु','छू','छैन','छैनन्','छौ','छौं','जता','जताततै','जना','जनाको','जनालाई','जनाले','जब','जबकि','जबकी','जसको','जसबाट','जसमा','जसरी','जसलाई','जसले','जस्ता','जस्तै','जस्तो','जस्तोसुकै','जहाँ','जान','जाने','जाहिर','जुन','जुनै','जे','जो','जोपनि','जोपनी','झैं','ठाउँमा','ठीक','ठूलो','त','तता','तत्काल','तथा','तथापि','तथापी','तदनुसार','तपाइ','तपाई','तपाईको','तब','तर','तर्फ','तल','तसरी','तापनि','तापनी','तिन','तिनि','तिनिहरुलाई','तिनी','तिनीहरु','तिनीहरुको','तिनीहरू','तिनीहरूको','तिनै','तिमी','तिर','तिरको','ती','तीन','तुरन्त','तुरुन्त','तुरुन्तै','तेश्रो','तेस्कारण','तेस्रो','तेह्र','तैपनि','तैपनी','त्यत्तिकै','त्यत्तिकैमा','त्यस','त्यसकारण','त्यसको','त्यसले','त्यसैले','त्यसो','त्यस्तै','त्यस्तो','त्यहाँ','त्यहिँ','त्यही','त्यहीँ','त्यहीं','त्यो','त्सपछि','त्सैले','थप','थरि','थरी','थाहा','थिए','थिएँ','थिएन','थियो','दर्ता','दश','दिए','दिएको','दिन','दिनुभएको','दिनुहुन्छ','दुइ','दुइवटा','दुई','देखि','देखिन्छ','देखियो','देखे','देखेको','देखेर','दोस्रो','द्वारा','धन्न','धेरै','धौ','न','नगर्नु','नगर्नू','नजिकै','नत्र','नत्रभने','नभई','नभएको','नभनेर','नयाँ','नि','निकै','निम्ति','निम्न','निम्नानुसार','नै','नौ','पक्का','पक्कै','पछाडि','पछाडी','पछि','पछिल्लो','पछी','पटक','पनि','पन्ध्र','पर्छ','पर्थ्यो','पर्दैन','पर्ने','पर्नेमा','पर्याप्त','पहिले','पहिलो','पहिल्यै','पाँच','पांच','पाचौँ','पाँचौं','पिच्छे','पूर्व','पो','प्रति','प्रतेक','प्रत्यक','प्राय','प्लस','फरक','फेरि','फेरी','बढी','बताए','बने','बरु','बाट','बारे','बाहिर','बाहेक','बाह्र','बिच','बिचमा','बिस','बीच','बीचमा','बीस','भए','भएँ','भएका','भएकालाई','भएको','भएन','भएर','भन','भने','भनेको','भनेर','भन्','भन्छन्','भन्छु','भन्दा','भन्दै','भन्नुभयो','भन्ने','भन्या','भयेन','भयो','भर','भरि','भरी',
'भा','भित्र','म','मलाई','मा','मात्र','मात्रै','माथि','माथी','मुनि','मुन्तिर','मेरो','मैले','यति','यथोचित','यदि','यद्ध्यपि','यद्यपि','यस','यसका','यसको','यसपछि','यसबाहेक','यसमा','यसरी','यसले','यसो','यस्तै','यस्तो','यहाँ','यहाँसम्म','यही','या','यी','यो','र','रही','रहेका','रहेको','रहेछ','राखे','राख्छ','राम्रो','रुपमा','रूप','रे','रही','रहेका','रहेको','रहेछ','राखे','राख्छ','राम्रो','रुपमा','रूप','रे','लगभग','लगायत','लाई','लाख','लागि','लागेको','ले','वटा','वरीपरी','वा','वाट','वापत','वास्तवमा','शायद','सक्छ','सक्ने','सँग','संग','सँगको','सँगसँगै','सँगै','संगै','सङ्ग','सङ्गको','सट्टा','सत्र','सधै','सबै','सबैको','सबैलाई','समय','समेत','सम्भव','सम्म','सय','सरह','सहित','सहितै','सही','साँच्चै','सात','साथ','साथै','सायद','सारा','सुनेको','सुनेर','सुरु','सुरुको','सुरुमै','सो','सोचेको','सोचेर','सोही','सोह्र','स्थित','स्पष्ट','हजार','हरे','हरेक','हामी','हामीले','हाम्रा','हाम्रो','हुँदैन','हुन','हुनत','हुनु','हुने','हुनेछ','हुन्','हुन्छ','हुन्थ्यो','हैन','हो','होइन','होकि','होला']

 temp1 = str.maketrans("!?.|,:;-/#@&",12*" ")
 preprocessed_input = user_input.translate(temp1)
 tokens = re.split(' ',preprocessed_input.lower())
 words_count = len(tokens)
 output_box_total.insert(0.0,str(words_count))

 global positive_list
 positive_list = []
 positive_count = 0
 for i in tokens:
     if (i in positive_words):
         positive_count += 1
         positive_list.append(i)
 output_box_positive.insert(0.0,str(positive_count))
 if (len(positive_list)) == 0:
     output_box_all_words_list.insert(0.0,'POSITIVE WORDS IN YOUR TEXT - पाठ्य मा सकारात्मक शब्दहरु:' + '\n' + 'None' + '\n' + 'कुनै पनि छैन' + '\n' + '\n')
 else:
     output_box_all_words_list.insert(0.0,'POSITIVE WORDS IN YOUR TEXT - पाठ्य मा सकारात्मक शब्दहरु:' + '\n' + str(positive_list) + '\n' + '\n')

 global negative_list
 negative_list = []
 negative_count = 0
 for j in tokens:
     if (j in negative_words):
         negative_count += 1
         negative_list.append(j)
 output_box_negative.insert(0.0,str(negative_count))
 if (len(negative_list)) == 0:
     output_box_all_words_list.insert(0.0,'NEGATIVE WORDS IN YOUR TEXT - पाठ्य मा नकारात्मक शब्दहरु :' + '\n' + 'None' +'\n' + 'कुनै पनि छैन' + '\n' + '\n')
 else:
     output_box_all_words_list.insert(0.0,'NEGATIVE WORDS IN YOUR TEXT - पाठ्य मा नकारात्मक शब्दहरु :' + '\n' + str(negative_list) + '\n' + '\n')

 stop_count = 0
 stop_list = []
 for k in tokens:
     if (k in stop_words_eng) or (k in stop_words_nep):
         stop_count += 1
         stop_list.append(k)
 output_box_stop.insert(0.0,str(stop_count))

 neutral_count = words_count-(positive_count+negative_count+stop_count)
 output_box_neutral.insert(0.0,str(neutral_count))
 merged_list = positive_list + negative_list + stop_list
 global neutral_list
 neutral_list = list(set(tokens)-set(merged_list))
 if (len(neutral_list)) == 0:
     output_box_all_words_list.insert(0.0,'NEUTRAL WORDS IN YOUR TEXT - पाठ्य मा निष्पक्ष शब्दहरु :' + '\n' + 'None' + '\n' +'कुनै पनि छैन' + '\n')
 else:
     output_box_all_words_list.insert(0.0,'NEUTRAL WORDS IN YOUR TEXT - पाठ्य मा निष्पक्ष शब्दहरु :' + '\n' + str(neutral_list) + '\n' + '\n')



 positive_percent = (positive_count/words_count)*100 #find effective values of each classification and only then convert to percentage for better, more accurate results.
 negative_percent = (negative_count/words_count)*100
 stop_percent = (stop_count/words_count)*100
 neutral_percent = 100-(positive_percent+negative_percent+stop_percent)

 positive_percent = format(positive_percent,'.2f')
 negative_percent = format(negative_percent,'.2f')
 neutral_percent = format(neutral_percent,'.2f')
 stop_percent = format(stop_percent,'.2f')


 output_box_positive_percent.insert(0.0,str(positive_percent)+ "%")
 output_box_negative_percent.insert(0.0,str(negative_percent) + "%")
 output_box_neutral_percent.insert(0.0,str(neutral_percent) + "%")
 output_box_stop_percent.insert(0.0, str(stop_percent) + "%")

 #compute polarities in both english and nepali using textblob.
 blob_inp = TextBlob(user_input)
 blob_detect = blob_inp.detect_language()

 if (blob_detect=='ne') or (blob_detect=='hi'):
     blob_inp = blob_inp.translate(to='en')

 global blob_value2
 global blob_value
 blob_value = blob_inp.sentiment.polarity
 blob_value2 = str(round(blob_value, 5))


 if (blob_value > 0) and (blob_value < 0.05):
     output_box_overall.insert(0.0, "तपाईको पाठ्य निष्पक्ष-सकारात्मक को बिचमा छ।"+"\n")
     output_box_overall.insert(0.0, "Your input text is 'Neutral to Positive'."+"\n")
 elif (blob_value >= 0.05) and (blob_value < 0.1):
     output_box_overall.insert(0.0, "तपाईको पाठ्य ठिक-ठिकै सकारात्मक छ।"+ "\n")
     output_box_overall.insert(0.0, "Your input text is 'Fairly Positive'."+"\n")
 elif blob_value >= 0.1:
     output_box_overall.insert(0.0, "तपाईको पाठ्य धेरै सकारात्मक छ।"+ "\n")
     output_box_overall.insert(0.0, "Your input text is 'Extremely Positive'."+"\n")
 elif (blob_value < 0) and (blob_value > -0.05):
     output_box_overall.insert(0.0, "तपाईको पाठ्य निष्पक्ष-नकारात्मक को बिचमा छ।"+ "\n")
     output_box_overall.insert(0.0, "Your input text is 'Neutral to Negative'."+"\n")
 elif (blob_value <= -0.05) and (blob_value > -0.1):
     output_box_overall.insert(0.0, "तपाईको पाठ्य ठिक-ठिकै नकारात्मक छ।"+ "\n")
     output_box_overall.insert(0.0, "Your input text is 'Fairly Negative'."+"\n")
 elif blob_value <= -0.1:
     output_box_overall.insert(0.0, "तपाईको पाठ्य धेरै नकारात्मक छ।"+ "\n")
     output_box_overall.insert(0.0, "Your input text is 'Extremely Negative'."+"\n")
 elif blob_value == 0:
     output_box_overall.insert(0.0, "तपाईको पाठ्य निष्पक्ष छ।"+ "\n")
     output_box_overall.insert(0.0, "Your input text is 'Neutral'."+"\n")

 output_box_overall.insert(0.0, "तपाईको पाठ्यको पूर्णरुपी भावनात्मक अंक हो: " + blob_value2 + "\n" + "\n")
 output_box_overall.insert(0.0, "The Polarity score of your input text is: " + blob_value2 + "\n")

 #Graphical Visualizations
 fig = matplotlib.figure.Figure(figsize=(12,5))
 fig.suptitle('GRAPHICAL VISUALIZATION',fontweight='bold',family='arial',horizontalalignment='center',fontsize=14)
 ax = fig.add_subplot(221)
 colors=['#32CD32','#FF0000','#FFD700','#00CED1']
 labels=['Positive-'+str(positive_percent)+'%', 'Negative-'+str(negative_percent)+'%','Neutral-'+str(neutral_percent)+'%','Stop-'+str(stop_percent)+'%']
 sizes=[positive_percent,negative_percent,neutral_percent,stop_percent]
 ax.pie(sizes,colors=colors,startangle=90,explode=(0.03,0.03,0.01,0.01),shadow=True)
 #inner_circle = matplotlib.patches.Circle((0,0),0.5,color='#ffffff')
 #ax.add_artist(inner_circle)
 ax.legend(loc=4,labels=labels,bbox_to_anchor=(0.01,0.2))
 #ax.text(0.01,1.5,'Percentage Distribution',fontweight="bold",fontsize=12,verticalalignment='top',horizontalalignment='right')
 ax.set_title('PERCENTAGE DISTRIBUTION',fontsize=11,family='arial',fontweight='bold')

 ax2 = fig.add_subplot(212)
 bar1 = [positive_count]
 bar2 = [negative_count]
 bar3 = [neutral_count]
 bar4 = [stop_count]
 bar1_pos = [1]
 bar2_pos = [1.25]
 bar3_pos = [1.5]
 bar4_pos = [1.75]
 bar_width = 0.1
 ax2.bar(bar1_pos, bar1, width=bar_width, color='#32CD32', label='Positive words-'+str(positive_count))
 ax2.bar(bar2_pos, bar2, width=bar_width, color='#FF0000', label='Negative words- '+str(negative_count))
 ax2.bar(bar3_pos, bar3, width=bar_width, color='#FFD700', label='Neutral words- '+str(neutral_count))
 ax2.bar(bar4_pos, bar4, width=bar_width, color='#00CED1', label='Stop words-'+str(stop_count))
 ax2.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol=4)
 ax2.set_xticklabels([])
 ax2.axes.get_xaxis().set_visible(False)
 ax2.set_title('FREQUENCY OF DIFFERENT WORDS',horizontalalignment='right',family='arial',fontsize=11,fontweight='bold')
 ax2.set_ylabel('Word Count')
 ax2.yaxis.grid(True)
 ax2.xaxis.grid(True)



 ax3 = fig.add_subplot(222)
 yval = [0]
 ax3.scatter(blob_value,yval,vmin=-5,marker="o",color="r")
 ax3.set_yticks([])
 ax3.set_ylabel('Polarity Score')
 ax3.xaxis.grid(True)
 ax3.yaxis.grid(True)
 ax3.axis('equal')
 ax3.set_title('EMOTION SPACE',horizontalalignment='left',family='arial',fontsize=11,fontweight='bold')
 ax3.axis('on')

 canvas = FigureCanvasTkAgg(fig, master=tab4)
 canvas.get_tk_widget().place(x=37,y=10)
 canvas.draw()
 global temp2
 temp2=canvas.get_tk_widget()

 toolbar = NavigationToolbar2Tk(canvas,tab4)
 toolbar.update()
 #toolbar.pack(side=RIGHT)
 toolbar.place(x=100,y=515)
 #canvas._tkcanvas.place(x=900,y=200)
 global temp3
 temp3 = toolbar



def clear_figure(event=''):
   temp2.destroy()
   temp3.destroy()
window.bind('<Control-g>',clear_figure)

#ttk.Style().configure("TButton", padding=20, relief="flat", #keep this button style for safety if any error occurs.
   #background="red",foreground="yellow",width=10,weight=30)

bstyle=ttk.Style() #set a certain style for the two button.
bstyle.configure("b2.TButton", padding=4,font=('tahoma',9), relief="raised",background="#778899",foreground="black",cursor='sailboat',width=18) #set a certain style for the button.

b2style=ttk.Style()
b2style.configure("b2a.TButton", padding=5,font=('tahoma',9), relief="raised",background="#778899",foreground="black",cursor='sailboat',width=17) #set a certain style for the button.

evaluate_icon = PhotoImage(file='evaluate-icon.png')
clear_icon = PhotoImage(file='clear-icon.png')
btn1_tab3_cal = ttk.Button(tab3,text="Calculate-विश्लेषण गर्नुहोस",style="b2.TButton",command=sentiment_analyzer)
btn1_tab3_cal.place(x=680,y=500)
btn1_tab3_cal.configure(image=evaluate_icon,compound=LEFT)
btn2_tab3_cal = ttk.Button(tab3,text="Clear All- सबै हटाउनुहोस्",style="b2a.TButton",command=clear_outputs)
btn2_tab3_cal.place(x=860,y=500)
btn2_tab3_cal.configure(image=clear_icon,compound=LEFT)

#relief="raised",background="#00CED1",foreground="black",cursor='hand1'
#tab 3 ends

#---------------------------------------------------------------------------------------------------------------#

#tab 4 begins
tab4 = ttk.Frame(mainframe)
mainframe.add(tab4, text="VISUALIZE-ग्राफहरू हेर्नुहोस्")
cstyle=ttk.Style() #set a certain style for the button.
cstyle.configure("b3.TButton", padding=6,font=('tahoma',9), relief="raised",background="#D5D5D5",foreground="black",cursor='hand1',width=22) #set a certain style for the button.
#All Functions called in tab3.
btn1_tab4 = ttk.Button(tab4,text="Clear Figure - चित्र हटाउनुहोस्",style="b3.TButton",command=clear_figure) #create button.
btn1_tab4.configure(image=clear_icon,compound=LEFT)
btn1_tab4.place(x=550,y=515)

#tab 4 ends

#---------------------------------------------------------------------------------------------------------------#

#TAB-5 BEGINS
tab5 = ttk.Frame(mainframe)
mainframe.add(tab5, text="FEEDBACK-तपाईंको मूल्यांकन")

label1_eng_tab5 = Label(tab5,text="THANK YOU FOR CHOOSING EMOGEN!",font=('tahoma',15),background="#4D4D4D",foreground="white").place(x=30,y=20)
label2_eng_tab5 = Label(tab5,text="Please spare a moment and give us your valuable feedback and suggestions.",font=('tahoma',9),background="#4D4D4D",foreground="white").place(x=30,y=60)
label3_eng_tab5 = Label(tab5,text="Save your response by clicking the save button and send it to- <gltech@gmail.com>. ",font=('tahoma',9),background="#4D4D4D",foreground="white").place(x=30,y=80)
label4_eng_tab5 = Label(tab5,text="It will be feasible for us to store and look into your responses",font=('tahoma',9),background="#4D4D4D",foreground="white").place(x=30,y=100)
label5_eng_tab5 = Label(tab5,text="in a better way and also improve ourselves in the future. ",font=('tahoma',9),background="#4D4D4D",foreground="white").place(x=30,y=120)


label4_nep_tab5 = Label(tab5,text="ईमोजेन चयन गर्नु भएकोमा धन्यबाद|",font=('tahoma',15),background="#4D4D4D",foreground="white").place(x=820,y=20)
label5_nep_tab5 = Label(tab5,text="कृपया हामीलाई आफ्नो सुझावहरु दिनुहोस् र इमोगेन को मुल्यांकन गर्नुहोस|",font=('tahoma',10),background="#4D4D4D",foreground="white").place(x=820,y=60)
label6_nep_tab5 = Label(tab5,text="मुल्यांकन गरेपछि फाइल लाई सेव गर्नुहोस र <gltech@gmail.com> मा पठाउनुहोस् | ",font=('tahoma',10),background="#4D4D4D",foreground="white").place(x=820,y=80)
label7_nep_tab5 = Label(tab5,text="यस्तो गर्दा भविष्यमा हामी आफ्नो सुबिधर्हरुलाई अझै राम्रो बनाउन सक्छौ। ",font=('tahoma',10),background="#4D4D4D",foreground="white").place(x=820,y=100)

emogen_img = PhotoImage(file='emogen_img_tab5.png')
emogen_img_tab5 = Label(tab5, image=emogen_img,background='#4D4D4D').place(x=520,y=20)

feedback_img = PhotoImage(file='feedback_img1.png')
feddback_img_tab5 = Label(tab5, image=feedback_img,background='#4D4D4D').place(x=30,y=150)

feedback_img2 = PhotoImage(file='suggest3.png')
feddback_img2_tab5 = Label(tab5, image=feedback_img2,background='#4D4D4D').place(x=900,y=180)
#create feedback form and store it in a canvas widget.
tab5_canvas = Canvas(tab5, width=500,height=500,bg="#D3D3D3",highlightthickness=0, highlightbackground="black")
tab5_canvas.place(x=360,y=120)
#create a save feedback function.
def save_feedback():
    #print(str(int(scale_interface_design.get())))
    Name = name_entry.get()
    Email = email_entry.get()
    Contact = str(contact_entry.get())
    Location = location_entry.get()

    file_to_save = filedialog.asksaveasfile(mode="wb", defaultextension=".htm")
    if file_to_save is None:
        return

    file_to_save.write(('<h1 align="center">YOUR FEEDBACK - तपाई को मुल्यांकन</h1>'+'<br>\n').encode('utf=8'))
    file_to_save.write(('<hr>').encode('utf-8'))

    file_to_save.write(('<h2>PERSONAL INFORMATION</h2>'+'<br>\n').encode('utf=8'))
    file_to_save.write(("Name: ").encode('utf-8'))
    file_to_save.write((str(Name)+'<br>\n').encode('utf-8'))
    file_to_save.write(("Email:").encode('utf-8'))
    file_to_save.write((str(Email)+'<br>\n').encode('utf-8'))
    file_to_save.write(("Contact:").encode('utf-8'))
    file_to_save.write((str(Contact)+'<br>\n').encode('utf-8'))
    file_to_save.write(("Location:").encode('utf-8'))
    file_to_save.write((str(Location)+'<br>\n'+'<br>\n').encode('utf-8'))

    file_to_save.write(('<hr>').encode('utf-8'))

    #scores by the user are stored in variables below
    file_to_save.write(('<h2> YOUR RATINGS FOR EMOGEN</h2>'+'<br>\n').encode('utf=8'))
    file_to_save.write(("Interface Design:").encode('utf-8'))
    interface_design_score = float(scale_interface_design.get())
    interface_design_score = format(interface_design_score,'.2f')
    file_to_save.write((str(interface_design_score)+'<br>\n').encode('utf-8'))

    file_to_save.write(("Ease of Using:").encode('utf-8'))
    easiness_score = float(scale_using_design.get())
    easiness_score = format(easiness_score,'.2f')
    file_to_save.write((str(easiness_score)+'<br>\n').encode('utf-8'))

    file_to_save.write(("Description and Illustration:").encode('utf-8'))
    description_score = float(scale_description_design.get())
    description_score = format(description_score,'.2f')
    file_to_save.write((str(description_score)+'<br>\n').encode('utf-8'))

    file_to_save.write(("Calculation Efficiency:").encode('utf-8'))
    calc_score = float(scale_calc_design.get())
    calc_score = format(calc_score,'.2f')
    file_to_save.write((str(calc_score)+'<br>\n').encode('utf-8'))

    file_to_save.write(("Graphs:").encode('utf-8'))
    graphs_score = float(scale_graphs_design.get())
    graphs_score = format(graphs_score,'.2f')
    file_to_save.write((str(graphs_score)+'<br>\n').encode('utf-8'))

    file_to_save.write(("Storing Results:").encode('utf-8'))
    storing_score = float(scale_storing_design.get())
    storing_score = format(storing_score,'.2f')
    file_to_save.write((str(storing_score)+'<br>\n').encode('utf-8'))

    file_to_save.write(("Overall Rating:").encode('utf-8'))
    overall_score = float(scale_overall_design.get())
    overall_score = format(overall_score,'.2f')
    file_to_save.write((str(overall_score)+'<br>\n'+'<br>\n').encode('utf-8'))

    file_to_save.write(('<hr>').encode('utf-8'))

    file_to_save.write(("<h2> OTHER COMMENTS AND SUGGESTIONS: </h2>" + "<br>\n").encode('utf-8'))
    suggestions = comment_box.get("1.0",END)
    file_to_save.write((str(suggestions)+'<br>\n').encode('utf-8'))

    file_to_save.write(('<hr>').encode('utf-8'))
    file_to_save.close()

label8_tab5 = Label(tab5_canvas,text="Your Name-तपाईको नाम :",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=10,y=10)
label9_tab5 = Label(tab5_canvas,text="Your Email Address-तपाईको इमेल :",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=10,y=40)
label10_tab5 = Label(tab5_canvas,text="Your Contact No-तपाइको फोन :",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=10,y=70)
label11_tab5 = Label(tab5_canvas,text="Your Location-तपाइको ठेगाना :",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=10,y=100)

#namevar = StringVar()
#emailvar = StringVar()
#contactvar = IntVar()
#locationvar = StringVar()

name_entry = ttk.Entry(tab5_canvas,width=45)
name_entry.place(x=200,y=10)
email_entry = ttk.Entry(tab5_canvas,width=45)
email_entry.place(x=200,y=40)
contact_entry = ttk.Entry(tab5_canvas,width=45)
contact_entry.place(x=200,y=70)
location_entry = ttk.Entry(tab5_canvas,width=45)
location_entry.place(x=200,y=100)

label12_tab5 = Label(tab5_canvas,text="YOUR FEEDBACK-तपाइको मुल्यांकन",font=('tahoma',10,'bold'),background="#D3D3D3",foreground="black").place(x=10,y=135)

#create an evaluation form with scaling facility

label14_tab5 = Label(tab5_canvas,text="Interface Design and Visuals-सफ्टवेयरको डिजाइन :",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=8,y=178)
label15_tab5 = Label(tab5_canvas,text="Ease of Using-प्रयोग गर्नमा सरलता :",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=95,y=197)
label16_tab5 = Label(tab5_canvas,text="Description and Illustration-विवरण र चित्रण :",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=42,y=216)
label17_tab5 = Label(tab5_canvas,text="Calculation Efficieny-गणनाको  क्षमता :",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=79,y=236)
label18_tab5 = Label(tab5_canvas,text="Graphs-ग्राफहरु :",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=186,y=257)
label19_tab5 = Label(tab5_canvas,text="Storing Results-परिणाम सेव गर्नको प्रावधान :",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=52,y=277)
label20_tab5 = Label(tab5_canvas,text="Overall Rating-पूर्णरुपी मुल्यांकन :",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=106,y=298)

label_tickvalue0 = Label(tab5_canvas,text="0",font=('tahoma',7),background="#D3D3D3",foreground="black").place(x=275,y=158)
label_tickvalue1 = Label(tab5_canvas,text="1",font=('tahoma',7),background="#D3D3D3",foreground="black").place(x=295,y=158)
label_tickvalue2 = Label(tab5_canvas,text="2",font=('tahoma',7),background="#D3D3D3",foreground="black").place(x=315,y=158)
label_tickvalue3 = Label(tab5_canvas,text="3",font=('tahoma',7),background="#D3D3D3",foreground="black").place(x=335,y=158)
label_tickvalue4 = Label(tab5_canvas,text="4",font=('tahoma',7),background="#D3D3D3",foreground="black").place(x=355,y=158)
label_tickvalue5 = Label(tab5_canvas,text="5",font=('tahoma',7),background="#D3D3D3",foreground="black").place(x=375,y=158)
label_tickvalue6 = Label(tab5_canvas,text="6",font=('tahoma',7),background="#D3D3D3",foreground="black").place(x=395,y=158)
label_tickvalue7 = Label(tab5_canvas,text="7",font=('tahoma',7),background="#D3D3D3",foreground="black").place(x=415,y=158)
label_tickvalue8 = Label(tab5_canvas,text="8",font=('tahoma',7),background="#D3D3D3",foreground="black").place(x=435,y=158)
label_tickvalue9 = Label(tab5_canvas,text="9",font=('tahoma',7),background="#D3D3D3",foreground="black").place(x=455,y=158)
label_tickvalue10 = Label(tab5_canvas,text="10",font=('tahoma',7),background="#D3D3D3",foreground="black").place(x=470,y=158)

label_tick1 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=275,y=170)
label_tick2 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=295,y=170)
label_tick3 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=315,y=170)
label_tick4 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=335,y=170)
label_tick5 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=355,y=170)
label_tick6 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=375,y=170)
label_tick7 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=395,y=170)
label_tick8 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=415,y=170)
label_tick9 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=435,y=170)
label_tick10 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=455,y=170)
label_tickextra1 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=469,y=170)

label_tick11 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=275,y=190)
label_tick12 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=295,y=190)
label_tick13 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=315,y=190)
label_tick14 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=335,y=190)
label_tick15 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=355,y=190)
label_tick16 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=375,y=190)
label_tick17 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=395,y=190)
label_tick18 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=415,y=190)
label_tick19 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=435,y=190)
label_tick20 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=455,y=190)
label_tickextra2 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=469,y=190)

label_tick21 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=275,y=210)
label_tick22 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=295,y=210)
label_tick23 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=315,y=210)
label_tick24 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=335,y=210)
label_tick25 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=355,y=210)
label_tick26 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=375,y=210)
label_tick27 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=395,y=210)
label_tick28 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=415,y=210)
label_tick29 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=435,y=210)
label_tick30 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=455,y=210)
label_tickextra3 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=469,y=210)

label_tick31 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=275,y=230)
label_tick32 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=295,y=230)
label_tick33 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=315,y=230)
label_tick34 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=335,y=230)
label_tick35 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=355,y=230)
label_tick36 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=375,y=230)
label_tick37 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=395,y=230)
label_tick38 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=415,y=230)
label_tick39 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=435,y=230)
label_tick40 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=455,y=230)
label_tickextra4 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=469,y=230)


label_tick41 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=275,y=250)
label_tick42 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=295,y=250)
label_tick43 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=315,y=250)
label_tick44 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=335,y=250)
label_tick45 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=355,y=250)
label_tick46 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=375,y=250)
label_tick47 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=395,y=250)
label_tick48 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=415,y=250)
label_tick49 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=435,y=250)
label_tick50 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=455,y=250)
label_tickextra5 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=469,y=250)

label_tick51 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=275,y=270)
label_tick52 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=295,y=270)
label_tick53 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=315,y=270)
label_tick54 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=335,y=270)
label_tick55 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=355,y=270)
label_tick56 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=375,y=270)
label_tick57 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=395,y=270)
label_tick58 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=415,y=270)
label_tick59 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=435,y=270)
label_tick60 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=455,y=270)
label_tickextra6 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=469,y=270)

label_tick61 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=275,y=290)
label_tick62 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=295,y=290)
label_tick63 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=315,y=290)
label_tick64 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=335,y=290)
label_tick65 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=355,y=290)
label_tick66 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=375,y=290)
label_tick67 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=395,y=290)
label_tick68 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=415,y=290)
label_tick69 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=435,y=290)
label_tick70 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=455,y=290)
label_tickextra7 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=469,y=290)
#label21_tab5 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=250,y=170)
#label22_tab5 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=268,y=170)
#label23_tab5 = Label(tab5_canvas,text="|",font=('tahoma',9),background="#D3D3D3",foreground="black").place(x=286,y=170)

scalestyle=ttk.Style()
scalestyle.configure("Horizontal.TScale",sliderthickness=6,background="#2F4F4F",troughcolor="#778899",sliderrelief="raise")

scale_interface_design=Scale(tab5_canvas,style="Horizontal.TScale",from_=0, to=10,length=200,orient=HORIZONTAL)
scale_interface_design.place(x=275,y=181)
scale_using_design=Scale(tab5_canvas,style="Horizontal.TScale",from_=0, to=10,length=200,orient=HORIZONTAL)
scale_using_design.place(x=275,y=201)
scale_description_design=Scale(tab5_canvas,style="Horizontal.TScale",from_=0, to=10,length=200,orient=HORIZONTAL)
scale_description_design.place(x=275,y=221)
scale_calc_design=Scale(tab5_canvas,style="Horizontal.TScale",from_=0, to=10,length=200,orient=HORIZONTAL)
scale_calc_design.place(x=275,y=241)
scale_graphs_design=Scale(tab5_canvas,style="Horizontal.TScale",from_=0, to=10,length=200,orient=HORIZONTAL)
scale_graphs_design.place(x=275,y=261)
scale_storing_design=Scale(tab5_canvas,style="Horizontal.TScale",from_=0, to=10,length=200,orient=HORIZONTAL)
scale_storing_design.place(x=275,y=281)
scale_overall_design=Scale(tab5_canvas,style="Horizontal.TScale",from_=0, to=10,length=200,orient=HORIZONTAL)
scale_overall_design.place(x=275,y=301)

label26_tab5 = Label(tab5_canvas,text="Other Suggestions-अन्य सुझावहरू",font=('tahoma',9,'bold'),background="#D3D3D3",foreground="black").place(x=80,y=335)
comment_box = Text(tab5_canvas,width=52,height=5,bg="white",fg="black",font=('tahoma',9))
comment_box.place(x=7,y=355)

label27_tab5 = Label(tab5_canvas,text="Scale",font=('tahoma',8),background="#D3D3D3",foreground="black").place(x=500,y=335)


dstyle=ttk.Style() #set a certain style for the button.
dstyle.configure("b4.TButton", padding=3,font=('tahoma',9), relief="raised",background="#778899",foreground="black",cursor='hand1',width=13) #set a certain style for the button.

save_comments_img = PhotoImage(file='save-comments.png')
save_comments_button = ttk.Button(tab5,text="Save-सेव गर्नुहोस",style="b4.TButton",command=save_feedback) #create button.
save_comments_button.place(x=737,y=525)
save_comments_button.configure(image=save_comments_img,compound=LEFT)


#TAB-5 ENDS

#---------------------------------------------------------------------------------------------------------------#

connect_canvas = Canvas(window, width=236, height=10, bg="white", highlightthickness=0, highlightbackground="black")
connect_canvas.place(x=9, y=610)
#bottom region of the entire window
label_connect = Label(window, text='CONNECT WITH US - हामी संग जुद्नुहोस ', font=("tahoma", 10,"bold"), foreground="#4D4D4D",background="white").place(x=9, y=592)

#create image icons and hyperlink them

def fb_callback(event): #hyperlink to facebook
    webbrowser.open_new(r"http://www.google.com")
#create the fb-icon
fb_icon = PhotoImage(file="icon-fb.png")
label_imgfb = Label(window, image=fb_icon, cursor="hand2", border=0)
label_imgfb.place(x=10,y=612)
label_imgfb.bind("<1>", fb_callback)

def linkedin_callback(event): #hyperlink to linkedin
    webbrowser.open_new(r"http://www.google.com")
#create the linkedin-icon
linkedin_icon = PhotoImage(file="icon-linkedin.png")
label_imglinkedin = Label(window,image=linkedin_icon, cursor="hand2", border=0)
label_imglinkedin.place(x=53, y=612)
label_imglinkedin.bind("<1>",linkedin_callback)

def slideshare_callback(event): #hyperlink to slideshare
    webbrowser.open_new(r"http://www.google.com")
#create the slideshare icon
slidershare_icon = PhotoImage(file="icon-slideshare.png")
label_imgslideshare = Label(window,image=slidershare_icon, cursor="hand2", border=0)
label_imgslideshare.place(x=143, y=611)
label_imgslideshare.bind("<1>",slideshare_callback)

def gl_callback(event): #hyperlink to GL Technologies website
    webbrowser.open_new(r"http://www.google.com")
#create GL tech icon
gl_icon = PhotoImage(file="icon-gltech.png")
label_imgl = Label(window, image=gl_icon, cursor="hand2", border=0)
label_imgl.place(x=95, y=614)
label_imgl.bind("<1>",gl_callback)

def twitter_callback(): #hyperlink to twitter
    webbrowser.open_new(r"http://www.google.com")
#create twitter icon
twitter_icon = PhotoImage(file="icon-twitter.png")
label_imgtwitter = Label(window, image=twitter_icon, cursor="hand2", border=0)
label_imgtwitter.place(x=180, y=612)
label_imgtwitter.bind("<1>", twitter_callback)

window.mainloop() #end of GUI

#---------------------------------------------------------------------------------------------------------------#