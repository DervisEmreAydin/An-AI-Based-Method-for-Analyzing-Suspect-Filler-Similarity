from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
from deepface import DeepFace
from deepface.basemodels import VGGFace, OpenFace, Facenet, FbDeepFace
from PIL import Image, ImageTk
import tkinter as tk
import conf
from screen import Screen


# The functions of suspect and fillers' upload buttons

def S_handle_button_image_upload():
    print("button_image_upload is pressed")
    filename = filedialog.askopenfilename(initialdir="/",
                                          title=conf.image_upload_menu_info,
                                          filetypes=[("Image Files", ('.png', '.jfif', '.jpg', '.jpeg'))])
    if filename != "":
        S_label_file_explorer.configure(text="Suspect uploaded")
        conf.suspect_image_path = filename

    global suspect
    suspect = ImageTk.PhotoImage(Image.open(conf.suspect_image_path).resize((200, 200), Image.ANTIALIAS))
    suspect_img = Label(page1Window, image=suspect)
    suspect_img.place(x=0, y=0, relx=0.416, rely=0.275, anchor='center')

def F1_handle_button_image_upload():
    print("button_image_upload is pressed")
    f1 = filedialog.askopenfilename(initialdir="/",
                                          title=conf.image_upload_menu_info,
                                          filetypes=[("Image Files", ('.png', '.jfif', '.jpg', '.jpeg'))])
    if f1 != "":
        F1_label_file_explorer.configure(text="1st filler uploaded")
        conf.f1_image_path = f1

    global filler1
    filler1 = ImageTk.PhotoImage(Image.open(conf.f1_image_path).resize((200, 200), Image.ANTIALIAS))
    filler1_img = Label(page1Window, image=filler1)
    filler1_img.place(x=0, y=0, relx=0.566, rely=0.275, anchor='center')

def F2_handle_button_image_upload():
    print("button_image_upload is pressed")
    f2 = filedialog.askopenfilename(initialdir="/",
                                          title=conf.image_upload_menu_info,
                                          filetypes=[("Image Files", ('.png', '.jfif', '.jpg', '.jpeg'))])
    if f2 != "":
        F2_label_file_explorer.configure(text="2nd filler uploaded")
        conf.f2_image_path = f2

    global filler2
    filler2 = ImageTk.PhotoImage(Image.open(conf.f2_image_path).resize((200, 200), Image.ANTIALIAS))
    filler2_img = Label(page1Window, image=filler2)
    filler2_img.place(x=0, y=0, relx=0.716, rely=0.275, anchor='center')

def F3_handle_button_image_upload():
    print("button_image_upload is pressed")
    f3 = filedialog.askopenfilename(initialdir="/",
                                          title=conf.image_upload_menu_info,
                                          filetypes=[("Image Files", ('.png', '.jfif', '.jpg', '.jpeg'))])
    if f3 != "":
        F3_label_file_explorer.configure(text="3rd filler uploaded")
        conf.f3_image_path = f3

    global filler3
    filler3 = ImageTk.PhotoImage(Image.open(conf.f3_image_path).resize((200, 200), Image.ANTIALIAS))
    filler3_img = Label(page1Window, image=filler3)
    filler3_img.place(x=0, y=0, relx=0.416, rely=0.665, anchor='center')

def F4_handle_button_image_upload():
    print("button_image_upload is pressed")
    f4 = filedialog.askopenfilename(initialdir="/",
                                          title=conf.image_upload_menu_info,
                                          filetypes=[("Image Files", ('.png', '.jfif', '.jpg', '.jpeg'))])
    if f4 != "":
        F4_label_file_explorer.configure(text="4th filler uploaded")
        conf.f4_image_path = f4

    global filler4
    filler4 = ImageTk.PhotoImage(Image.open(conf.f4_image_path).resize((200, 200), Image.ANTIALIAS))
    filler4_img = Label(page1Window, image=filler4)
    filler4_img.place(x=0, y=0, relx=0.566, rely=0.665, anchor='center')

def F5_handle_button_image_upload():
    print("button_image_upload is pressed")
    f5 = filedialog.askopenfilename(initialdir="/",
                                          title=conf.image_upload_menu_info,
                                          filetypes=[("Image Files", ('.png', '.jfif', '.jpg', '.jpeg'))])
    if f5 != "":
        F5_label_file_explorer.configure(text="5th filler uploaded")
        conf.f5_image_path = f5

    global filler5
    filler5 = ImageTk.PhotoImage(Image.open(conf.f5_image_path).resize((200,200), Image.ANTIALIAS))
    filler5_img = Label(page1Window, image=filler5)
    filler5_img.place(x=0, y=0, relx=0.716, rely=0.665, anchor='center')


