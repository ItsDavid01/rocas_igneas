#python -m streamlit run <filename.py> to run de app
import streamlit as st
import pandas as pd
import numpy as np

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
        rmv(st.session_state.EssMinList, "Piroxeno")
    if "Piroxeno" in st.session_state.EssMinReturn:
        rmv(st.session_state.EssMinList, "Cuarzo")
        rmv(st.session_state.EssMinList, "Feldespato")
        rmv(st.session_state.EssMinList, "Muscovita")
        rmv(st.session_state.EssMinList, "Plagioclasa intermedia")
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

st.title("Title des Websites")

with st.sidebar:
    user = st.text_input("Usuario:", placeholder="Digite su usuario")
    password = st.text_input("Contraseña:", placeholder="Digite su contraseña", type="password")

selectBox_1_p = st.selectbox("Roca compuesta por granos minerales o vidrio?",
                             ["Vidrio", "Minerales"],
                             index=None,
                             placeholder="Seleccione una opción")

if selectBox_1_p == "Vidrio":
    selectBox_2_p = st.selectbox("La roca presenta textura vesicular o vítrea?",
                                 ["Vesicular", "Vitrea"],
                                 index=None,
                                 placeholder="Seleccione una opcion")
    
    if selectBox_2_p == "Vesicular":
        st.write("Su roca corresponde a una PUMITA")
        st.write("Imagen de referencia: No_Image_Yet")
        
    if selectBox_2_p == "Vitrea":
        st.write("Su roca es una OBSIDIANA")
        st.write("Imagen de referencia: No_Image_Yet")

if selectBox_1_p == "Minerales":
    minerales_esenciales = ["Cuarzo", "Muscovita", "Feldespato", "Biotita", "Anfibol", "Piroxeno", "Olivino",
                            "Plagioclasa sódica", "Plagioclasa intermedia", "Plagioclasa cálcica"]
    
    if "EssMinList" not in st.session_state:
        st.session_state.EssMinList = minerales_esenciales
    
    if "EssMinReturn" not in st.session_state:
        st.session_state.EssMinReturn = []
        
    mineralEssenCheckList = st.multiselect("Seleccione los minerales esenciales",
                                        st.session_state.EssMinList,
                                        default=st.session_state.EssMinReturn,
                                        placeholder="Ningun mineral seleccionado",
                                        help="Seleccione los minerales principales de la roca, según Bowen",
                                        key="EssMinReturn",
                                        on_change=On_EssMinMultiList_Change)
    
    MinEssBin = [0,0,0,0,0,0,0,0,0,0] #Minerales_esenciales_lista_binaria
    for i in range(10):
        if minerales_esenciales[i] in mineralEssenCheckList:
            MinEssBin[i] = 1
        else:
            MinEssBin[i] = 0
    
    minerales_accesorios = ["Sulfuros", "Oxidos"]
    mineralAccesCheckList = st.multiselect("Seleccione los minerales accesorios",
                                        minerales_accesorios,
                                        placeholder="No tiene")
    
    TamGrano = st.selectbox("Tamaño de grano",
                            ["Fanerítica (Cristales visibles a simple vista)",
                             "Mixto",
                             "Afanítica (Cristales no visibles a simple vista)"],
                            index=None,
                            placeholder="Seleccione una opción")
    
    if TamGrano == "Mixto":
        preguntaMatriz = st.selectbox("Seleccione la composición de la matriz de la roca",
                                      ["Vidrio", "Granos minerales"],
                                      index=None,
                                      placeholder="Seleccione una opción")
        
        mixto_grano_selectBox = st.selectbox("Seleccione la textura de la roca",
                                                ["Porfirítica (Fenocristales rodeados de matriz)",
                                                "Pegmatítica (Xenocristales rodeados de una matriz)"],
                                                index=None,
                                                placeholder="Seleccione una opción")
    if TamGrano == "Fanerítica (Cristales visibles a simple vista)":
        homogeneidad = st.selectbox("Seleccione la homogeneidad de los cristales",
                                    ["Equigranular", "Inequigranular"],
                                    index=None,
                                    placeholder="Seleccione una opción")
        
    rocasDF = pd.read_csv("Rocas_Igneas.csv")
    
    selectionDF = rocasDF[((rocasDF["Cuarzo"] == 1) | (MinEssBin[0] == 0)) &
                          ((rocasDF["Muscovita"] == 1) | (MinEssBin[1] == 0)) &
                          ((rocasDF["Feldespato"] == 1) | (MinEssBin[2] == 0)) &
                          ((rocasDF["Biotita"] == 1) | (MinEssBin[3] == 0)) &
                          ((rocasDF["Anfibol"] == 1) | (MinEssBin[4] == 0)) &
                          ((rocasDF["Piroxeno"] == 1) | (MinEssBin[5] == 0)) &
                          ((rocasDF["Olivino"] == 1) | (MinEssBin[6] == 0)) &
                          ((rocasDF["Plg Na"] == 1) | (MinEssBin[7] == 0)) &
                          ((rocasDF["Plg Int"] == 1) | (MinEssBin[8] == 0)) &
                          ((rocasDF["Plg Ca"] == 1) | (MinEssBin[9] == 0))]
    
    st.dataframe(selectionDF, hide_index=True, column_order=("Nombre Roca", "Origen", "Color", "Tipo de magma"))

    
            
    