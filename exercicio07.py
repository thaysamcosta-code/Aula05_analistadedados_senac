#5 nomes, provas e média

for contador in range(1,6):
    nome = input("Nome: ")
    p1 = float(input("Prova 01: ").replace (",", "."))
    p2 = float(input("Prova 02: ").replace (",", "."))
    p3 = float(input("Prova 03: ").replace (",", "."))
    md = (p1 + p2 + p3)/3
    if md >= 7:
        situacao = "aprovado"
    elif md >= 6:
        situacao = "recuperação"
    else: 
        situacao = "reprovado"
    print("\n---RESULTADO FINAL---")
    print(f"Aluno: {contador}")    
    print(f"Nome: {nome}")    
    print(f"Prova 1: {p1}".replace(".", ","))    
    print(f"Prova 2: {p2}".replace(".", ","))
    print(f"Prova 3: {p3}".replace(".", ","))
    print(f"Média: {md}")    
    print(f"Situação: {situacao}") 
    print(f"\n")   


