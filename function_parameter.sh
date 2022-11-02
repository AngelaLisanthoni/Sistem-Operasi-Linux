#mendeklarasikan fungsi
identitas() {
        parameter1=$1
        parameter2=$2
        parameter3=$3
        echo "$parameter1"
        echo "$parameter2"
        echo "$parameter3"
}

echo "Masukkan nama : "
read a
echo "Masukkan npm : "
read b
echo "Hobimu apa: "
read c

printf "\n"
identitas $a $b $c
