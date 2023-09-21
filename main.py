import sys
from consulta import Consulta

def main():
    # Check if the RUT argument is provided
    if len(sys.argv) != 2:
        print("Usage: python main.py <RUT>")
        return

    # Get the RUT from the command-line argument
    rut = sys.argv[1]

    # Create a Consulta instance with the provided RUT
    consulta = Consulta(rut)
    
    try:
        if consulta.validate():
            # Perform the RUT query and retrieve the result
            result = consulta.resultado()
            print(result)
        else:
            print("Rut invalido")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

