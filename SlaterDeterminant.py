import numpy as np

# Kullanıcıdan 3x3'lük matris için değerler al
def get_matrix():
    matrix = np.zeros((3, 3))  # 3x3'lük sıfır matris oluştur

    for i in range(3):
        for j in range(3):
            matrix[i, j] = float(input(f"Matrisin [{i+1}, {j+1}] elemanını girin: "))

    return matrix

# Matrisin determinantını hesapla
def calculate_determinant(matrix):
    return np.linalg.det(matrix)

# Ana program
def main():
    print("3x3'lük matrisin elemanlarını giriniz:")
    matrix = get_matrix()

    determinant = calculate_determinant(matrix)

    print("\nGirilen 3x3'lük matris:")
    print(matrix)
    print("\nBu matrisin Slater determinantı:", determinant)

if __name__ == "__main__":
    main()
