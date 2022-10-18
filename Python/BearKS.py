def draw():
    x = """                                                                                                    
                                                                                
                                      7.                                        
                                      G~                                        
                                    .GP   ?                                     
                                   ~#7   !5                                     
                                   &~   5J                                      
                                   J:  !Y                                       
                                    .   :                                       
                           .:~!??JYYYYYYJYJJ?7!~^:.                             
                       :?PP5J7~^:..      ...::^~!7?7!:.                         
                     :B&5:                        .:75~.                        
                     Y&&~                           ~B7 !B###B57.               
                     ~#JGG57^..               ..:~!?7~: J&5!^!5&&5              
                     .#  .:!?Y5555YYJJJJJJJJJJJ?7!^.    P~     :#&5             
                    ..G7           ........            .J       B&P             
                 :^:. :B                               J~      Y&B.             
              .~:.     7G                             ^B    .?##?               
             7!         YB.           Code           ^#!:!5GGJ^                 
            :B           J#?                       .Y&BP5?^.                    
             #?           :G#Y:                  ^5#Y.          ~               
             .PB7.          :Y##PJ!^:......:^7YG#B?.         .!7.               
               .JGGJ~:         :75B###&&&&&#BGY~.        :~?J7.                 
                  .~JPGGPJ7~:..     ...::...    ..:~7J55Y?~.                    
                       .^5B&&##BGGGPPP555PPPGGBB##&BY^.                         
                           .:~7?JYY55555555YYJ?7~:.                             
                                                                                
    """     
    return x

def CoffeeToCode(word):
    if word.lower() == 'coffee' :
        word = word.replace("ff", "d")[:-1]
    else:
        word = word
    return word.capitalize()

if __name__ == '__main__' :
    state = 0
    a = list(input("#############################\n#   I turn Coffee to Code   #\n#############################\nSay something? : ").split(' '))
    st = ""
    for i in range(len(a)):
        st += CoffeeToCode(a[i])+' '
        if(a[i].lower() == 'coffee'):
            state += 1
    print("Output : ",end="")
    if state > 0 :
        print(st)
        print(draw())
    else:
        print('What you say? AGAIN PLEASE!!\n')
        
###############################################
##                by BearKS                  ##
###############################################