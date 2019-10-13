
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.pylab as pl  #colores del plot
import scipy




class patata:
    def __init__(self,ia,ja,numPath,v):
        self.ia=ia
        self.ja=ja
        self.numPath=numPath
        self.dir_allow=v
        self.doMe=True
        
    def setBool(self,value):
        self.doMe=value
        
    def giveCredit(self,x):
        self.credit=x

def call_next(vector,i):
  vector[i].doMe=False
  if((i+1)>=len(vector)):
    for j in range(len(vector)):
      vector[j].doMe=True

def hell(snake, direction,rows,columns,init_points,index):
  came_from=(direction+2)%4  
  snake.dir_allow[came_from]=1 #en la contraria
  snake.dir_allow[direction]=1
  for i in range(4):
    if(i!=came_from and i!=direction): #las que acabas de prohibir
      if(i==0):
        if(snake.ja<columns and (snake.ia!=init_points[index][0] or (snake.ja+2)!=init_points[index][1])):
            snake.dir_allow[i]=0
        else:
          snake.dir_allow[i]=1       
      elif(i==1):
          if (snake.ia>0 and ((snake.ia-2)!=init_points[index][0] or (snake.ja)!=init_points[index][1])):  
              snake.dir_allow[i]=0
          else:
              snake.dir_allow[i]=1
      elif(i==2):
          if(snake.ja>0 and (snake.ia!=init_points[index][0] or (snake.ja-2)!=init_points[index][1])):
              snake.dir_allow[i]=0
          else:
              snake.dir_allow[i]=1
      elif(i==3):
          if(snake.ia<rows and ((snake.ia+2)!=init_points[index][0] or (snake.ja)!=init_points[index][1])):
              snake.dir_allow[i]=0
          else:
              snake.dir_allow[i]=1
  if(sum(snake.dir_allow)==4):
      snake.dir_allow[came_from]=0
      
def hell0(snake, direction,rows,columns,init_points,A):
  came_from=(direction+2)%4  
  snake.dir_allow[came_from]=1 #en la contraria
  snake.dir_allow[direction]=1
  for i in range(4):
    if(i!=came_from and i!=direction): #las que acabas de prohibir
      if(i==0):
          if(snake.ja<columns):
              ob=A[snake.ia][snake.ja+2]
              if(ob!=0 and ob!=snake.numPath):
                  if(snake.credit>=1 or ob==1):
                      snake.dir_allow[i]=0
                  else:
                      snake.dir_allow[i]=1
              else:
                  snake.dir_allow[i]=1
          else:
              snake.dir_allow[i]=1
      if(i==1):
          if(snake.ia>0):
              ob=A[snake.ia-2][snake.ja]
              if(ob!=0 and ob!=snake.numPath):
                  if(snake.credit>=1 or ob==1):
                      snake.dir_allow[i]=0
                  else:
                      snake.dir_allow[i]=1
              else:
                  snake.dir_allow[i]=1
          else:
              snake.dir_allow[i]=1
      if(i==2):
          if(snake.ja>0):
              ob=A[snake.ia][snake.ja-2]
              if(ob!=0 and ob!=snake.numPath):
                  if(snake.credit>=1 or ob==1):
                      snake.dir_allow[i]=0
                  else:
                      snake.dir_allow[i]=1
              else:
                  snake.dir_allow[i]=1
          else:
              snake.dir_allow[i]=1                   
      if(i==3):
          if(snake.ia<rows):
              ob=A[snake.ia+2][snake.ja]
              if(ob!=0 and ob!=snake.numPath):
                  if(snake.credit>=1 or ob==1):
                      snake.dir_allow[i]=0
                  else:
                      snake.dir_allow[i]=1
              else:
                  snake.dir_allow[i]=1
          else:
              snake.dir_allow[i]=1

        
def doMovement(A,direction,num_steps,snake,convergence):
  if(direction%2==0):
    for i in range(1,num_steps+1):
      found=A[snake.ia][snake.ja+(1-direction)*i]
      if (found!=1 and found!=snake.numPath): #NO SETEADO PARA N
        if(len(convergence)>1):
            convergence[int(min(found,snake.numPath))-2]=True
        else:
            convergence[0]=True
        break
      else:
        A[snake.ia][snake.ja+(1-direction)*i]=snake.numPath
    snake.ja=snake.ja+(1-direction)*num_steps  
  else:
    for i in range(1,num_steps+1):
      found=A[snake.ia+(direction-2)*i][snake.ja]
      if (found!=1 and found!=snake.numPath): #NO SETEADO PARA N
        if(len(convergence)>1):
            convergence[int(min(found,snake.numPath))-2]=True
        else:
            convergence[0]=True
        break
      else:
        A[snake.ia+(direction-2)*i][snake.ja]=snake.numPath
    snake.ia=snake.ia+(direction-2)*num_steps  
  
  return [A,convergence]


