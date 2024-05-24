import numpy as np
import random as rd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

'''Nombres d'élèves : Ne
Filères :
    Info= GI
    Maths Info= GMI
    Maths FI= GMF
Dictionnaire élèves : Student
Pour les GI -> General= Maths / Spé=info
Pour les GMI -> General =matiere maths info / Spe=matiere GMI
Pour les GMF->General= matiere maths info /Spe=matiere GMF
'''

Ne=168
Student={}
prenoms= ["Emma", "Liam", "Olivia", "Noah", "Ava", "William", "Isabella", "James", "Sophia", "Logan",
           "Mia", "Benjamin", "Charlotte", "Mason", "Amelia", "Elijah", "Harper", "Oliver", "Evelyn", "Jacob",
           "Abigail", "Michael", "Emily", "Alexander", "Elizabeth", "Ethan", "Avery", "Daniel", "Sofia", "Matthew",
           "Ella", "Henry", "Madison", "Sebastian", "Scarlett", "Jackson", "Victoria", "Aiden", "Aria", "Samuel",
           "Grace", "David", "Chloe", "Joseph", "Camila", "Carter", "Penelope", "Owen", "Luna", "Wyatt", "Layla",
           "John", "Riley", "Jack", "Zoey", "Luke", "Nora", "Jayden", "Lily", "Dylan", "Mila", "Grayson", "Hannah",
           "Levi", "Lillian", "Gabriel", "Addison", "Julian", "Ellie", "Mateo", "Stella", "Anthony", "Natalie",
           "Jaxon", "Zoe", "Lincoln", "Leah", "Joshua", "Willow", "Christopher", "Hazel", "Andrew", "Violet",
           "Theodore", "Aurora", "Caleb", "Savannah", "Ryan", "Audrey", "Asher", "Brooklyn", "Nathan", "Bella",
           "Thomas", "Claire","Yannis","Adele","Philippine","Ademe","Stanislas","Celeste"]
noms= ["Martin", "Bernard", "Dubois", "Thomas", "Robert", "Richard", "Petit", "Durand", "Leroy", "Moreau",
                "Simon", "Laurent", "Lefebvre", "Michel", "Garcia", "David", "Bertrand", "Roux", "Vincent", "Fournier",
                "Morel", "Girard", "Andre", "Lefevre", "Mercier", "Dupont", "Lambert", "Bonnet", "Francois", "Martinez",
                "Legrand", "Garnier", "Faure", "Rousseau", "Blanc", "Guerin", "Muller", "Henry", "Roussel", "Nicolas",
                "Perrin", "Morin", "Gauthier", "Maillard", "Perez", "Marchand", "Dumas", "Joly", "Denis", "Colin",
                "Dufour", "Lemaire", "Vidal", "Brun", "Chevalier", "Leclerc", "Gautier", "Benoit", "Antoine", "Fernandez",
                "Lopez", "Robin", "Gillet", "Fabre", "Renard", "Masson", "Meyer", "Gonzalez", "Gallet", "Philippe",
                "Leclercq", "Boucher", "Giraud", "Huet", "Jacquet", "Lemaître", "Caron", "Barbier", "Bertin", "Descamps",
                "Collet", "Poirier", "Perez", "Guillaume", "Lucas", "Voisin", "Rolland", "Pascal", "Leconte", "Rodriguez",
                "Vasseur", "Hubert", "Lebrun", "Da silva", "Gay","Lopes","Silva Da Costa","Quellec","Sebilleau","Dumont"]

orientation_GI=["IA","CyberSecurite","InfoEmbarque","VisualComputing"]

orientation_GMI=["DataScience","FinTech","DataAnal"]

orientation_GMF=["Actuariat","IngFinance","MMF"]

matiere_humanite=["Anglais","Ethique","Gestion"]

matiere_GI_Info=["DevWeb","ProgramObjet","Java"]

matiere_GI_Maths=["OptiLin","AlgoProc","Proba"]

matiere_GM_MathsInfo=["Java","DevWeb","Proba"]

matiere_GMF=["Topologie","EquaDiff","Opti"]

matiere_GMI=["Datamining","Graph","AnalNum"]

def Filiere(Ne,Student):
    Ne=len(Student)
    for i in range (0,Ne):
        p=rd.randint(1,3)
        if (p==1):
            Student[i+1]["Filiere"]="GI"
        elif (p==2):
            Student[i+1]["Filiere"]="GMI"
        elif (p==3):
            Student[i+1]["Filiere"]="GMF"
    return Student

