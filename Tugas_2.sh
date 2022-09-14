printf "Operasi matematika apa yang kamu mau?\n"
printf "penjumlahan?\n"
printf "pengurangan?\n"
printf "perkalian?\n"
printf "pembagian?\n"
printf "modus?\n"

read operasi
printf "Operasi yang dipilih $operasi\n"

printf "angka a?"
read a
printf "angka a adalah $a\n"
printf "angka b?"
read b
printf "angka b adalah $b\n"

let jumlah=$a+$b
let kurang=$a-$b
let kali=$a*$b
bagi=`expr $a / $b`
mod=$(($a%$b))


case "$operasi" in
  "penjumlahan")
   echo "Penjumlahan $a dan $b adalah $jumlah"
  ;;
  "pengurangan")
   echo "Pengurangan $a dan $b adalah $kurang"
  ;;
  "perkalian")
   echo "Perkalian $a dan $b adalah $kali"
  ;;
  "pembagian")
   echo "Pembagian $a dan $b adalah $bagi"
  ;;
  "modus")
   echo "modus $a dan $b adalah $modus"
  ;;
  *)
   echo "Tidak ada operasi yang sesuai"
  ;;
esac
