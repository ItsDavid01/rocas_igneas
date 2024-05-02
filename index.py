#python -m streamlit run <filename.py> to run de app
import streamlit as st
import pandas as pd
import numpy as np
#import cv2

def rmv(list, elem): #remove
    try:
        list.remove(elem)
    except:
        pass

def On_EssMinMultiList_Change():
    st.session_state.EssMinList = ["Cuarzo", "Muscovita", "Feldespato", "Biotita", "Anfibol", "Piroxeno", "Olivino",
                                   "Plagioclasa sódica", "Plagioclasa intermedia", "Plagioclasa cálcica"]
    if "Plagioclasa intermedia" in st.session_state.EssMinReturn:
        rmv(st.session_state.EssMinList, "Cuarzo")
        rmv(st.session_state.EssMinList, "Feldespato")
        rmv(st.session_state.EssMinList, "Muscovita")
        rmv(st.session_state.EssMinList, "Plagioclasa sódica")
        rmv(st.session_state.EssMinList, "Plagioclasa cálcica")
        rmv(st.session_state.EssMinList, "Olivino")
    if "Piroxeno" in st.session_state.EssMinReturn:
        rmv(st.session_state.EssMinList, "Cuarzo")
        rmv(st.session_state.EssMinList, "Feldespato")
        rmv(st.session_state.EssMinList, "Muscovita")
    if "Cuarzo" in st.session_state.EssMinReturn:
        rmv(st.session_state.EssMinList, "Olivino")
        rmv(st.session_state.EssMinList, "Plagioclasa cálcica")
        rmv(st.session_state.EssMinList, "Piroxeno")
        rmv(st.session_state.EssMinList, "Plagioclasa intermedia")
    if "Feldespato" in st.session_state.EssMinReturn:
        rmv(st.session_state.EssMinList, "Plagioclasa intermedia")
        rmv(st.session_state.EssMinList, "Piroxeno")
    if "Muscovita" in st.session_state.EssMinReturn:
        rmv(st.session_state.EssMinList, "Plagioclasa intermedia")
        rmv(st.session_state.EssMinList, "Piroxeno")
    if "Olivino" in st.session_state.EssMinReturn:
        rmv(st.session_state.EssMinList, "Cuarzo")
        rmv(st.session_state.EssMinList, "Plagioclasa intermedia")
    if "Plagioclasa cálcica" in st.session_state.EssMinReturn:
        rmv(st.session_state.EssMinList, "Cuarzo")
        rmv(st.session_state.EssMinList, "Plagioclasa intermedia")
    if "Plagioclasa sódica" in st.session_state.EssMinReturn:
        rmv(st.session_state.EssMinList, "Plagioclasa intermedia")

st.title("Clasificación de Rocas ígneas en Muestra de Mano")
with st.sidebar:
    user = st.text_input("Usuario:", placeholder="Digite su usuario")
    password = st.text_input("Contraseña:", placeholder="Digite su contraseña", type="password")
    
composicion = st.selectbox("Roca compuesta por granos minerales o vidrio?",
                             ["Vidrio", "Mineral"],
                             index=None,
                             placeholder="Seleccione una opción")
textura = None
if composicion == "Vidrio":
    textura = st.selectbox("La roca presenta textura vesicular o vítrea?",
                                 ["Vesicular", "Vitrea"],
                                 index=None,
                                 placeholder="Seleccione una opcion")

minerales_esenciales = ["Cuarzo", "Muscovita", "Feldespato", "Biotita", "Anfibol", "Piroxeno", "Olivino",
                        "Plagioclasa sódica", "Plagioclasa intermedia", "Plagioclasa cálcica"]
MinEss = ["Cuarzo", "Muscovita", "Feldespato", "Biotita", "Anfibol", "Piroxeno", "Olivino", "Plg Na", "Plg Int", "Plg Ca"]
MinEssBin = [0,0,0,0,0,0,0,0,0,0] #Minerales_esenciales_lista_binaria
TamGrano = None
txMixta = None
hasSulfurosOxidos = None
homogeneidad = ""
minAccesorios = ""
mineralEssenCheckList = []

