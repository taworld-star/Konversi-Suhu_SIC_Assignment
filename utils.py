def konversi_suhu(nilai, dari, ke):
    """
    Fungsi untuk konversi suhu antar satuan Celsius, Fahrenheit, dan Kelvin
    
    Parameters:
    nilai (float): Nilai suhu yang akan dikonversi
    dari (str): Satuan asal ("c", "f", "k") - tidak case sensitive
    ke (str): Satuan tujuan ("c", "f", "k") - tidak case sensitive
    
    Returns:
    float atau str: Hasil konversi atau pesan error
    """
    
    # Konversi input ke lowercase untuk validasi
    dari = dari.lower()
    ke = ke.lower()
    
    # Validasi satuan
    satuan_valid = ["c", "f", "k"]
    if dari not in satuan_valid or ke not in satuan_valid:
        return "Error: Satuan harus 'c', 'f', atau 'k'"
    
    # Validasi nilai suhu
    if dari == "k" and nilai < 0:
        return "Error: Suhu Kelvin tidak boleh negatif"
    
    # Jika satuan sama, return nilai asli
    if dari == ke:
        return nilai
    
    # Konversi suhu
    try:
        # Konversi dari Celsius
        if dari == "c":
            if ke == "f":
                hasil = (nilai * 9/5) + 32
            elif ke == "k":
                hasil = nilai + 273.15
        
        # Konversi dari Fahrenheit
        elif dari == "f":
            if ke == "c":
                hasil = (nilai - 32) * 5/9
            elif ke == "k":
                hasil = (nilai - 32) * 5/9 + 273.15
        
        # Konversi dari Kelvin
        elif dari == "k":
            if ke == "c":
                hasil = nilai - 273.15
            elif ke == "f":
                hasil = (nilai - 273.15) * 9/5 + 32
        
        # Validasi hasil untuk Kelvin
        if ke == "k" and hasil < 0:
            return "Error: Hasil konversi menghasilkan Kelvin negatif"
        
        return round(hasil, 2)
    
    except Exception as e:
        return f"Error dalam perhitungan: {str(e)}"


# Fungsi tambahan untuk mendapatkan nama lengkap satuan
def nama_satuan(kode):
    """
    Mengkonversi kode satuan ke nama lengkap
    """
    satuan_map = {
        "c": "Celsius",
        "f": "Fahrenheit", 
        "k": "Kelvin"
    }
    return satuan_map.get(kode.lower(), "Unknown")