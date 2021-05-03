# -*- coding: utf-8 -*-

import datetime
import calendar
import random
import time

from flask import Flask, request, render_template
import random

app = Flask(__name__)


@app.route('/')
def home():
    kuu_list = ["jaanuar", "veebruar", "m2rts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    aasta_list = [2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,2031,2032,2033,2034,2035]
    t66tajate_arv = [1,2,3,4,5,6,7,8,9,10,11,12]
    
    return render_template("home.html",kuu_list = kuu_list, aasta_list = aasta_list, t66tajate_arv = t66tajate_arv)

@app.route('/tulem', methods=["POST"])
def transformed():
    text = request.form['text']

    ffe = "kala"
    print(text,type(text))
  
    input_l = text.split("\r")
    input_l2 = []
    for i in input_l:
        if len(i) > 3:
            input_l2.append(i.replace("\n",""))

    t66tajate_ei_p2evad = {}
    for i in input_l2:
        print(i)
        nimi = str(i.split(":")[0])
        ei_p2evad = i.split(":")[1]
        ei_p2evad_lst = []
        #[ei_p2evad_lst.append(int(m)) for m in ei_p2evad.split(",")]
        if len(ei_p2evad) == 0:
            ei_p2evad_lst.append((random.randint(1,28)))
        else:
            [ei_p2evad_lst.append(int(m)) for m in ei_p2evad.split(",")]     
        
        t66tajate_ei_p2evad[nimi] = ei_p2evad_lst
    
        #exec("t66tajate_ei_p2evad['{}'] = [{}]".format(i.split(":")[0],i.split(":")[1]))
    
    print(t66tajate_ei_p2evad)

    kuu = request.form['kuu']
    kuu = str(kuu)

    present_year = request.form['aasta']
    present_year = int(present_year)

    t66p2val_t66tajaid = request.form["n2d_sees"]
    t66p2val_t66tajaid = int(t66p2val_t66tajaid)
       
    n2dalavahetusel_t66tajaid = request.form["n2d_vahetus"]
    n2dalavahetusel_t66tajaid = int(n2dalavahetusel_t66tajaid)

    print(kuu,present_year)
    print(type(kuu))
    print(type(present_year))
    print(type(t66p2val_t66tajaid))
    print(type(n2dalavahetusel_t66tajaid))

    # loome listi, kus on esindatud k6ik kalendrikuud
    kuu_list = ["jaanuar", "veebruar", "m2rts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]

    # iga kalendrikuu lyhendiga loome omakorda vastava kuu kuup2evadega listi, mille sees onakorda listid (n2dalad)
    kuu_number = 1
    for i in kuu_list:
        #print('{} = calendar.monthcalendar(present_year, {})'.format(i,kuu_number))
        exec('{} = calendar.monthcalendar(present_year, {})'.format(i,kuu_number))
        kuu_number += 1
        
    # kuu_list_n_p2evadega = ["jan_p", "veb_p", "m2r_p", "apr_p", "mai_p", "jun_p", 
    #... "jul_p", "aug_p", "sep_p", "okt_p", "nov_p", "det_p"]
    jooksev_kuu_p2evad = []
    n2dal_p2evad = ["E","T","K","N","R","L","P"]
    # funktsioon, mis paneb kuup2eva ja n2dalap2eva kokku

    # jooksva_kuu_p2evad = kuu_ja_n2dalap2ev(jul)
    exec("jooksva_kuu_p2evad = kuu_ja_n2dalap2ev({})".format(kuu))

    # print(jooksva_kuu_p2evad)    


    # arvutame, mitu reedet, laup2eva ja pyhap2eva on antud kuu jooksul
    nv_p2ev_arv = 0
    for i in jooksva_kuu_p2evad:
        if "R" in i or "L" in i or "P" in i:
            nv_p2ev_arv += 1

    # loome igale kuup2va nimelise tyhja listi
    for i in jooksva_kuu_p2evad:
        exec('{} = []'.format(i))


    jooksva_kuu_p2evad_bingo = []
    # Vaatame, mitu t66tajat peaks olema t66p2eval t66l, ning lisame niimitu p2eva bingo listi
    for i in range(0,t66p2val_t66tajaid):
        for i in jooksva_kuu_p2evad:
            if "E" in i or "T" in i or "K" in i or "N" in i:
                jooksva_kuu_p2evad_bingo.append(i)
    # Vaatame, mitu t66tajat peaks olema n2dalavahetusel  t66l, ning lisame niimitu p2eva bingo listi
    for i in range(0,n2dalavahetusel_t66tajaid):
        for i in jooksva_kuu_p2evad:
            if "R" in i or "L" in i or "P" in i:
                jooksva_kuu_p2evad_bingo.append(i)
            
    vahe_v2ikseim = []

    # Loome funktsiooni, millega on h6lbus j2rjestada n2dalap2evade_ja_kuup2evade listi
    # Loome listi, kuhu sisse paneme iga graafiku genereerimise j2rel probleemsete p2evade aru,
    # kui tehakse umbes 30-100 (miks mitte rohkem) genereerimist, vaadatakse mis on väikseim probleemsete p2vade arv;
    # ning kui j2rmine kord saadakse see sama v2ikseim probleene arv, lopetatakse genereerimine
    problm_paeva_loendur = []
    start = time.time()
    
    for kordaja in range(0,150):
        #for i in range(0,2):
            #random.shuffle(jooksva_kuu_p2evad_bingo)
        jooksva_kuu_p2evad_bingo.sort(key=take_second)
    
        # loome iga t66taja nimelise listi
        for i in list(t66tajate_ei_p2evad.keys()):
            exec("{} = []".format(i))
        # Loome listi, kus sees puhtalt t66tajad
        t66tajate_list = []
        for i in t66tajate_ei_p2evad.keys():
            t66tajate_list.append(i)
        
        # segame töötajte listi ära
        random.shuffle(t66tajate_list)
    
        # J2rgnevalt saame t66tajaid j2rjesteda selle j2rgi kui palju neil parasjagu t66p2evi listis on, 
        # mida v2hem p2evi - seda rohkem eespool
        sorting_list = []
        for i in t66tajate_list:
            exec("sorting_list.append(['{}',len({})])".format(i,i))

        # j2rgneva lambda funktsiooniga saab panna j2jrestama sorting_list-i
        #sorting_list.sort(key=lambda x: x[1])
        #[print(e[0],e[1]) for e in sorting_list]
    
        # teeme listi, kuhu lisada probleemsed kuup2evad, mida on keeruline sobitada graafikusse
        # graafikut genereeritakse uuesti, eesm2rgiga et probleemsed p2evi on voimalikult v2he, voi yldse pole
        prob_p2evad = []
        #print(jooksva_kuu_p2evad_bingo)
        # J2rvnevalt k2ime l2bi iga itemi bingo listis ja proovime panna neid itmeid t66tajte erinevatesse listidesse
        for num, i in enumerate(jooksva_kuu_p2evad_bingo):
            lisatud = 0
            # alumine list on vabade p2evade markeerimiseks; lisatakse kolm eelnevat kuup2eva listi
            vbd_p2evd, vbd_p2evd2 = [], []
            vbd_p2evd.append(int(i[1:])-1)
            vbd_p2evd.append(int(i[1:])-2)
            vbd_p2evd.append(int(i[1:])-3)
        
            vbd_p2evd2.append(int(i[1:])-2)
            vbd_p2evd2.append(int(i[1:])-3)
            vbd_p2evd2.append(int(i[1:])-4)    

            #print(i[1:])
            
            sorting_list = []
            for m in t66tajate_list:
                exec("sorting_list.append(['{}',len({})])".format(m,m))
            # j2rjestame t66tate listi iga paaris kuup2eva tagant
            #if int(i[1:]) % 2 != 0:
            sorting_list.sort(key=lambda x: x[1])
            esimene = sorting_list[0][0]
            # tootaja_list-i loome, et saaksime vaadata mis p2evad antud t66taja listis juba on
            exec("tootaja_list = {}".format(esimene))
            #if len(tootaja_list) == 0:
                #tootaja_list.append(100)
            #print(esimene)
            #print(type(tootaja_list))
            #print(len(tootaja_list))
            # vaatame, kas ei i ei ole ei p2evade listis, kui on siis ei lisa talle seda t66p2eva; ja ega
            # t66taja pole juba m22ratud antud p2eval t66d tegema
            # ning vaatame, ega t66tajal pole eelnevalt 3 j2rjestikkust t66p2eva
            #print(t66tajate_ei_p2evad[esimene])
            
            if int(i[1:]) not in t66tajate_ei_p2evad[esimene] and int(i[1:]) not in tootaja_list:
                #break
                #print(tootaja_list)
                #print(vbd_p2evd)
                #if all(x in tootaja_list for x in vbd_p2evd) == False:
                    #print("ff")
                    #if all(x in tootaja_list for x in vbd_p2evd2) == False:
                        #break
                ck1 = []
                for g in tootaja_list:
                    if g in vbd_p2evd or g in vbd_p2evd2:
                        ck1.append(1)        
                
                if len(ck1) < 3:
                    exec("{}.append({})".format(esimene,int(i[1:])))    
                    lisatud = 1
                
            # allolev 'if' on loodud, et kui esimese korraga ei saa t66tajale p2eva m22rata, proovitakse m22rata
            # teistele t66tajatele; koik t66tajad loop-itakse l2bi, ja kui ikka ei saa voetakse ette kolmas 'if'
            if lisatud == 0:
                f = 0
                while f < len(t66tajate_list)-1:
                    f = f + 1
                    esimene = sorting_list[f][0]
                    exec("tootaja_list = {}".format(esimene))
                    if int(i[1:]) not in t66tajate_ei_p2evad[esimene] and int(i[1:]) not in tootaja_list:
                        
                        ck2 = []
                        for g in tootaja_list:
                            if g in vbd_p2evd or g in vbd_p2evd2:
                                ck2.append(1)  

                        if len(ck2) < 3:
                            exec("{}.append({})".format(esimene,int(i[1:])))    
                            lisatud = 1
                            break

                        '''
                        if all(x in tootaja_list for x in vbd_p2evd) == False:
                            if all(x in tootaja_list for x in vbd_p2evd2) == False:
                                
                                exec("{}.append({})".format(esimene,int(i[1:])))
                                lisatud = 1
                                #print(int(i[1:]),vbd_p2evd,vbd_p2evd2,tootaja_list,esimene)
                                break
                        '''
            
            if lisatud == 0:
                prob_p2evad.append(int(i[1:]))
                #exec("print('{}')".format("ei koiki p2evi 2ra jagada"))
                #print(esimene)  
                
        sorting_list.sort(key=lambda x: x[1])
        enim = sorting_list[-1][1]
        v2him = sorting_list[0][1]
        vahe = enim-v2him
        #print(vahe)
        vahe_v2ikseim.append(vahe)

        problm_paeva_loendur.append(len(prob_p2evad))
        #print(prob_p2evad)
        #print("kk\n")
        if kordaja > 80:
            if len(prob_p2evad) == sorted(problm_paeva_loendur)[0] and vahe == min(vahe_v2ikseim):
                break

    print(prob_p2evad)
    print(min(vahe_v2ikseim))            
    print(kordaja)

    t66tajate_t66p2evad = {}

    for i in list(t66tajate_ei_p2evad.keys()):
        exec("t66tajate_t66p2evad[i] = {}".format(i))

    print(t66tajate_t66p2evad)
    with open("/var/www/html/graafikud_d97LjZsUj9j1/el_graafik.csv","w") as ef:
        ef.write('"{}"'.format(kuu))
        for i in t66tajate_t66p2evad:
            ef.write(',"{}"'.format(i))
    
        ef.write("\n")

        for i in range(len(jooksva_kuu_p2evad)):
            ef.write('"{}"'.format(jooksva_kuu_p2evad[i]))

            
            for m in range(len(t66tajate_t66p2evad)):
                #print(t66tajate_ei_p2evad[list(t66tajate_ei_p2evad.keys())[m]])
            
                if i+1 in t66tajate_t66p2evad[list(t66tajate_t66p2evad.keys())[m]]:
                    ef.write(',"T"')
                    #ef.write(',"T{}-{}"'.format(t6,p))
                    #t6 +=1
                    
                if i+1 in t66tajate_ei_p2evad[list(t66tajate_ei_p2evad.keys())[m]]:
                    ef.write(',"Ei"')
                    #ef.write(',"Ei{}-{}"'.format(EI,p))                 
                    #EI +=1
                
                if i+1 not in t66tajate_t66p2evad[list(t66tajate_t66p2evad.keys())[m]] and i+1 not in t66tajate_ei_p2evad[list(t66tajate_ei_p2evad.keys())[m]]:
                    ef.write(',""')
                    #ef.write(',"Nil{}-{}"'.format(NO,p))
                    #NO +=1
    
                #p +=1      
            
            ef.write("\n") 

    ffe = prob_p2evad
    
    #graafikud_d97LjZsUj9j1/el_graafik.csv
    try:                   
        return render_template("results.html",
        #output = text)
        output = ffe)
    except:
        return("Midagi läks valesti, palun kontrollige kas kõik väljad said valitud(kuu, aasta jne)")

def kuu_ja_n2dalap2ev(kuu):
    jooksev_kuu_p2evad = []
    n2dal_p2evad = ["E","T","K","N","R","L","P"]
    for i in kuu:
        for n in range(0,7):
            if i[n] != 0:
                #kp_np = "{}{}".format(i[n],n2dal_p2evad[n])
                kp_np = "{}{}".format(n2dal_p2evad[n],i[n])
                #print(kp_np)
                #print("efe")
                jooksev_kuu_p2evad.append(kp_np)
    return(jooksev_kuu_p2evad)
                #exec("{}_p.append(kp_np)".format(str(kuu)))
                #print("{}{}".format(i[n],n2dal_päevad[n]))


# Loome funktsiooni, millega on h6lbus j2rjestada n2dalap2evade_ja_kuup2evade listi
def take_second(elem):
    return int(elem[1:])




    
if __name__ == '__main__':
  app.run()
