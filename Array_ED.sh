declare -a angka

i=0;
while [ $i -le 4 ];
do
   let isi=$i*2;
   angka[$i]=$isi;
   let i=$i+1;
done

echo ${angka[@]}
