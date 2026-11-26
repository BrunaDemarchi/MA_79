#Aqui vou desenvolver meu código de teste para a revisão.
# Lista (array) global que funciona como banco de dados em memória
motores = []
proximo_id = 1


def cadastrar_motor():
    global proximo_id
    print("\n--- CADASTRAR NOVO MOTOR ---")

    modelo = input("Modelo/Referência: ").strip()
    fabricante = input("Fabricante (ex: WEG, Siemens): ").strip()

    try:
        potencia_cv = float(input("Potência (CV): ").replace(",", "."))
        tensao_v = int(input("Tensão nominal (V) [ex: 220, 380]: "))
        rpm = int(input("Rotação (RPM): "))
    except ValueError:
        print("\n[ERRO] Potência, tensão e RPM devem ser valores numéricos. Cadastro cancelado.")
        return

    motor = {
        "id": proximo_id,
        "modelo": modelo,
        "fabricante": fabricante,
        "potencia_cv": potencia_cv,
        "tensao_v": tensao_v,
        "rpm": rpm
    }

    motores.append(motor)
    proximo_id += 1
    print(f"\n[SUCESSO] Motor ID #{motor['id']} ({modelo}) cadastrado!")


def listar_motores():
    print("\n--- LISTA DE MOTORES CADASTRADOS ---")
    if not motores:
        print("Nenhum motor cadastrado no momento.")
        return

    print(f"{'ID':<4} | {'Modelo':<18} | {'Fabricante':<14} | {'Potência':<10} | {'Tensão':<8} | {'RPM':<6}")
    print("-" * 74)
    for m in motores:
        print(
            f"{m['id']:<4} | "
            f"{m['modelo']:<18} | "
            f"{m['fabricante']:<14} | "
            f"{m['potencia_cv']:<7.1f} CV | "
            f"{m['tensao_v']:<5} V  | "
            f"{m['rpm']:<6}"
        )


def buscar_motor_por_id(motor_id):
    for motor in motores:
        if motor["id"] == motor_id:
            return motor
    return None


def editar_motor():
    print("\n--- EDITAR MOTOR ---")
    listar_motores()
    if not motores:
        return

    try:
        motor_id = int(input("\nDigite o ID do motor que deseja editar: "))
    except ValueError:
        print("[ERRO] ID inválido.")
        return

    motor = buscar_motor_por_id(motor_id)
    if not motor:
        print(f"[ERRO] Motor com ID #{motor_id} não encontrado.")
        return

    print("\nPressione ENTER para manter o valor atual.")

    novo_modelo = input(f"Modelo [{motor['modelo']}]: ").strip()
    if novo_modelo:
        motor["modelo"] = novo_modelo

    novo_fabricante = input(f"Fabricante [{motor['fabricante']}]: ").strip()
    if novo_fabricante:
        motor["fabricante"] = novo_fabricante

    try:
        nova_potencia = input(f"Potência CV [{motor['potencia_cv']}]: ").strip()
        if nova_potencia:
            motor["potencia_cv"] = float(nova_potencia.replace(",", "."))

        nova_tensao = input(f"Tensão V [{motor['tensao_v']}]: ").strip()
        if nova_tensao:
            motor["tensao_v"] = int(nova_tensao)

        novo_rpm = input(f"RPM [{motor['rpm']}]: ").strip()
        if novo_rpm:
            motor["rpm"] = int(novo_rpm)
    except ValueError:
        print("\n[AVISO] Um dos valores numéricos digitados era inválido. Os campos anteriores foram mantidos.")

    print(f"\n[SUCESSO] Motor ID #{motor_id} atualizado!")


def excluir_motor():
    print("\n--- EXCLUIR MOTOR ---")
    listar_motores()
    if not motores:
        return

    try:
        motor_id = int(input("\nDigite o ID do motor que deseja excluir: "))
    except ValueError:
        print("[ERRO] ID inválido.")
        return

    motor = buscar_motor_por_id(motor_id)
    if not motor:
        print(f"[ERRO] Motor com ID #{motor_id} não encontrado.")
        return

    confirmacao = input(f"Tem certeza que deseja remover '{motor['modelo']}'? (s/n): ").strip().lower()
    if confirmacao == "s":
        motores.remove(motor)
        print(f"\n[SUCESSO] Motor ID #{motor_id} removido!")
    else:
        print("\nOperação cancelada.")


def popular_dados_teste():
    """Adiciona alguns motores iniciais para facilitar os testes."""
    global proximo_id
    exemplos = [
        {"id": 1, "modelo": "W22 IR3 Premium", "fabricante": "WEG", "potencia_cv": 5.0, "tensao_v": 380, "rpm": 1750},
        {"id": 2, "modelo": "1LE0", "fabricante": "Siemens", "potencia_cv": 10.0, "tensao_v": 220, "rpm": 3500},
        {"id": 3, "modelo": "W21 Trifásico", "fabricante": "WEG", "potencia_cv": 1.5, "tensao_v": 380, "rpm": 1150},
    ]
    motores.extend(exemplos)
    proximo_id = 4


def menu():
    popular_dados_teste()

    while True:
        print("\n==================================")
        print("   SISTEMA DE CADASTRO DE MOTORES ")
        print("==================================")
        print("1. Cadastrar motor")
        print("2. Listar motores")
        print("3. Editar motor")
        print("4. Excluir motor")
        print("0. Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_motor()
        elif opcao == "2":
            listar_motores()
        elif opcao == "3":
            editar_motor()
        elif opcao == "4":
            excluir_motor()
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("\n[ERRO] Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()