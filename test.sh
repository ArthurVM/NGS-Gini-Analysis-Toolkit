root="."

gini="python3 $root/src/gini.py"
g_merge="python3 $root/src/GG_out_merge.py"
gg_curve="python3 $root/src/GG_curve.py"

test_dir="$root/test_data"

lb=1
ub=5002
s=5

for cov in $test_dir/*; do
	fbname=$(basename "$cov" .cov)
	echo $fbname".GG"
	$gini $cov -G $lb $ub $s > $root/$fbname".GG"
done

$g_merge --Gini_file $root/*.GG -o test_g_merged.GG

$gg_curve $root/test_g_merged.GG

echo "All Done"
