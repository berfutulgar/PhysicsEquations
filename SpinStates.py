import numpy as np

#Spin yukarı durumu |0⟩ veya |↑⟩
spin_up = np.array([1, 0])

# Spin aşağı durumu |1⟩ veya |↓⟩
spin_down = np.array([0, 1])

# İki parçacıklı sistemdeki dört olası durum
# |↑↑⟩
state_1 = np.kron(spin_up, spin_up)

# |↑↓⟩
state_2 = np.kron(spin_up, spin_down)

# |↓↑⟩
state_3 = np.kron(spin_down, spin_up)

# |↓↓⟩
state_4 = np.kron(spin_down, spin_down)

print("State |↑↑⟩:", state_1)
print("State |↑↓⟩:", state_2)
print("State |↓↑⟩:", state_3)
print("State |↓↓⟩:", state_4)

# Simetrik spin durumları (Triplet)
triplet_1 = np.kron(spin_up, spin_up)  # |↑↑⟩
triplet_2 = np.kron(spin_down, spin_down)  # |↓↓⟩
triplet_3 = 1/np.sqrt(2) * (np.kron(spin_up, spin_down) + np.kron(spin_down, spin_up))  # |↑↓⟩ + |↓↑⟩

# Antisimetik spin durumu (Singlet)
singlet = 1/np.sqrt(2) * (np.kron(spin_up, spin_down) - np.kron(spin_down, spin_up))  # |↑↓⟩ - |↓↑⟩

print("Singlet durumu:")
print(singlet)

print("\nTriplet durumları:")
print("Triplet 1 (|↑↑⟩):", triplet_1)
print("Triplet 2 (|↓↓⟩):", triplet_2)
print("Triplet 3 (|↑↓⟩ + |↓↑⟩):", triplet_3)