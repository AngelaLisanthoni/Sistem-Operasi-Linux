printf "Banyak Semester yang sudah diikuti?"
read semester

declare -a IPSMahasiswa

i=0
let banyak=$semester-1

while [ $i -le $banyak ];
do
  let angka=$i+1
  printf "nilai Semester %.1i:" $angka;
  read nilaisemester;
  IPSMahasiswa[$i]=$nilaisemester;
  let jumlah=jumlah+$nilaisemester;
  let i=$i+1;
done

let IPK=$jumlah/$semester
echo "nilai per semester" ${IPSMahasiswa[@]}
echo "Nilai IPS:" $jumlah "/" $semester
echo "Nilai IPK:" $IPK