def chooseDir(snake):
  my_list = []
  for i in range(4): 
    if (snake.dir_allow[i]==0):
      my_list.append(i)
  if(len(my_list)==0):
      print('fuck, no hay direcciones posibles')
      return -1
  random.shuffle(my_list)
  return my_list[0]



def chooseSteps(A,direction,snake,index,init_points):
  steps = 1
  while (not steps%2==0):
    if (not direction%2):
      if (direction==0):
        if(snake.ia!=init_points[index][0] or snake.ja>init_points[index][1]):
          var=columns-snake.ja
        else:
            var=init_points[index][1]-snake.ja       
        if(var>2 ):
            var=var-2
        if(var==0):
            var=2

        steps = random.randint(2,var)
      else:
        if(snake.ia!=init_points[index][0] or snake.ja<init_points[index][1]):
          var=snake.ja
        else:
            var=snake.ja -init_points[index][1]
        if(var>2):
            var=var-2
        if(var==0):
            var=2

        steps = random.randint(2,var)
    else:
      if (direction == 1):
        if(snake.ja!=init_points[index][1] or snake.ia<init_points[index][0]):  
          var=snake.ia
        else:
            var=snake.ia-init_points[index][0]
        if(var>2):
            var=var-2
        if(var==0):
            var=2

        steps = random.randint(2,var)
      else:
        if(snake.ja!=init_points[index][1] or snake.ia>init_points[index][0]):  
          var=rows-snake.ia
        else:
            var=-snake.ia+init_points[index][0]
        if(var>2):
            var=var-2
        if(var==0):
            var=2
        
        if ((not var%2) and var>2):
            steps = random.randint(2,var/2) #modif. chun
        else:
            steps = random.randint(2,var) #modif. chun
  return steps
  

def bucle(x,y,snake,A,row,cols):
    pasitos=2
    ob=A[snake.ia+x*pasitos][snake.ja+y*pasitos]
    if(not x):
        number=cols*(1+y)/2-y*snake.ja
    if(not y):
        number=rows*(1+x)/2-x*snake.ia
    while(pasitos<number):
        if(ob==0 or ob==snake.numPath):
            pasitos=pasitos-2
            break
        elif(ob!=1 and snake.credit==0):
            pasitos=pasitos-2
            break
        elif(ob!=1 and snake.credit>0):
            pasitos=pasitos+2
            snake.credit=snake.credit-1
        elif(ob==1):
            pasitos=pasitos+2
    return pasitos

def stepsRestricted(snake,direction,A,row,cols):
    pas=0
    if(direction==0):
        pas=bucle(0,1,snake,A,row,cols)
    if(direction==1):
        pas=bucle(-1,0,snake,A,row,cols)
    if(direction==2):
        pas=bucle(0,-1,snake,A,row,cols)
    if(direction==3):
        pas=bucle(1,0,snake,A,row,cols)
    if(pas==2):
        return pas
    elif((not pas%4) and pas>4):
        return ((random.randint(1,pas/4))*2) #modif. chun
    else:
        return ((random.randint(1,pas/2))*2)





def allowed(points,rows,columns):
    ia=points[0];ja=points[1]
    v=np.zeros(4)
    if(ia==0):
        v[1]=1
    elif(ia==rows):
        v[3]=1
    if(ja==0):
        v[2]=1
    elif(ja==columns):
        v[0]=1
    return v



def initialize(rows,columns,n_exits,init_points):
    A = np.ones((rows+1,columns+1))
    vector=[]
    for i in range(n_exits):
        vector.append(patata(init_points[i][0],init_points[i][1],2+i,allowed(init_points[i],rows,columns)))
        A[init_points[i][0]][init_points[i][1]]=vector[i].numPath
    return [A,vector]

def phase1(A, vector, rows,columns,init_points,n_paths):
  convergence=[False for x in range(n_paths-1)]
  while (sum(convergence)<n_paths-1):
    for i in range(len(vector)):
      if(vector[i].doMe):
        break
    snake=vector[i]
#    print('hola soy numpath ',snake.numPath)
#    print('buenas estoy en ',snake.ia,snake.ja)
    direction = chooseDir(snake)
#    print('voy hacia ', direction)
    num_steps=chooseSteps(A,direction,snake,i,init_points)
#    print('dando ',num_steps, 'pasos')
    aws=doMovement(A,direction,num_steps,snake,convergence)
    A=aws[0]
    convergence=aws[1]
    hell(snake, direction,rows,columns,init_points,i)
    call_next(vector,i)
        
  return A

def sweep(A,rows,colums,select,put,cleanall):
    for i in range(columns+1):
        for j in range(rows+1):
            if(cleanall==True):
                if(A[j][i]!=1):
                    A[j][i]=0
            else:
                if(A[j][i]==select): 
                    A[j][i]=put 
    return A



def pickIJ(rows,cols):
    i=random.randint(0,rows/2)
    j=random.randint(0,cols/2)
    return [i*2,j*2]

def finalMess(rows,cols,A):
    for i in range(0,rows+1,2):
        for j in range(0,cols+1,2):
            if(A[i][j]):
                A=doPath1(A,[[i,j]],rows,cols)
    return A
                
           

