import PySimpleGUI as sg
import numpy as np
from numpy import linalg
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


sg.theme('Light Brown 3')
layout = [
 [sg.Text('Chose what are expected isotopes (max.6):', font='Helvetica 11', size = (33,1)), sg.VerticalSeparator(pad=None), sg.Text('', size = (2,1)), sg.Text('Enter detector`s response:', font='Helvetica 11')],
 [sg.Checkbox('125I',size = (15,1), key='125I'), sg.Checkbox('44Ti',size = (15,1), key='44Ti'), sg.VerticalSeparator(pad=None), sg.Text('', size = (2,1)), sg.Text('YAG', size = (6,1)), sg.Input('', size = (10,1), key='YAG')],
 [sg.Checkbox('133Xe',size = (15,1), key='133Xe'), sg.Checkbox('243Am',size = (15,1), key='243Am'), sg.VerticalSeparator(pad=None), sg.Text('', size = (2,1)), sg.Text('YAP', size = (6,1)), sg.Input('', size = (10,1), key='YAP')],
 [sg.Checkbox('67Ga (39%)',size = (15,1), key='67Ga (39%)'), sg.Checkbox('133Ba',size = (15,1), key='133Ba'), sg.VerticalSeparator(pad=None), sg.Text('', size = (2,1)), sg.Text('YAM', size = (6,1)), sg.Input('', size = (10,1), key='YAM')],
 [sg.Checkbox('178Ta',size = (15,1), key='178Ta'), sg.Checkbox('153Gd(1) (97.4)',size = (15,1), key='153Gd(1)'), sg.VerticalSeparator(pad=None), sg.Text('', size = (2,1)), sg.Text('Y2O3', size = (6,1)), sg.Input('', size = (10,1), key='Y2O3')],
 [sg.Checkbox('99mTc',size = (15,1), key='99mTc'), sg.Checkbox('153Gd(2) (103.2)',size = (15,1), key='153Gd(2)'), sg.VerticalSeparator(pad=None), sg.Text('', size = (2,1)), sg.Text('Al2O3', size = (6,1)), sg.Input('', size = (10,1), key='Al2O3')],
 [sg.Checkbox('123I',size = (15,1), key='123I'), sg.Checkbox('152Eu',size = (15,1), key='152Eu'), sg.VerticalSeparator(pad=None), sg.Text('', size = (2,1)), sg.Text('BeO', size = (6,1)), sg.Input('', size = (10,1), key='BeO')],
 [sg.Checkbox('111In',size = (15,1), key='111In'), sg.Checkbox('57Co',size = (15,1), key='57Co'), sg.VerticalSeparator(pad=None)],
 [sg.Checkbox('67Ga (21%)',size = (15,1), key='67Ga (21%)'), sg.Checkbox('139Ce',size = (15,1), key='139Ce'), sg.VerticalSeparator(pad=None)],
 [sg.Checkbox('81mKr',size = (15,1), key='81mKr'), sg.Checkbox('109Cd', size=(15,1), key='109Cd'), sg.VerticalSeparator(pad=None)],
 [sg.Button('Submit'), sg.Button('Clear'), sg.Button('Save'), sg.Button('Exit')],
 [sg.Canvas(key='-CANVAS-')]
]



def iso_value(values):
    iso_list = []
    if values['125I'] is True:
        iso_list.append('125I')
    if values['133Xe'] is True:
        iso_list.append('133Xe')
    if values['67Ga (39%)'] is True:
        iso_list.append('67Ga (39%)')
    if values['178Ta'] is True:
        iso_list.append('178Ta')
    if values['99mTc'] is True:
        iso_list.append('99mTc')
    if values['123I'] is True:
        iso_list.append('123I')
    if values['111In'] is True:
        iso_list.append('111In')
    if values['67Ga (21%)'] is True:
        iso_list.append('67Ga (21%)')
    if values['81mKr'] is True:
        iso_list.append('81mKr')
    if values['44Ti'] is True:
        iso_list.append('44Ti')
    if values['243Am'] is True:
        iso_list.append('243Am')
    if values['133Ba'] is True:
        iso_list.append('133Ba')
    if values['109Cd'] is True:
        iso_list.append('109Cd')
    if values['153Gd(1)'] is True:
        iso_list.append('153Gd(1)')
    if values['152Eu'] is True:
        iso_list.append('152Eu')
    if values['57Co'] is True:
        iso_list.append('57Co')
    if values['139Ce'] is True:
        iso_list.append('139Ce')
    if values['153Gd(2)'] is True:
        iso_list.append('153Gd(2)')
    return iso_list               # filling V list from dictionaries YAG, YAP...

def linear (Flist,Rlist):
    F = np.array(Flist)
    R = np.array(Rlist)
    I = linalg.solve(F,R)
    return I            # resolve system of linear equations

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='x', expand=True)
    return figure_canvas_agg   # ploting diagram

def delete_figure(figure):
    figure.get_tk_widget().forget()
    plt.close('all')   # clearing canvas

