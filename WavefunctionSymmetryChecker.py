import numpy as np

# Basit bir uzaysal dalga fonksiyonu (örneğin, bir Gauss fonksiyonu)
def wavefunction(r, alpha=1.0):
    return np.exp(-alpha * np.linalg.norm(r)**2)

# Simetrik uzaysal dalga fonksiyonu
def symmetric_spatial_wavefunction(r1, r2, alpha=1.0):
    return 1/np.sqrt(2) * (wavefunction(r1, alpha) * wavefunction(r2, alpha) + wavefunction(r2, alpha) * wavefunction(r1, alpha))

# Antisimetik uzaysal dalga fonksiyonu
def antisymmetric_spatial_wavefunction(r1, r2, alpha=1.0):
    return 1/np.sqrt(2) * (wavefunction(r1, alpha) * wavefunction(r2, alpha) - wavefunction(r2, alpha) * wavefunction(r1, alpha))

# Konumları kullanıcıdan al
def get_positions():
    r1 = np.array([float(input("r1 konum vektörü için x koordinatı: ")), 
                   float(input("r1 konum vektörü için y koordinatı: ")), 
                   float(input("r1 konum vektörü için z koordinatı: "))])

    r2 = np.array([float(input("r2 konum vektörü için x koordinatı: ")), 
                   float(input("r2 konum vektörü için y koordinatı: ")), 
                   float(input("r2 konum vektörü için z koordinatı: "))])
    
    return r1, r2

# Dalga fonksiyonunun simetrik veya antisimetik olduğunu belirle
def determine_symmetry(r1, r2):
    # Simetrik ve antisimetik dalga fonksiyonlarını hesapla
    sym_wf_original = symmetric_spatial_wavefunction(r1, r2)
    antisym_wf_original = antisymmetric_spatial_wavefunction(r1, r2)

    # Konumları yer değiştir
    sym_wf_swapped = symmetric_spatial_wavefunction(r2, r1)
    antisym_wf_swapped = antisymmetric_spatial_wavefunction(r2, r1)

    # Simetri kontrolü
    if np.allclose(sym_wf_original, sym_wf_swapped):
        print("Bu uzaysal dalga fonksiyonu simetriktir.")
    elif np.allclose(antisym_wf_original, -antisym_wf_swapped):
        print("Bu uzaysal dalga fonksiyonu antisimetiktir.")
    else:
        print("Bu dalga fonksiyonu simetrik veya antisimetik değildir, muhtemelen başka bir kombinasyondur.")

# Ana program
def main():
    print("Lütfen r1 ve r2 konumlarını giriniz:")
    r1, r2 = get_positions()
    determine_symmetry(r1, r2)

if __name__ == "__main__":
    main()