def Nommer(Ne,Student):
    Ne=len(Student)
    for i in range (1,Ne+1):
        p1=rd.randint(0,99)
        p2=rd.randint(0,99)
        Student[i]["prenom"]=prenoms[p1]
        Student[i]["nom"]=noms[p2]
    return Student

def Voeu(Ne,Student):
    Ne=len(Student)
    for i in range(1,Ne+1):
        if (Student[i]["Filiere"]=="GI"):
            p=rd.randint(1,2)
            if (p==1):
                Student[i]["Voeu1"]=orientation_GI[0]
                Student[i]["Voeu2"]=orientation_GI[1]
                Student[i]["Voeu3"]=orientation_GI[2]
            else:
                L=[0,1,2,3]
                rd.shuffle(L)
                Student[i]["Voeu1"]=orientation_GI[L[0]]
                Student[i]["Voeu2"]=orientation_GI[L[1]]
                Student[i]["Voeu3"]=orientation_GI[L[2]]
        elif (Student[i]["Filiere"]=="GMI"):
            p=rd.randint(1,2)
            if (p==1):
                Student[i]["Voeu1"]=orientation_GMI[1]
                Student[i]["Voeu2"]=orientation_GMI[0]
                Student[i]["Voeu3"]=orientation_GMI[2]
            else:
                L=[0,1,2]
                rd.shuffle(L)
                Student[i]["Voeu1"]=orientation_GMI[L[0]]
                Student[i]["Voeu2"]=orientation_GMI[L[1]]
                Student[i]["Voeu3"]=orientation_GMI[L[2]]
        elif (Student[i]["Filiere"]=="GMF"):
            p=rd.randint(1,2)
            if (p==1):
                Student[i]["Voeu1"]=orientation_GMF[2]
                Student[i]["Voeu2"]=orientation_GMF[0]
                Student[i]["Voeu3"]=orientation_GMF[1]
            else:
                L=[0,1,2]
                rd.shuffle(L)
                Student[i]["Voeu1"]=orientation_GMF[L[0]]
                Student[i]["Voeu2"]=orientation_GMF[L[1]]
                Student[i]["Voeu3"]=orientation_GMF[L[2]]
    return Student

def RemplissageNote(Ne,Student):
    Ne=len(Student)
    for i in range(1,Ne+1):
        if (Student[i]["Filiere"]=="GI"):
            #Humanités
            for j in range (0,3):
                note=-1
                while (note<0) or (note>20):
                    note=rd.normalvariate(10.5, 5)
                Student[i]["Humanite"][matiere_humanite[j]]=note
            #GI maths
            for j in range (0,3):
                note=-1
                while (note<0) or (note>20):
                    note=rd.normalvariate(10.5, 5)
                Student[i]["General"][matiere_GI_Maths[j]]=note
            #GI info
            for j in range (0,3):
                note=-1
                while (note<0) or (note>20):
                    note=rd.normalvariate(10.5, 5)
                Student[i]["Spe"][matiere_GI_Info[j]]=note
        if (Student[i]["Filiere"]=="GMI"):
            #humanités
            for j in range (0,3):
                note=-1
                while (note<0) or (note>20):
                    note=rd.normalvariate(10.5, 5)
                Student[i]["Humanite"][matiere_humanite[j]]=note
            #GMI Maths info
            for j in range (0,3):
                note=-1
                while (note<0) or (note>20):
                    note=rd.normalvariate(10.5, 5)
                Student[i]["General"][matiere_GM_MathsInfo[j]]=note
            #GMI info
            for j in range (0,3):
                note=-1
                while (note<0) or (note>20):
                    note=rd.normalvariate(10.5, 5)
                Student[i]["Spe"][matiere_GMI[j]]=note
        if (Student[i]["Filiere"]=="GMF"):
            #humanités
            for j in range (0,3):
                note=-1
                while (note<0) or (note>20):
                    note=rd.normalvariate(10.5, 5)
                Student[i]["Humanite"][matiere_humanite[j]]=note
            #GMI Maths info
            for j in range (0,3):
                note=-1
                while (note<0) or (note>20):
                    note=rd.normalvariate(10.5, 5)
                Student[i]["General"][matiere_GM_MathsInfo[j]]=note
            #GMI info
            for j in range (0,3):
                note=-1
                while (note<0) or (note>20):
                    note=rd.normalvariate(10.5, 5)
                Student[i]["Spe"][matiere_GMF[j]]=note
    return Student