# When the user click the Start Similarity Analyzing, this function work

def handle_button_measurement_stage():
    print("measurement button is pressed")
    print(model)
    print(metric)

    # Deep Face Verify Function
    verify1 = DeepFace.verify(conf.suspect_image_path, conf.f1_image_path,
                              model_name= model,
                              distance_metric= metric)
    verify2 = DeepFace.verify(conf.suspect_image_path, conf.f2_image_path,
                              model_name= model,
                              distance_metric= metric)
    verify3 = DeepFace.verify(conf.suspect_image_path, conf.f3_image_path,
                              model_name= model,
                              distance_metric= metric)
    verify4 = DeepFace.verify(conf.suspect_image_path, conf.f4_image_path,
                              model_name= model,
                              distance_metric= metric)
    verify5 = DeepFace.verify(conf.suspect_image_path, conf.f5_image_path,
                              model_name= model,
                              distance_metric= metric)

    # Face Similarity
    verify1_list = [verify1.get('distance')]
    print(verify1_list)
    verify2_list = [verify2.get('distance')]
    verify3_list = [verify3.get('distance')]
    verify4_list = [verify4.get('distance')]
    verify5_list = [verify5.get('distance')]
    print(verify5_list)

    distance_value1 = ''.join(str(x) for x in verify1_list)
    distance_value2 = ''.join(str(x) for x in verify2_list)
    distance_value3 = ''.join(str(x) for x in verify3_list)
    distance_value4 = ''.join(str(x) for x in verify4_list)
    distance_value5 = ''.join(str(x) for x in verify5_list)

    text_box.delete(1.0, 'end')
    text_box.insert('end', 'Model =' + model +'\nMetric =' + metric + '\n')
    text_box.insert('end', '\nResults\n\n**** Filler1 **** \n')
    text_box.insert('end', distance_value1)
    text_box.insert('end', '\n**** Filler 2 ****\n')
    text_box.insert('end', distance_value2)
    text_box.insert('end', '\n**** Filler 3 ****\n')
    text_box.insert('end', distance_value3)
    text_box.insert('end', '\n**** Filler 4 ****\n')
    text_box.insert('end', distance_value4)
    text_box.insert('end', '\n**** Filler 5 ****\n')
    text_box.insert('end', distance_value5)
    text_box.insert('end', '\n***\nThe results include only facial similarity.')


# When the user click the Start Availability Analyzing, this function work

def handle_button_analyze_stage():
    print("analyze button is pressed")
    print(model)
    print(metric)
    print(lower_value)

    # Deep Face Verify Function
    verify1 = DeepFace.verify(conf.suspect_image_path, conf.f1_image_path,
                              model_name= model,
                              distance_metric= metric)
    verify2 = DeepFace.verify(conf.suspect_image_path, conf.f2_image_path,
                              model_name= model,
                              distance_metric= metric)
    verify3 = DeepFace.verify(conf.suspect_image_path, conf.f3_image_path,
                              model_name= model,
                              distance_metric= metric)
    verify4 = DeepFace.verify(conf.suspect_image_path, conf.f4_image_path,
                              model_name= model,
                              distance_metric= metric)
    verify5 = DeepFace.verify(conf.suspect_image_path, conf.f5_image_path,
                              model_name= model,
                              distance_metric= metric)

    # Face Similarity
    verify1_list = [verify1.get('distance')]
    print(verify1_list)
    verify2_list = [verify2.get('distance')]
    verify3_list = [verify3.get('distance')]
    verify4_list = [verify4.get('distance')]
    verify5_list = [verify5.get('distance')]
    print(verify5_list)

#Analyze
    analyze_s = DeepFace.analyze(conf.suspect_image_path)
    analyze_f1 = DeepFace.analyze(conf.f1_image_path)
    analyze_f2 = DeepFace.analyze(conf.f2_image_path)
    analyze_f3 = DeepFace.analyze(conf.f3_image_path)
    analyze_f4 = DeepFace.analyze(conf.f4_image_path)
    analyze_f5 = DeepFace.analyze(conf.f5_image_path)

