#mendeklarasikan fungsi
luas_persegi_panjang () {
      echo "Masukkan Panjang : "
      read panjang
      echo "Masukkan lebar : "
      read lebar
      let luas=$panjang*$lebar
      echo -e "Luas Persegi : \n$luas"
}

luas_persegi_panjang