def Moyenne(Ne,Student):
    Ne=len(Student)
    for i in range(1,Ne+1):
        m=0
        for j in range(0,3):
            m=m+Student[i]["Humanite"][matiere_humanite[j]]
        Student[i]["Humanite"]["Moy"]=m/3
        m=0
        if (Student[i]["Filiere"]=="GI"):
            for j in range(0,3):
                m=m+Student[i]["General"][matiere_GI_Maths[j]]
                Student[i]["General"]["Moy"]=m/3
        else:
            for j in range(0,3):
                m=m+Student[i]["General"][matiere_GM_MathsInfo[j]]
                Student[i]["General"]["Moy"]=m/3
        m=0
        if (Student[i]["Filiere"]=="GI"):
            for j in range(0,3):
                m=m+Student[i]["Spe"][matiere_GI_Info[j]]
                Student[i]["Spe"]["Moy"]=m/3
        elif (Student[i]["Filiere"]=="GMI"):
            for j in range(0,3):
                m=m+Student[i]["Spe"][matiere_GMI[j]]
                Student[i]["Spe"]["Moy"]=m/3
        elif (Student[i]["Filiere"]=="GMF"):
            for j in range(0,3):
                m=m+Student[i]["Spe"][matiere_GMF[j]]
                Student[i]["Spe"]["Moy"]=m/3
        for j in range(0,3):
            m=Student[i]["Spe"]["Moy"]+Student[i]["General"]["Moy"]+Student[i]["Humanite"]["Moy"]
            m=m/3
            Student[i]["Moy"]=m
    return Student

def GenerationStudent(Ne,Student):
    for i in range(1,Ne+1):
        Student[i]={"Filiere" : "", "prenom":"", "nom":"", "Voeu1":"","Voeu2":"","Voeu3":"","Humanite":"","General":"","Spe":"","Moy":"","VoeuAccepte":""}
        Student[i]["General"]={"OptiLin":"","AlgoProc":"","Proba":"","Java":"","DevWeb":"","Moy":""}
        Student[i]["Humanite"]={"Anglais":"","Ethique":"","Gestion":"","Moy":""}
        Student[i]["Spe"]={"Dataming":"","Graph":"","AnalNum":"","Topologie":"","EquaDiff":"","Opti":"","DevWeb":"","ProgramObjet":"","Java":"","Moy":""}
    Student=Filiere(Ne,Student)
    Student=Nommer(Ne,Student)
    Student=Voeu(Ne, Student)
    Student=RemplissageNote(Ne, Student)
    Student=Moyenne(Ne, Student)
    return Student

def F_Classement(Ne,Student):
    Ne=len(Student)
    Classement=[]
    Moyenne=[]
    for i in range(1,Ne+1):
        Classement.append(i)
        Moyenne.append(Student[i]["Moy"])
    for i in range(0,Ne):
        for j in range(0,Ne-1):
            while Moyenne[j]>Moyenne[j+1]:
                Moyenne[j],Moyenne[j+1]=Moyenne[j+1],Moyenne[j]
                Classement[j],Classement[j+1]=Classement[j+1],Classement[j]
    return Classement


def CompteurFiliere(Ne,Student):
    Ne=len(Student)
    nb_GMI=0
    nb_GMF=0
    nb_GI=0
    for i in range(1,Ne+1):
        if (Student[i]["Filiere"]=="GI"):
            nb_GI=nb_GI+1
        elif (Student[i]["Filiere"]=="GMI"):
            nb_GMI=nb_GMI+1
        elif (Student[i]["Filiere"]=="GMF"):
            nb_GMF=nb_GMF+1
    return nb_GMI,nb_GMF,nb_GI

def placeVoeu(Ne,Student,nb_GMI,nb_GMF,nb_GI):
    Ne=len(Student)
    voeuGI=nb_GI//4 +1
    voeuGMI=nb_GMI//3 +1
    voeuGMF=nb_GMF//3 +1
    return voeuGI,voeuGMI,voeuGMF


