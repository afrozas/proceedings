n=16;
max=19;
while [ "$n" -le "$max" ]; do
  mkdir "acl_$n"
  cd "acl_$n"
  wget -rcpk -l 1 -A .pdf -R '*-1.*' --no-check-certificate "https://www.aclweb.org/anthology/volumes/P$n-1"
  wget -rcpk -l 1 -A .pdf -R '*-2.*' --no-check-certificate "https://www.aclweb.org/anthology/volumes/P$n-2/"
  n=`expr "$n" + 1`;
  cd ..
done