#Results
    # for f1
    if analyze_s["gender"] != analyze_f1["gender"]:
        F1_label = Label(page1Window, text="Gender", bg='red', font=('calibre', 10, 'bold'))
        F1_label.place(relx=0.52, rely=0.43, anchor='center')
    else:
        F1_label = Label(page1Window, text="Gender", bg='green', font=('calibre', 10, 'bold'))
        F1_label.place(relx=0.52, rely=0.43, anchor='center')

    if analyze_s["dominant_race"] != analyze_f1["dominant_race"]:
        F1_label = Label(page1Window, text="Race", bg='red', font=('calibre', 10, 'bold'))
        F1_label.place(relx=0.55, rely=0.43, anchor='center')
    else:
        F1_label = Label(page1Window, text="Race", bg='green', font=('calibre', 10, 'bold'))
        F1_label.place(relx=0.55, rely=0.43, anchor='center')

    if (analyze_s["age"] - 3 <= analyze_f1["age"]) and (analyze_f1["age"] <= analyze_s["age"] + 3):
        F1_label = Label(page1Window, text="Age", bg='green', font=('calibre', 10, 'bold'))
        F1_label.place(relx=0.572, rely=0.43, anchor='center')
    else:
        F1_label = Label(page1Window, text="Age", bg='red', font=('calibre', 10, 'bold'))
        F1_label.place(relx=0.572, rely=0.43, anchor='center')

    if analyze_s["dominant_emotion"] != analyze_f1["dominant_emotion"]:
        F1_label = Label(page1Window, text="F.E.", bg='red', font=('calibre', 10, 'bold'))
        F1_label.place(relx=0.592, rely=0.43, anchor='center')
    else:
        F1_label = Label(page1Window, text="F.E.", bg='green', font=('calibre', 10, 'bold'))
        F1_label.place(relx=0.592, rely=0.43, anchor='center')

    if verify1_list[0] < float(lower_value):
        F1_label = Label(page1Window, text=" F.S. ", bg='red', font=('calibre', 10, 'bold'))
        F1_label.place(relx=0.614, rely=0.43, anchor='center')
    else:
        F1_label = Label(page1Window, text=" F.S. ", bg='green', font=('calibre', 10, 'bold'))
        F1_label.place(relx=0.614, rely=0.43, anchor='center')

    # for f2
    if analyze_s["gender"] != analyze_f2["gender"]:
        F2_label = Label(page1Window, text="Gender", bg='red', font=('calibre', 10, 'bold'))
        F2_label.place(relx=0.67, rely=0.43, anchor='center')
    else:
        F2_label = Label(page1Window, text="Gender", bg='green', font=('calibre', 10, 'bold'))
        F2_label.place(relx=0.67, rely=0.43, anchor='center')

    if analyze_s["dominant_race"] != analyze_f2["dominant_race"]:
        F2_label = Label(page1Window, text="Race", bg='red', font=('calibre', 10, 'bold'))
        F2_label.place(relx=0.70, rely=0.43, anchor='center')
    else:
        F2_label = Label(page1Window, text="Race", bg='green', font=('calibre', 10, 'bold'))
        F2_label.place(relx=0.70, rely=0.43, anchor='center')

    if (analyze_s["age"] - 3 <= analyze_f2["age"]) and (analyze_f2["age"] <= analyze_s["age"] + 3):
        F2_label = Label(page1Window, text="Age", bg='green', font=('calibre', 10, 'bold'))
        F2_label.place(relx=0.722, rely=0.43, anchor='center')
    else:
        F2_label = Label(page1Window, text="Age", bg='red', font=('calibre', 10, 'bold'))
        F2_label.place(relx=0.722, rely=0.43, anchor='center')

    if analyze_s["dominant_emotion"] != analyze_f2["dominant_emotion"]:
        F2_label = Label(page1Window, text="F.E.", bg='red', font=('calibre', 10, 'bold'))
        F2_label.place(relx=0.742, rely=0.43, anchor='center')
    else:
        F2_label = Label(page1Window, text="F.E.", bg='green', font=('calibre', 10, 'bold'))
        F2_label.place(relx=0.742, rely=0.43, anchor='center')

    if verify2_list[0] < float(lower_value):
        F2_label = Label(page1Window, text=" F.S. ", bg='red', font=('calibre', 10, 'bold'))
        F2_label.place(relx=0.764, rely=0.43, anchor='center')
    else:
        F2_label = Label(page1Window, text=" F.S. ", bg='green', font=('calibre', 10, 'bold'))
        F2_label.place(relx=0.764, rely=0.43, anchor='center')


    # for f3
    if analyze_s["gender"] != analyze_f3["gender"]:
        F3_label = Label(page1Window, text="Gender", bg='red', font=('calibre', 10, 'bold'))
        F3_label.place(relx=0.37, rely=0.82, anchor='center')
    else:
        F3_label = Label(page1Window, text="Gender", bg='green', font=('calibre', 10, 'bold'))
        F3_label.place(relx=0.37, rely=0.82, anchor='center')

    if analyze_s["dominant_race"] != analyze_f3["dominant_race"]:
        F3_label = Label(page1Window, text="Race", bg='red', font=('calibre', 10, 'bold'))
        F3_label.place(relx=0.40, rely=0.82, anchor='center')
    else:
        F3_label = Label(page1Window, text="Race", bg='green', font=('calibre', 10, 'bold'))
        F3_label.place(relx=0.40, rely=0.82, anchor='center')

    if (analyze_s["age"] - 3 <= analyze_f3["age"]) and (analyze_f3["age"] <= analyze_s["age"] + 3):
        F3_label = Label(page1Window, text="Age", bg='green', font=('calibre', 10, 'bold'))
        F3_label.place(relx=0.422, rely=0.82, anchor='center')
    else:
        F3_label = Label(page1Window, text="Age", bg='red', font=('calibre', 10, 'bold'))
        F3_label.place(relx=0.422, rely=0.82, anchor='center')

    if analyze_s["dominant_emotion"] != analyze_f3["dominant_emotion"]:
        F3_label = Label(page1Window, text="F.E.", bg='red', font=('calibre', 10, 'bold'))
        F3_label.place(relx=0.442, rely=0.82, anchor='center')
    else:
        F3_label = Label(page1Window, text="F.E.", bg='green', font=('calibre', 10, 'bold'))
        F3_label.place(relx=0.442, rely=0.82, anchor='center')

    if verify3_list[0] < float(lower_value):
        F3_label = Label(page1Window, text=" F.S. ", bg='red', font=('calibre', 10, 'bold'))
        F3_label.place(relx=0.464, rely=0.82, anchor='center')
    else:
        F3_label = Label(page1Window, text=" F.S. ", bg='green', font=('calibre', 10, 'bold'))
        F3_label.place(relx=0.464, rely=0.82, anchor='center')


    # for f4
    if analyze_s["gender"] != analyze_f4["gender"]:
        F4_label = Label(page1Window, text="Gender", bg='red', font=('calibre', 10, 'bold'))
        F4_label.place(relx=0.52, rely=0.82, anchor='center')
    else:
        F4_label = Label(page1Window, text="Gender", bg='green', font=('calibre', 10, 'bold'))
        F4_label.place(relx=0.52, rely=0.82, anchor='center')

    if analyze_s["dominant_race"] != analyze_f4["dominant_race"]:
        F4_label = Label(page1Window, text="Race", bg='red', font=('calibre', 10, 'bold'))
        F4_label.place(relx=0.55, rely=0.82, anchor='center')
    else:
        F4_label = Label(page1Window, text="Race", bg='green', font=('calibre', 10, 'bold'))
        F4_label.place(relx=0.55, rely=0.82, anchor='center')

    if (analyze_s["age"] - 3 <= analyze_f4["age"]) and (analyze_f4["age"] <= analyze_s["age"] + 3):
        F4_label = Label(page1Window, text="Age", bg='green', font=('calibre', 10, 'bold'))
        F4_label.place(relx=0.572, rely=0.82, anchor='center')
    else:
        F4_label = Label(page1Window, text="Age", bg='red', font=('calibre', 10, 'bold'))
        F4_label.place(relx=0.572, rely=0.82, anchor='center')

    if analyze_s["dominant_emotion"] != analyze_f4["dominant_emotion"]:
        F4_label = Label(page1Window, text="F.E.", bg='red', font=('calibre', 10, 'bold'))
        F4_label.place(relx=0.592, rely=0.82, anchor='center')
    else:
        F4_label = Label(page1Window, text="F.E.", bg='green', font=('calibre', 10, 'bold'))
        F4_label.place(relx=0.592, rely=0.82, anchor='center')

    if verify4_list[0] < float(lower_value):
        F4_label = Label(page1Window, text=" F.S. ", bg='red', font=('calibre', 10, 'bold'))
        F4_label.place(relx=0.614, rely=0.82, anchor='center')
    else:
        F4_label = Label(page1Window, text=" F.S. ", bg='green', font=('calibre', 10, 'bold'))
        F4_label.place(relx=0.614, rely=0.82, anchor='center')

    # for f5
    if analyze_s["gender"] != analyze_f5["gender"]:
        F5_label = Label(page1Window, text="Gender", bg='red', font=('calibre', 10, 'bold'))
        F5_label.place(relx=0.67, rely=0.82, anchor='center')
    else:
        F5_label = Label(page1Window, text="Gender", bg='green', font=('calibre', 10, 'bold'))
        F5_label.place(relx=0.67, rely=0.82, anchor='center')

    if analyze_s["dominant_race"] != analyze_f5["dominant_race"]:
        F5_label = Label(page1Window, text="Race", bg='red', font=('calibre', 10, 'bold'))
        F5_label.place(relx=0.70, rely=0.82, anchor='center')
    else:
        F5_label = Label(page1Window, text="Race", bg='green', font=('calibre', 10, 'bold'))
        F5_label.place(relx=0.70, rely=0.82, anchor='center')

    if (analyze_s["age"] - 3 <= analyze_f5["age"]) and (analyze_f5["age"] <= analyze_s["age"] + 3):
        F5_label = Label(page1Window, text="Age", bg='green', font=('calibre', 10, 'bold'))
        F5_label.place(relx=0.722, rely=0.82, anchor='center')
    else:
        F5_label = Label(page1Window, text="Age", bg='red', font=('calibre', 10, 'bold'))
        F5_label.place(relx=0.722, rely=0.82, anchor='center')

    if analyze_s["dominant_emotion"] != analyze_f5["dominant_emotion"]:
        F5_label = Label(page1Window, text="F.E.", bg='red', font=('calibre', 10, 'bold'))
        F5_label.place(relx=0.742, rely=0.82, anchor='center')
    else:
        F5_label = Label(page1Window, text="F.E.", bg='green', font=('calibre', 10, 'bold'))
        F5_label.place(relx=0.742, rely=0.82, anchor='center')

    if verify5_list[0] < float(lower_value):
        F5_label = Label(page1Window, text=" F.S. ", bg='red', font=('calibre', 10, 'bold'))
        F5_label.place(relx=0.764, rely=0.82, anchor='center')
    else:
        F5_label = Label(page1Window, text=" F.S. ", bg='green', font=('calibre', 10, 'bold'))
        F5_label.place(relx=0.764, rely=0.82, anchor='center')

    # The Results

    distance_value1 = ''.join(str(x) for x in verify1_list)
    distance_value2 = ''.join(str(x) for x in verify2_list)
    distance_value3 = ''.join(str(x) for x in verify3_list)
    distance_value4 = ''.join(str(x) for x in verify4_list)
    distance_value5 = ''.join(str(x) for x in verify5_list)


    text_box.delete(1.0, 'end')
    text_box.insert('end', 'Model =' + model +'\nMetric =' + metric + '\n')
    text_box.insert('end', 'Lower value =' + str(lower_value))
    text_box.insert('end', '\n\n   ***** RESULTS *****\n\n**** Suspect ****\n')
    text_box.insert('end', str(analyze_s["gender"]) + ',' + str(analyze_s["dominant_race"]) + ',' + str(analyze_s["age"])+ ',' + str(analyze_s["dominant_emotion"]) + '\n**** Filler1 **** \n')
    text_box.insert('end', str(analyze_f1["gender"]) + ',' + str(analyze_f1["dominant_race"]) + ',' + str(analyze_f1["age"]) + ','+ str(analyze_f1["dominant_emotion"]) + '\n' )
    text_box.insert('end', 'Dstn:' + distance_value1)
    text_box.insert('end', '\n**** Filler 2 ****\n')
    text_box.insert('end', str(analyze_f2["gender"]) + ',' + str(analyze_f2["dominant_race"]) + ',' + str(analyze_f2["age"]) + ','+ str(analyze_f2["dominant_emotion"]) + '\n' )
    text_box.insert('end', distance_value2)
    text_box.insert('end', '\n**** Filler 3 ****\n')
    text_box.insert('end', str(analyze_f3["gender"]) + ',' + str(analyze_f3["dominant_race"]) + ',' + str(analyze_f3["age"]) + ','+ str(analyze_f3["dominant_emotion"]) + '\n' )
    text_box.insert('end', distance_value3)
    text_box.insert('end', '\n**** Filler 4 ****\n')
    text_box.insert('end', str(analyze_f4["gender"]) + ',' + str(analyze_f4["dominant_race"]) + ',' + str(analyze_f4["age"]) + ','+ str(analyze_f4["dominant_emotion"]) + '\n' )
    text_box.insert('end', distance_value4)
    text_box.insert('end', '\n**** Filler 5 ****\n')
    text_box.insert('end', str(analyze_f5["gender"]) + ',' + str(analyze_f5["dominant_race"]) + ',' + str(analyze_f5["age"]) + ','+ str(analyze_f5["dominant_emotion"]) + '\n')
    text_box.insert('end', distance_value5)
    text_box.insert('end', '\n***\n The results only which include only gender, race, age, facial expression '
                           'and facial similarity.'
                           'It was determined only the lower threshold for facial similarity.'
                           'Other features such as hair color, hairstyle, facial hair eye color'
                           ' are not included in the analysis.'
                           )


