n=2015;
max=2017;
while [ "$n" -le "$max" ]; do
  mkdir "interspeech_$n"
  cd "interspeech_$n"
  wget -rcpk -l 3 -R "*booklet*" --no-check-certificate "https://www.isca-speech.org/archive/Interspeech_$n/"
  n=`expr "$n" + 1`;
  cd ..
done
