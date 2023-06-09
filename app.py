# -*- coding: utf-8 -*-
"""
Created on Thu May 19 19:15:01 2023

@author: Sandjak
"""

import numpy as np
from math import *
#import pickle
import streamlit as st


# loading the saved model
#loaded_model = pickle.load(open('D:/Work/Machine Learning/Deploying Machine Learning model/trained_model.sav', 'rb'))


# creating a function for Prediction
  
def main():
    
    
    # giving a title
    st.title('Prédiction des paramètres de résitance au cisaillement des sols')
    
    # getting the input data from the user
    
    Nat = st.selectbox("Nature du sol: ",('Argile','Limon','Sable'),key = 10) 
    Type = st.selectbox("Type d'essai:", ('UU','CU','CD'),key = 20)
    
    if(Nat=='Argile' or Nat=='Limon' ):
        if(Type=='UU'or Type=='CU'):
    
           # getting the input data from the user
         #
         FC = st.slider("Pourcentage des fines (passant au tamis 0.080 mm) Fc(%): ",43,100,key = 11) 
         WL = st.slider("Limite de Liquidité Wl(%): ",24,91,key = 21)
         IP = st.slider("Indice de Plasticité IP(%): ",8,45,key = 31)
         MC = st.slider("Teneur en eau naturelle W(%) : ",9,45,key = 41) 
         SR = st.slider("Degré de Saturation Sr(%) : ",13,100,key = 51) 
         ROD = st.slider("Masse volumique séche (g/cm3): ",1.30,2.0,key = 61)
         
         H1_1 = tanh((-1.73155470967094 + 0.431244552864852 * asinh((-13.8047060123454 + 0.316220244488437 * WL)) + 0.380883118007239 * asinh((-5.65869611341534 + 0.24144618851452 * IP)) + 2.63608229216892 * asinh((-0.220297410454875 + 0.052131567418078 * MC)) + 0.112342931209823 * log(((-34.5 + FC) / (100.72 + -1 * FC))) + -0.30465541794321 * log(((-10 + SR) / (100.29 + -1 * SR))) + 0.423538590589697 * log(((-1.15 + ROD) / (2.027 + -1 * ROD)))))
         H1_2 = tanh((6.47095822912295 + 0.608178304225179 * asinh((-13.8047060123454 + 0.316220244488437 * WL)) + 0.953898273921101 * asinh((-5.65869611341534 + 0.24144618851452 * IP)) + -8.67719141875302 * asinh((-0.220297410454875 + 0.052131567418078 * MC)) + -0.693137484275815 * log(((-34.5 + FC) / (100.72 + -1 * FC))) + 0.120373995855699 * log(((-10 + SR) / (100.29 + -1 * SR))) + 3.27698673827095 * log(((-1.15 + ROD) / (2.027 + -1 * ROD)))))
         H1_3 = tanh((0.708958186543585 + -1.2489134946272 * asinh((-13.8047060123454 + 0.316220244488437 * WL)) + -0.183375828501441 * asinh((-5.65869611341534 + 0.24144618851452 * IP)) + 1.54753434206195 * asinh((-0.220297410454875 + 0.052131567418078 * MC)) + 0.287681388636889 * log(((-34.5 + FC) / (100.72 + -1 * FC))) + -0.880754179770174 * log(((-10 + SR) / (100.29 + -1 * SR))) + 1.62390931200331 * log(((-1.15 + ROD) / (2.027 + -1 * ROD)))))
         H1_4 = tanh((-0.986348850492432 + -0.800463517842174 * asinh((-13.8047060123454 + 0.316220244488437 * WL)) + 0.289411534736928 * asinh((-5.65869611341534 + 0.24144618851452 * IP)) + 2.69451962877889 * asinh((-0.220297410454875 + 0.052131567418078 * MC)) + 0.0966631789263405 * log(((-34.5 + FC) / (100.72 + -1 * FC))) + -0.545878274292516 * log(((-10 + SR) / (100.29 + -1 * SR))) + 1.84055606162007 * log(((-1.15 + ROD) / (2.027 + -1 * ROD)))))
         H1_5 = tanh((0.281037567414743 + -0.558111596276607 * asinh((-13.8047060123454 + 0.316220244488437 * WL)) + 0.471923811931088 * asinh((-5.65869611341534 + 0.24144618851452 * IP)) + 0.0226994007059913 * asinh((-0.220297410454875 + 0.052131567418078 * MC)) + -0.16194253009527 * log(((-34.5 + FC) / (100.72 + -1 * FC))) + -0.31358578684513 * log(((-10 + SR) / (100.29 + -1 * SR))) + 1.4208736318413 * log(((-1.15 + ROD) / (2.027 + -1 * ROD)))))
         H1_6 = tanh((6.05077546018328 + 0.272656091000954 * asinh((-13.8047060123454 + 0.316220244488437 * WL)) + 0.689596405618575 * asinh((-5.65869611341534 + 0.24144618851452 * IP)) + -6.95841052122324 * asinh((-0.220297410454875 + 0.052131567418078 * MC)) + -0.438635146988941 * log(((-34.5 + FC) / (100.72 + -1 * FC))) + -0.173465121644215 * log(((-10 + SR) / (100.29 + -1 * SR))) + 0.99088258026372 * log(((-1.15 + ROD) / (2.027 + -1 * ROD)))))
         H1_7 = tanh((1.85048583743458 + 0.241453789875437 * asinh((-13.8047060123454 + 0.316220244488437 * WL)) + -0.0977892015055274 * asinh((-5.65869611341534 + 0.24144618851452 * IP)) + 2.77048163226091 * asinh((-0.220297410454875 + 0.052131567418078 * MC)) + -0.455973367195692 * log(((-34.5 + FC) / (100.72 + -1 * FC))) + -0.0690830127779746 * log(((-10 + SR) / (100.29 + -1 * SR))) + -1.65967994967884 * log(((-1.15 + ROD) / (2.027 + -1 * ROD)))))
         H1_8 = tanh((2.23738342904377 + -0.917415492496228 * asinh((-13.8047060123454 + 0.316220244488437 * WL)) + -0.0171046254432055 * asinh((-5.65869611341534 + 0.24144618851452 * IP)) + -5.28397595764835 * asinh((-0.220297410454875 + 0.052131567418078 * MC)) + 0.699158116030425 * log(((-34.5 + FC) / (100.72 + -1 * FC))) + 0.327714476698544 * log(((-10 + SR) / (100.29 + -1 * SR))) + -0.103143492148758 * log(((-1.15 + ROD) / (2.027 + -1 * ROD)))))
         H1_9 = tanh((-0.306111761845224 + -0.0381881219252892 * asinh((-13.8047060123454 + 0.316220244488437 * WL)) + 0.188777831849248 * asinh((-5.65869611341534 + 0.24144618851452 * IP)) + -0.448846959522646 * asinh((-0.220297410454875 + 0.052131567418078 * MC)) + 0.270478657562682 * log(((-34.5 + FC) / (100.72 + -1 * FC))) + -0.126042847264545 * log(((-10 + SR) / (100.29 + -1 * SR))) + -0.912200010583877 * log(((-1.15 + ROD) / (2.027 + -1 * ROD)))))
         H1_10 = tanh((-0.138051544753464 + -0.2250687976151 * asinh((-13.8047060123454 + 0.316220244488437 * WL)) + -0.446348088326204 * asinh((-5.65869611341534 + 0.24144618851452 * IP)) + -0.831054008241412 * asinh((-0.220297410454875 + 0.052131567418078 * MC)) + -0.0658834986763093 * log(((-34.5 + FC) / (100.72 + -1 * FC))) + 0.302008595068887 * log(((-10 + SR) / (100.29 + -1 * SR))) + -0.518755781059944 * log(((-1.15 + ROD) / (2.027 + -1 * ROD)))))
         #
         H2_1 = tanh((-10.4809148855243 + 0.32406493001291 * asinh((-13.8047060123454 + 0.316220244488437 * WL)) + -0.50228681104708 * asinh((-5.65869611341534 + 0.24144618851452 * IP)) + 9.59330655691272 * asinh((-0.220297410454875 + 0.052131567418078 * MC)) + 0.35267672054899 * log(((-34.5 + FC) / (100.72 + -1 * FC))) + 0.0424427529923658 * log(((-10 + SR) / (100.29 + -1 * SR))) + 3.03000222048757 * log(((-1.15 + ROD) / (2.027 + -1 * ROD)))))
         H2_2 = tanh((5.43735372967603 + 0.283946261456127 * asinh((-13.8047060123454 + 0.316220244488437 * WL)) + -0.17323376087935 * asinh((-5.65869611341534 + 0.24144618851452 * IP)) + -3.7021425962233 * asinh((-0.220297410454875 + 0.052131567418078 * MC)) + -0.107512478760838 * log(((-34.5 + FC) / (100.72 + -1 * FC))) + -0.695138423532689 * log(((-10 + SR) / (100.29 + -1 * SR))) + -0.605516029521549 * log(((-1.15 + ROD) / (2.027 + -1 * ROD)))))
         H2_3 = tanh((-0.918586038252341 + 0.0070974585843741 * asinh((-13.8047060123454 + 0.316220244488437 * WL)) + -0.721854529537237 * asinh((-5.65869611341534 + 0.24144618851452 * IP)) + 1.26874209701916 * asinh((-0.220297410454875 + 0.052131567418078 * MC)) + 0.032764601571086 * log(((-34.5 + FC) / (100.72 + -1 * FC))) + 0.277387111414123 * log(((-10 + SR) / (100.29 + -1 * SR))) + -0.512115591545759 * log(((-1.15 + ROD) / (2.027 + -1 * ROD)))))
         H2_4 = tanh((3.40944163610797 + 0.0619319340999845 * asinh((-13.8047060123454 + 0.316220244488437 * WL)) + 0.347203464148433 * asinh((-5.65869611341534 + 0.24144618851452 * IP)) + -1.75213202485094 * asinh((-0.220297410454875 + 0.052131567418078 * MC)) + 0.794618133603411 * log(((-34.5 + FC) / (100.72 + -1 * FC))) + -0.011257065035394 * log(((-10 + SR) / (100.29 + -1 * SR))) + -3.29692208775259 * log(((-1.15 + ROD) / (2.027 + -1 * ROD)))))
         H2_5 = tanh((3.52166335207492 + 0.559304231725961 * asinh((-13.8047060123454 + 0.316220244488437 * WL)) + -0.152846306701516 * asinh((-5.65869611341534 + 0.24144618851452 * IP)) + -5.45671142852235 * asinh((-0.220297410454875 + 0.052131567418078 * MC)) + 0.637095864764212 * log(((-34.5 + FC) / (100.72 + -1 * FC))) + -0.39489215983954 * log(((-10 + SR) / (100.29 + -1 * SR))) + -1.28325420549021 * log(((-1.15 + ROD) / (2.027 + -1 * ROD)))))
         H2_6 = tanh((-6.48898121113067 + -1.35073361571162 * asinh((-13.8047060123454 + 0.316220244488437 * WL)) + 2.13589888356889 * asinh((-5.65869611341534 + 0.24144618851452 * IP)) + 8.34582545276188 * asinh((-0.220297410454875 + 0.052131567418078 * MC)) + -0.215920473895209 * log(((-34.5 + FC) / (100.72 + -1 * FC))) + 0.222966145130312 * log(((-10 + SR) / (100.29 + -1 * SR))) + -1.60309469216271 * log(((-1.15 + ROD) / (2.027 + -1 * ROD)))))
         H2_7 = tanh((0.254746967699429 + 1.2483459945993 * asinh((-13.8047060123454 + 0.316220244488437 * WL)) + -0.405189038252279 * asinh((-5.65869611341534 + 0.24144618851452 * IP)) + 0.665724247718629 * asinh((-0.220297410454875 + 0.052131567418078 * MC)) + -0.517725555822598 * log(((-34.5 + FC) / (100.72 + -1 * FC))) + -0.00150742122171581 * log(((-10 + SR) / (100.29 + -1 * SR))) + -1.50736175270129 * log(((-1.15 + ROD) / (2.027 + -1 * ROD)))))
         H2_8 = tanh((9.85585138703988 + 1.27164736672478 * asinh((-13.8047060123454 + 0.316220244488437 * WL)) + -0.500189695507384 * asinh((-5.65869611341534 + 0.24144618851452 * IP)) + -11.3923901262716 * asinh((-0.220297410454875 + 0.052131567418078 * MC)) + -0.153141210801031 * log(((-34.5 + FC) / (100.72 + -1 * FC))) + 0.0763109600379642 * log(((-10 + SR) / (100.29 + -1 * SR))) + -1.8831862358003 * log(((-1.15 + ROD) / (2.027 + -1 * ROD)))))
         H2_9 = tanh((1.22466355121338 + 0.574893635845216 * asinh((-13.8047060123454 + 0.316220244488437 * WL)) + -0.214446538376777 * asinh((-5.65869611341534 + 0.24144618851452 * IP)) + -0.190907256926091 * asinh((-0.220297410454875 + 0.052131567418078 * MC)) + 0.544318778289196 * log(((-34.5 + FC) / (100.72 + -1 * FC))) + -0.143854732379185 * log(((-10 + SR) / (100.29 + -1 * SR))) + -1.11651926765956 * log(((-1.15 + ROD) / (2.027 + -1 * ROD)))))
         H2_10 = tanh((5.92019747508542 + -0.499299206424128 * asinh((-13.8047060123454 + 0.316220244488437 * WL)) + 0.34799177138606 * asinh((-5.65869611341534 + 0.24144618851452 * IP)) + -5.91806245344164 * asinh((-0.220297410454875 + 0.052131567418078 * MC)) + 0.125673297377105 * log(((-34.5 + FC) / (100.72 + -1 * FC))) + -0.281564767390919 * log(((-10 + SR) / (100.29 + -1 * SR))) + -0.390653702020724 * log(((-1.15 + ROD) / (2.027 + -1 * ROD)))))
                
         COH_Pred = 0.721972168147998 + -0.576010243775466 * H1_1 + -0.396496922564423 * H1_10 + 0.277826631731363 * H1_2 + -0.439795757196256 * H1_3 + 0.760502441041834 * H1_4 + -0.33554048508918 * H1_5 + -0.31921563281662 * H1_6 + -0.361411767306779 * H1_7 + -0.249951598768931 * H1_8 + 0.23660345689706 * H1_9
         PHI_Pred = 14.7647928898899 + 5.38815574970612 * H2_1 + -1.12153204514243 * H2_10 + 6.16425207024284 * H2_2 + 0.0468271446035384 * H2_3 + 8.59708366984537 * H2_4 + -2.82683136398748 * H2_5 + 6.24341249838151 * H2_6 + -3.99488206880019 * H2_7 + 8.39321769811191 * H2_8 + -14.879477378892 * H2_9
         
         COH_Pred =round(COH_Pred,2)
         PHI_Pred =round(PHI_Pred,2)
         
         if COH_Pred < 0:
                   COH_Pred = 0
         else:
                    COH_Pred = COH_Pred
         if PHI_Pred < 0:
                   PHI_Pred = 0
         else:
                    PHI_Pred = PHI_Pred
         
         # code for Prediction
    
         predict1 = ''
         predict2 = ''
         # creating a button for Prediction
    
         if st.button('Prédiction'):
          predict1 = ("Terme de Cohésion du sol en bars est:",COH_Pred)
          predict2 = ("Angle de frottement du sol en degrés est:",PHI_Pred)
         st.success(predict1)
         st.success(predict2)
        else:
            
         FC = st.slider("Pourcentage des fines (passant au tamis 0.080 mm) Fc(%): ",59,100,key = 12) 
         WL = st.slider("Limite de Liquidité Wl(%): ",34,88,key = 22)
         IP = st.slider("Indice de Plasticité IP(%): ",10,43,key = 32)
         MC = st.slider("Teneur en eau naturelle W(%) : ",13,38,key = 42) 
         SR = st.slider("Degré de Saturation Sr(%) : ",75,100,key = 52) 
         ROD = st.slider("Masse volumique séche (g/cm3): ",1.35,1.88,key = 62)
            
            
            
            
            
         H3_1 = tanh((283.7539120081 + -3.21616957538748 * asinh((-6.15110225216742 + 0.222181057715337 * IP)) + 0.61392394429391 * log(((-73 + SR) / (100.22 + -1 * SR))) + -1.41777907093791 * log(((-37.8030252237449 + FC) / (101 + -1 * FC))) + -0.392090419290649 * log(((-11 + MC) / (42.56 + -1 * MC))) + 0.00530169358417825 * log(((-1.29 + ROD) / (1.92 + -1 * ROD))) + -149.467576634946 * log(((5678.53539136785 + WL) / (916.872991051482 + -1 * WL)))))
         H3_2 = tanh((-348.17686572599 + -0.677780990853942 * asinh((-6.15110225216742 + 0.222181057715337 * IP)) + -0.308683201511462 * log(((-73 + SR) / (100.22 + -1 * SR))) + 0.980018366832495 * log(((-37.8030252237449 + FC) / (101 + -1 * FC))) + -1.21192219508968 * log(((-11 + MC) / (42.56 + -1 * MC))) + -0.437055485718281 * log(((-1.29 + ROD) / (1.92 + -1 * ROD))) + 181.939458116929 * log(((5678.53539136785 + WL) / (916.872991051482 + -1 * WL)))))
         H3_3 = tanh((-319.680489672141 + 0.914743657115374 * asinh((-6.15110225216742 + 0.222181057715337 * IP)) + -0.354393494097736 * log(((-73 + SR) / (100.22 + -1 * SR))) + -0.797912618236096 * log(((-37.8030252237449 + FC) / (101 + -1 * FC))) + -1.01481980581325 * log(((-11 + MC) / (42.56 + -1 * MC))) + -0.310455773194786 * log(((-1.29 + ROD) / (1.92 + -1 * ROD))) + 170.436019195458 * log(((5678.53539136785 + WL) / (916.872991051482 + -1 * WL)))))
         H3_4 = tanh((-534.48131302046 + 0.0966051160347666 * asinh((-6.15110225216742 + 0.222181057715337 * IP)) + 0.781688527489686 * log(((-73 + SR) / (100.22 + -1 * SR))) + 2.39456276331693 * log(((-37.8030252237449 + FC) / (101 + -1 * FC))) + 0.48475180803516 * log(((-11 + MC) / (42.56 + -1 * MC))) + -0.626385570449845 * log(((-1.29 + ROD) / (1.92 + -1 * ROD))) + 278.515673820759 * log(((5678.53539136785 + WL) / (916.872991051482 + -1 * WL)))))
         H3_5 = tanh((-205.983982339653 + -0.43598297290589 * asinh((-6.15110225216742 + 0.222181057715337 * IP)) + -1.69710400726998 * log(((-73 + SR) / (100.22 + -1 * SR))) + -1.04076488513038 * log(((-37.8030252237449 + FC) / (101 + -1 * FC))) + 1.04079982026572 * log(((-11 + MC) / (42.56 + -1 * MC))) + -1.69811132591526 * log(((-1.29 + ROD) / (1.92 + -1 * ROD))) + 111.541524859455 * log(((5678.53539136785 + WL) / (916.872991051482 + -1 * WL)))))
         H3_6 = tanh((-102.809790370196 + 0.947988221523862 * asinh((-6.15110225216742 + 0.222181057715337 * IP)) + 0.0269384263725257 * log(((-73 + SR) / (100.22 + -1 * SR))) + 0.822906537763512 * log(((-37.8030252237449 + FC) / (101 + -1 * FC))) + -1.57977718689651 * log(((-11 + MC) / (42.56 + -1 * MC))) + -0.201362577030743 * log(((-1.29 + ROD) / (1.92 + -1 * ROD))) + 52.2248070013057 * log(((5678.53539136785 + WL) / (916.872991051482 + -1 * WL)))))
         H3_7 = tanh((310.257088102366 + -0.793274995956179 * asinh((-6.15110225216742 + 0.222181057715337 * IP)) + 0.379234741675447 * log(((-73 + SR) / (100.22 + -1 * SR))) + 0.495229022296739 * log(((-37.8030252237449 + FC) / (101 + -1 * FC))) + 0.938714601905298 * log(((-11 + MC) / (42.56 + -1 * MC))) + 0.245610406405386 * log(((-1.29 + ROD) / (1.92 + -1 * ROD))) + -165.259405728951 * log(((5678.53539136785 + WL) / (916.872991051482 + -1 * WL)))))
         H3_8 = tanh((471.372790216941 + -0.811500932601311 * asinh((-6.15110225216742 + 0.222181057715337 * IP)) + -0.607114021921832 * log(((-73 + SR) / (100.22 + -1 * SR))) + -2.05958318991963 * log(((-37.8030252237449 + FC) / (101 + -1 * FC))) + -1.22698743325972 * log(((-11 + MC) / (42.56 + -1 * MC))) + -0.116614139464108 * log(((-1.29 + ROD) / (1.92 + -1 * ROD))) + -245.91778891003 * log(((5678.53539136785 + WL) / (916.872991051482 + -1 * WL)))))
         H3_9 = tanh((215.336988040832 + 1.33933075781881 * asinh((-6.15110225216742 + 0.222181057715337 * IP)) + -0.223070971523411 * log(((-73 + SR) / (100.22 + -1 * SR))) + 2.04379555397778 * log(((-37.8030252237449 + FC) / (101 + -1 * FC))) + -0.0683249406280067 * log(((-11 + MC) / (42.56 + -1 * MC))) + -1.25314992419078 * log(((-1.29 + ROD) / (1.92 + -1 * ROD))) + -116.869854980659 * log(((5678.53539136785 + WL) / (916.872991051482 + -1 * WL)))))
         H3_10 = tanh((247.047254609564 + 4.15084222397183 * asinh((-6.15110225216742 + 0.222181057715337 * IP)) + -1.09125772454473 * log(((-73 + SR) / (100.22 + -1 * SR))) + -2.30972468769097 * log(((-37.8030252237449 + FC) / (101 + -1 * FC))) + -1.7520916154522 * log(((-11 + MC) / (42.56 + -1 * MC))) + -4.01857653370927 * log(((-1.29 + ROD) / (1.92 + -1 * ROD))) + -127.100218639985 * log(((5678.53539136785 + WL) / (916.872991051482 + -1 * WL)))))
                #
         COH_Pred = 0.712687757391867 + 0.0162530106670883 * H3_1 + -0.611304824036782 * H3_10 + -0.523740058551597 * H3_2 + 1.24445879835346 * H3_3 + 0.973945586404473 * H3_4 + 0.635412007259911 * H3_5 + 0.430692285339638 * H3_6 + 1.32518608424177 * H3_7 + 0.994018867674986 * H3_8 + 0.323468566517323 * H3_9
         H4_1 = tanh((126.953792315662 + -0.899878729553033 * asinh((-6.15110225216742 + 0.222181057715337 * IP)) + -0.113463480889043 * log(((-73 + SR) / (100.22 + -1 * SR))) + 0.644014826077819 * log(((-37.8030252237449 + FC) / (101 + -1 * FC))) + -0.640098144522968 * log(((-11 + MC) / (42.56 + -1 * MC))) + 0.948597749631334 * log(((-1.29 + ROD) / (1.92 + -1 * ROD))) + -68.1064281588955 * log(((5678.53539136785 + WL) / (916.872991051482 + -1 * WL)))))
         H4_2 = tanh((160.845817654313 + 0.0327539415469679 * asinh((-6.15110225216742 + 0.222181057715337 * IP)) + 0.0278944597864314 * log(((-73 + SR) / (100.22 + -1 * SR))) + 0.206148328255711 * log(((-37.8030252237449 + FC) / (101 + -1 * FC))) + -1.43395509297723 * log(((-11 + MC) / (42.56 + -1 * MC))) + -0.546366389356557 * log(((-1.29 + ROD) / (1.92 + -1 * ROD))) + -85.1235189972184 * log(((5678.53539136785 + WL) / (916.872991051482 + -1 * WL)))))
         H4_3 = tanh((277.542436661722 + -2.9248309929939 * asinh((-6.15110225216742 + 0.222181057715337 * IP)) + 0.719738861346001 * log(((-73 + SR) / (100.22 + -1 * SR))) + 0.816852367719947 * log(((-37.8030252237449 + FC) / (101 + -1 * FC))) + -0.422146939789928 * log(((-11 + MC) / (42.56 + -1 * MC))) + 0.560183549036917 * log(((-1.29 + ROD) / (1.92 + -1 * ROD))) + -148.669500744407 * log(((5678.53539136785 + WL) / (916.872991051482 + -1 * WL)))))
         H4_4 = tanh((82.1756415256971 + 0.303564064416731 * asinh((-6.15110225216742 + 0.222181057715337 * IP)) + -0.14684699421645 * log(((-73 + SR) / (100.22 + -1 * SR))) + 0.684172285814332 * log(((-37.8030252237449 + FC) / (101 + -1 * FC))) + 2.71262773861388 * log(((-11 + MC) / (42.56 + -1 * MC))) + -0.218767456920025 * log(((-1.29 + ROD) / (1.92 + -1 * ROD))) + -43.4821982034683 * log(((5678.53539136785 + WL) / (916.872991051482 + -1 * WL)))))
         H4_5 = tanh((41.5518689906854 + -1.13104916563327 * asinh((-6.15110225216742 + 0.222181057715337 * IP)) + -0.208357912751549 * log(((-73 + SR) / (100.22 + -1 * SR))) + 0.773379145722031 * log(((-37.8030252237449 + FC) / (101 + -1 * FC))) + -1.23932725683784 * log(((-11 + MC) / (42.56 + -1 * MC))) + -0.311697898647039 * log(((-1.29 + ROD) / (1.92 + -1 * ROD))) + -21.5726571314369 * log(((5678.53539136785 + WL) / (916.872991051482 + -1 * WL)))))
         H4_6 = tanh((-222.00991379768 + 2.57446416959965 * asinh((-6.15110225216742 + 0.222181057715337 * IP)) + 0.141741046113073 * log(((-73 + SR) / (100.22 + -1 * SR))) + 0.56952041408056 * log(((-37.8030252237449 + FC) / (101 + -1 * FC))) + -0.685360115298092 * log(((-11 + MC) / (42.56 + -1 * MC))) + 1.73176884927566 * log(((-1.29 + ROD) / (1.92 + -1 * ROD))) + 116.696512429197 * log(((5678.53539136785 + WL) / (916.872991051482 + -1 * WL)))))
         H4_7 = tanh((-249.443175546508 + 0.318256271663616 * asinh((-6.15110225216742 + 0.222181057715337 * IP)) + -0.933758699579261 * log(((-73 + SR) / (100.22 + -1 * SR))) + 0.665927705417757 * log(((-37.8030252237449 + FC) / (101 + -1 * FC))) + 0.961104809976279 * log(((-11 + MC) / (42.56 + -1 * MC))) + -0.284450956502782 * log(((-1.29 + ROD) / (1.92 + -1 * ROD))) + 132.479382496159 * log(((5678.53539136785 + WL) / (916.872991051482 + -1 * WL)))))
         H4_8 = tanh((-416.226334131042 + -2.38621134826771 * asinh((-6.15110225216742 + 0.222181057715337 * IP)) + 0.28589763052818 * log(((-73 + SR) / (100.22 + -1 * SR))) + -0.827536678549197 * log(((-37.8030252237449 + FC) / (101 + -1 * FC))) + -0.529102324285139 * log(((-11 + MC) / (42.56 + -1 * MC))) + -0.501399380562628 * log(((-1.29 + ROD) / (1.92 + -1 * ROD))) + 220.689425845115 * log(((5678.53539136785 + WL) / (916.872991051482 + -1 * WL)))))
         H4_9 = tanh((-96.6134677388422 + -0.71012338061241 * asinh((-6.15110225216742 + 0.222181057715337 * IP)) + 0.428002478716759 * log(((-73 + SR) / (100.22 + -1 * SR))) + 0.225161898343048 * log(((-37.8030252237449 + FC) / (101 + -1 * FC))) + 0.802475181252694 * log(((-11 + MC) / (42.56 + -1 * MC))) + -0.902215344746379 * log(((-1.29 + ROD) / (1.92 + -1 * ROD))) + 50.4006462085115 * log(((5678.53539136785 + WL) / (916.872991051482 + -1 * WL)))))
         H4_10 = tanh((28.535999381478 + 0.922062284843418 * asinh((-6.15110225216742 + 0.222181057715337 * IP)) + 0.927719540487248 * log(((-73 + SR) / (100.22 + -1 * SR))) + -0.539573797559515 * log(((-37.8030252237449 + FC) / (101 + -1 * FC))) + -0.703340585181624 * log(((-11 + MC) / (42.56 + -1 * MC))) + 0.645182735494055 * log(((-1.29 + ROD) / (1.92 + -1 * ROD))) + -15.8172496318314 * log(((5678.53539136785 + WL) / (916.872991051482 + -1 * WL)))))
         PHI_Pred= 22.820502515408 + 2.31254282969617 * H4_1 + -4.52862642977753 * H4_10 + 15.4296183833079 * H4_2 + -4.77857422822139 * H4_3 + 7.58954850539402 * H4_4 + -23.3438176829593 * H4_5 + 4.0255958769485 * H4_6 + -6.19191806343352 * H4_7 + 8.75342168182563 * H4_8 + 0.444902469432059 * H4_9
         COH_Pred =round(COH_Pred,2)
         PHI_Pred =round(PHI_Pred,2)
        
        
         
         # code for Prediction
    
         predict1 = ''
         predict2 = ''
         # creating a button for Prediction
    
         if st.button('Prédiction'):
          predict1 = ("Terme de Cohésion du sol en bars est:",COH_Pred)
          predict2 = ("Angle de frottement du sol en degrés est:",PHI_Pred)
         st.success(predict1)
         st.success(predict2)
         
    else:
           
           if(Type=='UU'or Type=='CU'):
               
               
                FC = st.slider("Pourcentage des fines (passant au tamis 0.080 mm) Fc(%): ",25,74,key = 13) 
                WL = st.slider("Limite de Liquidité Wl(%): ",21,79,key = 23)
                IP = st.slider("Indice de Plasticité IP(%): ",4,39,key = 33)
                MC = st.slider("Teneur en eau naturelle W(%) : ",11.20,27.50,key = 43) 
                SR = st.slider("Degré de Saturation Sr(%) : ",52,100,key = 53) 
                ROD = st.slider("Masse volumique séche (g/cm3): ",1.55,1.92,key = 63)
                
                
                H5_1 = tanh((-19.7802457999034 + -1.60984534592833 * asinh((-27.5580476391638 + 0.651673834405395 * WL)) + 2.79607718898095 * asinh((-3.36087232926878 + 0.182739880195439 * IP)) + 0.909356808491053 * log(((-51.6546512218426 + SR) / (100.241731609338 + -1 * SR))) + 2.26499729677529 * log(((-22.2 + FC) / (74.46 + -1 * FC))) + -0.741869953339183 * log(((-11.11 + MC) / (30.58 + -1 * MC))) + -17.8878215393394 * log(((-1.12093249121382 + ROD) / (3.42547859607733 + -1 * ROD)))))
                H5_2 = tanh((12.9678886690727 + 0.984513483653368 * asinh((-27.5580476391638 + 0.651673834405395 * WL)) + -1.25182602268178 * asinh((-3.36087232926878 + 0.182739880195439 * IP)) + 0.295852073056382 * log(((-51.6546512218426 + SR) / (100.241731609338 + -1 * SR))) + 2.70513319830528 * log(((-22.2 + FC) / (74.46 + -1 * FC))) + -0.166415456396024 * log(((-11.11 + MC) / (30.58 + -1 * MC))) + 13.7018668830693 * log(((-1.12093249121382 + ROD) / (3.42547859607733 + -1 * ROD)))))
                H5_3 = tanh((8.68048660163938 + -1.18332490242903 * asinh((-27.5580476391638 + 0.651673834405395 * WL)) + 4.06845825700807 * asinh((-3.36087232926878 + 0.182739880195439 * IP)) + -1.24848675869542 * log(((-51.6546512218426 + SR) / (100.241731609338 + -1 * SR))) + -1.16058023412011 * log(((-22.2 + FC) / (74.46 + -1 * FC))) + 0.534185828599769 * log(((-11.11 + MC) / (30.58 + -1 * MC))) + 7.03653834264474 * log(((-1.12093249121382 + ROD) / (3.42547859607733 + -1 * ROD)))))
                H5_4 = tanh((-57.8762662737927 + -3.87302076691607 * asinh((-27.5580476391638 + 0.651673834405395 * WL)) + -0.529317271671223 * asinh((-3.36087232926878 + 0.182739880195439 * IP)) + -1.23918665831058 * log(((-51.6546512218426 + SR) / (100.241731609338 + -1 * SR))) + 1.99719235834295 * log(((-22.2 + FC) / (74.46 + -1 * FC))) + 2.00737829362033 * log(((-11.11 + MC) / (30.58 + -1 * MC))) + -51.2971010757331 * log(((-1.12093249121382 + ROD) / (3.42547859607733 + -1 * ROD)))))

                COH_Pred = 0.246082630950255 + 0.639273155054735 * H5_1 + -0.0360343823306046 * H5_2 + 0.0920002412203196 * H5_3 + -0.607344988063681 * H5_4
                #
                H6_1 = tanh((0.201118238005368 + 0.0175037214342317 * asinh((-27.5580476391638 + 0.651673834405395 * WL)) + 0.70073733776747 * asinh((-3.36087232926878 + 0.182739880195439 * IP)) + 0.00154764426820439 * log(((-51.6546512218426 + SR) / (100.241731609338 + -1 * SR))) + -0.0707015603819756 * log(((-22.2 + FC) / (74.46 + -1 * FC))) + 0.00742889172947301 * log(((-11.11 + MC) / (30.58 + -1 * MC))) + -0.332538130785024 * log(((-1.12093249121382 + ROD) / (3.42547859607733 + -1 * ROD)))))
                H6_2 = tanh((-2.82040118970591 + 0.323069007908259 * asinh((-27.5580476391638 + 0.651673834405395 * WL)) + -0.20052397106075 * asinh((-3.36087232926878 + 0.182739880195439 * IP)) + 0.209723823817174 * log(((-51.6546512218426 + SR) / (100.241731609338 + -1 * SR))) + 0.0520381386729724 * log(((-22.2 + FC) / (74.46 + -1 * FC))) + -0.955676640920639 * log(((-11.11 + MC) / (30.58 + -1 * MC))) + -1.13922485832781 * log(((-1.12093249121382 + ROD) / (3.42547859607733 + -1 * ROD)))))
                H6_3 = tanh((-5.44986622685673 + -0.532565942626136 * asinh((-27.5580476391638 + 0.651673834405395 * WL)) + 0.632465244945195 * asinh((-3.36087232926878 + 0.182739880195439 * IP)) + -0.407643450911617 * log(((-51.6546512218426 + SR) / (100.241731609338 + -1 * SR))) + 1.27155542956521 * log(((-22.2 + FC) / (74.46 + -1 * FC))) + -0.54876689070574 * log(((-11.11 + MC) / (30.58 + -1 * MC))) + -3.97128071895416 * log(((-1.12093249121382 + ROD) / (3.42547859607733 + -1 * ROD)))))
                H6_4 = tanh((3.0093813665044 + 0.537310935200807 * asinh((-27.5580476391638 + 0.651673834405395 * WL)) + -0.239907591105988 * asinh((-3.36087232926878 + 0.182739880195439 * IP)) + 0.314247356102684 * log(((-51.6546512218426 + SR) / (100.241731609338 + -1 * SR))) + -0.697474504258505 * log(((-22.2 + FC) / (74.46 + -1 * FC))) + -0.255579955574441 * log(((-11.11 + MC) / (30.58 + -1 * MC))) + 2.73139488563692 * log(((-1.12093249121382 + ROD) / (3.42547859607733 + -1 * ROD)))))
                H6_5 = tanh((-1.70571251430027 + 0.00897830776543651 * asinh((-27.5580476391638 + 0.651673834405395 * WL)) + 0.485115380820045 * asinh((-3.36087232926878 + 0.182739880195439 * IP)) + 0.110085760386834 * log(((-51.6546512218426 + SR) / (100.241731609338 + -1 * SR))) + -0.0164603107474388 * log(((-22.2 + FC) / (74.46 + -1 * FC))) + -0.23000824006547 * log(((-11.11 + MC) / (30.58 + -1 * MC))) + -1.27998204885813 * log(((-1.12093249121382 + ROD) / (3.42547859607733 + -1 * ROD)))))
            
                PHI_Pred = 16.0821019081896 + -17.8627819801435 * H6_1 + -19.5567220891732 * H6_2 + 12.4079096067161 * H6_3 + 13.2208904296179 * H6_4 + 13.9839962303599 * H6_5
                
                COH_Pred =round(COH_Pred,2)
                PHI_Pred =round(PHI_Pred,2)
                
                if COH_Pred < 0:
                   COH_Pred = 0
                else:
                    COH_Pred = COH_Pred
                if PHI_Pred < 0:
                   PHI_Pred = 0
                else:
                    PHI_Pred = PHI_Pred
                
                predict1 = ''
                predict2 = ''
                # creating a button for Prediction
    
                if st.button('Prédiction'):
                 predict1 = ("Terme de Cohésion du sol en bars est:",COH_Pred)
                 predict2 = ("Angle de frottement du sol en degrés est:",PHI_Pred)
                st.success(predict1)
                st.success(predict2)
           
           
           else:
               
                FC = st.slider("Pourcentage des fines (passant au tamis 0.080 mm) Fc(%): ",29,47,key = 14) 
                WL = st.slider("Limite de Liquidité Wl(%): ",30,53,key = 24)
                IP = st.slider("Indice de Plasticité IP(%): ",15,26,key = 34)
                MC = st.slider("Teneur en eau naturelle W(%) : ",10,21,key = 44) 
                SR = st.slider("Degré de Saturation Sr(%) : ",16,100,key = 54) 
                ROD = st.slider("Masse volumique séche (g/cm3): ",1.65,1.97,key = 64)
                
                H7_1 = tanh((-56.8554410572928 + 0.264000092453201 * asinh((-7410.59214685082 + 71.9167479034667 * SR)) + 1.62152379128569 * asinh((-50.0397680320744 + 3.72190510097577 * IP)) + 0.149839767080997 * log(((-28 + WL) / (56.6 + -1 * WL))) + -0.59947035591697 * log(((-7.91434817785376 + FC) / (47.0514612590705 + -1 * FC))) + -1.64393627065333 * log(((-1.62 + ROD) / (1.98 + -1 * ROD))) + -13.0124723530578 * log(((31.1381707022798 + MC) / (2867.57806229012 + -1 * MC)))))
                H7_2 = tanh((54.8475062770736 + -1.4507959353081 * asinh((-7410.59214685082 + 71.9167479034667 * SR)) + -1.4132198345904 * asinh((-50.0397680320744 + 3.72190510097577 * IP)) + -0.395968050961352 * log(((-28 + WL) / (56.6 + -1 * WL))) + 1.50691390414062 * log(((-7.91434817785376 + FC) / (47.0514612590705 + -1 * FC))) + 0.934968898786361 * log(((-1.62 + ROD) / (1.98 + -1 * ROD))) + 15.742491643657 * log(((31.1381707022798 + MC) / (2867.57806229012 + -1 * MC)))))
                H7_3 = tanh((90.3137988734307 + -0.951323305401283 * asinh((-7410.59214685082 + 71.9167479034667 * SR)) + -2.19053208852454 * asinh((-50.0397680320744 + 3.72190510097577 * IP)) + -0.361944302605043 * log(((-28 + WL) / (56.6 + -1 * WL))) + 0.35321709828088 * log(((-7.91434817785376 + FC) / (47.0514612590705 + -1 * FC))) + 0.144236659655546 * log(((-1.62 + ROD) / (1.98 + -1 * ROD))) + 21.8321913060376 * log(((31.1381707022798 + MC) / (2867.57806229012 + -1 * MC)))))
                H7_4 = tanh((86.3307415161543 + -1.75905269831774 * asinh((-7410.59214685082 + 71.9167479034667 * SR)) + -2.59448245464008 * asinh((-50.0397680320744 + 3.72190510097577 * IP)) + -0.651939322201127 * log(((-28 + WL) / (56.6 + -1 * WL))) + 0.433595166476188 * log(((-7.91434817785376 + FC) / (47.0514612590705 + -1 * FC))) + 0.00835923206820621 * log(((-1.62 + ROD) / (1.98 + -1 * ROD))) + 22.382093517224 * log(((31.1381707022798 + MC) / (2867.57806229012 + -1 * MC)))))
                H7_5 = tanh((141.502308162158 + 0.607702886627413 * asinh((-7410.59214685082 + 71.9167479034667 * SR)) + -4.36134080782972 * asinh((-50.0397680320744 + 3.72190510097577 * IP)) + -0.120557321958971 * log(((-28 + WL) / (56.6 + -1 * WL))) + -0.604085259703209 * log(((-7.91434817785376 + FC) / (47.0514612590705 + -1 * FC))) + -0.61797711433679 * log(((-1.62 + ROD) / (1.98 + -1 * ROD))) + 28.9753617421717 * log(((31.1381707022798 + MC) / (2867.57806229012 + -1 * MC)))))
                H7_6 = tanh((-11.0826461744471 + -0.54139695656695 * asinh((-7410.59214685082 + 71.9167479034667 * SR)) + -0.11536271490557 * asinh((-50.0397680320744 + 3.72190510097577 * IP)) + -1.10571921489659 * log(((-28 + WL) / (56.6 + -1 * WL))) + 0.869019668553374 * log(((-7.91434817785376 + FC) / (47.0514612590705 + -1 * FC))) + -0.786905953421451 * log(((-1.62 + ROD) / (1.98 + -1 * ROD))) + -1.06668097221976 * log(((31.1381707022798 + MC) / (2867.57806229012 + -1 * MC)))))

                COH_Pred = 0.10763235555145 + -0.336069728875435 * H7_1 + -0.307928906626545 * H7_2 + 0.669105912548888 * H7_3 + -0.487637655211735 * H7_4 + -0.231010663779483 * H7_5 + 0.380542378463561 * H7_6
                #
                H8_1 = tanh((-28.4610577859709 + 2.65906617364918 * asinh((-7410.59214685082 + 71.9167479034667 * SR)) + -1.77218442073586 * asinh((-50.0397680320744 + 3.72190510097577 * IP)) + 1.45278118751115 * log(((-28 + WL) / (56.6 + -1 * WL))) + -1.88341660106609 * log(((-7.91434817785376 + FC) / (47.0514612590705 + -1 * FC))) + 2.65657117547662 * log(((-1.62 + ROD) / (1.98 + -1 * ROD))) + -14.8556819122502 * log(((31.1381707022798 + MC) / (2867.57806229012 + -1 * MC)))))
                H8_2 = tanh((266.680077499101 + 6.26268958090784 * asinh((-7410.59214685082 + 71.9167479034667 * SR)) + 3.89825712334401 * asinh((-50.0397680320744 + 3.72190510097577 * IP)) + -3.10704842772345 * log(((-28 + WL) / (56.6 + -1 * WL))) + 0.218768921933584 * log(((-7.91434817785376 + FC) / (47.0514612590705 + -1 * FC))) + -0.391463951070374 * log(((-1.62 + ROD) / (1.98 + -1 * ROD))) + 57.3045122700847 * log(((31.1381707022798 + MC) / (2867.57806229012 + -1 * MC)))))
                H8_3 = tanh((93.2052039274017 + 1.89221534324715 * asinh((-7410.59214685082 + 71.9167479034667 * SR)) + 4.04742214499999 * asinh((-50.0397680320744 + 3.72190510097577 * IP)) + 4.5326031815446 * log(((-28 + WL) / (56.6 + -1 * WL))) + -0.21584842068355 * log(((-7.91434817785376 + FC) / (47.0514612590705 + -1 * FC))) + 1.65690870169738 * log(((-1.62 + ROD) / (1.98 + -1 * ROD))) + 20.5495675500511 * log(((31.1381707022798 + MC) / (2867.57806229012 + -1 * MC)))))
                
                H8_4 = tanh((-202.576112047416 + -1.9474658281945 * asinh((-7410.59214685082 + 71.9167479034667 * SR)) + 4.66226073140057 * asinh((-50.0397680320744 + 3.72190510097577 * IP)) + -1.69252189753594 * log(((-28 + WL) / (56.6 + -1 * WL))) + -0.920554608619591 * log(((-7.91434817785376 + FC) / (47.0514612590705 + -1 * FC))) + -1.06354832482039 * log(((-1.62 + ROD) / (1.98 + -1 * ROD))) + -41.9054315438332 * log(((31.1381707022798 + MC) / (2867.57806229012 + -1 * MC)))))
                H8_5 = tanh((-183.733987830584 + -6.10752584758945 * asinh((-7410.59214685082 + 71.9167479034667 * SR)) + -1.78265930126027 * asinh((-50.0397680320744 + 3.72190510097577 * IP)) + 0.137221107430952 * log(((-28 + WL) / (56.6 + -1 * WL))) + 2.73210627351068 * log(((-7.91434817785376 + FC) / (47.0514612590705 + -1 * FC))) + 0.307643663575499 * log(((-1.62 + ROD) / (1.98 + -1 * ROD))) + -32.579226294671 * log(((31.1381707022798 + MC) / (2867.57806229012 + -1 * MC)))))
                H8_6 = tanh((-90.2436038082867 + 5.71470069285215 * asinh((-7410.59214685082 + 71.9167479034667 * SR)) + 5.08199704692214 * asinh((-50.0397680320744 + 3.72190510097577 * IP)) + -0.766582088983712 * log(((-28 + WL) / (56.6 + -1 * WL))) + 0.126121003782704 * log(((-7.91434817785376 + FC) / (47.0514612590705 + -1 * FC))) + 2.47932328032076 * log(((-1.62 + ROD) / (1.98 + -1 * ROD))) + -27.6228068832317 * log(((31.1381707022798 + MC) / (2867.57806229012 + -1 * MC)))))
                PHI_Pred = 15.9450166447538 + 3.71220684926112 * H8_1 + -6.60678261545135 * H8_2 + 2.61059953403851 * H8_3 + -10.1973876047391 * H8_4 + 4.25862114970919 * H8_5 + -3.728639157326 * H8_6
                
                if COH_Pred < 0:
                   COH_Pred = 0
                else:
                    COH_Pred = COH_Pred
                if PHI_Pred < 0:
                   PHI_Pred = 0
                else:
                    PHI_Pred = PHI_Pred
                
                COH_Pred =round(COH_Pred,2)
                PHI_Pred =round(PHI_Pred,2)
                
                predict1 = ''
                predict2 = ''
                # creating a button for Prediction
    
                if st.button('Prédiction'):
                 predict1 = ("Terme de Cohésion du sol en bars est:",COH_Pred)
                 predict2 = ("Angle de frottement du sol en degrés est:",PHI_Pred)
                st.success(predict1)
                st.success(predict2)
               
               #st.write('pas de database fiable pour le sable en CD inchallah une mise a jour dans un future proche')       
    
if __name__ == '__main__':
    main()            
#            
            
    
         
         
         
    
    

  
    
    
    
    
    
    
    
    
    
    
    
    
  
    
  