#Select Threshold Values

def set_threshold():
    global lower_value
    global upper_value
    lower_value = lower_value_input.get(1.0, END)
    upper_value = upper_value_input.get(1.0, END)
    Label(page1Window, text= lower_value, font=('calibre', 15, 'bold')).place(x=0, y=0, relx=0.19, rely=0.40)
    Label(page1Window, text= "< x < " + upper_value, font=('calibre', 15, 'bold')).place(x=0, y=0, relx=0.225, rely=0.40)

def threshold2():
    global lower_value_input
    global upper_value_input

    Label(page1Window, text= "Lower value").place(x=0, y=0, relx=0.11, rely=0.64)
    lower_value_input = Text(page1Window, height=1.4,width=7)
    lower_value_input.place(x=0, y=0, relx=0.11, rely=0.66)
    Label(page1Window, text="Upper value").place(x=0, y=0, relx=0.17, rely=0.64)
    upper_value_input = Text(page1Window,height=1.4,width=7)
    upper_value_input.place(x=0, y=0, relx=0.17, rely=0.66)
    set_threshold_button = Button(page1Window, text='Set', command=lambda: set_threshold())
    set_threshold_button.place(x=0, y=0, relx=0.21, rely=0.66)



#Settings Functions

def default_setting1():
    global lower_value
    global model
    global metric
    model = "VGG-Face"
    metric = "cosine"
    lower_value = 0.383
    print(lower_value)

