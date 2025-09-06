# Import fungsi dari utils.py
from utils import konversi_suhu, nama_satuan

def main():
    """
    Program utama untuk konversi suhu
    """
    print("=== PROGRAM KONVERSI SUHU ===")
    print("Satuan yang tersedia:")
    print("C = Celsius")
    print("F = Fahrenheit") 
    print("K = Kelvin")
    print("-" * 30)
    
    while True:
        try:
            # Input satuan asal
            print("\n1. Pilih satuan asal:")
            dari = input("Masukkan satuan asal (C/F/K): ").strip()
            
            # Validasi input tidak kosong
            if not dari:
                print("Error: Input tidak boleh kosong!")
                continue
            
            # Input satuan tujuan
            print("\n2. Pilih satuan tujuan:")
            ke = input("Masukkan satuan tujuan (C/F/K): ").strip()
            
            # Validasi input tidak kosong
            if not ke:
                print("Error: Input tidak boleh kosong!")
                continue
            
            # Input nilai suhu
            print("\n3. Masukkan nilai suhu:")
            nilai_input = input(f"Masukkan nilai suhu dalam {nama_satuan(dari)}: ")
            
            # Konversi string ke float
            nilai = float(nilai_input)
            
            # Panggil fungsi konversi
            hasil = konversi_suhu(nilai, dari, ke)
            
            # Cek apakah hasil berupa error
            if isinstance(hasil, str) and hasil.startswith("Error"):
                print(f"\n❌ {hasil}")
            else:
                # Tampilkan hasil konversi
                print(f"\n✅ Hasil Konversi:")
                print(f"{nilai}° {nama_satuan(dari)} = {hasil}° {nama_satuan(ke)}")
            
            # Tanya apakah ingin melanjutkan
            print("\n" + "-" * 30)
            lanjut = input("Apakah ingin melakukan konversi lagi? (y/n): ").strip().lower()
            if lanjut not in ['y', 'yes', 'ya']:
                print("Terima kasih telah menggunakan program konversi suhu!")
                break
                
        except ValueError:
            print("❌ Error: Nilai suhu harus berupa angka!")
        except KeyboardInterrupt:
            print("\n\nProgram dihentikan oleh user. Terima kasih!")
            break
        except Exception as e:
            print(f"❌ Error tidak terduga: {str(e)}")

def demo_testing():
    """
    Fungsi untuk testing berbagai kasus
    """
    print("\n=== TESTING FUNGSI KONVERSI ===")
    
    test_cases = [
        (0, "c", "f"),      # 0°C ke °F
        (100, "c", "f"),    # 100°C ke °F
        (32, "f", "c"),     # 32°F ke °C
        (273.15, "k", "c"), # 273.15K ke °C
        (0, "c", "k"),      # 0°C ke K
        (-40, "c", "f"),    # -40°C ke °F (sama dengan °F)
        (-10, "k", "c"),    # Kelvin negatif (error)
        (25, "c", "c"),     # Sama satuan
    ]
    
    for nilai, dari, ke in test_cases:
        hasil = konversi_suhu(nilai, dari, ke)
        print(f"{nilai}° {nama_satuan(dari)} → {nama_satuan(ke)}: {hasil}")

if __name__ == "__main__":
    # Jalankan program utama
    main()
    
    # Uncomment baris berikut untuk melihat hasil testing