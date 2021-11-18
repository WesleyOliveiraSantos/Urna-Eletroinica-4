from model import *
 
#Iniciando o contador com 0
opcao = 0


#Inicializando a Urna
imprimeMenu()


#Iniciando laço de repetição
while opcao != 4:
    
    opcao = int(input("\nDigite a sua opção: "))

#Opção 1 LISTAR CANDIDATOS
    if opcao == 1:
    
        listarCandidatos()


#Escolha do Governador e Preisdente
    elif opcao == 2:
        
        candGov = int(input("\nDigite o numero do candidato escolhido a Governador: "))

    #Candidato a Governdaor 1        
        if candGov == 1:
            
            print(f"\nCandidato(a) escolhido(a): {nomeGov2}")
            confirma = input("\nConfirma o voto? (S ou N): ")
                
            if confirma == "S" or confirma == "s":
                votoGov1 += 1
                              
            elif confirma == "N" or confirma == "n":
                brancoOUnulo = input("\nDeseja votar em Branco ou Nulo (B ou N) ")
                
                if brancoOUnulo == "B" or brancoOUnulo == "b":
                    brancoGov += 1
                elif brancoOUnulo == "N" or brancoOUnulo == "n":
                    nuloGov += 1

                
    #Candidato a Governador 2             
        elif candGov == 2:
                
            print(f"\nCandidato(a) escolhido(a): {nomeGov2}")
            confirma = input("\nConfirma o voto? (S ou N): ")
                
            if confirma == "S" or confirma == "s":
                votoGov2 += 1
                              
            elif confirma == "N" or confirma == "n":
                brancoOUnulo = input("\nDeseja votar em Branco ou Nulo (B ou N) ")
                
                if brancoOUnulo == "B" or brancoOUnulo == "b":
                    brancoGov += 1
                elif brancoOUnulo == "N" or brancoOUnulo == "n":
                    nuloGov += 1

                
    #Candidato a Governador 3             
        elif candGov == 3:
                
            print(f"\nCandidato(a) escolhido(a): {nomeGov3}")
            confirma = input("\nConfirma o voto? (S ou N): ")
                
            if confirma == "S" or confirma == "s":
                votoGov3 += 1
                              
            elif confirma == "N" or confirma == "n":
                brancoOUnulo = input("\nDeseja votar em Branco ou Nulo (B ou N) ")
                
                if brancoOUnulo == "B" or brancoOUnulo == "b":
                    brancoGov += 1
                elif brancoOUnulo == "N" or brancoOUnulo == "n":
                    nuloGov += 1

                
    #Candidato a Governador 4             
        elif candGov == 4:
                
            print(f"\nCandidato(a) escolhido(a): {nomeGov4}")
            confirma = input("\nConfirma o voto? (S ou N): ")
                
            if confirma == "S" or confirma == "s":
                votoGov4 += 1
                              
            elif confirma == "N" or confirma == "n":
                brancoOUnulo = input("\nDeseja votar em Branco ou Nulo (B ou N) ")
                
                if brancoOUnulo == "B" or brancoOUnulo == "b":
                    brancoGov += 1
                elif brancoOUnulo == "N" or brancoOUnulo == "n":
                    nuloGov += 1

                
    #Candidato a Governador 5             
        elif candGov == 5:
                
            print(f"\nCandidato(a) escolhido(a): {nomeGov5}")
            confirma = input("\nConfirma o voto? (S ou N): ")
                
            if confirma == "S" or confirma == "s":
                votoGov5 += 1
                              
            elif confirma == "N" or confirma == "n":
                brancoOUnulo = input("\nDeseja votar em Branco ou Nulo (B ou N) ")
                
                if brancoOUnulo == "B" or brancoOUnulo == "b":
                    brancoGov += 1
                elif brancoOUnulo == "N" or brancoOUnulo == "n":
                    nuloGov += 1


    #Candidatos a Presidente
              
        nomePres = int(input("\nDigite o numero do candidato escolhido a Presidente: "))
                
    #Candidatos a Presidente 1             
        if nomePres == 1:
            print(f"\nCandidato(a) escolhido(a): {nomePres1}")
            confirma = input("\nConfirma o voto? (S ou N): ")
                
            if confirma == "S" or confirma == "s":
                votoPres1 += 1
                                  
            elif confirma == "N" or confirma == "n":
                brancoOUnulo = input("\nDeseja votar em Branco ou Nulo (B ou N) ")
                
                if brancoOUnulo == "B" or brancoOUnulo == "b":
                    brancoPres += 1
                elif brancoOUnulo == "N" or brancoOUnulo == "n":
                    nuloPres += 1
                

                
    #Candidato a Presidente 2
        elif nomePres == 2:
            print(f"\nCandidato(a) escolhido(a): {nomePres2}")
            confirma = input("\nConfirma o voto? (S ou N): ")
                
            if confirma == "S" or confirma == "s":
                votoPres2 += 1
                                  
            elif confirma == "N" or confirma == "n":
                brancoOUnulo = input("\nDeseja votar em Branco ou Nulo (B ou N) ")
                
                if brancoOUnulo == "B" or brancoOUnulo == "b":
                    brancoPres += 1
                elif brancoOUnulo == "N" or brancoOUnulo == "n":
                    nuloPres += 1

                
    #Candidato a Presidente 3
        elif nomePres == 3:
                    
            print(f"\nCandidato(a) escolhido(a): {nomePres3}")
            confirma = input("\nConfirma o voto? (S ou N): ")
                
            if confirma == "S" or confirma == "s":
                votoPres3 += 1
                                  
            elif confirma == "N" or confirma == "n":
                brancoOUnulo = input("\nDeseja votar em Branco ou Nulo (B ou N) ")
                
                if brancoOUnulo == "B" or brancoOUnulo == "b":
                    brancoPres += 1
                elif brancoOUnulo == "N" or brancoOUnulo == "n":
                    nuloPres += 1

            
    #Candidato a Presidente 4
        elif nomePres == 4:
                
            print(f"\nCandidato(a) escolhido(a): {nomePres4}")
            confirma = input("\nConfirma o voto? (S ou N): ")
                
            if confirma == "S" or confirma == "s":
                votoPres4 += 1
                                  
            elif confirma == "N" or confirma == "n":
                brancoOUnulo = input("\nDeseja votar em Branco ou Nulo (B ou N) ")
                
                if brancoOUnulo == "B" or brancoOUnulo == "b":
                    brancoPres += 1
                elif brancoOUnulo == "N" or brancoOUnulo == "n":
                    nuloPres += 1

                
    #Candidato a Presidente 5
        elif nomePres == 5:
                
            print(f"\nCandidato(a) escolhido(a): {nomePres5}")
            confirma = input("\nConfirma o voto? (S ou N): ")
                
            if confirma == "S" or confirma == "s":
                votoPres5 += 1
                                  
            elif confirma == "N" or confirma == "n":
                brancoOUnulo = input("\nDeseja votar em Branco ou Nulo (B ou N) ")
                
                if brancoOUnulo == "B" or brancoOUnulo == "b":
                    brancoPres += 1
                elif brancoOUnulo == "N" or brancoOUnulo == "n":
                    nuloPres += 1


    elif opcao == 3:
        print("\n\nApuração dos Votos para Governador e Presidente")
        apuracao()
        
        
    elif opcao == 4:
        print("Obrigado por utilizar a Urna Eletrônica")
        
    else:
        print("Digite uma opção valida!")