def default_setting2():
    global lower_value
    global model
    global metric
    model = "Facenet"
    metric = "euclidean_l2"
    lower_value = 1.16
    print(lower_value)

def default_setting3():
    global lower_value
    global upper_value
    global model
    global metric
    model = "Facenet"
    metric = "euclidean_l2"
    lower_value = 0.955
    print(lower_value)

def model1():
    global model
    model = "VGG-Face"
    print(model)

def model2():
    global model
    model = "Facenet"
    print(model)

def metric1():
    global metric
    metric = "cosine"
    print(metric)

def metric2():
    global metric
    metric = "euclidean"
    print(metric)

def metric3():
    global metric
    metric = "euclidean_l2"
    print(metric)

# Create the window
page1Screen = Screen(conf.lineup_logo_main)
page1Window = page1Screen.getWindow()

# Put the small logo
background_image_small = ImageTk.PhotoImage(Image.open(conf.lineup_logo_small))
background_label_small = Label(page1Window, image=background_image_small)
background_label_small.place(x=0,y=0,relx=0.234,rely=0.05, anchor='ne')

# Photo Analyze information label
PAlabel_info = Label(page1Window,text="    Suspect-Filler Face Similarity Analyze Module   ",
                   font=('calibre', 17, 'bold'), borderwidth= 1, relief="solid").place(x=0,y=0,relx=0.35,rely=0.05)