def path0Allowed(rows,cols,i,j,A):
    v=allowed([i,j],rows,cols)
    index=0
    if(v[index]==0):
        if((not A[i][j+1]) or (not A[i][j+2])):
            v[index]=1
    index=1
    if(v[index]==0):
        if((not A[i-1][j]) or (not A[i-2][j])):
            v[index]=1
    index=2
    if(v[index]==0):
        if((not A[i][j-1]) or (not A[i][j-2])):
            v[index]=1
    index=3
    if(v[index]==0):
        if((not A[i+1][j]) or (not A[i+2][j])):
            v[index]=1
    if(sum(v)==4):
        return [False,0]
    else:
        return [True,v]
    
def doPath1(A,init_points,rows,cols):
    vector=[patata(init_points[0][0],init_points[0][1],2,allowed([init_points[0][0],init_points[0][1]],rows,cols))]
    A[vector[0].ia][vector[0].ja]=vector[0].numPath
    A=phase1(A, vector, rows,columns,init_points,2) 
    A=sweep(A,rows,cols,2,0,False)
    return A
  
def doMovementMod(snake,A,num_steps,direction):   
  if(direction%2==0):
    for i in range(1,num_steps+1):
        A[snake.ia][snake.ja+(1-direction)*i]=snake.numPath
    snake.ja=snake.ja+(1-direction)*num_steps  
  else:
    for i in range(1,num_steps+1):
        A[snake.ia+(direction-2)*i][snake.ja]=snake.numPath
    snake.ia=snake.ia+(direction-2)*num_steps   
  return A



def doPath0(i,j,disp,num_4_class,credit,row,cols,A):
    snake=patata(i,j,num_4_class,disp) #se puede sacar del vector si las funciones las hacemos nuevas
    snake.giveCredit(random.randint(0,credit))
    while(sum(snake.dir_allow)<4):
        direction=chooseDir(snake)
        num_steps=stepsRestricted(snake,direction,A,row,cols)
        A=doMovementMod(snake,A,num_steps,direction)#actualiza ia,ja
        hell0(snake,direction,rows,cols,[i,j],A)#ok
    return A
        
    
def doPaths(i,j,A,count,rows,cols,numPaths_created,credit):
    if(A[i][j]==0):
        check=path0Allowed(rows,cols,i,j,A)
        if(check[0]):
            A=doPath0(i,j,check[1],numPaths_created,credit,rows,cols,A)
            numPaths_created=numPaths_created+1
            count=0
        else:
            count=count+1
    elif(A[i][j]==1):
        A=doPath1(A,[[i,j]],rows,cols)
        count=0
    else:
        count=count+1
    return [A,count,numPaths_created]

def liala(D,A,rows,columns,credit):
    count=0
    numPaths_created=3
    while(count<D):
        ax=pickIJ(rows,columns)
        my_i=ax[0]
        my_j=ax[1]
        aux2=doPaths(my_i,my_j,A,count,rows,columns,numPaths_created,credit)
        A=aux2[0]
        count=aux2[1]
        numPaths_created=aux2[2]
    A=sweep(A,rows,columns,1,0,True)
    A=finalMess(rows,columns,A)
    return A


def show_maze(A,rows,columns,init_points,save=False,name=""):
    A[init_points[0][0]][init_points[0][1]]=0.7
    for i in range(1,len(init_points)):
        A[init_points[i][0]][init_points[i][1]]=0.3
    B=np.ones((rows+3,columns+3))
    B[1:1+A.shape[0],1:1+A.shape[1]]=A
    frame1=plt.gca()
    frame1.set_aspect('equal', adjustable='box')
    frame1.axes.get_xaxis().set_visible(False)
    frame1.axes.get_yaxis().set_visible(False)
    plt.pcolormesh(B,cmap='binary')
    x=[]; y=[]
    for i in range(len(init_points)):
        y.append(init_points[i][0]+1.5)
        x.append(init_points[i][1]+1.5)
    colors = pl.cm.jet(np.linspace(0,1,len(init_points)))
    plt.scatter(x,y,c=colors)
    
    if(save):
        plt.savefig(name+'.png',dpi=300, bbox_inches='tight')
        f= open(name+'.txt',"w+")
        for i in range(rows+3):
            for j in range(columns+3):
                f.write('%d ' % B[i][j])
            f.write('\n')
        f.close()
    plt.show()



'''------------------------------------------------------'''
#Parameters:modify me!
rows = 60
columns = 60
n_paths=6
init_points=[[0,0],[0,columns],[rows,0],[0,30],[rows,30],[rows,columns]]
saving=False
name='ex1'


'''----'''
#Don't touch! Enjoy
par=initialize(rows,columns,n_paths,init_points)
A=par[0]
vector=par[1]
A=phase1(A, vector, rows,columns,init_points,n_paths)
A=liala(1,A,rows,columns,2)
show_maze(A,rows,columns,init_points,saving,name)

























