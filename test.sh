root="/home/amorris/BioInf/software/Read-distribution-analysis"

gini="python3 $root/src/gini.py"
test_dir="$root/test_data"

lb=1
ub=5002
s=5

for cov in $test_dir/*; do
	fbname=$(basename "$cov" .cov)
	echo $fbname".GG"
	$gini $cov -G $lb $ub $s > $root/$fbname".GG"
done