set1_stand = Label(page1Window,text="", width= 74, height= 18,
                  relief="solid").place(x=0,y=0,relx=0.01,rely=0.20)

set2_stand = Label(page1Window,text="", width= 74, height= 15,
                   relief="solid").place(x=0,y=0,relx=0.01,rely=0.56)

# The button of availability analyzing

button_analyze_stage = Button(page1Window, text="Start Availability Analyzing",font=('calibre', 12, 'bold'),
                            command=lambda: handle_button_analyze_stage()).place(x=0, y=0, relx=0.10, rely=0.48)

# The button of face similarity analyzing

button_analyze_fs_stage = Button(page1Window, text="Start Face Similarity Analyzing",font=('calibre', 12, 'bold'),
                            command=lambda: handle_button_measurement_stage()).place(x=0, y=0, relx=0.09, rely=0.785)


# Put the label and button for image upload of the suspect for Analyze Function
suspect_place = Label(page1Window,text="Suspect", width = 15, height = 9,
                   font=('calibre', 17, 'bold'), borderwidth= 1, relief="solid").place(x=0,y=0,relx=0.35,rely=0.15)

S_label_file_explorer = Label(page1Window, text=conf.image_upload_text)
S_label_file_explorer.place(relx=0.42, rely=0.403, anchor='center')