def Affectation(Student,voeuGI,voeuGMI,voeuGMF,Classement):
    Ne=len(Student)
    place={}
    place["IA"]=voeuGI
    place["CyberSecurite"]=voeuGI
    place["InfoEmbarque"]=voeuGI
    place["VisualComputing"]=voeuGI
    place["DataScience"]=voeuGMI
    place["FinTech"]=voeuGMI
    place["DataAnal"]=voeuGMI
    place["Actuariat"]=voeuGMF
    place["IngFinance"]=voeuGMF
    place["MMF"]=voeuGMF
    voeu1=0
    voeu2=0
    voeu3=0
    for i in range(0,Ne):
        id=Classement[i]
        if (place[Student[id]["Voeu1"]]>0):
            Student[id]["VoeuAccepte"]=Student[id]["Voeu1"]
            place[Student[id]["Voeu1"]]=place[Student[id]["Voeu1"]]-1
            voeu1=voeu1+1
        elif (place[Student[i]["Voeu2"]]>0):
            Student[id]["VoeuAccepte"]=Student[i]["Voeu2"]
            place[Student[id]["Voeu2"]]=place[Student[id]["Voeu2"]]-1
            voeu2=voeu2+1
        elif (place[Student[id]["Voeu3"]]>0):
            Student[id]["VoeuAccepte"]=Student[i]["Voeu3"]
            place[Student[id]["Voeu3"]]=place[Student[id]["Voeu3"]]-1
            voeu3=voeu3+1
        else:
            for k in range(0,4):
                if (orientation_GI[k]!=Student[id]["Voeu1"]) and (orientation_GI[k]!=Student[id]["Voeu2"]) and (orientation_GI[k]!=Student[id]["Voeu3"]):
                    Student[id]["VoeuAccepte"]=orientation_GI[k]
                    place[orientation_GI[k]]=place[orientation_GI[k]]-1
    return Student,voeu1,voeu2,voeu3

def Simulation(Ne,Student):
    Ne=len(Student)
    Student=GenerationStudent(Ne, Student)
    Student=SimulationPartie1(Ne,Student)
    return Student
def test2(Ne, Student):
    l=[]
    for k in range(1,Ne+1):
        if Student[k]['Moy']>10:
            l=l+[k]
    return l

def SimulationPartie1(Ne,Student):
    Ne=len(Student)
    Classement=F_Classement(Ne,Student)
    nb_GMI=CompteurFiliere(Ne,Student)[0]
    nb_GMF=CompteurFiliere(Ne,Student)[1]
    nb_GI=CompteurFiliere(Ne,Student)[2]
    voeuGI=placeVoeu(Ne,Student,nb_GMI,nb_GMF,nb_GI)[0]
    voeuGMI=placeVoeu(Ne,Student,nb_GMI,nb_GMF,nb_GI)[1]
    voeuGMF=placeVoeu(Ne,Student,nb_GMI,nb_GMF,nb_GI)[2]
    Student=Affectation(Student,voeuGI,voeuGMI,voeuGMF,Classement)[0]
    voeu1=Affectation(Student,voeuGI,voeuGMI,voeuGMF,Classement)[1]
    voeu2=Affectation(Student,voeuGI,voeuGMI,voeuGMF,Classement)[2]
    voeu3=Affectation(Student,voeuGI,voeuGMI,voeuGMF,Classement)[3]
    Stats(Ne,Student,voeu1,voeu2,voeu3)
    return Student