if composicion == "Mineral":
    if "EssMinReturn" not in st.session_state:
        st.session_state.EssMinReturn = []
    if "EssMinList" not in st.session_state:
        st.session_state.EssMinList = minerales_esenciales

    mineralEssenCheckList = st.multiselect("Seleccione los minerales esenciales",
                                        st.session_state.EssMinList,
                                        default=st.session_state.EssMinReturn,
                                        placeholder="Ningun mineral seleccionado",
                                        help="Seleccione los minerales principales de la roca, según Bowen",
                                        key="EssMinReturn",
                                        on_change=On_EssMinMultiList_Change,
                                        )
    for i in range(10): #Convertir cada mineral en vector binario
        if minerales_esenciales[i] in mineralEssenCheckList:
            MinEssBin[i] = 1
        else:
            MinEssBin[i] = 0

    hasSulfurosOxidos = st.selectbox("La roca presenta Sulfuros u Oxidos?",
                                        ["Si", "No"],
                                        index=None,
                                        placeholder="Seleccione una respuesta")
    
    minAccesorios = st.text_area("Escriba los minerales accesorios que contiene la roca", 
                                    placeholder="Escriba Aqui!")


    TamGrano = st.selectbox("Tamaño de grano",
                            ["Fanerítica",
                                "Mixto",
                                "Afanítica"],
                            index=None,
                            help="Fanerítica (Cristales visibles a simple vista) o Afanítica (Cristales no visibles a simple vista)",
                            placeholder="Seleccione una opción")

    if TamGrano == "Mixto":
        txMixta = st.selectbox("Seleccione la textura de la roca",
                                                ["Porfirítica",
                                                "Pegmatítica"],
                                                help="Porfirítica (Fenocristales rodeados de matriz) o Pegmatítica (Xenocristales rodeados de una matriz)",
                                                index=None,
                                                placeholder="Seleccione una opción")
        
    if TamGrano == "Fanerítica":
        homogeneidad = st.selectbox("Seleccione la homogeneidad de los cristales",
                                    ["Equigranular", "Inequigranular"],
                                    index=None,
                                    placeholder="Seleccione una opción")
        
rocasDF = pd.read_csv("RocasIgneasFinal.csv")
fault = ((MinEssBin[6] == 1) & (MinEssBin.count(1) == 1)) | ((MinEssBin[6] == 1) & (MinEssBin[5] == 1) & (MinEssBin.count(1) == 2))

selectionDF = rocasDF[((((rocasDF[MinEss[0]] == 1) | (MinEssBin[0] == 0)) & ((MinEssBin[0] == 1) | (rocasDF[MinEss[0]] == 0) | (fault == False))) &
                        (((rocasDF[MinEss[1]] == 1) | (MinEssBin[1] == 0)) & ((MinEssBin[1] == 1) | (rocasDF[MinEss[1]] == 0) | (fault == False))) &
                        (((rocasDF[MinEss[2]] == 1) | (MinEssBin[2] == 0)) & ((MinEssBin[2] == 1) | (rocasDF[MinEss[2]] == 0) | (fault == False))) &
                        (((rocasDF[MinEss[3]] == 1) | (MinEssBin[3] == 0)) & ((MinEssBin[3] == 1) | (rocasDF[MinEss[3]] == 0) | (fault == False))) &
                        (((rocasDF[MinEss[4]] == 1) | (MinEssBin[4] == 0)) & ((MinEssBin[4] == 1) | (rocasDF[MinEss[4]] == 0) | (fault == False))) &
                        (((rocasDF[MinEss[5]] == 1) | (MinEssBin[5] == 0)) & ((MinEssBin[5] == 1) | (rocasDF[MinEss[5]] == 0) | (fault == False))) &
                        (((rocasDF[MinEss[6]] == 1) | (MinEssBin[6] == 0)) & ((MinEssBin[6] == 1) | (rocasDF[MinEss[6]] == 0) | (fault == False))) &
                        (((rocasDF[MinEss[7]] == 1) | (MinEssBin[7] == 0)) & ((MinEssBin[7] == 1) | (rocasDF[MinEss[7]] == 0) | (fault == False))) &
                        (((rocasDF[MinEss[8]] == 1) | (MinEssBin[8] == 0)) & ((MinEssBin[8] == 1) | (rocasDF[MinEss[8]] == 0) | (fault == False))) &
                        (((rocasDF[MinEss[9]] == 1) | (MinEssBin[9] == 0)) & ((MinEssBin[9] == 1) | (rocasDF[MinEss[9]] == 0) | (fault == False)))) &
                      ((rocasDF["Composición"] == composicion) | (composicion == None)) &
                      ((rocasDF["Textura"] == textura) | (textura == None)) &
                      ((rocasDF["Tamaño de grano"] == TamGrano) | (TamGrano == None)) &
                      ((rocasDF["Textura mixta de grano"] == txMixta) | (txMixta == None)) &
                      ((rocasDF["Sulfuros u oxidos"] == hasSulfurosOxidos) | (hasSulfurosOxidos == None))
                        ]
