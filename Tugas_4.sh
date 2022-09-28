echo -n "Masukkan angka ganjil: ";
read a
mod=$(($a % 2))

if [ $mod == 0 ]
then
 echo "angka harus GANJIL"
 echo -n "Masukkan angka ganjil: ";
 read a
fi

echo "angka yang diinputkan $a";

while [ $a -gt 0 ]
do
  echo $a
  a=$((a - 2))
done