S_button_explore_file = Button(page1Window, text=conf.button_file_browser_text,
                             command=lambda: S_handle_button_image_upload()).place(x=0,y=0,relx=0.39,rely=0.45)

filler1_place = Label(page1Window,text="1st Filler", width = 15, height = 9,
                   font=('calibre', 17, 'bold'), borderwidth= 1, relief="solid").place(x=0,y=0,relx=0.50,rely=0.15)

F1_label_file_explorer = Label(page1Window, text=conf.filler_image_upload_text)
F1_label_file_explorer.place(relx=0.57, rely=0.403, anchor='center')

F1_button_explore_file = Button(page1Window, text=conf.button_file_browser_text,
                             command=lambda: F1_handle_button_image_upload()).place(x=0, y=0, relx=0.565, rely=0.465,
                                                                                 anchor='center')

filler2_place = Label(page1Window,text="2nd Filler", width = 15, height = 9,
                   font=('calibre', 17, 'bold'), borderwidth= 1, relief="solid").place(x=0,y=0,relx=0.65,rely=0.15)

F2_label_file_explorer = Label(page1Window, text=conf.filler_image_upload_text)
F2_label_file_explorer.place(relx=0.72, rely=0.403, anchor='center')

F2_button_explore_file = Button(page1Window, text=conf.button_file_browser_text,
                             command=lambda: F2_handle_button_image_upload()).place(x=0, y=0, relx=0.72, rely=0.465,
                                                                                 anchor='center')

filler3_place = Label(page1Window,text="3rd Filler", width = 15, height = 9,
                   font=('calibre', 17, 'bold'), borderwidth= 1, relief="solid").place(x=0,y=0,relx=0.35,rely=0.54)

F3_label_file_explorer = Label(page1Window, text=conf.filler_image_upload_text)
F3_label_file_explorer.place(relx=0.42, rely=0.795, anchor='center')

F3_button_explore_file = Button(page1Window, text=conf.button_file_browser_text,
                             command=lambda: F3_handle_button_image_upload()).place(x=0, y=0, relx=0.42, rely=0.86,
                                                                                 anchor='center')

filler4_place = Label(page1Window,text="4th Filler", width = 15, height = 9,
                   font=('calibre', 17, 'bold'), borderwidth= 1, relief="solid").place(x=0,y=0,relx=0.50,rely=0.54)


F4_label_file_explorer = Label(page1Window, text=conf.filler_image_upload_text)
F4_label_file_explorer.place(relx=0.57, rely=0.795, anchor='center')

F4_button_explore_file = Button(page1Window, text=conf.button_file_browser_text,
                             command=lambda: F4_handle_button_image_upload()).place(x=0, y=0, relx=0.57, rely=0.86,
                                                                                 anchor='center')

filler5_place = Label(page1Window,text="5th Filler", width = 15, height = 9,
                   font=('calibre', 17, 'bold'), borderwidth= 1, relief="solid").place(x=0,y=0,relx=0.65,rely=0.54)

F5_label_file_explorer = Label(page1Window, text=conf.filler_image_upload_text)
F5_label_file_explorer.place(relx=0.72, rely=0.795, anchor='center')

F5_button_explore_file = Button(page1Window, text=conf.button_file_browser_text,
                             command=lambda: F5_handle_button_image_upload()).place(x=0, y=0, relx=0.72, rely=0.86,
                                                                                 anchor='center')

# The labels of settings

settings_label = Label(page1Window, text="Settings",
                    font=('calibre', 17, 'bold'))
settings_label.place(x=0, y=0, relx=0.14, rely=0.15)

info1_label = Label(page1Window, text="If you want to do availability analysis \nSelect one of the settings"
                   ,font=('calibre', 12, 'bold'))
info1_label.place(x=0, y=0, relx=0.075, rely=0.21)

info2_label = Label(page1Window, text="If you want to do only facial similaritiy analysis \nSelect one of the models and metrics"
                   ,font=('calibre', 12, 'bold'))
info2_label.place(x=0, y=0, relx=0.055, rely=0.57)

default_settings1_label = Label(page1Window, text="✔ Gender \n✔ Race \n✔ Age ± 3 \n✔ Facial Expression\nFacial Similarity (F.S.): \nModel = VGG Face \nMetric = Cosine  \nThreshold Value = 0.383"
                    ,justify=LEFT,font=('calibre', 11), borderwidth=1, relief="solid")