def Stats(Ne, Student, voeu1, voeu2, voeu3):
    Ne=len(Student)
    V1 = voeu1 / Ne
    V2 = voeu2 / Ne
    V3 = voeu3 / Ne
    IA = 0
    CyberS = 0
    InfoEmbarque = 0
    VisualComputing = 0
    DataScience = 0
    FinTech = 0
    DataAnal = 0
    Actuariat = 0
    IngFinance = 0
    MMF = 0
    for i in range(1, Ne + 1):
        if Student[i]["Voeu1"] == "IA":
            IA += 1
        if Student[i]["Voeu1"] == "CyberSecurite":
            CyberS += 1
        if Student[i]["Voeu1"] == "InfoEmbarque":
            InfoEmbarque += 1
        if Student[i]["Voeu1"] == "VisualComputing":
            VisualComputing += 1
        if Student[i]["Voeu1"] == "DataScience":
            DataScience += 1
        if Student[i]["Voeu1"] == "FinTech":
            FinTech += 1
        if Student[i]["Voeu1"] == "DataAnal":
            DataAnal += 1
        if Student[i]["Voeu1"] == "Actuariat":
            Actuariat += 1
        if Student[i]["Voeu1"] == "IngFinance":
            IngFinance += 1
        if Student[i]["Voeu1"] == "MMF":
            MMF += 1
    V10 = [IA, CyberS, InfoEmbarque, VisualComputing, DataScience, FinTech, DataAnal, Actuariat, IngFinance, MMF]

    fig, axs = plt.subplots(2, 1, figsize=(10, 8))

    index = range(3)
    bar_width = 0.4

    axs[0].bar(index[0], V1, bar_width, label='Voeu n°1')
    axs[0].bar(index[1], V2, bar_width, label='Voeu n°2')
    axs[0].bar(index[2], V3, bar_width, label='Voeu n°3')

    axs[0].set_xlabel('Voeu')
    axs[0].set_ylabel('Pourcentage')
    axs[0].set_title('Histogramme des acceptations de voeux')
    axs[0].set_xticks(index)
    axs[0].set_xticklabels(['Voeu n°1', 'Voeu n°2', 'Voeu n°3'])
    axs[0].legend()

    index_10 = range(10)

    axs[1].bar(index_10, V10)
    axs[1].set_xlabel(' ')
    axs[1].set_ylabel('Nombre de demandes')
    axs[1].set_title('Histogramme du nombre de demandes par filière')
    axs[1].set_xticks(index_10)
    axs[1].set_xticklabels(['IA', 'Cyber Sécurité', 'Informatique Embarqué', 'Visual Computing', 'Data Science', 'Finance Technologie', 'Data Analytics', 'Actuariat', 'Ingénierie Financiere', 'MMF'])
    axs[1].tick_params(axis='x', labelsize=6)

    plt.tight_layout()
    plt.show()

Student=GenerationStudent(Ne,Student)

