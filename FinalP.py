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
        
    def shell(self,k=0):
        self.number=self.number+1
        nombre=str()
        if self.number==1 and k==0:
            print(f"Bienvenido a la 'Shell' de Store, en caso de necesitar ayuda, escribe: help_")
            print('Agrega tu nombre')
            nombre=input()
            self.user=nombre
            print("*"*50)
            print("Por favor agrega una entrada: \n >")
            entrada=input()
        elif self.number==2 and k==0:
            print("Por favor agrega una entrada: \n >")
            entrada=input()
        elif self.number>2 and k==0:
            print(">")
            entrada=input()
        elif k!=0:
            print('Agregue su modificación')
            print('e.g name=Mazorca price=500 quantity=133')
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
        
    def show(self,args):
        """
        """
        for i in self.products:
            #print(i,args[0])
            j=0
            j=j+1
            if i['name']==args[0]:
                u1,u2,u3 = [], [], []
                u1.append(i.get('name'))
                u2.append(i.get('price'))
                u3.append(i.get('quantity'))
                dat={'Name':u1,'Price':u2,'Quantity':u3}
                df=pd.DataFrame(data=dat)
                print(df)
                break
            elif j==len(self.products) and i['name']==args[0]:
                print(f'No hay ningun {args[0]}')
                break
    def edit(self, args):
        """
        """
        Store.show(self,args)
        for i in self.products:
            if i['name']==args[0]:
                entrada=Store.shell(self,1)
                c=Store.de_listas_a_diccionarios(entrada)
                i['name']=c['name']
                i['price']=c['price']
                i['quantity']=c['quantity']
                Store.show(self, [i['name']])
                print('Actualización Exitosa')
                break
    def delete(self, args):
        """
        """
        for i in self.products:
            if i['name']==args[0]:
                self.products.remove(i)
                break 
        print('Actualización Exitosa')
        Store.all(self,args)
        
    def aux_functions(self, args):
        """
        esta funcion llama a otras funciones de la clase si la primera
        entrada de la lista corresponde con el nombre de un metodo de la clase. 
        """
        try:
            getattr(self,args[0])(args[1::])
        except Exception as ex:
            pass 
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
            return df
              
    def help_(self, args):
        print('Estas son las funciones de Shell Store:\n')
        print('exit ---> salir del programa\n add ---> agregar productos e.g name=Mazorca price=500 quantity=133\n all ---> conocer todas las existencias')
        print('show ---> muestra las exixtencias de un producto\n edit ---> Edita las existencias de un producto seleccionado\n delete ---> borra un producto')
        

    
my_store = Store()
my_store.aux_functions(['add', 'name=a', 'price=12', 'quantity=15'])
my_store.aux_functions(['add', 'name=b', 'price=10', 'quantity=25'])

my_store.aux_functions(['show','a'])
while my_store.loop:
    entrada=my_store.shell()
    my_store.aux_functions(entrada)