default_settings1_label.place(x=0, y=0, relx=0.015, rely=0.30)

default_settings2_label = Label(page1Window, text="✔ Gender \n✔ Race \n✔ Age ± 3 \n✔ Facial Expression\nFacial Similarity (F.S.): \nModel = Facenet \nMetric = Euclidean_l2  \nThreshold Values = 1.16"
                    ,justify=LEFT, font=('calibre', 11), borderwidth=1, relief="solid")
default_settings2_label.place(x=0, y=0, relx=0.12, rely=0.30)

default_settings2_label = Label(page1Window, text="✔ Gender \n✔ Race \n✔ Age ± 3 \n✔ Facial Expression\nFacial Similarity (F.S.): \nModel = Facenet \nMetric = Euclidean_l2  \nThreshold Values = 0.955"
                    ,justify=LEFT, font=('calibre', 11), borderwidth=1, relief="solid")
default_settings2_label.place(x=0, y=0, relx=0.225, rely=0.30)


#The raido buttons of settigns

y = IntVar()

radiobutton_default_1 = Radiobutton(page1Window, text="Setting 1", variable=y,
                           font=('calibre', 12, 'bold'),
                           command=lambda: default_setting1(), value=1)
radiobutton_default_1.place(x=0, y=0, relx=0.04, rely=0.26)

radiobutton_default_2 = Radiobutton(page1Window, text="Setting 2", variable=y,
                           font=('calibre', 12, 'bold'),
                           command= lambda: default_setting2(), value=2)
radiobutton_default_2.place(x=0, y=0, relx=0.14, rely=0.26)

radiobutton_default_3 = Radiobutton(page1Window, text="Setting 3", variable=y,
                           font=('calibre', 12, 'bold'),
                           command= lambda: default_setting3(), value=3)
radiobutton_default_3.place(x=0, y=0, relx=0.24, rely=0.26)

#Models
settings_label = Label(page1Window, text="Models",
                    font=('calibre', 12, 'bold'))
settings_label.place(x=0, y=0, relx=0.06, rely=0.65)

r = IntVar()

radiobutton_model_VGGFace = Radiobutton(page1Window, text="VGG Face", variable=r,
                           font=('calibre', 11),
                           command=lambda: model1(), value=1)
radiobutton_model_VGGFace.place(x=0, y=0, relx=0.05, rely=0.68)

radiobutton_model_Facenet = Radiobutton(page1Window, text="Facenet", variable=r,
                           font=('calibre', 11),
                           command=lambda: model2(), value=2)
radiobutton_model_Facenet.place(x=0, y=0, relx=0.05, rely=0.71)

#Metrics

settings_label = Label(page1Window, text="Metrics",
                    font=('calibre', 12, 'bold'))
settings_label.place(x=0, y=0, relx=0.23, rely=0.65)

y = IntVar()

radiobutton_metric_cosine = Radiobutton(page1Window, text="Cosine", variable=y,
                           font=('calibre', 11),
                           command=lambda: metric1(), value=1)
radiobutton_metric_cosine.place(x=0, y=0, relx=0.22, rely=0.68)

radiobutton_metric_euclidean = Radiobutton(page1Window, text="Euclidean", variable=y,
                           font=('calibre', 11),
                           command=lambda: metric2(), value=2)
radiobutton_metric_euclidean.place(x=0, y=0, relx=0.22, rely=0.71)

radiobutton_metric_euclidean_l2 = Radiobutton(page1Window, text="Euclidean_l2", variable=y,
                           font=('calibre', 11),
                           command=lambda: metric3(), value=3)
radiobutton_metric_euclidean_l2.place(x=0, y=0, relx=0.22, rely=0.74)


#The textbox of the result

message = '''*** Welcome to the analysis module of the L(i)ne-up app.
        \n\n Please select one of the 1-2-3 settings and click the button to do a availability analysis.
        \n\n If you only want to analyze the similarity with the facial recognition model, please select the model and metric you want to use and press the button.
        \n\n You can see the results which is calculated through Deepface Framework in this field in about a minute ***
        \n\n L(i)ne-up application is an experimental project and the results have no legal validity. For more information about the white paper and L(i)ne-up project, see https://github.com/DervisEmreAydin'
'''

text_box = Text(page1Window,height=35,width=30, wrap='word')
text_box.place(x=0, y=0, relx=0.87, rely=0.486,anchor='center')
text_box.insert('end', message)


# Keep the window open
page1Window.mainloop()
