import numpy as np

# Basit bir uzaysal dalga fonksiyonu (örneğin, bir Gauss fonksiyonu)
def wavefunction(r, alpha=1.0):
    return np.exp(-alpha * np.linalg.norm(r)**2)

# Simetrik ve antisimetik uzaysal dalga fonksiyonları (2 parçacık)
def symmetric_spatial_wavefunction_2(r1, r2, alpha=1.0):
    return 1/np.sqrt(2) * (wavefunction(r1, alpha) * wavefunction(r2, alpha) + wavefunction(r2, alpha) * wavefunction(r1, alpha))

def antisymmetric_spatial_wavefunction_2(r1, r2, alpha=1.0):
    return 1/np.sqrt(2) * (wavefunction(r1, alpha) * wavefunction(r2, alpha) - wavefunction(r2, alpha) * wavefunction(r1, alpha))

# Simetrik ve antisimetik uzaysal dalga fonksiyonları (3 parçacık)
def symmetric_spatial_wavefunction_3(r1, r2, r3, alpha=1.0):
    return 1/np.sqrt(3) * (wavefunction(r1, alpha) * wavefunction(r2, alpha) * wavefunction(r3, alpha) + 
                           wavefunction(r2, alpha) * wavefunction(r1, alpha) * wavefunction(r3, alpha) +
                           wavefunction(r3, alpha) * wavefunction(r2, alpha) * wavefunction(r1, alpha))

def antisymmetric_spatial_wavefunction_3(r1, r2, r3, alpha=1.0):
    return 1/np.sqrt(3) * (wavefunction(r1, alpha) * wavefunction(r2, alpha) * wavefunction(r3, alpha) -
                           wavefunction(r2, alpha) * wavefunction(r1, alpha) * wavefunction(r3, alpha) +
                           wavefunction(r3, alpha) * wavefunction(r2, alpha) * wavefunction(r1, alpha))

# Slater determinantı hesapla (2 veya 3 parçacık)
def slater_determinant(states):
    # Durumlar matrisi oluştur (satırları spin-uzaysal durumları olan bir matris)
    matrix = np.array(states)
    
    # Matrisin determinantını hesapla
    return np.linalg.det(matrix)

# Kullanıcının girdiği konum vektörlerini al
def get_positions(particle_count):
    positions = []
    for i in range(1, particle_count + 1):
        x = float(input(f"r{i} konum vektörü için x koordinatı: "))
        y = float(input(f"r{i} konum vektörü için y koordinatı: "))
        z = float(input(f"r{i} konum vektörü için z koordinatı: "))
        positions.append(np.array([x, y, z]))
    return positions

# Kullanıcının girdiği spin durumlarını al (sadece 3 parçacık için)
def get_spin_states_3():
    spin_states = []
    for i in range(1, 4):
        spin = input(f"{i}. parçacık için spin durumu ('up' veya 'down'): ").strip().lower()
        if spin == 'up':
            spin_states.append(np.array([1, 0]))
        elif spin == 'down':
            spin_states.append(np.array([0, 1]))
        else:
            print("Geçersiz giriş. Lütfen 'up' veya 'down' giriniz.")
            return get_spin_states_3()
    return spin_states

# 2 parçacıklı kuantum durumunu analiz et ve gerekirse Slater determinantı uygula
def analyze_quantum_state_2(positions):
    r1, r2 = positions
    spin1 = np.array([1, 0])  # 1. parçacık spin up
    spin2 = np.array([0, 1])  # 2. parçacık spin down

    sym_spatial = symmetric_spatial_wavefunction_2(r1, r2)
    antisym_spatial = antisymmetric_spatial_wavefunction_2(r1, r2)

    # Uzaysal durumun simetrik mi antisimetik mi olduğunu kontrol et
    uzaysal_simetri = "antisimetik" if np.allclose(antisym_spatial, antisym_spatial) else "simetrik"

    # Spin durumunun simetrik mi antisimetik mi olduğunu kontrol et
    spin_simetri = "antisimetik" if np.allclose(np.kron(spin1, spin2) - np.kron(spin2, spin1), np.kron(spin1, spin2)) else "simetrik"

    # Durumların simetrilerini yazdır
    print(f"Uzaysal durum {uzaysal_simetri}tir.")
    print(f"Spin durumu {spin_simetri}tir.")

    # Uzaysal ve spin durumu aynıysa Slater determinantı uygulayın
    if uzaysal_simetri == spin_simetri:
        print("Hem uzaysal hem de spin durumları aynı (ikisi de simetrik veya ikisi de antisimetik). Slater determinantı uygulanıyor...")
        states = [np.append(wavefunction(r1), spin1), np.append(wavefunction(r2), spin2)]
        slater_result = slater_determinant(states)
        print("Slater determinantı sonucu:", slater_result)
    else:
        print("Kuantum durumu geçerli: Uzaysal ve spin simetri durumları farklı.")

# 3 parçacıklı kuantum durumunu analiz et ve gerekirse Slater determinantı uygula
def analyze_quantum_state_3(positions, spin_states):
    r1, r2, r3 = positions
    spin1, spin2, spin3 = spin_states

    sym_spatial = symmetric_spatial_wavefunction_3(r1, r2, r3)
    antisym_spatial = antisymmetric_spatial_wavefunction_3(r1, r2, r3)

    uzaysal_simetri = "simetrik" if np.allclose(sym_spatial, sym_spatial) else "antisimetik"
    spin_simetri = "antisimetik" if np.allclose(np.kron(spin1, spin2) - np.kron(spin2, spin1), np.kron(spin1, spin2)) else "simetrik"

    # Durumların simetrilerini yazdır
    print(f"Uzaysal durum {uzaysal_simetri}tir.")
    print(f"Spin durumu {spin_simetri}tir.")

    if uzaysal_simetri == spin_simetri:
        print("Hem uzaysal hem de spin durumları aynı (ikisi de simetrik veya ikisi de antisimetik). Bu durumda Slater determinantı uygulanarak sistemin antisimetri sağlanır.")
        states = [
            np.append(wavefunction(r1), spin1),
            np.append(wavefunction(r2), spin2),
            np.append(wavefunction(r3), spin3)
        ]
        slater_result = slater_determinant(states)
        print("Slater determinantı sonucu:", slater_result)
    else:
        print("Uzaysal ve spin durumları farklı olduğundan Slater determinantı uygulanmadı.")

# Ana program
def main():
    while True:
        try:
            particle_count = int(input("Parçacık sayısını girin (2 veya 3): "))
            if particle_count not in [2, 3]:
                print("Lütfen sadece 2 veya 3 parçacık seçin.")
                continue
            break
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")
    
    positions = get_positions(particle_count)

    if particle_count == 2:
        analyze_quantum_state_2(positions)
    elif particle_count == 3:
        spin_states = get_spin_states_3()
        analyze_quantum_state_3(positions, spin_states)

if __name__ == "__main__":
    main()