window = sg.Window('Isotopes determination', layout, size=(600, 700))
box = {}
fcount = 1
while True:
    event, values = window.read()
    box.update(values)

    F = []          # matrix of relative sensitivities values
    R = []          # detector energy response
    V = iso_value(values)    # list of isotopes which are used
    print ("V-list", V)
    if box['YAG'] != '':
        R_YAG=R.append(float(box['YAG']))
        YAG = {'125I': '22.232', '133Xe': '22.981', '67Ga (39%)': '16.669', '178Ta': '16.669', '99mTc': '5.606', '123I': '4.166', '111In': '3.482', '67Ga (21%)': '2.996', '81mKr': '2.783', '44Ti': '30.19', '243Am': '26.564', '133Ba': '22.98', '109Cd': '18.899', '153Gd(1)': '14.769', '153Gd(2)': '12.767', '152Eu': '8.17', '57Co': '6.072', '139Ce': '3.782'}
        lin_YAG = []
        for i1 in V:
            lin_YAG.append(float(YAG[i1]))
        F.append(lin_YAG)
    if box['YAP'] != '':
        R_YAP=R.append(float(box['YAP']))
        YAP = {'125I': '19.67', '133Xe': '26.022', '67Ga (39%)': '19.186', '178Ta': '19.186', '99mTc': '6.508', '123I': '4.804', '111In': '4.005', '67Ga (21%)': '3.415', '81mKr': '3.156', '44Ti': '33.257', '243Am': '29.68', '133Ba': '26.02', '109Cd': '21.644', '153Gd(1)': '17.084', '153Gd(2)': '14.805', '152Eu': '9.492', '57Co': '7.054', '139Ce': '4.356'}
        lin_YAP = []
        for i2 in V:
            lin_YAP.append(float(YAP[i2]))
        F.append(lin_YAP)
    if box['YAM'] != '':
        R_YAM=R.append(float(box['YAM']))
        YAM = {'125I': '23.333', '133Xe': '30.559', '67Ga (39%)': '22.382', '178Ta': '22.382', '99mTc': '7.46', '123I': '5.466', '111In': '4.521', '67Ga (21%)': '3.828', '81mKr': '3.524', '44Ti': '39.124', '243Am': '34.855', '133Ba': '30.507', '109Cd': '25.294', '153Gd(1)': '19.895', '153Gd(2)': '17.213', '152Eu': '10.948', '57Co': '8.098', '139Ce': '4.935'}
        lin_YAM = []
        for i3 in V:
            lin_YAM.append(float(YAM[i3]))
        F.append(lin_YAM)
    if box['Y2O3'] != '':
        R_Y2O3=R.append(float(box['Y2O3']))
        Y2O3 = {'125I': '21.163', '133Xe': '34.753', '67Ga (39%)': '25.972', '178Ta': '25.972', '99mTc': '8.779', '123I': '6.407', '111In': '5.267', '67Ga (21%)': '4.442', '81mKr': '4.08', '44Ti': '43.128', '243Am': '39.155', '133Ba': '34.75', '109Cd': '29.165', '153Gd(1)': '23.235', '153Gd(2)': '20.195', '152Eu': '12.946', '57Co': '9.536', '139Ce': '5.767'}
        lin_Y2O3 = []
        for i4 in V:
            lin_Y2O3.append(float(Y2O3[i4]))
        F.append(lin_Y2O3)
    if box['Al2O3'] != '':
        R_Al2O3=R.append(float(box['Al2O3']))
        Al2O3 = {'125I': '3.477', '133Xe': '1.714', '67Ga (39%)': '1.477', '178Ta': '1.477', '99mTc': '1.12', '123I': '1.071', '111In': '1.055', '67Ga (21%)': '1.039', '81mKr': '1.033', '44Ti': '2.091', '243Am': '1.888', '133Ba': '1.714', '109Cd': '1.561', '153Gd(1)': '1.406', '153Gd(2)': '1.346', '152Eu': '1.212', '57Co': '1.138', '139Ce': '1.062'}
        lin_Al2O3 = []
        for i5 in V:
            lin_Al2O3.append(float(Al2O3[i5]))
        F.append(lin_Al2O3)
    if box['BeO'] != '':
        R_BeO=R.append(float(box['BeO']))
        BeO = {'125I': '0.773', '133Xe': '0.917', '67Ga (39%)': '0.932', '178Ta': '0.932', '99mTc': '0.954', '123I': '0.958', '111In': '0.959', '67Ga (21%)': '0.959', '81mKr': '0.959', '44Ti': '0.89', '243Am': '0.904', '133Ba': '0.916', '109Cd': '0.927', '153Gd(1)': '0.937', '153Gd(2)': '0.941', '152Eu': '0.949', '57Co': '0.953', '139Ce': '0.959'}
        lin_BeO = []
        for i6 in V:
            lin_BeO.append(float(BeO[i6]))
        F.append(lin_BeO)
    energy = {'125I': '35', '133Xe': '80.997', '67Ga (39%)': '93',
    '178Ta': '93', '99mTc': '140.511', '123I': '159', '111In': '171.29',
    '67Ga (21%)': '184', '81mKr': '190', '44Ti': '68.9', '243Am': '74.7',
     '133Ba': '81', '109Cd': '88', '153Gd(1)': '97.4', '153Gd(2)': '103.2',
     '152Eu': '121.78', '57Co': '136.5', '139Ce': '165.9'}       # energy of each iso
    I = linear(F,R)


    energy_val = []
    for e in V:
        energy_val.append(energy[e])
    print ("energy_val",energy_val)
    labels = []
    for l in range(0,len(V)):
        labels.append(V[l]+", "+energy_val[l])
    print("labels", labels)

    print("F-matrix",F)
    print("R-Vector",R)
    print(I)
    print("V-list", V)
    res=np.allclose(np.dot(F, I), R)
    print(res)

    if event == 'Submit':
        x_pos = np.arange(len(V))
        plt.bar(x_pos, I, align='center', alpha=0.5)
        plt.xticks(x_pos, labels, rotation=12)
        plt.ylabel('Інтенсивність')
        plt.title('Джерело випромінювання та Е,кеВ')
        fig = plt.gcf()
        fig_photo = draw_figure(window['-CANVAS-'].TKCanvas, fig)
    if event == "Save":
        fname = str(fcount)+"_Chart"
        plt.savefig(fname)
    if event == 'Clear':
        delete_figure(fig_photo)
        fcount +=1
    if event in ('Exit', None):
        break