def submit_form():
    global Ne, Student  # Utilisation de variables globales
    prenom = entry_prenom.get()
    nom = entry_nom.get()
    classe = var_classe.get()
    print("Prénom:", prenom)
    print("Nom:", nom)
    print("Classe:", classe)
    # Déterminer le numéro d'élève pour le nouvel élève
    print(Ne)
    Ne=Ne+1
    print(Ne)

    # Créer un dictionnaire pour le nouvel élève
    Student[Ne] = {
        "Filiere": classe,
        "prenom": prenom,
        "nom": nom
    }
    moyenne=""
    voeux1 = ""
    voeux2 = ""
    voeux3 = ""
    acc = ""
    if classe == "GMF":
        # Créer une nouvelle fenêtre pour saisir les vœux
        nouvelle_fenetre = tk.Toplevel(root)
        nouvelle_fenetre.title("Saisie des vœux et moyenne")

        label_moyenne = tk.Label(nouvelle_fenetre, text="Moyenne:")
        label_moyenne.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        entry_moyenne = tk.Entry(nouvelle_fenetre)
        entry_moyenne.grid(row=0, column=1, padx=10, pady=5)

        # Créer des labels et des comboboxes pour les vœux
        label_voeux1 = tk.Label(nouvelle_fenetre, text="1er Vœux:")
        label_voeux1.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        combo_voeux1 = ttk.Combobox(nouvelle_fenetre, values=["Actuariat","IngFinance","MMF"])
        combo_voeux1.grid(row=1, column=1, padx=10, pady=5)

        label_voeux2 = tk.Label(nouvelle_fenetre, text="2ème Vœux:")
        label_voeux2.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        combo_voeux2 = ttk.Combobox(nouvelle_fenetre, values=["Actuariat","IngFinance","MMF"])
        combo_voeux2.grid(row=2, column=1, padx=10, pady=5)

        label_voeux3 = tk.Label(nouvelle_fenetre, text="3ème Vœux:")
        label_voeux3.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        combo_voeux3 = ttk.Combobox(nouvelle_fenetre, values=["Actuariat","IngFinance","MMF"])
        combo_voeux3.grid(row=3, column=1, padx=10, pady=5)

        # Définition des fonctions de mise à jour des comboboxes
        def update_combo2(event):
            options = ["Actuariat","IngFinance","MMF"]
            options.remove(combo_voeux1.get())
            combo_voeux2['values'] = options
        def update_combo3(event):
            options = ["Actuariat","IngFinance","MMF"]
            options.remove(combo_voeux1.get())
            options.remove(combo_voeux2.get())
            combo_voeux3['values'] = options

        # Lier les fonctions de mise à jour aux événements de sélection des comboboxes
        combo_voeux1.bind("<<ComboboxSelected>>", update_combo2)
        combo_voeux2.bind("<<ComboboxSelected>>", update_combo3)
        # Bouton de soumission des vœux
        submit_button = tk.Button(nouvelle_fenetre, text="Valider", command=lambda: valider_voeux(entry_moyenne.get(),combo_voeux1.get(), combo_voeux2.get(), combo_voeux3.get(),acc))
        submit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
    elif classe == "GI":
        # Créer une nouvelle fenêtre pour saisir les vœux
        nouvelle_fenetre = tk.Toplevel(root)
        nouvelle_fenetre.title("Saisie des vœux")


        label_moyenne = tk.Label(nouvelle_fenetre, text="Moyenne:")
        label_moyenne.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        entry_moyenne = tk.Entry(nouvelle_fenetre)
        entry_moyenne.grid(row=0, column=1, padx=10, pady=5)

        # Créer des labels et des comboboxes pour les vœux
        label_voeux1 = tk.Label(nouvelle_fenetre, text="1er Vœux:")
        label_voeux1.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        combo_voeux1 = ttk.Combobox(nouvelle_fenetre, values=["IA","CyberSecurite","InfoEmbarque","VisualComputing"])
        combo_voeux1.grid(row=1, column=1, padx=10, pady=5)

        label_voeux2 = tk.Label(nouvelle_fenetre, text="2ème Vœux:")
        label_voeux2.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        combo_voeux2 = ttk.Combobox(nouvelle_fenetre, values=["IA","CyberSecurite","InfoEmbarque","VisualComputing"])
        combo_voeux2.grid(row=2, column=1, padx=10, pady=5)

        label_voeux3 = tk.Label(nouvelle_fenetre, text="3ème Vœux:")
        label_voeux3.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        combo_voeux3 = ttk.Combobox(nouvelle_fenetre, values=["IA","CyberSecurite","InfoEmbarque","VisualComputing"])
        combo_voeux3.grid(row=3, column=1, padx=10, pady=5)

        # Définition des fonctions de mise à jour des comboboxes
        def update_combo2(event):
            options = ["IA","CyberSecurite","InfoEmbarque","VisualComputing"]
            options.remove(combo_voeux1.get())
            combo_voeux2['values'] = options
        def update_combo3(event):
            options = ["IA","CyberSecurite","InfoEmbarque","VisualComputing"]
            options.remove(combo_voeux1.get())
            options.remove(combo_voeux2.get())
            combo_voeux3['values'] = options

        # Lier les fonctions de mise à jour aux événements de sélection des comboboxes
        combo_voeux1.bind("<<ComboboxSelected>>", update_combo2)
        combo_voeux2.bind("<<ComboboxSelected>>", update_combo3)

        # Bouton de soumission des vœux
        submit_button = tk.Button(nouvelle_fenetre, text="Valider", command=lambda: valider_voeux(entry_moyenne.get(),combo_voeux1.get(), combo_voeux2.get(), combo_voeux3.get(),acc))
        submit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        pass
    elif classe == "GMI":
        # Créer une nouvelle fenêtre pour saisir les vœux
        nouvelle_fenetre = tk.Toplevel(root)
        nouvelle_fenetre.title("Saisie des vœux")

        label_moyenne = tk.Label(nouvelle_fenetre, text="Moyenne:")
        label_moyenne.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        entry_moyenne = tk.Entry(nouvelle_fenetre)
        entry_moyenne.grid(row=0, column=1, padx=10, pady=5)

        # Créer des labels et des comboboxes pour les vœux
        label_voeux1 = tk.Label(nouvelle_fenetre, text="1er Vœux:")
        label_voeux1.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        combo_voeux1 = ttk.Combobox(nouvelle_fenetre, values=["DataScience","FinTech","DataAnal"])
        combo_voeux1.grid(row=1, column=1, padx=10, pady=5)

        label_voeux2 = tk.Label(nouvelle_fenetre, text="2ème Vœux:")
        label_voeux2.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        combo_voeux2 = ttk.Combobox(nouvelle_fenetre, values=["DataScience","FinTech","DataAnal"])
        combo_voeux2.grid(row=2, column=1, padx=10, pady=5)

        label_voeux3 = tk.Label(nouvelle_fenetre, text="3ème Vœux:")
        label_voeux3.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        combo_voeux3 = ttk.Combobox(nouvelle_fenetre, values=["DataScience","FinTech","DataAnal"])
        combo_voeux3.grid(row=3, column=1, padx=10, pady=5)

        # Définition des fonctions de mise à jour des comboboxes
        def update_combo2(event):
            options = ["DataScience","FinTech","DataAnal"]
            options.remove(combo_voeux1.get())
            combo_voeux2['values'] = options
        def update_combo3(event):
            options = ["DataScience","FinTech","DataAnal"]
            options.remove(combo_voeux1.get())
            options.remove(combo_voeux2.get())
            combo_voeux3['values'] = options

        # Lier les fonctions de mise à jour aux événements de sélection des comboboxes
        combo_voeux1.bind("<<ComboboxSelected>>", update_combo2)
        combo_voeux2.bind("<<ComboboxSelected>>", update_combo3)

        # Bouton de soumission des vœux
        submit_button = tk.Button(nouvelle_fenetre, text="Valider", command=lambda: valider_voeux(entry_moyenne.get(),combo_voeux1.get(), combo_voeux2.get(), combo_voeux3.get(),acc))
        submit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        pass
    else:
        messagebox.showinfo("Information", "Vœux non requis pour cette classe")



