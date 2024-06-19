echo "MAIN:"
for file in test_main/test_*.txt; do
    n=$(basename "$file" .txt | cut -d '_' -f 2)
    echo "N = $n"
    python3 ./main.py < "$file" | grep "^Результат"
    echo
done
echo "REV_MAIN:"
for file in test_rev_main/test_*.txt; do
    n=$(basename "$file" .txt | cut -d '_' -f 2)
    echo "N = $n"
    python3 ./rev_main.py < "$file" | grep "^Результат"
    echo
done