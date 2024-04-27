#python -m streamlit run <filename.py> to run de app
import streamlit as st

#Piroxeno EXCLUDES cuarzo, feldespato, muscovita
#cuarzo EXCLUDES olivino, plagioclasa calcica, piroxeno
def rmv(list, elem): #remove
    try:
        list.remove(elem)
    except:
        pass

def On_EssMinMultiList_Change():
    st.session_state.EssMinList = ["Cuarzo", "Feldespato", "Muscovita", "Anfibol", "Piroxeno",
                                  "Plagioclasa sódica", "Plagioclasa cálcica", "Olivino", "Biotita"]
    if "Piroxeno" in st.session_state.EssMinReturn:
        rmv(st.session_state.EssMinList, "Cuarzo")
        rmv(st.session_state.EssMinList, "Feldespato")
        rmv(st.session_state.EssMinList, "Muscovita")       
    if "Cuarzo" in st.session_state.EssMinReturn:
        rmv(st.session_state.EssMinList, "Olivino")
        rmv(st.session_state.EssMinList, "Plagioclasa cálcica")
        rmv(st.session_state.EssMinList, "Piroxeno")       
    if "Feldespato" in st.session_state.EssMinReturn:
        rmv(st.session_state.EssMinList, "Piroxeno")
    if "Muscovita" in st.session_state.EssMinReturn:
        rmv(st.session_state.EssMinList, "Piroxeno")
    if "Olivino" in st.session_state.EssMinReturn:
        rmv(st.session_state.EssMinList, "Cuarzo")
    if "Plagioclasa cálcica" in st.session_state.EssMinReturn:
        rmv(st.session_state.EssMinList, "Cuarzo")

st.title("Title des Websites")

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
        st.write("Su roca es una OBISIDIANA")
        st.write("Imagen de referencia: No_Image_Yet")


if selectBox_1_p == "Minerales":
    minerales_esenciales = ["Cuarzo", "Feldespato", "Muscovita", "Anfibol", "Piroxeno",
                            "Plagioclasa sódica", "Plagioclasa cálcica", "Olivino", "Biotita"]
    
    if "EssMinList" not in st.session_state:
        st.session_state.EssMinList = minerales_esenciales
        
    if "EssMinReturn" not in st.session_state:
        st.session_state.EssMinReturn = []
        
    mineralEssenCheckList = st.multiselect("Seleccione los minerales esenciales",
                                        st.session_state.EssMinList,
                                        default=st.session_state.EssMinReturn,
                                        placeholder="Ningun mineral seleccionado",
                                        help="Seleccione almenos uno",
                                        key="EssMinReturn",
                                        on_change=On_EssMinMultiList_Change)
    
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
        if preguntaMatriz == "Granos minerales":
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
            
    