def valider_voeux(moyenne,voeux1, voeux2, voeux3,acc):
    global Ne, Student
    Student[Ne]["Voeu1"]=voeux1
    Student[Ne]["Voeu2"]=voeux2
    Student[Ne]["Voeu3"]=voeux3
    Student[Ne]["Moy"]=int(moyenne)
    Student[Ne]["VoeuAccepte"]=acc
    print("Moyenne:", Student[Ne]["Moy"])
    print("1er Vœux:", Student[Ne]["Voeu1"])
    print("2ème Vœux:", Student[Ne]["Voeu2"])
    print("3ème Vœux:", Student[Ne]["Voeu3"])
    print("Vœu Accepté:", Student[Ne]["VoeuAccepte"])

def submit_eleve_form():
    global Ne, Student
    eleve_id = entry_eleve_id.get()
    print("Connexion en tant qu'élève - Identifiant:",eleve_id )
    entier = int(eleve_id)
    print(entier)
    # Créer une nouvelle fenêtre pour afficher les tableaux des choix de l'élève
    choix_window = tk.Toplevel(root)
    choix_window.title("Choix de l'Élève")

    # Information sur l'élève
    choix_tree1 = ttk.Treeview(choix_window, columns=('Nom', 'Prénom', 'Classe'), show='headings')
    choix_tree1.heading('Nom', text='Nom')
    choix_tree1.heading('Prénom', text='Prénom')
    choix_tree1.heading('Classe', text='Classe')
    choix_tree1.grid(row=0, column=0, padx=10, pady=10)

    choix_tree1.insert('', 'end', values=(Student[entier]["nom"], Student[entier]["prenom"], Student[entier]["Filiere"]))

    # Création du tableau pour afficher les choix de l'élève
    choix_tree = ttk.Treeview(choix_window, columns=('Mes Voeux', 'État'), show='headings')
    choix_tree.heading('Mes Voeux', text='Mes Voeux')
    choix_tree.heading('État', text='État')
    choix_tree.grid(row=1, column=0, padx=10, pady=10)

    # Ajouter les choix de l'élève dans le tableau des choix
    choix_tree.insert('', 'end', values=(Student[entier]["Voeu1"], Student[entier]["Voeu1"]==Student[entier]["VoeuAccepte"]))
    choix_tree.insert('', 'end', values=(Student[entier]["Voeu2"], Student[entier]["Voeu2"]==Student[entier]["VoeuAccepte"]))
    choix_tree.insert('', 'end', values=(Student[entier]["Voeu3"], Student[entier]["Voeu3"]==Student[entier]["VoeuAccepte"]))
    if not any([Student[entier]["Voeu1"] == Student[entier]["VoeuAccepte"],
                Student[entier]["Voeu2"] == Student[entier]["VoeuAccepte"],
                Student[entier]["Voeu3"] == Student[entier]["VoeuAccepte"]]):
        no_allocation_label = tk.Label(choix_window, text="L'affectation n'a pas eu lieu pour cet élève.")
        no_allocation_label.grid(row=2, column=0, padx=10, pady=5)

