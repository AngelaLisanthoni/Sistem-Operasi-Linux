#mendeklarasikan fungsi
function nama {
    echo "Siapa namamu?"
    read nama
}
function npm {
   echo "Sebutkan npm mu"
   read npm
   echo -e "Hai $nama dengan npm $npm, selamat datang \n di pratikum sistem operasi yang seru ini ya!"
}

#memanggil fungsi
nama
npm
