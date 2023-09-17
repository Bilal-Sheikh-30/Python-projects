def maingame():
    # score=0
    print('''AVAILABLE SUBJECT:
    1) GENERAL KNOWLEDGE
    2) PHYSICS
    3) TECHNOLOGY
    4) PAK STUDIES''')
    pl_choice=input('Enter serial number of your desired subject: ')
    option=['1','2','3','4']
    if pl_choice in option:
        print('--' * 99)
        if pl_choice=='1':
            def gk():
                main_ques=['which is the longest river on Earth?','Who invented radio?','Which African nation is famous for chocolates?','Which instrument is used for measuring wind speed?','Which is the smallest continent in the world?','Which country gifted The Statue of Liberty to the United States?']
                poss=[['Indus','Nile','Amazon','Mississippi'],['Newton','Al-Beruni','Marconi','Chadwick'],['Nigeria','Ethopia','Ghana','South Africa'],['Anemometer','Sonometer','Ammemeter','Screw guage'],['Antarctica','Asia','Australia','Europe'],['France','Brazil','Germany','Russia']]
                ans=['Nile','Marconi','Ghana','Anemometer','Australia','France']
                import random
                ques = random.choice(main_ques)
                print(ques)
                ques_ind = main_ques.index(ques)
                for i in range(4):
                    print('>', poss[ques_ind][i])

                def user_input():
                    pl_input = input('type your answer: ').capitalize()
                    if pl_input == ans[ques_ind]:
                        print('congrats!! your answer is correct')
                    else:
                        print('oops!! your answer is wrong :(')
                        print('--' * 99)
                        pass_choice=input('press "p" to skip this question or press any key to answer it again: ').lower()
                        if pass_choice=='p':
                            print('--' * 99)
                            maingame()
                        else:
                            user_input()
                user_input()
                print('--' * 99)
                again = input('press "y" to play again: ').lower()
                if again == 'y':
                    maingame()
                else:
                    print('game exit')
                    # print(f'{name} your score is {score}')
                    print('.'*99)
            gk()
        elif pl_choice=='2':
            def phy():
                main_ques = [['Which of  the following substances possess the highest elasticity?'],['What is the effect of impurities on freezing point of water?'],['Solubility and density are ________ properties.'],['Which quantity has the unit "Light year"?']]
                poss = [['Steel','Rubber','Glass','Copper'],['Increase','Accelerate','Decrease','No effect'],['Additive','Chemical','Physical','Constitutive'],['Light','Distance','Time','Velocity']]
                ans = ['Steel','Decrease','Physical','Distance']
                import random
                ques = random.choice(main_ques)
                print(ques)
                ques_ind = main_ques.index(ques)
                for i in range(4):
                    print('>', poss[ques_ind][i])

                def user_input():
                    pl_input = input('type your answer: ').capitalize()
                    if pl_input == ans[ques_ind]:
                        print('congrats!! your answer is correct')
                    else:
                        print('oops!! your answer is wrong :(')
                        print('--' * 99)
                        pass_choice = input('press "p" to skip this question or press any key to answer it again: ').lower()
                        if pass_choice == 'p':
                            print('--' * 99)
                            maingame()
                        else:
                            user_input()
                user_input()
                print('--' * 99)
                again = input('press "y" to play again: ').lower()
                if again == 'y':
                    maingame()
                else:
                    print('game exit')
                    print('.' * 99)
            phy()
        elif pl_choice=='3':
            def tech():
                main_ques = [['Who is the father of internet?'],['If a computer has more than one processor, then it is known as:'],['If a computer has more than one processor on a single chip, then it is known as:'],["Which technology is used in CD's?"]]
                poss = [['Babage','Vint','Martin','Denis'],['Uniprocessor','Multithreaded','Multiprocessor','Multiprogramming'],['Uniprocessor','Multithreaded','Multiprocessor','Multicore'],['Laser',"Mechanical",'Electrical','Megnatic']]
                ans = ['Vint','Multiprocessor','Multicore','Laser']
                import random
                ques = random.choice(main_ques)
                print(ques)
                ques_ind = main_ques.index(ques)
                for i in range(4):
                    print('>', poss[ques_ind][i])

                def user_input():
                    pl_input = input('type your answer: ').capitalize()
                    if pl_input == ans[ques_ind]:
                        print('congrats!! your answer is correct')
                    else:
                        print('oops!! your answer is wrong :(')
                        print('--' * 99)
                        pass_choice = input('press "p" to skip this question or press any key to answer it again: ').lower()
                        if pass_choice == 'p':
                            print('--' * 99)
                            maingame()
                        else:
                            user_input()
                user_input()
                print('--' * 99)
                again = input('press "y" to play again: ').lower()
                if again == 'y':
                    maingame()
                else:
                    print('game exit')
                    print('.' * 99)
            tech()
        elif pl_choice=='4':
            def pst():
                main_ques = [['The stock exchange of Pakistan is regulated by:'],['Population wise, Pakistan is _____ largest country in the world'],['Which is the largest river of Pakistan?'],['In which year did the current constitution of Pakistan was enforced?']]
                poss = [['State bank','Finance ministry','SECP','ECO'],['Fourth','Fifth','Sixth','Ninth'],['Indus',"Ravi",'Chenab','Bias'],['1947','1956','1962','1973']]
                ans = ['SECP','Fifth','Indus','1973']
                import random
                ques = random.choice(main_ques)
                print(ques)
                ques_ind = main_ques.index(ques)
                for i in range(4):
                    print('>', poss[ques_ind][i])

                def user_input():
                    pl_input = input('type your answer: ').capitalize()
                    if pl_input == ans[ques_ind]:
                        print('congrats!! your answer is correct')
                    else:
                        print('oops!! your answer is wrong :(')
                        print('--' * 99)
                        pass_choice = input('press "p" to skip this question or press any key to answer it again: ').lower()
                        if pass_choice == 'p':
                            print('--' * 99)
                            maingame()
                        else:
                            user_input()
                user_input()
                print('--' * 99)
                again = input('press "y" to play again: ').lower()
                if again == 'y':
                    maingame()
                else:
                    print('game exit')
                    print('.' * 99)
            pst()
    else:
        print('Enter correct serial number')
        print('--' * 99)
        print('choose the correct option!!')
        print('--' * 99)
        maingame()
name=input('Enter your name: ').capitalize()
# score=0
print(f'Welcome {name} to the quiz game!!')
maingame()