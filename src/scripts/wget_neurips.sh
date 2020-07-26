n=28;
max=31;
year=2015;
while [ "$n" -le "$max" ]; do
  mkdir "neurips_$year"
  cd "neurips-$year"
  wget -rcpk -A .pdf "https://papers.nips.cc/book/advances-in-neural-information-processing-systems-$n-$year"
  n=`expr "$n" + 1`;
  year=`expr "$year" + 1`;
done
