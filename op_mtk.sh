a=15
b=7

let jumlah=$a+$b
let kurang=$a-$b
let kali=$a*$b
bagi=`expr $a / $b`
mod=$(($a%$b))

echo "a + b = $jumlah"
echo "a - b = $kurang"
echo "a * b = $kali"
echo "a / b = $bagi"
echo "a % b = $mod"

b=$a
echo "a = $a"
echo "b = $b"
