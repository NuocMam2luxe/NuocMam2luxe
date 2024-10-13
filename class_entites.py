# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class enemy():
    def __init__(self,hp,vit,vit_atk,atk):
        self.vie=hp
        self.vitesse=vit
        self.vitesse_attaque=vit_atk
        self.attaque=atk
        
    def prend_degat(): # Tom: ??? C'est les towers qui vont définir combien de dégâts ils vont prendre
        pass
    
    def regen():
        pass
    
    def trame():
        pass
    
    def anim_marche():
        pass
    
    def anim_atk():
        pass
    
    def etat():
        pass
    
    def anim_etat():
        pass

#------------------------------------------------------------

class tower():
    def __init__(self,hp,vit_atk,atk):
        self.vie=hp
        self.vitesse_attaque=vit_atk
        self.attaque=atk
        
    def prend_degat():# Tom: ??? C'est les ennemis qui vont définir combien de dégâts ils vont prendre
        pass
    
    def regen():
        pass
    
    def anim_atk():
        pass
    
    def etat():
        pass
    
    def anim_etat():
        pass
