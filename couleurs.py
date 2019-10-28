"""
Module de couleurs répertoriant quelques constantes de couleurs RGB/RVB
ainsi que des fonctions simple manipulant ces couleurs RGB/RVB
"""

from random import randint
from math import exp,log


# CONSTANTE DE COULEURS RGB

BLEU       = (  0,  0,255)
ROUGE      = (255,  0,  0)
VERT       = (  0,255,  0)
VERT_FONCE = (  0,100,  0)
NOIR       = (  0,  0,  0)
BLANC      = (255,255,255)
JAUNE      = (255,255,  0)
VIOLET     = (100,  0,100)
ORANGE     = (255,200,  0)
ROSE       = (255,192,203)

BLUE       = (  0,  0,255)
RED        = (255,  0,  0)
GREEN      = (  0,255,  0)
YELLOW     = (255,255,  0)
BLACK      = (  0,  0,  0)
WHITE      = (255,255,255)
GREY       = (100,100,100)
PURPLE     = (100,  0,100)
ORANGE     = (255,165,  0)
HALFGREY   = ( 50, 50, 50)
DARKGREY   = ( 20, 20, 20)
DARKRED    = ( 10, 10, 10)
DARKGREEN  = ( 10, 10, 10)
DARKBLUE   = ( 10, 10, 10)
LIGHTRED   = (255,200,200)
LIGHTGREEN = (200,255,200)
LIGHTBLUE  = (200,200,255)
LIGHTBROWN = (229,219,222)
LIGHTGREY  = (200,200,200)
BEIGE      = (199,175,138)


# FONCTION MATHÉMATIQUE UTILISER PAR LES FONCTIONS SUIVANT CELLES-CI

sigmoid         = lambda x:1/(1+exp(-x))
reverse_sigmoid = lambda x:log(x/(1-x))
bijection  = lambda x,e,s:(x-e[0])/(e[1]-e[0])*(s[1]-s[0])+s[0]


# FONCTIONS SIMPLE MANIPULANT DES COULEURS

random    = lambda :            tuple([randint(0,255)                 for i in range(3)])
reverse   = lambda color:       tuple([255-c                          for c in color])
darken    = lambda color,n=0:   tuple([int(c*sigmoid(n/10))           for c in color])
lighten   = lambda color,n=0:   tuple([int(255-(255-c)*sigmoid(n/10)) for c in color])
mix       = lambda cl1,cl2:     tuple([(c1+c2)//2                     for (c1,c2) in zip(cl1,cl2)])
substract = lambda cl1,cl2:     tuple([max(min(2*c1-c2,255),0)        for (c1,c2) in zip(cl1,cl2)])
increase  = lambda color,n=2:   tuple([int(255*exp(n*log(c/255)))     for c in color])


def setFromWavelength(wavelength):
    """Return a color using wavelength."""
    gamma,max_intensity=0.80,255
    def adjust(color, factor):
        if color==0: return 0
        else: return round(max_intensity*pow(color*factor,gamma))
    if   380<=wavelength<=440: r,g,b=-(wavelength-440)/(440-380),0,1
    elif 440<=wavelength<=490: r,g,b=0,(wavelength-440)/(490-440),1
    elif 490<=wavelength<=510: r,g,b=0,1,-(wavelength-510)/(510-490)
    elif 510<=wavelength<=580: r,g,b=(wavelength-510)/(580-510),1,0
    elif 580<=wavelength<=645: r,g,b=1,-(wavelength-645)/(645-580),0
    elif 645<=wavelength<=780: r,g,b=1,0,0
    else: r,g,b=0,0,0
    if 380<=wavelength<=420: factor=0.3+0.7*(wavelength-380)/(420-380)
    elif 420<=wavelength<=701: factor=1
    elif 701<=wavelength<=780: factor=0.3+0.7*(780-wavelength)/(780-700)
    else: factor=0
    r,g,b=adjust(r,factor),adjust(g,factor),adjust(b,factor)
    return (r,g,b)

if __name__=="__main__":
    print(darken(RED,10))
    print(mix(YELLOW,RED))
    print(reverse(LIGHTBROWN))
    print(substract(LIGHTBROWN,ORANGE))
    print(increase(LIGHTBROWN))

    for i in range(380,780,10):
        print(setFromWavelength(i))

    print("mycolors imported")
