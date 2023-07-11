from random import *

# print(randint(0,2))
# (0,1)V;(1,0)V;(2,0)V;(0,2)V;(1,2)V;(2,1)V:

print("0 = pedra")
print("1 = papel")
print("2 = tesoura")
escolha = int(input("Faça a sua escolha: "))

maquina_escolha = randint(0, 2)

if maquina_escolha == 0:
    maquina_escolha_texto = "pedra"
else:
    if maquina_escolha == 1:
        maquina_escolha_texto = "papel"
    else:
        maquina_escolha_texto = "tesoura"

if escolha < 0 or escolha > 2:
    print("Escolha inválida")
else:
    if escolha == maquina_escolha:
        print(f"Maquina jogou {escolha} também")
        print("Empate, jogue novamente")
    else:
        # (0,1) certo
        if escolha == 0 and maquina_escolha == 1:
            print(f"Maquina jogou f{maquina_escolha_texto}")
            print("Máquina venceu!")
        else:
            # (0,2) certo
            if escolha == 0 and maquina_escolha == 2:
                print(f"Maquina jogou {maquina_escolha_texto}")
                print("Você venceu!")
            else:
                # (1,0) certo
                if escolha == 1 and maquina_escolha == 0:
                    print(f"Maquina jogou {maquina_escolha_texto}")
                    print("Você venceu!")
                else:
                    # (2,0) certo
                    if escolha == 2 and maquina_escolha == 0:
                        print(f"Maquina jogou {maquina_escolha_texto}")
                        print("Máquina venceu!")
                    else:
                        # (1,2)V
                        if escolha == 1 and maquina_escolha == 2:
                            print(f"Maquina jogou {maquina_escolha_texto}")
                            print("Máquina venceu!")
                        else:
                            # (2,1)
                            if escolha == 2 and maquina_escolha == 1:
                                print(f"Maquina jogou {maquina_escolha_texto}")
                                print("Você venceu!")
