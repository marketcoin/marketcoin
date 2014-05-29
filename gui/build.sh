for i in *.ui; do
	pyuic5 $i > ${i%%ui}py
done