def submit_admin_form():
    admin_nom = entry_admin_nom.get()
    admin_prenom = entry_admin_prenom.get()
    print("Connexion en tant qu'administrateur - Nom:", admin_nom, "Prénom:", admin_prenom)
    # Créer une nouvelle fenêtre pour afficher les tableaux des choix de l'élève
    choix_window = tk.Toplevel(root)
    choix_window.title("Choix de l'Administrateur")

    # Information sur l'élève
    choix_tree2 = ttk.Treeview(choix_window, columns=('Nom', 'Prénom', 'Classe', 'Voeu1', 'Voeu2', 'Voeu3'), show='headings')
    choix_tree2.heading('Nom', text='Nom')
    choix_tree2.heading('Prénom', text='Prénom')
    choix_tree2.heading('Classe', text='Classe')
    choix_tree2.heading('Voeu1', text='Voeu1')
    choix_tree2.heading('Voeu2', text='Voeu2')
    choix_tree2.heading('Voeu3', text='Voeu3')
    choix_tree2.grid(row=0, column=0, padx=10, pady=10)
    for k in range(1,len(Student)+1):
        choix_tree2.insert('', 'end', values=(Student[k]["nom"], Student[k]["prenom"], Student[k]["Filiere"], Student[k]["Voeu1"],Student[k]["Voeu2"], Student[k]["Voeu3"]))

    # Bouton pour lancer l'algorithme
    lancer_algo_button = tk.Button(choix_window, text="Lancer Algorithme", command=lancer_algorithme)
    lancer_algo_button.grid(row=1, column=0, padx=10, pady=10)

def visualiser_histogramme():
    global Student
    print("Visualisation de l'histogramme")
    Simulation(len(Student),Student)

def lancer_algorithme():
    global Student
    print("Lancement de l'algorithme")
    SimulationPartie1(len(Student),Student)

# Création de la fenêtre principale
root = tk.Tk()
root.title("Connexion")

# Bouton pour visualiser l'histogramme
text_hist = tk.Label(root, text="Cliquez sur le bouton ci-dessous pour visualiser l'histogramme d'affectation des élèves en fonction de leurs vœux")
text_hist.pack(padx=10, pady=10)

visualiser_histogramme_button = tk.Button(root, text="Visualiser l'histogramme", command=visualiser_histogramme)
visualiser_histogramme_button.pack(padx=10, pady=5)

# Création des libellés et des champs de saisie
text_eleve = tk.Label(root, text="Faire ses voeux pour Élève")
text_eleve.pack(padx=10, pady=10)

label_prenom = tk.Label(root, text="Prénom:")
label_prenom.pack(padx=10, pady=5)
entry_prenom = tk.Entry(root)
entry_prenom.pack(padx=10, pady=5)

label_nom = tk.Label(root, text="Nom:")
label_nom.pack(padx=10, pady=5)
entry_nom = tk.Entry(root)
entry_nom.pack(padx=10, pady=5)

label_classe = tk.Label(root, text="Classe:")
label_classe.pack(padx=10, pady=5)
var_classe = tk.StringVar(root)
var_classe.set("Sélectionner classe")
classe_options = ["Sélectionner classe", "GI", "GMI", "GMF"]
dropdown_classe = tk.OptionMenu(root, var_classe, *classe_options)
dropdown_classe.pack(padx=10, pady=5)

# Bouton de soumission du formulaire
submit_button = tk.Button(root, text="Faire ses choix", command=submit_form)
submit_button.pack(padx=10, pady=5)


# Connexion pour l'élève
text_eleve = tk.Label(root, text="Consulter resultat pour Élève")
text_eleve.pack(padx=10, pady=10)

label_eleve_id = tk.Label(root, text="Identifiant(Élève):")
label_eleve_id.pack(padx=10, pady=5)
entry_eleve_id = tk.Entry(root)
entry_eleve_id.pack(padx=10, pady=5)

submit_eleve_button = tk.Button(root, text="Connexion Élève", command=submit_eleve_form)
submit_eleve_button.pack(padx=10, pady=10)

# Connexion pour l'administrateur
text_admin = tk.Label(root, text="Connexion pour Administrateur")
text_admin.pack(padx=10, pady=10)

label_admin_nom = tk.Label(root, text="Nom (Administrateur):")
label_admin_nom.pack(padx=10, pady=5)
entry_admin_nom = tk.Entry(root)
entry_admin_nom.pack(padx=10, pady=5)

label_admin_prenom = tk.Label(root, text="Prénom (Administrateur):")
label_admin_prenom.pack(padx=10, pady=5)
entry_admin_prenom = tk.Entry(root)
entry_admin_prenom.pack(padx=10, pady=5)

submit_admin_button = tk.Button(root, text="Connexion Administrateur", command=submit_admin_form)
submit_admin_button.pack(padx=10, pady=10)

root.mainloop()