if homogeneidad == None:
    selectionDF["Homogeneidad"] = ""
else:
    selectionDF["Homogeneidad"] = homogeneidad
    
selectionDF["Minerales accesorios"] = minAccesorios
textMinEss = ""
for mineral in mineralEssenCheckList:
    textMinEss += (f"{mineral}, ")

selectionDF["Minerales esenciales"] = textMinEss

columnas = ["Nombre Roca", "Composición", "Origen", "Color", "Etapa del magma", "Tipo de magma",
            "Velocidad de enfriamiento", "Tamaño de grano", "Textura mixta de grano", "Cristalinidad", "Homogeneidad",
            "Minerales esenciales", "Minerales accesorios", "Textura"]

if composicion == "Vidrio":
    columnas = ["Nombre Roca", "Composición", "Textura", "Origen", "Color", "Velocidad de enfriamiento", "Cristalinidad"]
elif composicion == "Mineral":
    columnas = ["Nombre Roca", "Composición", "Origen", "Color", "Etapa del magma", "Tipo de magma",
            "Velocidad de enfriamiento", "Tamaño de grano", "Textura mixta de grano", "Cristalinidad", "Homogeneidad",
            "Minerales esenciales", "Minerales accesorios"]
    if TamGrano == "Mixto":
        columnas = ["Nombre Roca", "Composición", "Origen", "Color", "Etapa del magma", "Tipo de magma",
            "Velocidad de enfriamiento", "Tamaño de grano", "Textura mixta de grano","Cristalinidad",
            "Minerales esenciales", "Minerales accesorios"]
    elif TamGrano == "Afanítica":
        columnas = ["Nombre Roca", "Composición", "Origen", "Color", "Etapa del magma", "Tipo de magma",
            "Velocidad de enfriamiento", "Tamaño de grano", "Cristalinidad",
            "Minerales esenciales", "Minerales accesorios"]
    elif TamGrano == "Fanerítica":
        columnas = ["Nombre Roca", "Composición", "Origen", "Color", "Etapa del magma", "Tipo de magma",
            "Velocidad de enfriamiento", "Tamaño de grano", "Cristalinidad", "Homogeneidad",
            "Minerales esenciales", "Minerales accesorios"]
        
    

st.subheader("A continuación se muestra una lista con todas las posibles clasificaciones de roca con base a los criterios especificados:")
st.write(f"Mostrando {selectionDF.shape[0]} tipos distintos de roca")
st.dataframe(selectionDF, hide_index=True, column_order=columnas)
if selectionDF.shape[0] == 1:
    with st.expander("Ver imágenes de la roca"):
        nombreRoca = selectionDF.iloc[0,0]
        try:
            st.image(f"Images\{nombreRoca}.jpeg", caption=f"{nombreRoca}", use_column_width=True)
        except:
            st.write("No hay imágenes de la clasificación de roca seleccionada. Añade la tuya!")
        
    

#up_files = st.file_uploader("Sube una foto de tu muestra para la comunidad!", accept_multiple_files=True, type=["png", "jpg"])

#for file in up_files:
#    data = file.read()
#    st.write(file)