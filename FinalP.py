# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 20:36:19 2020

@author: Juan Pablo Nicolás
"""
import pandas as pd 
class Store:
    
    def __init__(self, products=[], loop=True):
        self.products=products
        self.loop=loop
        self.number=0
        self.user='Default'
        
    @staticmethod
    def de_listas_a_diccionarios(lista):
      dic={}
      for i in lista:
        c = i.split('=')
        dic[c[0]]=c[1]  
      return dic
        
    def shell(self):
        self.number=self.number+1
        nombre=str()
        if self.number==1:
            print(f"Bienvenido a la 'Shell' de Store, en caso de necesitar ayuda, escribe: help_")
            print('Agrega tu nombre')
            nombre=input()
            self.user=nombre
            print("*"*50)
            print("Por favor agrega una entrada: \n >")
            entrada=input()
        else:
            print("Por favor agrega una entrada: \n >")
            entrada=input()
        
        return entrada.split()    

    def exit(self,args):
        self.loop = False 
        print(f'{self.user} ha terminado la ejecucion del programa')
        
    def add(self,args):
        dic={}
        dic=Store.de_listas_a_diccionarios(args)
        a , b, c = dic['name'], dic['price'], dic['quantity']
        self.products.append(dic)
        print(f'Se han agregado {c} unidades de {a}')
        
    def aux_functions(self, args):
        """
        esta función se encarga de llamar a otras funciones,
        si la lista que se le pase como arguemento contiene en la primera posición el nombre de la función 
        """
        getattr(self,args[0])(args[1::])
        
    def all(self,args):
        if self.products==[]:
            print('Aun no se han agregado productos')
        else: 
            u1,u2,u3 = [], [], []
            for i in self.products:
                u1.append(i.get('name'))
                u2.append(i.get('price'))
                u3.append(i.get('quantity'))
            dat={'Name':u1,'Price':u2,'Quantity':u3}
            df=pd.DataFrame(data=dat)
            print(df)
            
    def help_(self, args):
        print('Estas son las funciones de Shell Store:\n')
        print('exit ---> salir del programa\n add ---> agregar productos e.g name=Mazorca price=500 quantity=133\n all ---> conocer todas las existencias')
    
my_store = Store()
while my_store.loop:
    entrada=my_store.shell()
    try:
        my_store.aux_functions(entrada)
    except AttributeError:
        pass
