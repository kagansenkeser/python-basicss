#bu kisimda for dongusunden bahsedecegim
x=1
for x in range(6):
    print(x)
#oncelikle for dan sonra altindaki satirda (tab) boslugu birakmalisiniz
#range i ust sinir olarak dusunebiliriz x 6 ya gelinceye kadar devam ediyor dongüye
#yada baska bir örnekle göstermek gerekirse

meyveler = ["elma", "armut", "muz"]
for x in meyveler:
  if x == "muz":
    break
  print(x)
#bu dongüde elemanlari deniyor tek tek elma muza esit olmadigi icin
#onu yazdirdi armut da muz a esit oldugu icin yazdirdi ama 
#ama muz muz a esit olduğu icin if e girdi ve break ile donguden cikti 
